import os
from dotenv import load_dotenv
from typing import cast
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")


@cl.on_chat_start
async def start():
    external_client = AsyncOpenAI(
        api_key=gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    )

    config = RunConfig(
        model=model,
        model_provider=external_client,
        tracing_disabled=True
    )
    """Set up the chat session when a user connects."""

    cl.user_session.set("chat_history", [])

    cl.user_session.set("config", config)
    agent: Agent = Agent(name="Assistant", 
                         instructions="""
You are a fact-checking expert AI assistant. When a user provides a claim, your task is to:
0. You tell the status of the claim on the very first line profeesionally.
1. Search the internet for recent, credible, and authoritative sources that relate to the claim.
2. Evaluate whether the sources support, refute, or do not mention the claim.
3. Based on this evidence, classify the claim as one of the following: 'True', 'flase', 'Likely True', 'Likely False', or 'Unverified'.
4. Summarize your reasoning in clear, neutral language.
5. Always provide at least 2 cited sources (including URLs) from reputable organizations (e.g., WHO, BBC, Reuters, academic publications, government sites).
6. Do not make assumptions or guesses — only rely on real sources.
7. If the claim is unverifiable due to lack of information, clearly state so and explain why.

Your tone should be factual, professional, and unbiased.
""", 
                         model=model)
    cl.user_session.set("agent", agent)

    await cl.Message(content="Welcome to the FactCheck AI Assistant!").send()

@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses."""
    
    msg = cl.Message(content="Thinking☁️...")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    config: RunConfig = cast(RunConfig, cl.user_session.get("config"))

    history = cl.user_session.get("chat_history") or []
    
    history.append({"role": "user", "content": message.content})
    

    try:
        print("\n[CALLING_AGENT_WITH_CONTEXT]\n", history, "\n")
        result = Runner.run_sync(starting_agent = agent,
                    input=history,
                    run_config=config)
        
        response_content = result.final_output
        
        msg.content = response_content
        await msg.update()
    
        cl.user_session.set("chat_history", result.to_input_list())
        
        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")
        
    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
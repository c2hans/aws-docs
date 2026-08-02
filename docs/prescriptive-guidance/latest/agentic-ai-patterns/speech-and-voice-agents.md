---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/speech-and-voice-agents.html
---

# Speech and voice agents
<a name="speech-and-voice-agents"></a>

Speech and voice agents interact with users through spoken dialogue. These agents integrate speech recognition, natural-language understanding, and speech synthesis to enable conversational AI across telephony, mobile, web, and embedded platforms.

Voice agents are particularly effective in hands-free, real-time, or accessibility-driven environments. By combining streaming interfaces with LLM-powered reasoning, they facilitate rich, dynamic interactions that feel natural to users.

## Architecture
<a name="architecture.b3434d67-48de-54a7-a0df-4e9f8df80b0f"></a>

A speech and voice agent is shown in the following diagram:

![Speech and voice agents.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/40d20568-97a0-48a1-99e2-2d789710fb39.png)

## Description
<a name="description.a986784a-83be-52ec-a936-607d716e41f0"></a>

1. Receives a voice query
   + The user voices a request to a phone, microphone, or embedded system.
   + A speech-to-text (STT) module converts the audio to text.

1. Integrates streaming and telephony context
   + The agent uses a streaming interface to manage audio I/O in real time.
   + If it's deployed in a contact center or telecom context, telephony integration handles session routing, dual-tone multi-frequency (DTMF) input, and media transport.

Note: DTMF refers to the tones generated when you press buttons on a telephone keypad. In the context of streaming and telephony context integration within voice agents, DTMF is used as a signal input mechanism during a phone call, especially in interactive voice response (IVR) systems. DTMF inputs enable the agent to:
+ Recognize menu selections (for example, "Press 1 for billing. Press 2 for support.")
+ Collect numeric inputs (for example, account numbers, PINs, and confirmation numbers)
+ Trigger workflows or state transitions in call flows
+ Revert from speech to touch-tone when necessary

1. Reasons through LLM stream context
   + The query is sent to the agent, which passes it, along with any session metadata (for example, caller ID, prior context), to an LLM.
   + The LLM generates a response, possibly using a chain-of-thought strategy or multiturn memory if the interaction is ongoing.

1. Returns a voice response
   + The agent converts its response to speech using text-to-speech (TTS).
   + It returns audio to the user through a voice channel.

## Capabilities
<a name="capabilities.d2cb7873-75be-5304-9c43-309772e8debf"></a>
+ Real-time speech understanding and generation
+ Multilingual I/O with STT and TTS support
+ Integration with telephony or streaming APIs
+ Session awareness and memory handoff between turns

## Common use cases
<a name="common-use-cases.6f864b50-328c-5bb5-8e52-36ff21096238"></a>
+ Conversational IVR systems
+ Virtual receptionists and appointment schedulers
+ Voice-driven helpdesk agents
+ Wearable voice assistants
+ Voice interfaces for smart homes and accessibility tools

## Implementation guidance
<a name="implementation-guidance.979446de-15f8-5a58-b5ad-c89e93e7fdd0"></a>

You can build this pattern using the following tools and AWS services:
+ Amazon Lex V2 or Amazon Transcribe for STT
+ Amazon Polly for TTS
+ Amazon Chime SDK, Amazon Connect Customer, or Amazon Interactive Video Service (Amazon IVS) for streaming and telephony
+ Amazon Bedrock for reasoning with Anthropic, AI21, or other foundation models
+ AWS Lambda to connect STT, LLM, TTS, and session context

(Optional) Additional enhancements may include the following:
+ Amazon Kendra or OpenSearch for context-aware RAG
+ Amazon DynamoDB for session memory
+ Amazon CloudWatch Logs and AWS X-Ray for traceability

## Summary
<a name="summary.bef787d6-f747-5bf0-a778-b2269b58d6c3"></a>

Speech and voice agents are intelligent systems that interact through natural conversations. By integrating speech interfaces with LLM reasoning and real-time streaming infrastructure, voice agents enable seamless, accessible, and scalable interactions.

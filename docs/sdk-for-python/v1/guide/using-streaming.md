---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/using-streaming.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Working with event streams
<a name="using-streaming"></a>

A standard request-response call works well when the service can return a complete result at once, but some workloads — live transcription, real-time inference, interactive conversations — produce data continuously while an operation is still running. For these cases, the SDK provides event stream operations that stay open and exchange a sequence of modeled events over time. The SDK supports multiple types of event streams:
+ A unidirectional *output event stream*: The service sends events to the application. The application reads events until the service closes the output.
+ A bidirectional *duplex event stream*: The application sends events through `input_stream` while it receives service events from the output side.

A service can also model an input-only event stream, in which only the application sends events. The pattern for sending events matches the input side of a bidirectional stream.

Every event stream's lifecycle is managed with an asynchronous context manager. Leaving the context closes its resources. The service model defines the generated input and output event types and any other events required to complete the operation.

This page explains how to invoke and handle output and bidirectional event streams.

## Consuming an output-only stream
<a name="using-streaming-output"></a>

An output event stream operation returns an open stream object. Calling the operation starts the request, but event data arrives later as the application iterates `output_stream`. Each item is one generated variant of the operation's output event union. The union represents the several possible event types.

The following example follows the stream lifecycle: call the operation, enter its asynchronous context, and wait for events with `async for`. It collects payload chunks and reports an event type that the current client doesn't recognize.

```
from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.models import (
    InvokeModelWithResponseStreamInput,
    ResponseStreamChunk,
    ResponseStreamUnknown,
)

async def collect_response_chunks(
    client: AsyncBedrockRuntimeClient,
    request: InvokeModelWithResponseStreamInput,
) -> list[bytes]:
    response = await client.invoke_model_with_response_stream(input=request)
    chunks: list[bytes] = []

    async with response as stream:
        async for event in stream.output_stream:
            if isinstance(event, ResponseStreamChunk):
                if event.value.bytes_:
                    chunks.append(event.value.bytes_)
            elif isinstance(event, ResponseStreamUnknown):
                raise RuntimeError(
                    f"Unknown output event: {event.tag}"
                )
            else:
                raise RuntimeError(
                    f"Unexpected output event: {type(event).__name__}"
                )

    return chunks
```

Leaving the asynchronous context closes the output stream even when event processing raises an exception. A modeled stream error can arrive while the application is iterating events; the SDK raises it as a generated service exception at that point. The event payloads and the signal that completes a stream vary by operation. For details, see the [invoke\_model\_with\_response\_stream()](clients/bedrock-runtime/operations/invoke_model_with_response_stream/) API reference.

## Using a bidirectional event stream
<a name="using-streaming-bidirectional"></a>

A bidirectional application sends input and receives output at the same time. Its overall lifecycle is:

1. Call the operation to open the stream, and enter the stream's asynchronous context.

1. Run a sender and receiver concurrently so that neither side waits for the other side to finish first.

1. Send modeled input events. After the last required input or completion event, close `input_stream` to indicate that no more input will follow.

1. Continue processing output events until the service closes the output side, and then leave the context to release the stream resources.

Bidirectional operations require the AWS Common Runtime (CRT) HTTP client as the client's transport. To opt in, install the client's `awscrt` extra and set `AWSCRTHTTPClient` as the transport. For more information, see [Use the AWS CRT client for bidirectional streaming](http-configuration.md#http-crt-streaming).

The following example uses Amazon Transcribe types to make the bidirectional pattern concrete. It represents application-provided input as an asynchronous iterable and delegates output events to an application-provided handler. This keeps producing and interpreting service payloads separate from opening, using, and closing the stream.

The following snippet contains only the imports that the rest of this section shares.

```
import asyncio
from collections.abc import AsyncIterable, Callable

from smithy_core.aio.interfaces.eventstream import EventPublisher, EventReceiver

from aws_sdk_transcribe_streaming.client import AsyncTranscribeStreamingClient
from aws_sdk_transcribe_streaming.models import (
    AudioEvent,
    AudioStream,
    AudioStreamAudioEvent,
    StartStreamTranscriptionInput,
    TranscriptEvent,
    TranscriptResultStream,
    TranscriptResultStreamTranscriptEvent,
    TranscriptResultStreamUnknown,
)
```

### Sending input events
<a name="using-streaming-publish"></a>

A bidirectional stream exposes `input_stream` for events sent by the application. The operation model defines an input event union, and each generated union variant represents one event type. For Amazon Transcribe, `AudioStreamAudioEvent` is the variant that carries an `AudioEvent`.

The sender wraps each prepared payload in the generated event classes and awaits `send()`. The asynchronous source determines how the application produces those payloads.

```
async def send_audio(
    input_stream: EventPublisher[AudioStream],
    audio_chunks: AsyncIterable[bytes],
) -> None:
    """Send prepared audio chunks to the input side of the stream."""
    try:
        async for chunk in audio_chunks:
            await input_stream.send(
                AudioStreamAudioEvent(value=AudioEvent(audio_chunk=chunk))
            )
    finally:
        await input_stream.close()
```

Closing `input_stream` half-closes the operation: the application can send no more input events, but the service can continue returning output events. The `finally` block closes the input side even if producing or sending a chunk fails. Closing this side doesn't close the output side or discard output that is still arriving.

### Receiving output events
<a name="using-streaming-receive"></a>

A bidirectional operation can return an initial modeled response before it starts yielding output events. This response contains the non-streaming members of the operation output; a separate receiver supplies the later events. The coordinating function below calls `await_output()` to wait for both, ignores the initial response, and passes the receiver to `receive_events()`.

Each received item is one variant of the generated output event union. The receiver validates the variant and delegates the modeled event payload to an application-provided handler. The handler determines how to interpret or store the service-specific payload.

```
async def receive_events(
    output_stream: EventReceiver[TranscriptResultStream],
    handle_event: Callable[[TranscriptEvent], None],
) -> None:
    """Receive modeled events and pass them to an application handler."""
    async for event in output_stream:
        if isinstance(event, TranscriptResultStreamUnknown):
            raise RuntimeError(f"Unknown stream event: {event.tag}")
        if not isinstance(event, TranscriptResultStreamTranscriptEvent):
            raise RuntimeError(f"Unexpected stream event: {type(event).__name__}")

        handle_event(event.value)
```

A modeled service error can also arrive as the application iterates the receiver; the SDK raises it as a generated exception. A generated `TranscriptResultStreamUnknown` value means that the service sent an event variant the installed SDK doesn't recognize. Its `tag` identifies that unrecognized variant so the application can report it without treating it as a known event.

When iteration ends, the service has closed `output_stream` and no more output events remain.

### Coordinating both sides
<a name="using-streaming-run"></a>

If an application waits for all input to finish before reading output, the service or client can block while output waits to be consumed. The following function accepts an application-configured request and event handler, starts the operation, enters the stream context, and uses `asyncio.gather()` to run the sender and receiver concurrently.

```
async def transcribe_audio(
    client: AsyncTranscribeStreamingClient,
    request: StartStreamTranscriptionInput,
    audio_chunks: AsyncIterable[bytes],
    handle_event: Callable[[TranscriptEvent], None],
) -> None:
    """Exchange events over a bidirectional transcription stream."""
    stream = await client.start_stream_transcription(input=request)

    async with stream:
        _, output_stream = await stream.await_output()
        if output_stream is None:
            raise RuntimeError("The service returned no output stream")
        await asyncio.gather(
            send_audio(stream.input_stream, audio_chunks),
            receive_events(output_stream, handle_event),
        )
```

On successful completion, `send_audio` closes the input side after the source has no more chunks, while `receive_events` continues until the service closes the output side. Leaving the asynchronous stream context then releases both sides.

The operation model defines how a bidirectional stream ends. Send any required completion event before closing `input_stream`.

See [Example 2: Stream audio bidirectionally with Amazon Transcribe](getting-started-transcribe-streaming.md) in the Getting Started chapter for a runnable application. The SDK repository also provides examples for a [prerecorded file](https://github.com/aws/aws-sdk-python/blob/develop/clients/aws-sdk-transcribe-streaming/examples/simple_file.py) and [live microphone input](https://github.com/aws/aws-sdk-python/blob/develop/clients/aws-sdk-transcribe-streaming/examples/simple_mic.py) on GitHub.

## Applying the pattern to other operations
<a name="using-streaming-other-operations"></a>

The following generated Python methods support HTTP/2 bidirectional event streams:
+ **Amazon Bedrock Runtime:** [invoke\_model\_with\_bidirectional\_stream()](clients/bedrock-runtime/operations/invoke_model_with_bidirectional_stream/)
+ **Amazon Connect Health:** [start\_medical\_scribe\_listening\_session()](clients/connecthealth/operations/start_medical_scribe_listening_session/)
+ **Amazon Lex Runtime V2:** [start\_conversation()](clients/lex-runtime-v2/operations/start_conversation/)
+ **Amazon Polly:** [start\_speech\_synthesis\_stream()](clients/polly/operations/start_speech_synthesis_stream/)
+ **Amazon Q Business:** [chat()](clients/qbusiness/operations/chat/)
+ **Amazon SageMaker Runtime HTTP2:** [invoke\_endpoint\_with\_bidirectional\_stream()](clients/sagemaker-runtime-http2/operations/invoke_endpoint_with_bidirectional_stream/)
+ **Amazon Transcribe Streaming:** [start\_call\_analytics\_stream\_transcription()](clients/transcribe-streaming/operations/start_call_analytics_stream_transcription/), [start\_medical\_scribe\_stream()](clients/transcribe-streaming/operations/start_medical_scribe_stream/), [start\_medical\_stream\_transcription()](clients/transcribe-streaming/operations/start_medical_stream_transcription/), and [start\_stream\_transcription()](clients/transcribe-streaming/operations/start_stream_transcription/)

Each operation defines its own input and output event variants and the signal used to finish the stream. Read the operation API reference before reusing the Amazon Transcribe coordination pattern. For the Amazon Nova Sonic protocol used by Bedrock Runtime, see [Use bidirectional streaming](bedrock-bidirectional-streaming.md).

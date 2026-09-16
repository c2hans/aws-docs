---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/bedrock-bidirectional-streaming.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use bidirectional streaming
<a name="bedrock-bidirectional-streaming"></a>

A bidirectional event stream lets the application publish input events to the service while it receives output events over the same connection. Use it with a compatible model when the application must keep sending input, such as live audio, while it receives model output. The event protocol depends on the selected model. For an introduction to event streams, see [Working with event streams](using-streaming.md).

This example uses Amazon Nova 2 Sonic. The program loads its input audio from a `test.pcm` file in the working directory. To provide it, do one of the following:
+ Use the SDK repository's [sample `test.pcm` file](https://github.com/aws/aws-sdk-python/blob/develop/clients/aws-sdk-bedrock-runtime/tests/integration/assets/test.pcm) on GitHub. The sample contains headerless, 16 kHz, signed 16-bit, mono PCM audio.
+ Use your own recording saved in the same format, and set `audio_file` in `main` to its path.

For request and response details, see the [invoke\_model\_with\_bidirectional\_stream()](clients/bedrock-runtime/operations/invoke_model_with_bidirectional_stream/) API reference.

Bidirectional streaming requires the AWS Common Runtime (CRT) HTTP client, which supports HTTP/2 bidirectional event streams. The SDK's default HTTP transport does not, so opt in by installing the client's `awscrt` extra and passing `transport=AWSCRTHTTPClient()` when you resolve the configuration. For more information, see [Use the AWS CRT client for bidirectional streaming](http-configuration.md#http-crt-streaming).

```
python -m pip install "aws-sdk-bedrock-runtime[awscrt]"
```

 **Imports**

```
import asyncio
import base64
import json
import uuid
from pathlib import Path
from typing import Any

from smithy_http.aio.crt import AWSCRTHTTPClient

from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import AsyncBedrockRuntimeConfig
from aws_sdk_bedrock_runtime.models import (
    BidirectionalInputPayloadPart,
    InvokeModelWithBidirectionalStreamInputChunk,
    InvokeModelWithBidirectionalStreamOperationInput,
    InvokeModelWithBidirectionalStreamOutputChunk,
    InvokeModelWithBidirectionalStreamOutputInternalServerException,
    InvokeModelWithBidirectionalStreamOutputModelStreamErrorException,
    InvokeModelWithBidirectionalStreamOutputModelTimeoutException,
    InvokeModelWithBidirectionalStreamOutputServiceUnavailableException,
    InvokeModelWithBidirectionalStreamOutputThrottlingException,
    InvokeModelWithBidirectionalStreamOutputUnknown,
    InvokeModelWithBidirectionalStreamOutputValidationException,
)
```

The program sends the audio in 512-byte chunks and sleeps 0.016 seconds after each chunk, simulating the real-time delay of live audio. The first four constants control that timing. `DEFAULT_SYSTEM_PROMPT` is the system instruction that the session sends before the audio, and `BIDIRECTIONAL_STREAM_ERRORS` groups the modeled stream-error events. The validation helper rejects a missing or empty audio file before any network call.

```
CHUNK_SIZE = 512
SILENCE_CHUNKS = 125
CHUNK_INTERVAL_SECONDS = 0.016
RESPONSE_WAIT_SECONDS = 3

DEFAULT_SYSTEM_PROMPT = (
    "You are a friendly assistant. Keep your responses short, "
    "generally one or two sentences."
)

BIDIRECTIONAL_STREAM_ERRORS = (
    InvokeModelWithBidirectionalStreamOutputInternalServerException,
    InvokeModelWithBidirectionalStreamOutputModelStreamErrorException,
    InvokeModelWithBidirectionalStreamOutputModelTimeoutException,
    InvokeModelWithBidirectionalStreamOutputServiceUnavailableException,
    InvokeModelWithBidirectionalStreamOutputThrottlingException,
    InvokeModelWithBidirectionalStreamOutputValidationException,
)
```

```
def validate_audio_input(audio_file: Path) -> None:
    """Require a nonempty audio file supplied by the caller."""
    if not audio_file.is_file() or audio_file.stat().st_size == 0:
        raise ValueError(f"Audio file is missing or empty: {audio_file}")
```

## Define and send model-native events
<a name="bedrock-bidirectional-events"></a>

Nova 2 Sonic input events are JSON documents. The session nests three scopes, and an event pair opens and closes each scope: `sessionStart` and `sessionEnd` wrap the connection, `promptStart` and `promptEnd` wrap one prompt, and `contentStart` and `contentEnd` wrap each content block inside the prompt. A content block carries either text or audio. More than one content block opens and closes on the same stream, so each event carries the `promptName` and `contentName` of the scope it belongs to. The templates leave those values as `%s` placeholders. The following templates define every event that this example sends.

```
START_SESSION_EVENT = """{
    "event": {
        "sessionStart": {
            "inferenceConfiguration": {
                "maxTokens": 1024,
                "topP": 0.9,
                "temperature": 0.7
            }
        }
    }
}"""

START_PROMPT_EVENT = """{
    "event": {
        "promptStart": {
            "promptName": "%s",
            "textOutputConfiguration": {
                "mediaType": "text/plain"
            },
            "audioOutputConfiguration": {
                "mediaType": "audio/lpcm",
                "sampleRateHertz": 24000,
                "sampleSizeBits": 16,
                "channelCount": 1,
                "voiceId": "matthew",
                "encoding": "base64",
                "audioType": "SPEECH"
            }
        }
    }
}"""

TEXT_CONTENT_START_EVENT = """{
    "event": {
        "contentStart": {
            "promptName": "%s",
            "contentName": "%s",
            "type": "TEXT",
            "interactive": true,
            "role": "%s",
            "textInputConfiguration": {
                "mediaType": "text/plain"
            }
        }
    }
}"""

TEXT_INPUT_EVENT = """{
    "event": {
        "textInput": {
            "promptName": "%s",
            "contentName": "%s",
            "content": "%s"
        }
    }
}"""

AUDIO_CONTENT_START_EVENT = """{
    "event": {
        "contentStart": {
            "promptName": "%s",
            "contentName": "%s",
            "type": "AUDIO",
            "interactive": true,
            "role": "USER",
            "audioInputConfiguration": {
                "mediaType": "audio/lpcm",
                "sampleRateHertz": 16000,
                "sampleSizeBits": 16,
                "channelCount": 1,
                "audioType": "SPEECH",
                "encoding": "base64"
            }
        }
    }
}"""

AUDIO_INPUT_EVENT = """{
    "event": {
        "audioInput": {
            "promptName": "%s",
            "contentName": "%s",
            "content": "%s"
        }
    }
}"""

CONTENT_END_EVENT = """{
    "event": {
        "contentEnd": {
            "promptName": "%s",
            "contentName": "%s"
        }
    }
}"""

PROMPT_END_EVENT = """{
    "event": {
        "promptEnd": {
            "promptName": "%s"
        }
    }
}"""

SESSION_END_EVENT = """{
    "event": {
        "sessionEnd": {}
    }
}"""
```

The following function encodes one filled-in template and wraps it in the generated input union before sending it to the stream.

```
async def send_event(stream: Any, event_json: str) -> None:
    """Send one JSON input event to the stream."""
    await stream.input_stream.send(
        InvokeModelWithBidirectionalStreamInputChunk(
            value=BidirectionalInputPayloadPart(bytes_=event_json.encode("utf-8"))
        )
    )
```

## Publish audio in real time
<a name="bedrock-bidirectional-publish"></a>

Read 512-byte chunks, encode them as base64, and wait `CHUNK_INTERVAL_SECONDS` after each chunk to keep the real-time pacing. After the file, the function sends two seconds of silence, waits three seconds for the model to respond, then closes the audio content, prompt, and session in order.

```
async def publish_audio(
    stream: Any,
    prompt_name: str,
    content_name: str,
    audio_file: Path,
) -> None:
    """Publish caller-provided PCM audio, trailing silence, and end events."""
    try:
        chunks_sent = 0
        with audio_file.open("rb") as source:
            while chunk := source.read(CHUNK_SIZE):
                chunks_sent += 1
                encoded = base64.b64encode(chunk).decode("utf-8")
                await send_event(
                    stream, AUDIO_INPUT_EVENT % (prompt_name, content_name, encoded)
                )
                await asyncio.sleep(CHUNK_INTERVAL_SECONDS)
        if chunks_sent == 0:
            raise RuntimeError(f"No audio read from {audio_file}")

        silence = base64.b64encode(bytes(CHUNK_SIZE)).decode("utf-8")
        for _ in range(SILENCE_CHUNKS):
            await send_event(
                stream, AUDIO_INPUT_EVENT % (prompt_name, content_name, silence)
            )
            await asyncio.sleep(CHUNK_INTERVAL_SECONDS)

        await send_event(stream, CONTENT_END_EVENT % (prompt_name, content_name))
        await asyncio.sleep(RESPONSE_WAIT_SECONDS)
        await send_event(stream, PROMPT_END_EVENT % prompt_name)
        await send_event(stream, SESSION_END_EVENT)
    finally:
        await stream.input_stream.close()
```

## Receive text and audio output
<a name="bedrock-bidirectional-receive"></a>

Await the service output before iterating it. Narrow every generated output event, decode its JSON payload, collect text, and record audio output. Stop when the model sends `completionEnd`.

```
async def receive_events(stream: Any) -> tuple[list[str], bool, bool]:
    """Receive narrowed output events until the model signals completion."""
    _, output_stream = await stream.await_output()
    if output_stream is None:
        raise RuntimeError("The service returned no output stream")

    text_output: list[str] = []
    got_audio = False
    completed = False
    async for event in output_stream:
        if isinstance(event, InvokeModelWithBidirectionalStreamOutputChunk):
            payload = event.value.bytes_
            if not payload:
                continue
            event_data = json.loads(payload.decode("utf-8")).get("event", {})
            if "textOutput" in event_data:
                text_output.append(event_data["textOutput"].get("content", ""))
            if "audioOutput" in event_data:
                got_audio = True
            if "completionEnd" in event_data:
                completed = True
                break
        elif isinstance(event, BIDIRECTIONAL_STREAM_ERRORS):
            raise RuntimeError(event.value.message or type(event).__name__)
        elif isinstance(event, InvokeModelWithBidirectionalStreamOutputUnknown):
            raise RuntimeError(f"Unknown bidirectional stream event: {event.tag}")
        else:
            raise RuntimeError(
                f"Unexpected bidirectional stream event: {type(event).__name__}"
            )
    return text_output, got_audio, completed
```

## Open the stream and exchange audio
<a name="bedrock-bidirectional-run"></a>

Open the stream, then send the `init_events` list in protocol order: start the session and the prompt, send the system instruction as a complete text content block, and open the user audio content block. Then run the publisher and receiver concurrently, so the program keeps sending audio while it receives output. Verify that the stream completed and produced both text and audio before accepting the result.

```
async def invoke_model_with_bidirectional_stream(
    client: AsyncBedrockRuntimeClient,
    audio_file: Path,
) -> str:
    """Open a Nova 2 Sonic stream and concurrently send and receive audio."""
    validate_audio_input(audio_file)

    stream = await client.invoke_model_with_bidirectional_stream(
        InvokeModelWithBidirectionalStreamOperationInput(
            model_id="amazon.nova-2-sonic-v1:0"
        )
    )
    prompt_name = str(uuid.uuid4())
    system_content_name = str(uuid.uuid4())
    audio_content_name = str(uuid.uuid4())

    init_events = [
        START_SESSION_EVENT,
        START_PROMPT_EVENT % prompt_name,
        TEXT_CONTENT_START_EVENT % (prompt_name, system_content_name, "SYSTEM"),
        TEXT_INPUT_EVENT % (prompt_name, system_content_name, DEFAULT_SYSTEM_PROMPT),
        CONTENT_END_EVENT % (prompt_name, system_content_name),
        AUDIO_CONTENT_START_EVENT % (prompt_name, audio_content_name),
    ]

    async with stream:
        for event in init_events:
            await send_event(stream, event)
        _, received = await asyncio.gather(
            publish_audio(stream, prompt_name, audio_content_name, audio_file),
            receive_events(stream),
        )

    text_output, got_audio, completed = received
    if not completed or not text_output or not got_audio:
        raise RuntimeError(
            "The stream ended without completion, text, and audio output"
        )
    # The first text event is the transcript of the input audio, and the
    # following events are the model's reply, one segment per event.
    text = "\n".join(part.strip() for part in text_output)
    print(text)
    return text
```

The entry point creates the client with the CRT transport and runs the streaming session. Run the program with `python invoke_model_with_bidirectional_stream.py`.

```
async def main() -> None:
    """Create a client with the CRT transport and run the example."""
    # Load the input audio (headerless, 16 kHz, signed 16-bit, mono PCM).
    audio_file = Path("test.pcm")
    # Bidirectional streaming requires the AWS CRT HTTP client.
    config = await AsyncBedrockRuntimeConfig.resolve(
        region="us-east-1",
        transport=AWSCRTHTTPClient(),
    )
    async with AsyncBedrockRuntimeClient(config=config) as client:
        await invoke_model_with_bidirectional_stream(client, audio_file)

if __name__ == "__main__":
    asyncio.run(main())
```

The example follows the same event sequence as [`test_bidirectional_streaming.py`](https://github.com/aws/aws-sdk-python/blob/develop/clients/aws-sdk-bedrock-runtime/tests/integration/test_bidirectional_streaming.py) in the AWS SDK for Python repository on GitHub.

## More information
<a name="bedrock-bidirectional-more-info"></a>
+ [Speech-to-Speech (Amazon Nova 2 Sonic)](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html) in the Amazon Nova User Guide
+ [InvokeModelWithBidirectionalStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithBidirectionalStream.html) in the Amazon Bedrock API Reference

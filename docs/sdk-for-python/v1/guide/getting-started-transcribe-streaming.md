---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/getting-started-transcribe-streaming.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Example 2: Stream audio bidirectionally with Amazon Transcribe
<a name="getting-started-transcribe-streaming"></a>

This example uses `AsyncTranscribeStreamingClient` to send prerecorded audio to Amazon Transcribe while receiving transcription results over the same HTTP/2 bidirectional event stream. It uses `asyncio.gather()` to publish audio and receive completed transcript segments concurrently.

## Before you begin
<a name="getting-started-transcribe-streaming-before"></a>

Complete [Prerequisites and installation](getting-started-prerequisites-installation.md) and [Authenticating with AWS using the AWS SDK for Python](getting-started-authentication.md). This example also requires the following:
+ The identity selected by your authentication method must allow `transcribe:StartStreamTranscription`. To learn how IAM policies grant permissions like these, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ Use the SDK repository's [sample `test.wav` file](https://github.com/aws/aws-sdk-python/blob/develop/clients/aws-sdk-transcribe-streaming/examples/test.wav). The sample contains 16 kHz, 16-bit, mono PCM audio. The example validates the WAV format and sends only its audio frames, without the WAV container header.

Bidirectional streaming requires the AWS Common Runtime (CRT) HTTP client, which the example selects as the client's transport. Opt in by installing the client's `awscrt` extra. For more information, see [Use the AWS CRT client for bidirectional streaming](http-configuration.md#http-crt-streaming).

```
python -m pip install "aws-sdk-transcribe-streaming[awscrt]"
```

Download the linked file in your browser and save it as `test.wav` in the directory where you will create the example. Alternatively, download it with Python:

```
python -c "from urllib.request import urlretrieve; urlretrieve('https://github.com/aws/aws-sdk-python/raw/refs/heads/develop/clients/aws-sdk-transcribe-streaming/examples/test.wav', 'test.wav')"
```

**Warning**
Streaming audio with Amazon Transcribe can incur charges. Review [Amazon Transcribe pricing](https://aws.amazon.com/transcribe/pricing/) before repeated use.

## Write the code
<a name="getting-started-transcribe-streaming-code"></a>

Create a file named `getting_started_transcribe.py` with the following code:

```
"""Transcribe a prerecorded audio stream with the AWS SDK for Python."""

import asyncio
import wave
from pathlib import Path

from smithy_http.aio.crt import AWSCRTHTTPClient

from aws_sdk_transcribe_streaming.client import AsyncTranscribeStreamingClient
from aws_sdk_transcribe_streaming.config import AsyncTranscribeStreamingConfig
from aws_sdk_transcribe_streaming.models import (
    AudioEvent,
    AudioStreamAudioEvent,
    LanguageCode,
    MediaEncoding,
    StartStreamTranscriptionInput,
    TranscriptResultStreamTranscriptEvent,
)

AUDIO_FILE = Path("test.wav")
SAMPLE_RATE = 16_000
BYTES_PER_SAMPLE = 2
CHANNELS = 1
CHUNK_FRAMES = 1_600  # 100 ms of audio

async def send_audio(stream) -> None:
    loop = asyncio.get_running_loop()
    started = loop.time()
    audio_seconds = 0.0
    chunks_sent = 0

    try:
        with wave.open(str(AUDIO_FILE), "rb") as source:
            audio_format = (
                source.getnchannels(),
                source.getsampwidth(),
                source.getframerate(),
                source.getcomptype(),
            )
            expected_format = (
                CHANNELS,
                BYTES_PER_SAMPLE,
                SAMPLE_RATE,
                "NONE",
            )
            if audio_format != expected_format:
                raise ValueError(
                    "test.wav must be uncompressed 16 kHz, "
                    "16-bit, mono PCM audio"
                )

            while chunk := await asyncio.to_thread(
                source.readframes, CHUNK_FRAMES
            ):
                await stream.input_stream.send(
                    AudioStreamAudioEvent(
                        value=AudioEvent(audio_chunk=chunk)
                    )
                )
                chunks_sent += 1
                audio_seconds += len(chunk) / (
                    BYTES_PER_SAMPLE * SAMPLE_RATE * CHANNELS
                )
                delay = started + audio_seconds - loop.time()
                if delay > 0:
                    await asyncio.sleep(delay)

        if chunks_sent == 0:
            raise RuntimeError(f"No audio read from {AUDIO_FILE}")
    finally:
        await stream.input_stream.close()

async def print_transcripts(stream) -> None:
    _, output_stream = await stream.await_output()
    if output_stream is None:
        raise RuntimeError("The service returned no output stream")

    async for event in output_stream:
        if not isinstance(
            event, TranscriptResultStreamTranscriptEvent
        ):
            raise RuntimeError(
                f"Unexpected stream event: {type(event).__name__}"
            )

        transcript = event.value.transcript
        if transcript is None:
            continue
        for result in transcript.results or []:
            if result.is_partial:
                continue
            alternatives = result.alternatives or []
            if alternatives and alternatives[0].transcript:
                print(alternatives[0].transcript)

async def main() -> None:
    # Bidirectional streaming requires the AWS CRT HTTP client.
    config = await AsyncTranscribeStreamingConfig.resolve(
        region="us-east-1",
        transport=AWSCRTHTTPClient(),
    )
    async with AsyncTranscribeStreamingClient(config=config) as client:
        stream = await client.start_stream_transcription(
            input=StartStreamTranscriptionInput(
                language_code=LanguageCode.EN_US,
                media_sample_rate_hertz=SAMPLE_RATE,
                media_encoding=MediaEncoding.PCM,
            )
        )

        async with stream:
            await asyncio.gather(
                send_audio(stream),
                print_transcripts(stream),
            )

if __name__ == "__main__":
    asyncio.run(main())
```

Amazon Transcribe returns partial and final results while audio is streamed. The example validates and paces PCM audio in `send_audio()`, wraps each chunk in the generated input event type, receives final results concurrently in `print_transcripts()`, and closes the input stream in a `finally` block. The client resolves credentials from the default credential chain and sets only the AWS Region explicitly.

## Run the application
<a name="getting-started-transcribe-streaming-run"></a>

Run the program from the directory that contains `getting_started_transcribe.py` and `test.wav`:

```
python getting_started_transcribe.py
```

## Success
<a name="getting-started-transcribe-streaming-success"></a>

A successful run prints one or more completed transcript segments and then exits.

## Cleanup
<a name="getting-started-transcribe-streaming-cleanup"></a>

This example creates no persistent AWS resources. It closes the input stream after sending the file, and the `async with` block closes the bidirectional stream when the application finishes.

## Next steps
<a name="getting-started-transcribe-streaming-next-steps"></a>
+ For service concepts, audio requirements, and streaming best practices, see [Transcribing streaming audio](https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html) in the *Amazon Transcribe Developer Guide*.
+ For generated request and response types, see the [`start_stream_transcription()` API reference](https://docs.aws.amazon.com/sdk-for-python/v1/reference/clients/transcribe-streaming/operations/start_stream_transcription/).
+ For more information about publishing and consuming event streams, see [Working with event streams](using-streaming.md).
+ For complete SDK repository examples, see the [Amazon Transcribe streaming examples](https://github.com/aws/aws-sdk-python/tree/develop/clients/aws-sdk-transcribe-streaming/examples). The directory includes one example for a prerecorded file and another for live microphone input.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Python. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-python` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

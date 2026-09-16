---
source_url: https://docs.aws.amazon.com/sdk-for-python/v1/guide/working-with-boto3-coexistence.html
---

**Developer Preview** — This documentation covers the AWS SDK for Python, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use both SDKs in one application
<a name="working-with-boto3-coexistence"></a>

You can use the AWS SDK for Python and Boto3 together in the same application. The most common reasons to combine both SDKs are:
+ A service or operation you need isn't yet available in the AWS SDK for Python, so you use Boto3 for that service while using the new SDK for async or streaming workloads.
+ You want to evaluate the async capabilities of the AWS SDK for Python in an existing Boto3 application without rewriting your synchronous code.

Keep existing Boto3 code when it continues to meet your application's needs, and add the AWS SDK for Python for supported capabilities such as native asynchronous APIs, concurrent I/O, bidirectional streaming, modular service packages, and generated types.

## Configuration and credentials
<a name="working-with-boto3-configuration"></a>

Both SDKs can resolve standard AWS settings and authenticate as the same AWS identity, but each SDK resolves and refreshes its own configuration independently. Programmatic settings aren't shared between the SDKs.

Key points:
+ A profile or Region selected with a Boto3 `Session` doesn't apply to AWS SDK for Python configuration resolution.
+ The generated asynchronous service configuration requires a Region. Resolution fails if no Region is available.
+ Configure equivalent options for each SDK when necessary (Region, credentials, endpoint overrides).

Before running either scenario, make a Region available to each SDK through standard AWS settings (environment variables or config files) or an SDK-specific override.

## Combining synchronous and asynchronous code
<a name="working-with-boto3-sync-async"></a>

How you combine synchronous and asynchronous code depends on which SDK is primary:

| Your application is... | Pattern | Example |
| --- | --- | --- |
| Async-primary (AWS SDK for Python owns the event loop) | Use asyncio.to\_thread() for Boto3 calls so they don't block the event loop | [Scenario 1](#working-with-boto3-sdk-primary) |
| Sync-primary (Boto3 owns the main thread) | Use asyncio.run() to enter an async workflow for the AWS SDK for Python | [Scenario 2](#working-with-boto3-coexistence-example) |

For details on running asynchronous code, see [Running asynchronous code](using-async.md#using-async-run). For keeping blocking work off the event loop, see [Keeping blocking work off the event loop](using-async.md#using-async-blocking-work).

## Before you begin
<a name="working-with-boto3-before"></a>

Both scenarios require the following:
+ Complete [Prerequisites and installation](getting-started-prerequisites-installation.md) and [Authenticating with AWS using the AWS SDK for Python](getting-started-authentication.md).
+ A Region available to both SDKs through standard AWS settings or SDK-specific configuration.
+ IAM permissions as described in each scenario.

**Warning**
Both scenarios use AWS services that can incur charges. Use non-production resources and review pricing for the relevant services before repeated use.

## Scenario 1: Async-primary application with Boto3 for unsupported services
<a name="working-with-boto3-sdk-primary"></a>

This scenario represents a new asynchronous application that uses `AsyncBedrockRuntimeClient` for output streaming. The application sends a request to Amazon Bedrock Runtime and asynchronously processes response events as the model generates output. After the stream completes, the application uses Boto3 to save the prompt and completed response as a JSON object in Amazon S3, which isn't yet available in the AWS SDK for Python.

**When to use this pattern:** Your application is async-first and you need Boto3 only for services or features not yet available in the AWS SDK for Python.

### Install
<a name="working-with-boto3-sdk-primary-install"></a>

```
python -m pip install boto3 aws-sdk-bedrock-runtime
```

### Additional requirements
<a name="working-with-boto3-sdk-primary-requirements"></a>
+ Access to an Amazon Bedrock model that supports `ConverseStream` in the configured AWS Region. This example processes text output only.
+ An Amazon S3 bucket and key where the example can store the model response.
+ The identity resolved by the AWS SDK for Python allows `bedrock:InvokeModelWithResponseStream` for the selected model.
+ The identity resolved by Boto3 allows `s3:PutObject` for the output object.

### Write the code
<a name="working-with-boto3-sdk-primary-code"></a>

Create a file named `sdk_primary_with_boto3.py` with the following code:

```
"""Use Boto3 from an asynchronous AWS SDK for Python application."""

import argparse
import asyncio
import json

import boto3

from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
from aws_sdk_bedrock_runtime.config import AsyncBedrockRuntimeConfig
from aws_sdk_bedrock_runtime.models import (
    ContentBlockDeltaText,
    ContentBlockText,
    ConverseStreamInput,
    ConverseStreamOutputContentBlockDelta,
    ConverseStreamOutputMessageStop,
    ConverseStreamOutputMetadata,
    ConverseStreamOutputUnknown,
    InternalServerException,
    Message,
    ModelStreamErrorException,
    ServiceUnavailableException,
    ThrottlingException,
    ValidationException,
)

DEFAULT_MODEL_ID = "global.amazon.nova-2-lite-v1:0"
MODELED_STREAM_ERRORS = (
    InternalServerException,
    ModelStreamErrorException,
    ServiceUnavailableException,
    ThrottlingException,
    ValidationException,
)

async def stream_response(
    client: AsyncBedrockRuntimeClient,
    model_id: str,
    prompt: str,
) -> str:
    text_parts: list[str] = []
    stop_reason = None
    got_metadata = False
    try:
        response = await client.converse_stream(
            input=ConverseStreamInput(
                model_id=model_id,
                messages=[
                    Message(
                        role="user",
                        content=[ContentBlockText(value=prompt)],
                    )
                ],
            )
        )
        async with response as stream:
            async for event in stream.output_stream:
                if isinstance(
                    event, ConverseStreamOutputContentBlockDelta
                ):
                    delta = event.value.delta
                    if isinstance(delta, ContentBlockDeltaText):
                        text_parts.append(delta.value)
                        print(delta.value, end="", flush=True)
                elif isinstance(event, ConverseStreamOutputMessageStop):
                    stop_reason = event.value.stop_reason
                elif isinstance(event, ConverseStreamOutputMetadata):
                    got_metadata = True
                elif isinstance(event, ConverseStreamOutputUnknown):
                    raise RuntimeError(
                        f"Unknown stream event: {event.tag}"
                    )
    except MODELED_STREAM_ERRORS as error:
        raise RuntimeError(
            error.message or type(error).__name__
        ) from error

    if not text_parts or stop_reason is None or not got_metadata:
        raise RuntimeError("Amazon Bedrock returned an incomplete response")
    print()
    return "".join(text_parts)

def save_response(
    bucket: str,
    key: str,
    prompt: str,
    response: str,
) -> None:
    body = json.dumps(
        {"prompt": prompt, "response": response},
        ensure_ascii=False,
        indent=2,
    ).encode("utf-8")
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=body,
        ContentType="application/json",
    )

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("bucket")
    parser.add_argument("key")
    parser.add_argument("prompt")
    parser.add_argument("--model-id", default=DEFAULT_MODEL_ID)
    return parser.parse_args()

async def main(args: argparse.Namespace) -> None:
    config = await AsyncBedrockRuntimeConfig.resolve()
    async with AsyncBedrockRuntimeClient(config=config) as client:
        response = await stream_response(
            client,
            args.model_id,
            args.prompt,
        )

        await asyncio.to_thread(
            save_response,
            args.bucket,
            args.key,
            args.prompt,
            response,
        )
        print(f"Saved response to s3://{args.bucket}/{args.key}")

if __name__ == "__main__":
    asyncio.run(main(parse_args()))
```

### How it works
<a name="working-with-boto3-sdk-primary-how"></a>

The AWS SDK for Python owns the event loop and the application's primary workflow:

1. `AsyncBedrockRuntimeConfig.resolve()` resolves Region and credentials from standard AWS settings.

1. `stream_response()` consumes response events that Amazon Bedrock Runtime streams as the model generates output.

1. After the stream completes, `asyncio.to_thread()` runs the synchronous Boto3 S3 upload without blocking the event loop.

`AsyncBedrockRuntimeConfig.resolve()` and `boto3.client("s3")` independently use the standard AWS settings configured for the environment. The application doesn't copy the Region or credentials from one SDK to the other.

### Run the application
<a name="working-with-boto3-sdk-primary-run"></a>

Pass the output bucket, output key, and model prompt:

```
python sdk_primary_with_boto3.py amzn-s3-demo-bucket responses/example.json "Give three tips for writing clear Python code."
```

### Success
<a name="working-with-boto3-sdk-primary-success"></a>

A successful run prints the streamed model response and the output Amazon S3 URI. The output object contains the prompt and completed response as UTF-8 JSON.

### Cleanup
<a name="working-with-boto3-sdk-primary-cleanup"></a>

This example doesn't create persistent resources other than the output Amazon S3 object. Delete that object when you no longer need it.

### Next steps
<a name="working-with-boto3-sdk-primary-next-steps"></a>
+ For how the SDK resolves configuration values, see [Configuration resolution](config-resolution.md). For how it finds credentials, see [Credential providers](credential-providers.md).
+ For running blocking functions from an asynchronous application, see [Keeping blocking work off the event loop](using-async.md#using-async-blocking-work).
+ For more Amazon Bedrock Runtime operations and streaming behavior, see [Amazon Bedrock Runtime](services-bedrock.md).
+ For generated Amazon Bedrock Runtime request, response, and event types, see the [ConverseStream API reference](clients/bedrock-runtime/operations/converse_stream/).
+ For Boto3 S3 operations, see the [SDK for Python (Boto3) S3 API reference](https://docs.aws.amazon.com/boto3/latest/reference/services/s3.html).

## Scenario 2: Sync-primary application adding bidirectional streaming
<a name="working-with-boto3-coexistence-example"></a>

This scenario represents an existing synchronous application that uses Boto3 to download PCM audio from Amazon S3. The application adds `AsyncTranscribeStreamingClient` to send audio to Amazon Transcribe and receive transcript events concurrently over a bidirectional stream. After the stream completes, the existing Boto3 workflow uploads the completed transcript to Amazon S3.

**When to use this pattern:** You have an existing Boto3 application and want to add async or streaming capabilities for specific operations without rewriting your synchronous code.

### Install
<a name="working-with-boto3-coexistence-install"></a>

Install the `awscrt` extra to use the AWS Common Runtime (CRT) HTTP client that bidirectional streaming requires. For more information, see [Use the AWS CRT client for bidirectional streaming](http-configuration.md#http-crt-streaming).

```
python -m pip install boto3 "aws-sdk-transcribe-streaming[awscrt]"
```

### Additional requirements
<a name="working-with-boto3-coexistence-requirements"></a>
+ An Amazon S3 object containing US English audio as headerless, signed 16-bit little-endian, mono PCM sampled at 16 kHz. WAV files include a container header and aren't valid input for this example. To transcribe another supported language, change `LanguageCode.EN_US` in the request. To try this example, you can download a [sample PCM clip](https://github.com/aws/aws-sdk-python/blob/a2e87107936bb897863cdd31679f73b6fbdb1802/clients/aws-sdk-bedrock-runtime/tests/integration/assets/test.pcm) (`test.pcm`) from the aws-sdk-python repository on GitHub.
+ An output Amazon S3 bucket and key where the example can store the UTF-8 transcript.
+ The identity resolved by Boto3 allows `s3:GetObject` for the input object and `s3:PutObject` for the output object.
+ The identity resolved by the AWS SDK for Python allows `transcribe:StartStreamTranscription`.

### Write the code
<a name="working-with-boto3-coexistence-code"></a>

Create a file named `boto3_with_streaming.py` with the following code:

```
"""Add bidirectional transcription to a synchronous Boto3 application."""

import argparse
import asyncio
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

import boto3

from smithy_http.aio.crt import AWSCRTHTTPClient

from aws_sdk_transcribe_streaming.client import (
    AsyncTranscribeStreamingClient,
)
from aws_sdk_transcribe_streaming.config import (
    AsyncTranscribeStreamingConfig,
)
from aws_sdk_transcribe_streaming.models import (
    AudioEvent,
    AudioStreamAudioEvent,
    BadRequestException,
    ConflictException,
    InternalFailureException,
    LanguageCode,
    LimitExceededException,
    MediaEncoding,
    ServiceUnavailableException,
    StartStreamTranscriptionInput,
    TranscriptResultStreamTranscriptEvent,
    TranscriptResultStreamUnknown,
)

SAMPLE_RATE = 16_000
BYTES_PER_SAMPLE = 2
CHUNK_SIZE = 3_200  # 100 ms of 16 kHz, 16-bit, mono PCM
MODELED_STREAM_ERRORS = (
    BadRequestException,
    ConflictException,
    InternalFailureException,
    LimitExceededException,
    ServiceUnavailableException,
)

async def send_audio(stream: Any, audio_path: Path) -> None:
    loop = asyncio.get_running_loop()
    started = loop.time()
    audio_seconds = 0.0

    try:
        with audio_path.open("rb") as source:
            while chunk := await asyncio.to_thread(
                source.read, CHUNK_SIZE
            ):
                await stream.input_stream.send(
                    AudioStreamAudioEvent(
                        value=AudioEvent(audio_chunk=chunk)
                    )
                )
                audio_seconds += len(chunk) / (
                    BYTES_PER_SAMPLE * SAMPLE_RATE
                )
                delay = started + audio_seconds - loop.time()
                if delay > 0:
                    await asyncio.sleep(delay)
    finally:
        await stream.input_stream.close()

async def receive_transcripts(stream: Any) -> list[str]:
    transcripts: list[str] = []
    try:
        _, output_stream = await stream.await_output()
        if output_stream is None:
            raise RuntimeError("Amazon Transcribe returned no output stream")

        async for event in output_stream:
            if isinstance(event, TranscriptResultStreamUnknown):
                raise RuntimeError(
                    f"Unknown stream event: {event.tag}"
                )
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
                    transcripts.append(alternatives[0].transcript)
    except MODELED_STREAM_ERRORS as error:
        raise RuntimeError(
            error.message or type(error).__name__
        ) from error

    return transcripts

async def transcribe_audio(audio_path: Path) -> str:
    # Bidirectional streaming requires the AWS CRT HTTP client.
    config = await AsyncTranscribeStreamingConfig.resolve(
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
            _, transcripts = await asyncio.gather(
                send_audio(stream, audio_path),
                receive_transcripts(stream),
            )

        return "\n".join(transcripts)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_bucket")
    parser.add_argument("input_key")
    parser.add_argument("output_bucket")
    parser.add_argument("output_key")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    s3 = boto3.client("s3")

    with TemporaryDirectory() as temp_directory:
        audio_path = Path(temp_directory) / "input.pcm"
        s3.download_file(
            args.input_bucket,
            args.input_key,
            str(audio_path),
        )
        print(
            f"Downloaded s3://{args.input_bucket}/{args.input_key}"
        )

        transcript = asyncio.run(transcribe_audio(audio_path))

    if not transcript:
        raise RuntimeError("Amazon Transcribe returned no completed text")

    s3.put_object(
        Bucket=args.output_bucket,
        Key=args.output_key,
        Body=transcript.encode("utf-8"),
        ContentType="text/plain; charset=utf-8",
    )
    print(
        f"Uploaded transcript to "
        f"s3://{args.output_bucket}/{args.output_key}"
    )

if __name__ == "__main__":
    main()
```

### How it works
<a name="working-with-boto3-coexistence-how"></a>

The synchronous `main()` function keeps the existing Boto3 workflow unchanged:

1. Boto3 downloads the PCM audio from Amazon S3.

1. `asyncio.run()` enters the async transcription workflow once — the event loop starts and stops within this call.

1. Inside the async context, `asyncio.gather()` sends audio and receives transcript events concurrently over one bidirectional HTTP/2 stream.

1. After `asyncio.run()` returns, Boto3 uploads the completed transcript to Amazon S3 synchronously.

`AsyncTranscribeStreamingConfig.resolve()` and `boto3.client("s3")` independently use the standard AWS settings configured for the environment. The application doesn't pass the Region or credentials between the SDKs.

### Run the application
<a name="working-with-boto3-coexistence-run"></a>

Pass the input bucket and PCM object key, followed by the output bucket and transcript object key:

```
python boto3_with_streaming.py amzn-s3-demo-input-bucket audio/test.pcm amzn-s3-demo-output-bucket transcripts/test.txt
```

### Success
<a name="working-with-boto3-coexistence-success"></a>

A successful run prints the input and output Amazon S3 URIs. The output object contains the completed transcript segments returned by Amazon Transcribe.

### Cleanup
<a name="working-with-boto3-coexistence-cleanup"></a>

The temporary local audio file is removed automatically. This example doesn't delete the input or output Amazon S3 objects. Delete the output object when you no longer need it.

### Next steps
<a name="working-with-boto3-coexistence-next-steps"></a>
+ For how the SDK resolves configuration values, see [Configuration resolution](config-resolution.md). For how it finds credentials, see [Credential providers](credential-providers.md).
+ For running an asynchronous workflow from a synchronous application, see [Running asynchronous code](using-async.md#using-async-run).
+ For event-stream lifecycle and completion behavior, see [Working with event streams](using-streaming.md).
+ For generated Amazon Transcribe Streaming request and event types, see the [StartStreamTranscription API reference](clients/transcribe-streaming/operations/start_stream_transcription/).
+ For Boto3 S3 operations, see the [SDK for Python (Boto3) S3 API reference](https://docs.aws.amazon.com/boto3/latest/reference/services/s3.html).

## Common pitfalls
<a name="working-with-boto3-pitfalls"></a>

Avoid these issues when using both SDKs together:

| Pitfall | Impact | Resolution |
| --- | --- | --- |
| Calling synchronous Boto3 methods inside an active asyncio event loop | Blocks the event loop, eliminating concurrency benefits and potentially causing timeouts | Use asyncio.to\_thread() to run Boto3 calls in a thread pool (see [Scenario 1](#working-with-boto3-sdk-primary)) |
| Assuming configuration is shared between SDKs | One SDK may use an unexpected Region or credentials | Verify each SDK resolves the correct Region and credentials independently |
| Calling asyncio.run() from inside a running event loop | Raises RuntimeError — you cannot nest event loops | Use await directly if already inside an async context, or restructure to call asyncio.run() only from synchronous code |
| Creating Boto3 clients inside tight async loops | Client construction is synchronous and repeated creation adds latency | Create Boto3 clients once outside the loop and pass them in, wrapped with asyncio.to\_thread() if called from async code |

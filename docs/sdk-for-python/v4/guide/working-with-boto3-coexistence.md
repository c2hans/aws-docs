---
source_url: https://docs.aws.amazon.com/sdk-for-python/v4/guide/working-with-boto3-coexistence.html
---

**Developer Preview**: This documentation covers the AWS SDK for Python v4, which is in Developer Preview and intended for evaluation and testing only. Do not use it for production workloads. For production applications, use the [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/boto3/latest/guide/quickstart.html). To understand the differences between the two SDKs, see [Choosing the right AWS SDK for Python](choosing-sdk.md).

# Use both SDKs in one application

You can use the AWS SDK for Python v4 and AWS SDK for Python (Boto3) together in the same application. The most common reasons to combine both SDKs are the following:
+ A service or feature that you need isn't available in the AWS SDK for Python v4 yet, so you use Boto3 for it and the AWS SDK for Python v4 for the rest of the application.
+ You want to evaluate the AWS SDK for Python v4 in an existing Boto3 application one workflow at a time, without rewriting the rest of your code.

Keep existing Boto3 code when it continues to meet your application's needs. Add the AWS SDK for Python v4 where you want its generated types, modular service packages, asynchronous clients, or bidirectional streaming.

## Configuration and credentials
<a name="working-with-boto3-configuration"></a>

Both SDKs can resolve standard AWS settings, such as environment variables and the shared AWS `config` and `credentials` files. Each SDK resolves and refreshes its own configuration independently. Programmatic settings aren't shared between the SDKs. Keep the following in mind:
+ A profile or Region selected with a Boto3 `Session` doesn't apply to AWS SDK for Python v4 configuration resolution.
+ The generated service configuration requires a Region for both client types. `resolve()` fails if no Region is available.
+ Boto3 supports credential sources that the AWS SDK for Python v4 doesn't support yet, such as AWS IAM Identity Center. The AWS SDK for Python v4 gets container, Amazon EC2 instance metadata, assume role, and web identity credentials only from optional packages. If Boto3 gets its credentials from a source that the AWS SDK for Python v4 doesn't support, or whose package isn't installed, the AWS SDK for Python v4 can use a different identity or fail to find credentials. For the supported sources, see [Credential providers](credential-providers.md).
+ Configure equivalent options for each SDK when necessary, such as the Region, credentials, and endpoint overrides.

## Combining synchronous and asynchronous code
<a name="working-with-boto3-sync-async"></a>

Boto3 operations and AWS SDK for Python v4 synchronous client operations both block the calling thread. An application that uses only synchronous clients calls both SDKs directly and doesn't need `asyncio`. Combining synchronous and asynchronous code matters only when an application uses AWS SDK for Python v4 asynchronous clients alongside blocking Boto3 calls. The pattern depends on which code owns the event loop.

| Application type | Pattern | Example |
| --- | --- | --- |
| Synchronous only. Boto3 and AWS SDK for Python v4 synchronous clients run in the same thread. | Call both SDKs directly. The application doesn't run an event loop. | [GetItem example](working-with-boto3-migration.md#working-with-boto3-migration-example) |
| Async-primary. Asynchronous AWS SDK for Python v4 code owns the event loop. | Use asyncio.to\_thread() for Boto3 calls so they don't block the event loop. | [Scenario 1](#working-with-boto3-sdk-primary) |
| Sync-primary. Synchronous code, including Boto3 calls, owns the main thread. | Use asyncio.run() to enter an asynchronous workflow for operations that need an asynchronous client, such as bidirectional streams. Use synchronous clients for the other AWS SDK for Python v4 calls. | [Scenario 2](#working-with-boto3-coexistence-example) |

For how the two client types differ, see [Synchronous and asynchronous clients](using-sync-async.md). For details on running asynchronous code, see [Running asynchronous code](using-async.md#using-async-run). For keeping blocking work off the event loop, see [Keeping blocking work off the event loop](using-async.md#using-async-blocking-work).

## Before you begin
<a name="working-with-boto3-before"></a>

Both scenarios require the following:
+ Complete [Prerequisites and installation](getting-started-prerequisites-installation.md) and [Authenticating with AWS](getting-started-authentication.md).
+ A Region available to both SDKs. Boto3 doesn't read the `AWS_REGION` environment variable, so set the Region in the shared config file or with `AWS_DEFAULT_REGION`.
+ IAM permissions as described in each scenario.

**Warning**
Both scenarios use AWS services that can incur charges. Use non-production resources and review pricing for the relevant services before repeated use.

## Scenario 1: Async-primary application with Boto3 for unsupported services
<a name="working-with-boto3-sdk-primary"></a>

This scenario represents a new asynchronous application that uses `AsyncBedrockRuntimeClient` for output streaming. The application sends a request to Amazon Bedrock Runtime and asynchronously processes response events as the model generates output. `ConverseStream` is an event-stream operation, so only the asynchronous client provides it. After the stream completes, the application uses Boto3 to write the prompt and completed response as a JSON log event to Amazon CloudWatch Logs, which doesn't have a client in the AWS SDK for Python v4 yet.

Use this pattern when your application is built on asynchronous clients and needs Boto3 only for services or features that the AWS SDK for Python v4 doesn't provide yet.

### Install
<a name="working-with-boto3-sdk-primary-install"></a>

```
python -m pip install boto3 aws-sdk-bedrock-runtime
```

### Additional requirements
<a name="working-with-boto3-sdk-primary-requirements"></a>
+ Access to an Amazon Bedrock model that supports `ConverseStream` in the configured AWS Region. This example processes text output only.
+ A CloudWatch Logs log group and log stream where the example can write the model response.
+ The identity resolved by the AWS SDK for Python v4 allows `bedrock:InvokeModelWithResponseStream` for the selected model.
+ The identity resolved by Boto3 allows `logs:PutLogEvents` for the log stream.

### Write the code
<a name="working-with-boto3-sdk-primary-code"></a>

Create a file named `sdk_primary_with_boto3.py` with the following code:

```
"""Use Boto3 from an asynchronous AWS SDK for Python v4 application."""

import argparse
import asyncio
import json
import time

import boto3

from aws_sdk_bedrock_runtime import AsyncBedrockRuntimeClient, AsyncBedrockRuntimeConfig
from aws_sdk_bedrock_runtime.models import (
    ContentBlockDeltaText,
    ConverseStreamOutputContentBlockDelta,
    ConverseStreamOutputMessageStop,
    ConverseStreamOutputMetadata,
    ConverseStreamOutputUnknown,
    InternalServerException,
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
            model_id=model_id,
            messages=[{"role": "user", "content": [{"text": prompt}]}],
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
    log_group: str,
    log_stream: str,
    prompt: str,
    response: str,
) -> None:
    message = json.dumps(
        {"prompt": prompt, "response": response},
        ensure_ascii=False,
    )
    logs = boto3.client("logs")
    logs.put_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        logEvents=[
            {
                "timestamp": int(time.time() * 1000),
                "message": message,
            }
        ],
    )

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("log_group")
    parser.add_argument("log_stream")
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
            args.log_group,
            args.log_stream,
            args.prompt,
            response,
        )
        print(
            f"Saved response to log stream {args.log_stream} "
            f"in log group {args.log_group}"
        )

if __name__ == "__main__":
    asyncio.run(main(parse_args()))
```

### How it works
<a name="working-with-boto3-sdk-primary-how"></a>

The asynchronous AWS SDK for Python v4 code owns the event loop and the application's primary workflow:

1. `AsyncBedrockRuntimeConfig.resolve()` resolves Region and credentials from standard AWS settings.

1. `stream_response()` calls `converse_stream()` with keyword arguments and consumes the response events that Amazon Bedrock Runtime streams as the model generates output.

1. After the stream completes, `asyncio.to_thread()` runs the synchronous Boto3 `put_log_events()` call in a worker thread, so the call doesn't block the event loop.

### Run the application
<a name="working-with-boto3-sdk-primary-run"></a>

Pass the log group, log stream, and model prompt:

```
python sdk_primary_with_boto3.py example-bedrock-responses example-stream "Give three tips for writing clear Python code."
```

### Success
<a name="working-with-boto3-sdk-primary-success"></a>

A successful run prints the streamed model response and the names of the log stream and log group that received it. The log stream contains a log event with the prompt and completed response as JSON.

### Cleanup
<a name="working-with-boto3-sdk-primary-cleanup"></a>

This example doesn't create resources. It writes one log event to the log stream that you provide each time it runs. Delete the log stream or log group when you no longer need it.

### Next steps
<a name="working-with-boto3-sdk-primary-next-steps"></a>
+ For how the SDK resolves configuration values, see [Configuration resolution](config-resolution.md). For how it finds credentials, see [Credential providers](credential-providers.md).
+ For running blocking functions from an asynchronous application, see [Keeping blocking work off the event loop](using-async.md#using-async-blocking-work).
+ For more Amazon Bedrock Runtime operations and streaming behavior, see [Amazon Bedrock Runtime](services-bedrock.md).
+ For generated Amazon Bedrock Runtime request, response, and event types, see the [ConverseStream API reference](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/bedrock-runtime/operations/converse_stream/).
+ For CloudWatch Logs operations in Boto3, see the [CloudWatchLogs API reference](https://docs.aws.amazon.com/boto3/latest/reference/services/logs.html).

## Scenario 2: Sync-primary application adding bidirectional streaming
<a name="working-with-boto3-coexistence-example"></a>

This scenario represents an existing synchronous application that uses Boto3 to download PCM audio from Amazon S3. The application adds `AsyncTranscribeStreamingClient` to send audio to Amazon Transcribe and receive transcript events concurrently over a bidirectional stream. After the stream completes, the existing Boto3 workflow uploads the completed transcript to Amazon S3.

Use this pattern when you have a synchronous application and need an operation that only asynchronous clients provide, such as a bidirectional stream. The rest of the application stays synchronous. Its other AWS SDK for Python v4 calls can use synchronous clients, which you call directly like Boto3 clients.

### Install
<a name="working-with-boto3-coexistence-install"></a>

Install the `awscrt` extra to use the AWS Common Runtime (CRT) HTTP client that bidirectional streaming requires. For more information, see [Use the AWS CRT client for bidirectional streaming](http-configuration.md#http-crt-streaming).

```
python -m pip install boto3 "aws-sdk-transcribe-streaming[awscrt]"
```

### Additional requirements
<a name="working-with-boto3-coexistence-requirements"></a>
+ An Amazon S3 object containing US English audio as headerless, signed 16-bit little-endian, mono PCM sampled at 16 kHz. WAV files include a container header and aren't valid input for this example. To transcribe another supported language, change `LanguageCode.EN_US` in the request. To try this example, you can download a [sample PCM clip](https://github.com/aws/aws-sdk-python/blob/develop/clients/aws-sdk-bedrock-runtime/tests/integration/assets/test.pcm) (`test.pcm`) from the aws-sdk-python repository on GitHub.
+ An output Amazon S3 bucket and key where the example can store the UTF-8 transcript.
+ The identity resolved by Boto3 allows `s3:GetObject` for the input object and `s3:PutObject` for the output object.
+ The identity resolved by the AWS SDK for Python v4 allows `transcribe:StartStreamTranscription`.

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

from aws_sdk_transcribe_streaming import (
    AsyncTranscribeStreamingClient,
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
            language_code=LanguageCode.EN_US,
            media_sample_rate_hertz=SAMPLE_RATE,
            media_encoding=MediaEncoding.PCM,
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

1. `asyncio.run()` enters the asynchronous transcription workflow once. The event loop starts and stops within this call.

1. Inside the asynchronous workflow, `start_stream_transcription()` opens the stream with keyword arguments. Then `asyncio.gather()` sends audio and receives transcript events concurrently over one bidirectional HTTP/2 stream.

1. After `asyncio.run()` returns, Boto3 uploads the completed transcript to Amazon S3 synchronously.

### Run the application
<a name="working-with-boto3-coexistence-run"></a>

Pass the input bucket and PCM object key, followed by the output bucket and transcript object key:

```
python boto3_with_streaming.py amzn-s3-demo-source-bucket audio/test.pcm amzn-s3-demo-destination-bucket transcripts/test.txt
```

### Success
<a name="working-with-boto3-coexistence-success"></a>

A successful run prints the input and output Amazon S3 URIs. The output object contains the completed transcript segments returned by Amazon Transcribe.

### Cleanup
<a name="working-with-boto3-coexistence-cleanup"></a>

The `TemporaryDirectory` context manager deletes the local audio file. This example doesn't delete the input or output Amazon S3 objects. Delete the output object when you no longer need it.

### Next steps
<a name="working-with-boto3-coexistence-next-steps"></a>
+ For how the SDK resolves configuration values, see [Configuration resolution](config-resolution.md). For how it finds credentials, see [Credential providers](credential-providers.md).
+ For running an asynchronous workflow from a synchronous application, see [Running asynchronous code](using-async.md#using-async-run).
+ For event-stream lifecycle and completion behavior, see [Working with event streams](using-streaming.md).
+ For generated Amazon Transcribe Streaming request and event types, see the [StartStreamTranscription API reference](https://docs.aws.amazon.com/sdk-for-python/v4/reference/clients/transcribe-streaming/operations/start_stream_transcription/).
+ For S3 operations in Boto3, see the [S3 API reference](https://docs.aws.amazon.com/boto3/latest/reference/services/s3.html).

## Common pitfalls
<a name="working-with-boto3-pitfalls"></a>

The following issues are common when you use both SDKs together or move Boto3 code to the AWS SDK for Python v4.

| Pitfall | Impact | Resolution |
| --- | --- | --- |
| Calling Boto3 operations or AWS SDK for Python v4 synchronous client operations inside a running asyncio event loop | Blocks the event loop, which stops other tasks from running and can cause timeouts | Use asyncio.to\_thread() to run the blocking call in a worker thread, as in [Scenario 1](#working-with-boto3-sdk-primary). For AWS SDK for Python v4 calls, you can use an asynchronous client instead. |
| Assuming configuration is shared between SDKs | One SDK can use an unexpected Region or credentials | Verify each SDK resolves the correct Region and credentials independently |
| Calling asyncio.run() from inside a running event loop | Raises RuntimeError, because an event loop is already running in the thread | Use await directly if already inside an async context, or restructure to call asyncio.run() only from synchronous code |
| Creating Boto3 clients inside tight async loops | Client construction is synchronous. Repeated creation adds latency. | Create Boto3 clients once outside the loop and pass them in, wrapped with asyncio.to\_thread() if called from async code |
| Passing Boto3 request parameters, such as TableName="Books", to a AWS SDK for Python v4 operation | Raises TypeError for an unknown argument | Use the snake-case member names, such as table\_name="Books". For the accepted argument forms, see [Making requests and handling responses](using-requests.md). |
| Using Boto3 union keys in dictionaries, such as {"S": "Mary Major"} | Raises TypeError for an unknown union member | Use the snake-case member name as the key, such as {"s": "Mary Major"}, or a generated union variant, such as AttributeValueS(value="Mary Major") |
| Catching ClientError around AWS SDK for Python v4 calls | The handler doesn't catch service errors, because the AWS SDK for Python v4 raises generated exception classes | Catch the modeled exception class from the service's models module, such as ResourceNotFoundException. For more information, see [Handling errors](using-errors.md). |

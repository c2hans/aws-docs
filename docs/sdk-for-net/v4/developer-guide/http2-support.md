---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/http2-support.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Support for HTTP 2 in the AWS SDK for .NET
<a name="http2-support"></a>

Some AWS services and operations require HTTP 2. For example, bi-directional streaming in Amazon Transcribe Streaming isn't possible over HTTP 1.1 and so requires HTTP 2 instead. Version 4 of the AWS SDK for .NET added support for HTTP 2 so that you can use these operations in your applications. For a bi-directional HTTP 2 operation, the behavior of the SDK when receiving streams is similar to that for HTTP 1.1. That is, when applications that use the SDK send events to the service, the request has a publisher that is assigned by the developer.

To see this behavior in action, consider the following example for Amazon Transcribe Streaming. It uses the [Amazon.TranscribeStreaming](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/TranscribeStreaming/NTranscribeStreaming.html) and [Amazon.TranscribeStreaming.Model](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/TranscribeStreaming/NTranscribeStreamingModel.html) namespaces.

In this example, the developer defines the `StartStreamTranscriptionRequest.AudioStreamPublisher` property with a callback function, which is a .NET `Func`. The SDK uses the `Func` defined for `AudioStreamPublisher` to pull events from the user's code to stream to the user. The SDK calls the `Func` until it returns null.

The code demonstrates how audio from a file can be streamed into Amazon Transcribe Streaming for processing.

```
using Amazon;
using Amazon.TranscribeStreaming;
using Amazon.TranscribeStreaming.Model;

CancellationTokenSource cancelSource = new CancellationTokenSource();

var client = new AmazonTranscribeStreamingClient(RegionEndpoint.USEast1);

var startRequest = new StartStreamTranscriptionRequest
{
    LanguageCode = LanguageCode.EnUS,
    MediaEncoding = MediaEncoding.Flac,
    MediaSampleRateHertz = 44100,
    NumberOfChannels = 2,
    EnableChannelIdentification = true
};

Stream fileStream = File.OpenRead("hello-world.flac");
var buffer = new byte[1024 * 10];
startRequest.AudioStreamPublisher += async () =>
{
    var bytesRead = await fileStream.ReadAsync(buffer, 0, buffer.Length);

    if (bytesRead == 0)
        return null;

    var audioEvent = new AudioEvent
    {
        AudioChunk = new MemoryStream(buffer, 0, bytesRead)
    };

    return audioEvent;
};

using var response = await client.StartStreamTranscriptionAsync(startRequest);
Console.WriteLine(response.HttpStatusCode);

response.TranscriptResultStream.ExceptionReceived += TranscriptResultStream_ExceptionReceived;
response.TranscriptResultStream.TranscriptEventReceived += TranscriptResultStream_TranscriptEventReceived;

void TranscriptResultStream_ExceptionReceived(object? sender, Amazon.Runtime.EventStreams.EventStreamExceptionReceivedArgs<TranscribeStreamingEventStreamException> e)
{
    Console.WriteLine(e.EventStreamException.Message);
    cancelSource.Cancel();
}
void TranscriptResultStream_TranscriptEventReceived(object? sender, Amazon.Runtime.EventStreams.EventStreamEventReceivedArgs<TranscriptEvent> e)
{
    foreach (var result in e.EventStreamEvent.Transcript.Results)
    {
        if (!string.Equals("ch_0", result.ChannelId, StringComparison.OrdinalIgnoreCase))
            continue;

        var text = result.Alternatives[0].Transcript;
        if (!string.IsNullOrEmpty(text))
        {
            Console.WriteLine(text);
        }
    }
}

_ = response.TranscriptResultStream.StartProcessingAsync();

try
{
    await Task.Delay(10000, cancelSource.Token);
}
catch (TaskCanceledException) { }
```

**Warning**
Some bi-directional HTTP 2 operations, such as the `InvokeModelWithBidirectionalStreamAsync` method from Amazon Bedrock, the [Amazon.BedrockRuntime](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/BedrockRuntime/NBedrockRuntime.html) namespace, don't return a response from the initial invocation on the service client until some events have been published. This behavior could cause your application to be blocked. To avoid this situation, separate the application code that provides events to the publisher, and run it on a thread that is different from the thread that invokes operations on the service client.

## Additional considerations
<a name="http2-support-additional"></a>
+ AWS SDK for .NET support for HTTP 2 is available only in versions that target .NET 8 and above. It isn't available in versions that target .NET Framework.
+ For more detailed information, see [PR 3730](https://github.com/aws/aws-sdk-net/pull/3730) in the [aws-sdk-net](https://github.com/aws/aws-sdk-net) GitHub repository.

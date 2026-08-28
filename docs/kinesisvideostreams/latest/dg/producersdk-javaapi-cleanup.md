---
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-cleanup.html
---

# Clean up resources
<a name="producersdk-javaapi-cleanup"></a>

In order to avoid memory leaks, do the following to unregister a media source from the client and free the client.

```
try {
    kinesisVideoClient.unregisterMediaSource(mediaSource);
    kinesisVideoClient.free();
} catch (final KinesisVideoException e) {
    throw new RuntimeException(e);
}
```

If you added any items to the cache using the [`CachedInfoMultiAuthServiceCallbacks`](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java/blob/master/src/main/java/com/amazonaws/kinesisvideo/java/service/CachedInfoMultiAuthServiceCallbacksImpl.java), for example:

```
serviceCallbacks.addStreamInfoToCache(streamName, streamInfo);
serviceCallbacks.addStreamingEndpointToCache(streamName, dataEndpoint);
```

Clear the cache when you're done:

```
serviceCallbacks.removeStreamFromCache(streamName);
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Video Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisvideostreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

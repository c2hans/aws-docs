---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/content-stream-provider.html
---

# Implement `ContentStreamProvider` in the AWS SDK for Java 2.x
<a name="content-stream-provider"></a>

`ContentStreamProvider` is an abstraction used in the AWS SDK for Java 2.x to allow multiple reads of input data. This topic explains how to implement a `ContentStreamProvider` correctly for your applications.

The SDK for Java 2.x uses the `ContentStreamProvider#newStream()` method each time it needs to read an entire stream. For this to work for the entire stream, the returned stream must always be at the start of the content and it must contain the same data.

In the following sections, we provide three approaches for how to implement this behavior correctly.

## Use `mark()` and `reset()`
<a name="csp-impl-mark-reset"></a>

In the example below, we use `mark(int)` in the constructor before reading begins to ensure that we can reset the stream back to the beginning. For each invocation of `newStream()` we reset the stream:

```
public class MyContentStreamProvider implements ContentStreamProvider {
    private InputStream contentStream;

    public MyContentStreamProvider(InputStream contentStream) {
        this.contentStream = contentStream;
        this.contentStream.mark(MAX_LEN);
    }

    @Override
    public InputStream newStream() {
        contentStream.reset();
        return contentStream;
    }
}
```

## Use buffering if `mark()` and `reset()` are not available
<a name="csp-impl-unsupported-streams"></a>

 If your stream doesn't support `mark()` and `reset()` directly, you can still use the solution shown previously by first wrapping the stream in a `BufferedInputStream`:

```
public class MyContentStreamProvider implements ContentStreamProvider {
    private BufferedReader contentStream;

    public MyContentStreamProvider(InputStream contentStream) {
        this.contentStream = new BufferedInputStream(contentStream);
        this.contentStream.mark(MAX_LEN);
    }

    @Override
    public InputStream newStream() {
        contentStream.reset();
        return contentStream;
    }
}
```

## Create new streams
<a name="csp-impl-new-stream"></a>

A simpler approach is to simply obtain a new stream to your data on each invocation and close the previous one:

```
public class MyContentStreamProvider implements ContentStreamProvider {
    private InputStream contentStream;

    @Override
    public InputStream newStream() {
        if (contentStream != null) {
            contentStream.close();
        }
        contentStream = openStream();
        return contentStream;
    }
}
```

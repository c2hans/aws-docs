---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrate-s3.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Amazon S3 considerations
<a name="migrate-s3"></a>

## Amazon S3 multipart upload
<a name="s3-multipart-upload"></a>

 In v2, the Amazon S3 client contains an [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#upload-property](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#upload-property) operation that supports uploading large objects with [multipart upload feature offered by Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html).

 In v3, the [https://github.com/aws/aws-sdk-js-v3/blob/main/lib/lib-storage](https://github.com/aws/aws-sdk-js-v3/blob/main/lib/lib-storage) package is available. It supports all the features offered in the v2 `upload()` operation and supports both Node.js and browsers runtime.

## Amazon S3 presigned URL
<a name="s3-presigned-url"></a>

 In v2, the Amazon S3 client contains the [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#getSignedUrl-property](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#getSignedUrl-property) and [https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#getSignedUrlPromise-property](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#getSignedUrlPromise-property) operations to generate an URL that users can use to upload or download objects from Amazon S3.

 In v3, the [https://github.com/aws/aws-sdk-js-v3/tree/main/packages/s3-request-presigner](https://github.com/aws/aws-sdk-js-v3/tree/main/packages/s3-request-presigner) package is available. This package contains the functions for both `getSignedUrl()` and ` getSignedUrlPromise()` operations. This [ blog post](https://aws.amazon.com/blogs/developer/generate-presigned-url-modular-aws-sdk-javascript/) discusses the details of this package.

## Amazon S3 region redirects
<a name="s3-global-client-region-redirects"></a>

If an incorrect region is passed to the Amazon S3 client and a subsequent ` PermanentRedirect` (status 301) error is thrown, the Amazon S3 client in v3 supports region redirects (previously known as the Amazon S3 Global Client in v2). You can use the [https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-middleware-sdk-s3/Interface/S3InputConfig/](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-middleware-sdk-s3/Interface/S3InputConfig/) flag in the client configuration to make the Amazon S3 client follow region redirects and support its function as a global client.

**Note**
Note that this feature can result in additional latency as failed requests are retried with a corrected region when receiving a `PermanentRedirect` error with status 301. This feature should only be used if you do not know the region of your bucket(s) ahead of time.

## Amazon S3 streaming and buffered responses
<a name="amazon-s3-stream-vs-buffer"></a>

 The v3 SDK prefers not to buffer potentially large responses. This is commonly encountered in the Amazon S3 `GetObject` operation, which returned a `Buffer` in v2, but returns a `Stream` in v3.

 For Node.js, you must consume the stream or garbage collect the client or its request handler to keep the connections open to new traffic by freeing sockets.

```
// v2
const get = await s3.getObject({ ... }).promise(); // this buffers consumes the stream already.
```

```
// v3, consume the stream to free the socket
const get = await s3.getObject({ ... }); // object .Body has unconsumed stream
const str = await get.Body.transformToString(); // consumes the stream

// other ways to consume the stream include writing it to a file,
// passing it to another consumer like an upload, or buffering to
// a string or byte array.
```

 For more information, see section on [ socket exhaustion](https://github.com/aws/aws-sdk-js-v3/blob/main/supplemental-docs/CLIENTS.md#request-handler-requesthandler).

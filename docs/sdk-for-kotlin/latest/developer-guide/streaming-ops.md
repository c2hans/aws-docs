---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/streaming-ops.html
---

# Streaming operations
<a name="streaming-ops"></a>

In the AWS SDK for Kotlin, binary data (streams) are represented as a [ByteStream](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.content/-byte-stream/index.html) type, which is an abstract read-only stream of bytes.

## Streaming responses
<a name="streaming-responses"></a>

Responses with a binary stream (such as the Amazon Simple Storage Service (Amazon S3) [GetObject](/AmazonS3/latest/API/API_GetObject.html) API operation) are handled differently from other methods. These methods take a lambda function that handles the response rather than returning the response directly. This limits the scope of the response to the function and simplifies lifetime management for both the caller and the SDK runtime.

After the lambda function returns, any resources like the underlying HTTP connection are released. (The [`ByteStream`](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.content/-byte-stream/index.html) should not be accessed after the lambda returns and should not be passed out of the closure.) The result of the call is whatever the lambda returns.

The following code example shows the [getObject](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3/-s3-client/get-object.html) function receiving a lambda parameter, which handles the response.

```
val s3Client = S3Client.fromEnvironment()
val req = GetObjectRequest { ... }

val path = Paths.get("/tmp/download.txt")

// S3Client.getObject has the following signature:
// suspend fun <T> getObject(input: GetObjectRequest, block: suspend (GetObjectResponse) -> T): T

val contentSize = s3Client.getObject(req) { resp ->
    // resp is valid until the end of the block.
    // Do not attempt to store or process the stream after the block returns.

    // resp.body is of type ByteStream.
    val rc = resp.body?.writeToFile(path)
    rc
}
println("wrote $contentSize bytes to $path")
```

The [`ByteStream`](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.content/-byte-stream/index.html) type has the following extensions for common ways of consuming it:
+  `ByteStream.writeToFile(file: File): Long`
+  `ByteStream.writeToFile(path: Path): Long`
+  `ByteStream.toByteArray(): ByteArray`
+  `ByteStream.decodeToString(): String`

All of these are defined in the `aws.smithy.kotlin.runtime.content` package.

## Streaming requests
<a name="streaming-requests"></a>

To supply a [`ByteStream`](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.content/-byte-stream/index.html), there are also several convenience methods, including the following:
+  `ByteStream.fromFile(file: File)`
+  `File.asByteStream(): ByteStream`
+  `Path.asByteStream(): ByteStream`
+  `ByteStream.fromBytes(bytes: ByteArray)`
+  `ByteStream.fromString(str: String)`

All of these are defined in the `aws.smithy.kotlin.runtime.content` package.

The following code example shows the use of [`ByteStream`](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime.content/-byte-stream/index.html) convenience methods that provide the body property in the creation of a [PutObjectRequest](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3.model/-put-object-request/index.html):

```
val req = PutObjectRequest {
    ...
    body = ByteStream.fromFile(file)
    // body = ByteStream.fromBytes(byteArray)
    // body = ByteStream.fromString("string")
    // etc
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

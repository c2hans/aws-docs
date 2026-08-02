---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/presign-requests.html
---

# Presign requests
<a name="presign-requests"></a>

You can presign requests for some AWS API operations so that another caller can use the request later without presenting their own credentials.

For example, assume that Alice has access to an Amazon Simple Storage Service (Amazon S3) object and she wants to temporarily share object access with Bob. Alice can generate a presigned `GetObject` request to share with Bob so that he can download the object without requiring access to Alice’s credentials.

## Presigning basics
<a name="presign-requests-basics"></a>

The SDK for Kotlin provides extension methods on service clients to presign requests. All presigned requests require a duration that represents how long the signed request is valid. After the duration ends, the presigned request expires and raises an authentication error if executed.

The following code shows an example that creates a presigned `GetObject` request for Amazon S3. The request is valid for 24 hours after creation.

```
val s3 = S3Client.fromEnvironment()

val unsignedRequest = GetObjectRequest {
    bucket = "foo"
    key = "bar"
}

val presignedRequest = s3.presignGetObject(unsignedRequest, 24.hours)
```

The [presignGetObject](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3.presigners/presign-get-object.html) extension method returns an [HttpRequest](/smithy-kotlin/api/latest/http/aws.smithy.kotlin.runtime.http.request/-http-request/index.html) object. The request object contains the presigned URL where the operation can be invoked. Another caller can use the URL (or the entire request) in a different codebase or programming language environment.

After creating the presigned request, use an HTTP client to invoke a request. The API to invoke an HTTP GET request depends on the HTTP client. The following example uses the Kotlin [URL.readText](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/java.net.-u-r-l/read-text.html) method.

```
val objectContents = URL(presignedRequest.url.toString()).readText()
println(objectContents)
```

## Advanced presigning configuration
<a name="presign-requests-conf-advanced"></a>

In the SDK, each method that can presign requests has an overload that you can use to provide advanced configuration options, such as a specific signer implementation or detailed signing parameters.

The following example shows an Amazon S3 `GetObject` request that uses the CRT signer variant and specifies a future signing date.

```
val s3 = S3Client.fromEnvironment()

val unsignedRequest = GetObjectRequest {
    bucket = "foo"
    key = "bar"
}

val presignedRequest = s3.presignGetObject(unsignedRequest, signer = CrtAwsSigner) {
    signingDate = Instant.now() + 24.hours
    expiresAfter = 8.hours
}
```

The returned presigned request is forward-dated 24 hours and is not valid before then. It expires 8 hours after that.

## Presigning POST and PUT requests
<a name="presign-requests-post-put"></a>

Many operations that are presignable require only a URL and must be executed as HTTP GET requests. Some operations, however, take a body and must be executed as an HTTP POST or HTTP PUT request along with headers in some cases. Presigning these requests is identical to presigning GET requests, but invoking the presigned request is more complicated.

Here is an example of presigning an S3 `PutObject` request:

```
val s3 = S3Client.fromEnvironment()

val unsignedRequest = PutObjectRequest {
    bucket = "foo"
    key = "bar"
}

val presignedRequest = s3.presignPutObject(unsignedRequest, 24.hours)
```

The returned `HttpRequest` has a method value of `HttpMethod.PUT` and includes a URL and headers that must be included in the future invocation of the HTTP request. You can pass this request to a caller that can execute it in a different codebase or programming language environment.

After creating the presigned POST or PUT request, use an HTTP client to invoke a request. The API to invoke a POST or PUT request URL depends on the HTTP client used. The following example uses an [OkHttp HTTP client](https://square.github.io/okhttp) and includes a body that contains `Hello world`.

```
val putRequest = Request
    .Builder()
    .url(presignedRequest.url.toString())
    .apply {
        presignedRequest.headers.forEach { key, values ->
            header(key, values.joinToString(", "))
        }
    }
    .put("Hello world".toRequestBody())
    .build()

val response = okHttp.newCall(putRequest).execute()
```

## Operations the SDK can presign
<a name="presign-ops-supported"></a>

The SDK for Kotlin currently supports presigning the following API operations that need to be called with the associated HTTP method.

|  AWS service | Operation | SDK extension method | Use HTTP method |
| --- | --- | --- | --- |
| Amazon S3 | GetObject |  [presignGetObject](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3.presigners/presign-get-object.html)  | HTTP GET |
| Amazon S3 | PutObject |  [presignPutObject](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3.presigners/presign-put-object.html)  | HTTP PUT |
| Amazon S3 | UploadPart |  [presignUploadPart](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3.presigners/presign-upload-part.html)  | HTTP PUT |
|  AWS Security Token Service | GetCallerIdentity |  [presignGetCallerIdentity](/sdk-for-kotlin/api/latest/sts/aws.sdk.kotlin.services.sts.presigners/presign-get-caller-identity.html)  | HTTP POST |
| Amazon Polly | SynthesizeSpeech |  [presignSynthesizeSpeech](/sdk-for-kotlin/api/latest/polly/aws.sdk.kotlin.services.polly.presigners/presign-synthesize-speech.html)  | HTTP POST |

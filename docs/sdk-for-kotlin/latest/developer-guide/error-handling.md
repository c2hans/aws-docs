---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/error-handling.html
---

# Error handling
<a name="error-handling"></a>

Understanding how and when the AWS SDK for Kotlin throws exceptions is important to building high-quality applications using the SDK. The following sections describe the different cases of exceptions that are thrown by the SDK and how to handle them appropriately.

## Service exceptions
<a name="service-exceptions"></a>

The most common exception is [`AwsServiceException`](/sdk-for-kotlin/api/latest/aws-core/aws.sdk.kotlin.runtime/-aws-service-exception/index.html), from which all service-specific exceptions (such as [`S3Exception`](/sdk-for-kotlin/api/latest/s3/aws.sdk.kotlin.services.s3.model/-s3-exception/index.html)) inherit. This exception represents an error response from an AWS service. For example, if you try to terminate an Amazon EC2 instance that doesn’t exist, Amazon EC2 returns an error response. The error response details are included in the [`AwsServiceException`](/sdk-for-kotlin/api/latest/aws-core/aws.sdk.kotlin.runtime/-aws-service-exception/index.html) that’s thrown.

When you encounter an [`AwsServiceException`](/sdk-for-kotlin/api/latest/aws-core/aws.sdk.kotlin.runtime/-aws-service-exception/index.html), this means that your request was successfully sent to the AWS service but could not be processed. This can be because of errors in the request’s parameters or because of issues on the service side.

## Client exceptions
<a name="client-exceptions"></a>

 [`ClientException`](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime/-client-exception/index.html) indicates that a problem occurred inside the AWS SDK for Kotlin client code, either while trying to send a request to AWS or while trying to parse a response from AWS. A [`ClientException`](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime/-client-exception/index.html) is generally more severe than an [`AwsServiceException`](/sdk-for-kotlin/api/latest/aws-core/aws.sdk.kotlin.runtime/-aws-service-exception/index.html) and indicates that a major problem is preventing the client from processing service calls to AWS services. For example, the AWS SDK for Kotlin throws a [`ClientException`](/smithy-kotlin/api/latest/runtime-core/aws.smithy.kotlin.runtime/-client-exception/index.html) if it fails to parse a response from a service.

## Error metadata
<a name="error-metadata"></a>

Every service exception and client exception has the `sdkErrorMetadata` property. This is a typed property bag that can be used to retrieve additional details about the error.

Several predefined extensions exist to the `AwsErrorMetadata` type directly, including but not limited to the following:
+  `sdkErrorMetadata.requestId` – the unique request id
+  `sdkErrorMetadata.errorMessage` – the human readable message (usually matches the `Exception.message`, but might contain more information if the exception was unknown to the service)
+  `sdkErrorMetadata.protocolResponse` – The raw protocol response

The following example demonstrates accessing the error metadata.

```
try {
    s3Client.listBuckets { ... }
} catch (ex: S3Exception) {
    val awsRequestId = ex.sdkErrorMetadata.requestId
    val httpResp = ex.sdkErrorMetadata.protocolResponse as? HttpResponse

    println("requestId was: $awsRequestId")
    println("http status code was: ${httpResp?.status}")
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

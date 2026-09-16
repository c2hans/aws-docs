---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_DeleteS3AccessPolicy.html
---

# DeleteS3AccessPolicy
<a name="API_DeleteS3AccessPolicy"></a>

Deletes an access policy for the specified store.

## Request Syntax
<a name="API_DeleteS3AccessPolicy_RequestSyntax"></a>

```
DELETE /s3accesspolicy/{{s3AccessPointArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteS3AccessPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [s3AccessPointArn](#API_DeleteS3AccessPolicy_RequestSyntax) **   <a name="omics-DeleteS3AccessPolicy-request-uri-s3AccessPointArn"></a>
The S3 access point ARN that has the access policy.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[^:]*:s3:[^:]*:[^:]*:accesspoint/.*`
Required: Yes

## Request Body
<a name="API_DeleteS3AccessPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteS3AccessPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteS3AccessPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteS3AccessPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** NotSupportedOperationException **
 The operation is not supported by Amazon Omics, or the API does not exist.
HTTP Status Code: 405

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteS3AccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/DeleteS3AccessPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/DeleteS3AccessPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/DeleteS3AccessPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/DeleteS3AccessPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/DeleteS3AccessPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/DeleteS3AccessPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/DeleteS3AccessPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/DeleteS3AccessPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/DeleteS3AccessPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/DeleteS3AccessPolicy)

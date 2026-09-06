---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_PutS3AccessPolicy.html
---

# PutS3AccessPolicy
<a name="API_PutS3AccessPolicy"></a>

Adds an access policy to the specified store.

## Request Syntax
<a name="API_PutS3AccessPolicy_RequestSyntax"></a>

```
PUT /s3accesspolicy/{{s3AccessPointArn}} HTTP/1.1
Content-type: application/json

{
   "s3AccessPolicy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutS3AccessPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [s3AccessPointArn](#API_PutS3AccessPolicy_RequestSyntax) **   <a name="omics-PutS3AccessPolicy-request-uri-s3AccessPointArn"></a>
The S3 access point ARN where you want to put the access policy.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[^:]*:s3:[^:]*:[^:]*:accesspoint/.*`
Required: Yes

## Request Body
<a name="API_PutS3AccessPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [s3AccessPolicy](#API_PutS3AccessPolicy_RequestSyntax) **   <a name="omics-PutS3AccessPolicy-request-s3AccessPolicy"></a>
The resource policy that controls S3 access to the store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: Yes

## Response Syntax
<a name="API_PutS3AccessPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "s3AccessPointArn": "string",
   "storeId": "string",
   "storeType": "string"
}
```

## Response Elements
<a name="API_PutS3AccessPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [s3AccessPointArn](#API_PutS3AccessPolicy_ResponseSyntax) **   <a name="omics-PutS3AccessPolicy-response-s3AccessPointArn"></a>
The S3 access point ARN that now has the access policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:[^:]*:s3:[^:]*:[^:]*:accesspoint/.*`

 ** [storeId](#API_PutS3AccessPolicy_ResponseSyntax) **   <a name="omics-PutS3AccessPolicy-response-storeId"></a>
The AWS-generated Sequence Store or Reference Store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [storeType](#API_PutS3AccessPolicy_ResponseSyntax) **   <a name="omics-PutS3AccessPolicy-response-storeType"></a>
The type of store associated with the access point.
Type: String
Valid Values: `SEQUENCE_STORE | REFERENCE_STORE`

## Errors
<a name="API_PutS3AccessPolicy_Errors"></a>

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
<a name="API_PutS3AccessPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/PutS3AccessPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/PutS3AccessPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/PutS3AccessPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/PutS3AccessPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/PutS3AccessPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/PutS3AccessPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/PutS3AccessPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/PutS3AccessPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/PutS3AccessPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/PutS3AccessPolicy)

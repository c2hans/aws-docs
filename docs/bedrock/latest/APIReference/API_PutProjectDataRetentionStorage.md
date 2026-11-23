---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutProjectDataRetentionStorage.html
---

# PutProjectDataRetentionStorage

Creates or replaces a project's retention storage record for a model provider. The project must be active in this AWS Region and owned by the calling account. A missing or unowned project returns `ResourceNotFoundException`; an archived project returns `ValidationException`.

Requires applicable project, account, or organization approval for a storage-capable trusted access program of the provider, with no applicable revocation. Otherwise, the operation returns `ConflictException`. Enrollment is not required to save the configuration.

The request replaces the complete stored configuration. The last successful write wins.

For `customer_managed` destinations, Amazon Bedrock validates the caller's and service's access to the bucket and key before saving the configuration. The bucket and key must be in the AWS Region where you register the configuration. Validation failures reject the write.

## Request Syntax
<a name="API_PutProjectDataRetentionStorage_RequestSyntax"></a>

```
PUT /v1/projects/{{projectIdentifier}}/data_retention/storage/{{modelProvider}} HTTP/1.1
Content-type: application/json

{
   "storageConfiguration": {
      "kmsKeyArn": "{{string}}",
      "s3BucketArn": "{{string}}",
      "s3BucketOwner": "{{string}}"
   },
   "storageDestination": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutProjectDataRetentionStorage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelProvider](#API_PutProjectDataRetentionStorage_RequestSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-request-uri-modelProvider"></a>
The model provider whose retention storage configuration is addressed by this request.
Valid Values: `anthropic | openai`
Required: Yes

 ** [projectIdentifier](#API_PutProjectDataRetentionStorage_RequestSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-request-uri-projectIdentifier"></a>
The ID or ARN of a named project owned by the calling account in this AWS Region. The default project is not supported; use the account-level retention storage operations instead.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([a-zA-Z0-9_-]+|arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_PutProjectDataRetentionStorage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [storageConfiguration](#API_PutProjectDataRetentionStorage_RequestSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-request-storageConfiguration"></a>
Destination bucket and key. Required when storageDestination is customer\_managed; rejected with ValidationException when amazon\_managed.
Type: [DataRetentionStorageConfiguration](API_DataRetentionStorageConfiguration.md) object
Required: No

 ** [storageDestination](#API_PutProjectDataRetentionStorage_RequestSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-request-storageDestination"></a>
Where retained data is delivered for this scope. customer\_managed requires storageConfiguration; amazon\_managed forbids it.
Type: String
Valid Values: `customer_managed | amazon_managed`
Required: Yes

## Response Syntax
<a name="API_PutProjectDataRetentionStorage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "kmsKeyStatus": "string",
   "modelProvider": "string",
   "projectArn": "string",
   "s3BucketStatus": "string",
   "scope": "string",
   "storageConfiguration": {
      "kmsKeyArn": "string",
      "s3BucketArn": "string",
      "s3BucketOwner": "string"
   },
   "storageDestination": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_PutProjectDataRetentionStorage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kmsKeyStatus](#API_PutProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-response-kmsKeyStatus"></a>
Validation state of the KMS key. Present only when storageDestination is customer\_managed.
Type: String
Valid Values: `pending | active | access_denied`

 ** [modelProvider](#API_PutProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-response-modelProvider"></a>
Model provider this configuration applies to.
Type: String
Valid Values: `anthropic | openai`

 ** [projectArn](#API_PutProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-response-projectArn"></a>
ARN of the configured project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+`

 ** [s3BucketStatus](#API_PutProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-response-s3BucketStatus"></a>
Validation state of the bucket. Present only when storageDestination is customer\_managed.
Type: String
Valid Values: `pending | active | access_denied`

 ** [scope](#API_PutProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-response-scope"></a>
Scope addressed by the operation that returned this record.
Type: String
Valid Values: `account | organization | project`

 ** [storageConfiguration](#API_PutProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-response-storageConfiguration"></a>
The stored destination and key. Present only when storageDestination is customer\_managed.
Type: [DataRetentionStorageConfiguration](API_DataRetentionStorageConfiguration.md) object

 ** [storageDestination](#API_PutProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-response-storageDestination"></a>
Where this record delivers retained data.
Type: String
Valid Values: `customer_managed | amazon_managed`

 ** [updatedAt](#API_PutProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutProjectDataRetentionStorage-response-updatedAt"></a>
Time the stored record last changed.
Type: Timestamp

## Errors
<a name="API_PutProjectDataRetentionStorage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

 ** ConflictException **
Error occurred because of a conflict while performing an operation.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_PutProjectDataRetentionStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/PutProjectDataRetentionStorage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/PutProjectDataRetentionStorage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/PutProjectDataRetentionStorage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/PutProjectDataRetentionStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/PutProjectDataRetentionStorage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/PutProjectDataRetentionStorage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/PutProjectDataRetentionStorage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/PutProjectDataRetentionStorage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/PutProjectDataRetentionStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/PutProjectDataRetentionStorage)

---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetProjectDataRetentionStorage.html
---

# GetProjectDataRetentionStorage

Returns a project's retention storage configuration for a model provider. Returns ResourceNotFoundException when the project does not exist, is not owned by the calling account, or has no configuration.

## Request Syntax
<a name="API_GetProjectDataRetentionStorage_RequestSyntax"></a>

```
GET /v1/projects/{{projectIdentifier}}/data_retention/storage/{{modelProvider}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetProjectDataRetentionStorage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelProvider](#API_GetProjectDataRetentionStorage_RequestSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-request-uri-modelProvider"></a>
The model provider whose retention storage configuration is addressed by this request.
Valid Values: `anthropic | openai`
Required: Yes

 ** [projectIdentifier](#API_GetProjectDataRetentionStorage_RequestSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-request-uri-projectIdentifier"></a>
The ID or ARN of a named project owned by the calling account in this AWS Region. The default project is not supported; use the account-level retention storage operations instead.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `([a-zA-Z0-9_-]+|arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+)`
Required: Yes

## Request Body
<a name="API_GetProjectDataRetentionStorage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetProjectDataRetentionStorage_ResponseSyntax"></a>

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
<a name="API_GetProjectDataRetentionStorage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kmsKeyStatus](#API_GetProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-response-kmsKeyStatus"></a>
Validation state of the KMS key. Present only when storageDestination is customer\_managed.
Type: String
Valid Values: `pending | active | access_denied`

 ** [modelProvider](#API_GetProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-response-modelProvider"></a>
Model provider this configuration applies to.
Type: String
Valid Values: `anthropic | openai`

 ** [projectArn](#API_GetProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-response-projectArn"></a>
ARN of the configured project.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:bedrock:[0-9a-z-]{1,20}:[0-9]{12}:project/[a-zA-Z0-9_-]+`

 ** [s3BucketStatus](#API_GetProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-response-s3BucketStatus"></a>
Validation state of the bucket. Present only when storageDestination is customer\_managed.
Type: String
Valid Values: `pending | active | access_denied`

 ** [scope](#API_GetProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-response-scope"></a>
Scope addressed by the operation that returned this record.
Type: String
Valid Values: `account | organization | project`

 ** [storageConfiguration](#API_GetProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-response-storageConfiguration"></a>
The stored destination and key. Present only when storageDestination is customer\_managed.
Type: [DataRetentionStorageConfiguration](API_DataRetentionStorageConfiguration.md) object

 ** [storageDestination](#API_GetProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-response-storageDestination"></a>
Where this record delivers retained data.
Type: String
Valid Values: `customer_managed | amazon_managed`

 ** [updatedAt](#API_GetProjectDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetProjectDataRetentionStorage-response-updatedAt"></a>
Time the stored record last changed.
Type: Timestamp

## Errors
<a name="API_GetProjectDataRetentionStorage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because of missing access permissions.
HTTP Status Code: 403

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
<a name="API_GetProjectDataRetentionStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetProjectDataRetentionStorage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetProjectDataRetentionStorage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetProjectDataRetentionStorage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetProjectDataRetentionStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetProjectDataRetentionStorage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetProjectDataRetentionStorage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetProjectDataRetentionStorage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetProjectDataRetentionStorage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetProjectDataRetentionStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetProjectDataRetentionStorage)

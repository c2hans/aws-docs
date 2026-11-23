---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetAccountDataRetentionStorage.html
---

# GetAccountDataRetentionStorage

Returns your account's stored retention storage configuration for a model provider. Amazon Bedrock determines whether the configuration applies when processing an inference request. Returns `ResourceNotFoundException` when no configuration exists.

## Request Syntax
<a name="API_GetAccountDataRetentionStorage_RequestSyntax"></a>

```
GET /v1/data_retention/storage/{{modelProvider}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountDataRetentionStorage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelProvider](#API_GetAccountDataRetentionStorage_RequestSyntax) **   <a name="bedrock-GetAccountDataRetentionStorage-request-uri-modelProvider"></a>
The model provider whose retention storage configuration is addressed by this request.
Valid Values: `anthropic | openai`
Required: Yes

## Request Body
<a name="API_GetAccountDataRetentionStorage_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountDataRetentionStorage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "kmsKeyStatus": "string",
   "modelProvider": "string",
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
<a name="API_GetAccountDataRetentionStorage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kmsKeyStatus](#API_GetAccountDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetAccountDataRetentionStorage-response-kmsKeyStatus"></a>
Validation state of the KMS key. Present only when storageDestination is customer\_managed.
Type: String
Valid Values: `pending | active | access_denied`

 ** [modelProvider](#API_GetAccountDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetAccountDataRetentionStorage-response-modelProvider"></a>
Model provider this configuration applies to.
Type: String
Valid Values: `anthropic | openai`

 ** [s3BucketStatus](#API_GetAccountDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetAccountDataRetentionStorage-response-s3BucketStatus"></a>
Validation state of the bucket. Present only when storageDestination is customer\_managed.
Type: String
Valid Values: `pending | active | access_denied`

 ** [scope](#API_GetAccountDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetAccountDataRetentionStorage-response-scope"></a>
Scope addressed by the operation that returned this record.
Type: String
Valid Values: `account | organization | project`

 ** [storageConfiguration](#API_GetAccountDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetAccountDataRetentionStorage-response-storageConfiguration"></a>
The stored destination and key. Present only when storageDestination is customer\_managed.
Type: [DataRetentionStorageConfiguration](API_DataRetentionStorageConfiguration.md) object

 ** [storageDestination](#API_GetAccountDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetAccountDataRetentionStorage-response-storageDestination"></a>
Where this record delivers retained data.
Type: String
Valid Values: `customer_managed | amazon_managed`

 ** [updatedAt](#API_GetAccountDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-GetAccountDataRetentionStorage-response-updatedAt"></a>
Time the stored record last changed.
Type: Timestamp

## Errors
<a name="API_GetAccountDataRetentionStorage_Errors"></a>

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
<a name="API_GetAccountDataRetentionStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetAccountDataRetentionStorage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetAccountDataRetentionStorage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetAccountDataRetentionStorage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetAccountDataRetentionStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetAccountDataRetentionStorage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetAccountDataRetentionStorage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetAccountDataRetentionStorage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetAccountDataRetentionStorage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetAccountDataRetentionStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetAccountDataRetentionStorage)

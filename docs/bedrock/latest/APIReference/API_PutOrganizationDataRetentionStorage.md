---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutOrganizationDataRetentionStorage.html
---

# PutOrganizationDataRetentionStorage

Creates or replaces the organization's retention storage record for a model provider. The organization is resolved from the authenticated caller's management context; the caller must be the organization's management account or a delegated administrator. Requires resolved organization-scope trusted access eligibility for a storage-capable program of the provider; otherwise returns ConflictException. Writes replace the whole record; the last write wins.

For `customer_managed` destinations, Amazon Bedrock validates the caller's and service's access to the bucket and key before saving the configuration. The bucket and key must be in the AWS Region where you register the configuration. Validation failures reject the write.

## Request Syntax
<a name="API_PutOrganizationDataRetentionStorage_RequestSyntax"></a>

```
PUT /v1/data_retention/organization-storage/{{modelProvider}} HTTP/1.1
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
<a name="API_PutOrganizationDataRetentionStorage_RequestParameters"></a>

The request uses the following URI parameters.

 ** [modelProvider](#API_PutOrganizationDataRetentionStorage_RequestSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-request-uri-modelProvider"></a>
The model provider whose retention storage configuration is addressed by this request.
Valid Values: `anthropic | openai`
Required: Yes

## Request Body
<a name="API_PutOrganizationDataRetentionStorage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [storageConfiguration](#API_PutOrganizationDataRetentionStorage_RequestSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-request-storageConfiguration"></a>
Destination bucket and key. Required when storageDestination is customer\_managed; rejected with ValidationException when amazon\_managed.
Type: [DataRetentionStorageConfiguration](API_DataRetentionStorageConfiguration.md) object
Required: No

 ** [storageDestination](#API_PutOrganizationDataRetentionStorage_RequestSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-request-storageDestination"></a>
Where retained data is delivered for this scope. customer\_managed requires storageConfiguration; amazon\_managed forbids it.
Type: String
Valid Values: `customer_managed | amazon_managed`
Required: Yes

## Response Syntax
<a name="API_PutOrganizationDataRetentionStorage_ResponseSyntax"></a>

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
<a name="API_PutOrganizationDataRetentionStorage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [kmsKeyStatus](#API_PutOrganizationDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-response-kmsKeyStatus"></a>
Validation state of the KMS key. Present only when storageDestination is customer\_managed.
Type: String
Valid Values: `pending | active | access_denied`

 ** [modelProvider](#API_PutOrganizationDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-response-modelProvider"></a>
Model provider this configuration applies to.
Type: String
Valid Values: `anthropic | openai`

 ** [s3BucketStatus](#API_PutOrganizationDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-response-s3BucketStatus"></a>
Validation state of the bucket. Present only when storageDestination is customer\_managed.
Type: String
Valid Values: `pending | active | access_denied`

 ** [scope](#API_PutOrganizationDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-response-scope"></a>
Scope addressed by the operation that returned this record.
Type: String
Valid Values: `account | organization | project`

 ** [storageConfiguration](#API_PutOrganizationDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-response-storageConfiguration"></a>
The stored destination and key. Present only when storageDestination is customer\_managed.
Type: [DataRetentionStorageConfiguration](API_DataRetentionStorageConfiguration.md) object

 ** [storageDestination](#API_PutOrganizationDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-response-storageDestination"></a>
Where this record delivers retained data.
Type: String
Valid Values: `customer_managed | amazon_managed`

 ** [updatedAt](#API_PutOrganizationDataRetentionStorage_ResponseSyntax) **   <a name="bedrock-PutOrganizationDataRetentionStorage-response-updatedAt"></a>
Time the stored record last changed.
Type: Timestamp

## Errors
<a name="API_PutOrganizationDataRetentionStorage_Errors"></a>

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

 ** ThrottlingException **
The number of requests exceeds the limit. Resubmit your request later.
HTTP Status Code: 429

 ** ValidationException **
Input validation failed. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_PutOrganizationDataRetentionStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/PutOrganizationDataRetentionStorage)

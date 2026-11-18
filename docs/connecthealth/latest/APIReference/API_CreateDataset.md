---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateDataset.html
---

# CreateDataset
<a name="API_CreateDataset"></a>

Creates a Dataset in a Domain and starts building it. A new dataset has the status CREATING. When it's ready to use, its status changes to ACTIVE, or to CREATE\_FAILED if it fails to build. To check the status, call GetDataset.

This operation is idempotent: if you retry a request with the same clientToken, it returns the dataset that the first request created.

For a medical coding dataset, Amazon Connect Health uses the coded examples that are in the s3InputPath when you create the dataset, and writes evaluation scores to the s3OutputPath. Later changes to the s3InputPath don't change the dataset. To use this operation, you must have s3:GetObject and s3:ListBucket permissions for the input location and s3:PutObject permission for the output location, and kms:Decrypt and kms:GenerateDataKey permissions if you encrypt the locations with an AWS KMS key.

Datasets are in preview release and are subject to change.

## Request Syntax
<a name="API_CreateDataset_RequestSyntax"></a>

```
POST /domains/{{domainId}}/datasets HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "config": { ... },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_CreateDataset_RequestSyntax) **   <a name="connecthealth-CreateDataset-request-uri-domainId"></a>
The unique identifier of the parent Domain.
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_CreateDataset_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDataset_RequestSyntax) **   <a name="connecthealth-CreateDataset-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation returns the dataset that the first request created. If you reuse a clientToken with different parameters, the request fails with ConflictException. Use a new clientToken for a request with different parameters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [config](#API_CreateDataset_RequestSyntax) **   <a name="connecthealth-CreateDataset-request-config"></a>
The configuration of the dataset. The member that you set determines the dataset type. You can't change the configuration after you create the dataset.
Type: [DatasetConfig](API_DatasetConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_CreateDataset_RequestSyntax) **   <a name="connecthealth-CreateDataset-request-name"></a>
A name for the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1028.
Pattern: `[\x20-\x21\x23\x24\x2A-\x3A\x3F-\x7E]*`
Required: Yes

## Response Syntax
<a name="API_CreateDataset_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "createdAt": number,
   "datasetId": "string",
   "status": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_CreateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateDataset_ResponseSyntax) **   <a name="connecthealth-CreateDataset-response-arn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String
Pattern: `arn:aws[a-z\-]*:[a-z0-9\-]+:[a-z0-9\-]*:[0-9]{12}:.+`

 ** [createdAt](#API_CreateDataset_ResponseSyntax) **   <a name="connecthealth-CreateDataset-response-createdAt"></a>
The date and time that the dataset was created.
Type: Timestamp

 ** [datasetId](#API_CreateDataset_ResponseSyntax) **   <a name="connecthealth-CreateDataset-response-datasetId"></a>
The unique identifier of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [status](#API_CreateDataset_ResponseSyntax) **   <a name="connecthealth-CreateDataset-response-status"></a>
The status of the dataset. A new dataset has the status CREATING.
Type: String
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | DELETING | DELETE_FAILED | DELETED`

 ** [type](#API_CreateDataset_ResponseSyntax) **   <a name="connecthealth-CreateDataset-response-type"></a>
The type of the dataset, determined by the configuration that you provided.
Type: String
Valid Values: `MEDICAL_CODING`

## Errors
<a name="API_CreateDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error is thrown when the client does not supply proper credentials to the API.
HTTP Status Code: 401

 ** ConflictException **
This error is thrown when a resource update is no longer valid due to assumptions about initial state changing.
HTTP Status Code: 409

 ** InternalServerException **
This error is thrown when a transient error causes our API to fail.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error is thrown when the requested resource is not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
This error is thrown when the client exceeds the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
This error is thrown when the client supplies invalid input to the API.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/CreateDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/CreateDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/CreateDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/CreateDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/CreateDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/CreateDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/CreateDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/CreateDataset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/CreateDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/CreateDataset)

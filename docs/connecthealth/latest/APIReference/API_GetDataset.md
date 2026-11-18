---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetDataset.html
---

# GetDataset
<a name="API_GetDataset"></a>

Retrieves information about a Dataset, including its status and, after it is built, its results. A dataset whose status is DELETED returns ResourceNotFoundException.

Datasets are in preview release and are subject to change.

## Request Syntax
<a name="API_GetDataset_RequestSyntax"></a>

```
GET /domains/{{domainId}}/datasets/{{datasetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_GetDataset_RequestSyntax) **   <a name="connecthealth-GetDataset-request-uri-datasetId"></a>
The unique identifier of the dataset.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`
Required: Yes

 ** [domainId](#API_GetDataset_RequestSyntax) **   <a name="connecthealth-GetDataset-request-uri-domainId"></a>
The unique identifier of the parent Domain.
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_GetDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "artifacts": { ... },
   "config": { ... },
   "createdAt": number,
   "datasetId": "string",
   "name": "string",
   "status": "string",
   "statusDetails": "string",
   "type": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-arn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String
Pattern: `arn:aws[a-z\-]*:[a-z0-9\-]+:[a-z0-9\-]*:[0-9]{12}:.+`

 ** [artifacts](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-artifacts"></a>
The results of building the dataset, such as medical coding evaluation scores. Available after Amazon Connect Health builds the dataset.
Type: [DatasetArtifacts](API_DatasetArtifacts.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [config](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-config"></a>
The configuration that you provided when you created the dataset.
Type: [DatasetConfig](API_DatasetConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-createdAt"></a>
The date and time that the dataset was created.
Type: Timestamp

 ** [datasetId](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-datasetId"></a>
The unique identifier of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [name](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-name"></a>
The name of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1028.
Pattern: `[\x20-\x21\x23\x24\x2A-\x3A\x3F-\x7E]*`

 ** [status](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-status"></a>
The status of the dataset.
Type: String
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | DELETING | DELETE_FAILED | DELETED`

 ** [statusDetails](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-statusDetails"></a>
Details about the status of the dataset, such as the reason that it failed to build or delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1028.
Pattern: `[\x20-\x21\x23\x24\x2A-\x3A\x3F-\x7E]*`

 ** [type](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-type"></a>
The type of the dataset.
Type: String
Valid Values: `MEDICAL_CODING`

 ** [updatedAt](#API_GetDataset_ResponseSyntax) **   <a name="connecthealth-GetDataset-response-updatedAt"></a>
The date and time that the dataset was last updated.
Type: Timestamp

## Errors
<a name="API_GetDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error is thrown when the client does not supply proper credentials to the API.
HTTP Status Code: 401

 ** InternalServerException **
This error is thrown when a transient error causes our API to fail.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error is thrown when the requested resource is not found.
HTTP Status Code: 404

 ** ThrottlingException **
This error is thrown when the client exceeds the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
This error is thrown when the client supplies invalid input to the API.
HTTP Status Code: 400

## See Also
<a name="API_GetDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/GetDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/GetDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/GetDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/GetDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/GetDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/GetDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/GetDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/GetDataset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/GetDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/GetDataset)

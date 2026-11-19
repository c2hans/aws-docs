---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DeleteDataset.html
---

# DeleteDataset

Starts deleting a Dataset and the resources that Amazon Connect Health built for it. You can delete a dataset whose status is ACTIVE, CREATE\_FAILED, or DELETE\_FAILED. The dataset moves to DELETING, and then to DELETED. If the delete fails, the dataset moves to DELETE\_FAILED, and you can call DeleteDataset again.

Medical coding jobs that already use the dataset finish. Amazon Connect Health rejects new requests that specify the dataset.

Datasets are in preview release and are subject to change.

## Request Syntax
<a name="API_DeleteDataset_RequestSyntax"></a>

```
DELETE /domains/{{domainId}}/datasets/{{datasetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datasetId](#API_DeleteDataset_RequestSyntax) **   <a name="connecthealth-DeleteDataset-request-uri-datasetId"></a>
The unique identifier of the dataset to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`
Required: Yes

 ** [domainId](#API_DeleteDataset_RequestSyntax) **   <a name="connecthealth-DeleteDataset-request-uri-domainId"></a>
The unique identifier of the parent Domain.
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

## Request Body
<a name="API_DeleteDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDataset_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "arn": "string",
   "datasetId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteDataset_ResponseSyntax) **   <a name="connecthealth-DeleteDataset-response-arn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String
Pattern: `arn:aws[a-z\-]*:[a-z0-9\-]+:[a-z0-9\-]*:[0-9]{12}:.+`

 ** [datasetId](#API_DeleteDataset_ResponseSyntax) **   <a name="connecthealth-DeleteDataset-response-datasetId"></a>
The unique identifier of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`

 ** [status](#API_DeleteDataset_ResponseSyntax) **   <a name="connecthealth-DeleteDataset-response-status"></a>
The status of the dataset. After Amazon Connect Health accepts the request, the status is DELETING.
Type: String
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | DELETING | DELETE_FAILED | DELETED`

## Errors
<a name="API_DeleteDataset_Errors"></a>

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

 ** ThrottlingException **
This error is thrown when the client exceeds the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
This error is thrown when the client supplies invalid input to the API.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/DeleteDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/DeleteDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/DeleteDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/DeleteDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/DeleteDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/DeleteDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/DeleteDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/DeleteDataset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/DeleteDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/DeleteDataset)

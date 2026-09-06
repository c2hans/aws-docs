---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateWorkloadShare.html
---

# UpdateWorkloadShare
<a name="API_UpdateWorkloadShare"></a>

Update a workload share.

## Request Syntax
<a name="API_UpdateWorkloadShare_RequestSyntax"></a>

```
PATCH /workloads/{{WorkloadId}}/shares/{{ShareId}} HTTP/1.1
Content-type: application/json

{
   "PermissionType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkloadShare_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ShareId](#API_UpdateWorkloadShare_RequestSyntax) **   <a name="wellarchitected-UpdateWorkloadShare-request-uri-ShareId"></a>
The ID associated with the share.
Pattern: `[0-9a-f]{32}`
Required: Yes

 ** [WorkloadId](#API_UpdateWorkloadShare_RequestSyntax) **   <a name="wellarchitected-UpdateWorkloadShare-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_UpdateWorkloadShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PermissionType](#API_UpdateWorkloadShare_RequestSyntax) **   <a name="wellarchitected-UpdateWorkloadShare-request-PermissionType"></a>
Permission granted on a share request.
Type: String
Valid Values: `READONLY | CONTRIBUTOR`
Required: Yes

## Response Syntax
<a name="API_UpdateWorkloadShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "WorkloadId": "string",
   "WorkloadShare": {
      "PermissionType": "string",
      "SharedBy": "string",
      "SharedWith": "string",
      "ShareId": "string",
      "Status": "string",
      "WorkloadId": "string",
      "WorkloadName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateWorkloadShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkloadId](#API_UpdateWorkloadShare_ResponseSyntax) **   <a name="wellarchitected-UpdateWorkloadShare-response-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`

 ** [WorkloadShare](#API_UpdateWorkloadShare_ResponseSyntax) **   <a name="wellarchitected-UpdateWorkloadShare-response-WorkloadShare"></a>
A workload share return object.
Type: [WorkloadShare](API_WorkloadShare.md) object

## Errors
<a name="API_UpdateWorkloadShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UpdateWorkloadShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateWorkloadShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateWorkloadShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateWorkloadShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateWorkloadShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateWorkloadShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateWorkloadShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateWorkloadShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateWorkloadShare)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateWorkloadShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateWorkloadShare)

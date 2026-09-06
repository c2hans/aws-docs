---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_GetWorkload.html
---

# GetWorkload
<a name="API_GetWorkload"></a>

Get an existing workload.

## Request Syntax
<a name="API_GetWorkload_RequestSyntax"></a>

```
GET /workloads/{{WorkloadId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkload_RequestParameters"></a>

The request uses the following URI parameters.

 ** [WorkloadId](#API_GetWorkload_RequestSyntax) **   <a name="wellarchitected-GetWorkload-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_GetWorkload_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkload_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Workload": {
      "AccountIds": [ "string" ],
      "Applications": [ "string" ],
      "ArchitecturalDesign": "string",
      "AwsRegions": [ "string" ],
      "Description": "string",
      "DiscoveryConfig": {
         "TrustedAdvisorIntegrationStatus": "string",
         "WorkloadResourceDefinition": [ "string" ]
      },
      "Environment": "string",
      "ImprovementStatus": "string",
      "Industry": "string",
      "IndustryType": "string",
      "IsReviewOwnerUpdateAcknowledged": boolean,
      "JiraConfiguration": {
         "IssueManagementStatus": "string",
         "IssueManagementType": "string",
         "JiraProjectKey": "string",
         "StatusMessage": "string"
      },
      "Lenses": [ "string" ],
      "NonAwsRegions": [ "string" ],
      "Notes": "string",
      "Owner": "string",
      "PillarPriorities": [ "string" ],
      "PrioritizedRiskCounts": {
         "string" : number
      },
      "Profiles": [
         {
            "ProfileArn": "string",
            "ProfileVersion": "string"
         }
      ],
      "ReviewOwner": "string",
      "ReviewRestrictionDate": number,
      "RiskCounts": {
         "string" : number
      },
      "ShareInvitationId": "string",
      "Tags": {
         "string" : "string"
      },
      "UpdatedAt": number,
      "WorkloadArn": "string",
      "WorkloadId": "string",
      "WorkloadName": "string"
   }
}
```

## Response Elements
<a name="API_GetWorkload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Workload](#API_GetWorkload_ResponseSyntax) **   <a name="wellarchitected-GetWorkload-response-Workload"></a>
A workload return object.
Type: [Workload](API_Workload.md) object

## Errors
<a name="API_GetWorkload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

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
<a name="API_GetWorkload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/GetWorkload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/GetWorkload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/GetWorkload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/GetWorkload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/GetWorkload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/GetWorkload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/GetWorkload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/GetWorkload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/GetWorkload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/GetWorkload)

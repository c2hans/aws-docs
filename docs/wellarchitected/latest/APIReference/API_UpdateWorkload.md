---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UpdateWorkload.html
---

# UpdateWorkload
<a name="API_UpdateWorkload"></a>

Update an existing workload.

## Request Syntax
<a name="API_UpdateWorkload_RequestSyntax"></a>

```
PATCH /workloads/{{WorkloadId}} HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "Applications": [ "{{string}}" ],
   "ArchitecturalDesign": "{{string}}",
   "AwsRegions": [ "{{string}}" ],
   "Description": "{{string}}",
   "DiscoveryConfig": {
      "TrustedAdvisorIntegrationStatus": "{{string}}",
      "WorkloadResourceDefinition": [ "{{string}}" ]
   },
   "Environment": "{{string}}",
   "ImprovementStatus": "{{string}}",
   "Industry": "{{string}}",
   "IndustryType": "{{string}}",
   "IsReviewOwnerUpdateAcknowledged": {{boolean}},
   "JiraConfiguration": {
      "IssueManagementStatus": "{{string}}",
      "IssueManagementType": "{{string}}",
      "JiraProjectKey": "{{string}}"
   },
   "NonAwsRegions": [ "{{string}}" ],
   "Notes": "{{string}}",
   "PillarPriorities": [ "{{string}}" ],
   "ReviewOwner": "{{string}}",
   "WorkloadName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateWorkload_RequestParameters"></a>

The request uses the following URI parameters.

 ** [WorkloadId](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-uri-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`
Required: Yes

## Request Body
<a name="API_UpdateWorkload_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-AccountIds"></a>
The list of AWS account IDs associated with the workload.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** [Applications](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-Applications"></a>
List of AppRegistry application ARNs to associate to the workload.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`
Required: No

 ** [ArchitecturalDesign](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-ArchitecturalDesign"></a>
The URL of the architectural design for the workload.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^(|(https?|ftp):\/\/[^\s/$.?#].[^\s]*)$`
Required: No

 ** [AwsRegions](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-AwsRegions"></a>
The list of AWS Regions associated with the workload, for example, `us-east-2`, or `ca-central-1`.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Maximum length of 100.
Required: No

 ** [Description](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-Description"></a>
The description for the workload.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 250.
Required: No

 ** [DiscoveryConfig](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-DiscoveryConfig"></a>
Well-Architected discovery configuration settings to associate to the workload.
Type: [WorkloadDiscoveryConfig](API_WorkloadDiscoveryConfig.md) object
Required: No

 ** [Environment](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-Environment"></a>
The environment for the workload.
Type: String
Valid Values: `PRODUCTION | PREPRODUCTION`
Required: No

 ** [ImprovementStatus](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-ImprovementStatus"></a>
The improvement status for a workload.
Type: String
Valid Values: `NOT_APPLICABLE | NOT_STARTED | IN_PROGRESS | COMPLETE | RISK_ACKNOWLEDGED`
Required: No

 ** [Industry](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-Industry"></a>
The industry for the workload.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IndustryType](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-IndustryType"></a>
The industry type for the workload.
If specified, must be one of the following:
+  `Agriculture`
+  `Automobile`
+  `Defense`
+  `Design and Engineering`
+  `Digital Advertising`
+  `Education`
+  `Environmental Protection`
+  `Financial Services`
+  `Gaming`
+  `General Public Services`
+  `Healthcare`
+  `Hospitality`
+  `InfoTech`
+  `Justice and Public Safety`
+  `Life Sciences`
+  `Manufacturing`
+  `Media & Entertainment`
+  `Mining & Resources`
+  `Oil & Gas`
+  `Power & Utilities`
+  `Professional Services`
+  `Real Estate & Construction`
+  `Retail & Wholesale`
+  `Social Protection`
+  `Telecommunications`
+  `Travel, Transportation & Logistics`
+  `Other`
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IsReviewOwnerUpdateAcknowledged](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-IsReviewOwnerUpdateAcknowledged"></a>
Flag indicating whether the workload owner has acknowledged that the *Review owner* field is required.
If a **Review owner** is not added to the workload within 60 days of acknowledgement, access to the workload is restricted until an owner is added.
Type: Boolean
Required: No

 ** [JiraConfiguration](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-JiraConfiguration"></a>
Configuration of the Jira integration.
Type: [WorkloadJiraConfigurationInput](API_WorkloadJiraConfigurationInput.md) object
Required: No

 ** [NonAwsRegions](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-NonAwsRegions"></a>
 The list of non-AWS Regions associated with the workload.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 3. Maximum length of 25.
Required: No

 ** [Notes](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Maximum length of 2084.
Required: No

 ** [PillarPriorities](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-PillarPriorities"></a>
The priorities of the pillars, which are used to order items in the improvement plan. Each pillar is represented by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [ReviewOwner](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-ReviewOwner"></a>
The review owner of the workload. The name, email address, or identifier for the primary group or individual that owns the workload review process.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** [WorkloadName](#API_UpdateWorkload_RequestSyntax) **   <a name="wellarchitected-UpdateWorkload-request-WorkloadName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

## Response Syntax
<a name="API_UpdateWorkload_ResponseSyntax"></a>

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
<a name="API_UpdateWorkload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Workload](#API_UpdateWorkload_ResponseSyntax) **   <a name="wellarchitected-UpdateWorkload-response-Workload"></a>
A workload return object.
Type: [Workload](API_Workload.md) object

## Errors
<a name="API_UpdateWorkload_Errors"></a>

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
<a name="API_UpdateWorkload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UpdateWorkload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UpdateWorkload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UpdateWorkload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UpdateWorkload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UpdateWorkload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UpdateWorkload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UpdateWorkload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UpdateWorkload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UpdateWorkload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UpdateWorkload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

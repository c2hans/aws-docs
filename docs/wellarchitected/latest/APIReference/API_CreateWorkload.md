---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateWorkload.html
---

# CreateWorkload
<a name="API_CreateWorkload"></a>

Create a new workload.

The owner of a workload can share the workload with other AWS accounts, users, an organization, and organizational units (OUs) in the same AWS Region. Only the owner of a workload can delete it.

For more information, see [Defining a Workload](https://docs.aws.amazon.com/wellarchitected/latest/userguide/define-workload.html) in the * AWS Well-Architected Tool User Guide*.

**Important**
Either `AwsRegions`, `NonAwsRegions`, or both must be specified when creating a workload.
You also must specify `ReviewOwner`, even though the parameter is listed as not being required in the following section.

When creating a workload using a review template, you must have the following IAM permissions:
+  `wellarchitected:GetReviewTemplate`
+  `wellarchitected:GetReviewTemplateAnswer`
+  `wellarchitected:ListReviewTemplateAnswers`
+  `wellarchitected:GetReviewTemplateLensReview`

## Request Syntax
<a name="API_CreateWorkload_RequestSyntax"></a>

```
POST /workloads HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "Applications": [ "{{string}}" ],
   "ArchitecturalDesign": "{{string}}",
   "AwsRegions": [ "{{string}}" ],
   "ClientRequestToken": "{{string}}",
   "Description": "{{string}}",
   "DiscoveryConfig": {
      "TrustedAdvisorIntegrationStatus": "{{string}}",
      "WorkloadResourceDefinition": [ "{{string}}" ]
   },
   "Environment": "{{string}}",
   "Industry": "{{string}}",
   "IndustryType": "{{string}}",
   "JiraConfiguration": {
      "IssueManagementStatus": "{{string}}",
      "IssueManagementType": "{{string}}",
      "JiraProjectKey": "{{string}}"
   },
   "Lenses": [ "{{string}}" ],
   "NonAwsRegions": [ "{{string}}" ],
   "Notes": "{{string}}",
   "PillarPriorities": [ "{{string}}" ],
   "ProfileArns": [ "{{string}}" ],
   "ReviewOwner": "{{string}}",
   "ReviewTemplateArns": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "WorkloadName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkload_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkload_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-AccountIds"></a>
The list of AWS account IDs associated with the workload.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** [Applications](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-Applications"></a>
List of AppRegistry application ARNs associated to the workload.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`
Required: No

 ** [ArchitecturalDesign](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-ArchitecturalDesign"></a>
The URL of the architectural design for the workload.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^(|(https?|ftp):\/\/[^\s/$.?#].[^\s]*)$`
Required: No

 ** [AwsRegions](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-AwsRegions"></a>
The list of AWS Regions associated with the workload, for example, `us-east-2`, or `ca-central-1`.
Type: Array of strings
Array Members: Maximum number of 50 items.
Length Constraints: Maximum length of 100.
Required: No

 ** [ClientRequestToken](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[\x00-\x7F]*$`
Required: Yes

 ** [Description](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-Description"></a>
The description for the workload.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 250.
Required: Yes

 ** [DiscoveryConfig](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-DiscoveryConfig"></a>
Well-Architected discovery configuration settings associated to the workload.
Type: [WorkloadDiscoveryConfig](API_WorkloadDiscoveryConfig.md) object
Required: No

 ** [Environment](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-Environment"></a>
The environment for the workload.
Type: String
Valid Values: `PRODUCTION | PREPRODUCTION`
Required: Yes

 ** [Industry](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-Industry"></a>
The industry for the workload.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IndustryType](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-IndustryType"></a>
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

 ** [JiraConfiguration](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-JiraConfiguration"></a>
Jira configuration settings when creating a workload.
Type: [WorkloadJiraConfigurationInput](API_WorkloadJiraConfigurationInput.md) object
Required: No

 ** [Lenses](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-Lenses"></a>
The list of lenses associated with the workload. Each lens is identified by its [LensSummary:LensAlias](API_LensSummary.md#wellarchitected-Type-LensSummary-LensAlias).
If a review template that specifies lenses is applied to the workload, those lenses are applied to the workload in addition to these lenses.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [NonAwsRegions](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-NonAwsRegions"></a>
 The list of non-AWS Regions associated with the workload.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 3. Maximum length of 25.
Required: No

 ** [Notes](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-Notes"></a>
The notes associated with the workload.
For a review template, these are the notes that will be associated with the workload when the template is applied.
Type: String
Length Constraints: Maximum length of 2084.
Required: No

 ** [PillarPriorities](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-PillarPriorities"></a>
The priorities of the pillars, which are used to order items in the improvement plan. Each pillar is represented by its [PillarReviewSummary:PillarId](API_PillarReviewSummary.md#wellarchitected-Type-PillarReviewSummary-PillarId).
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [ProfileArns](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-ProfileArns"></a>
The list of profile ARNs associated with the workload.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`
Required: No

 ** [ReviewOwner](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-ReviewOwner"></a>
The review owner of the workload. The name, email address, or identifier for the primary group or individual that owns the workload review process.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** [ReviewTemplateArns](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-ReviewTemplateArns"></a>
The list of review template ARNs to associate with the workload.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 50. Maximum length of 250.
Pattern: `arn:aws(-us-gov|-iso(-[a-z])?|-cn)?:wellarchitected:[a-z]{2}(-gov|-iso([a-z])?)?-[a-z]+-\d:\d{12}:(review-template)/[a-f0-9]{32}`
Required: No

 ** [Tags](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-Tags"></a>
The tags to be associated with the workload.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [WorkloadName](#API_CreateWorkload_RequestSyntax) **   <a name="wellarchitected-CreateWorkload-request-WorkloadName"></a>
The name of the workload.
The name must be unique within an account within an AWS Region. Spaces and capitalization are ignored when checking for uniqueness.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: Yes

## Response Syntax
<a name="API_CreateWorkload_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "WorkloadArn": "string",
   "WorkloadId": "string"
}
```

## Response Elements
<a name="API_CreateWorkload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [WorkloadArn](#API_CreateWorkload_ResponseSyntax) **   <a name="wellarchitected-CreateWorkload-response-WorkloadArn"></a>
The ARN for the workload.
Type: String

 ** [WorkloadId](#API_CreateWorkload_ResponseSyntax) **   <a name="wellarchitected-CreateWorkload-response-WorkloadId"></a>
The ID assigned to the workload. This ID is unique within an AWS Region.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[0-9a-f]{32}`

## Errors
<a name="API_CreateWorkload_Errors"></a>

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

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

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
<a name="API_CreateWorkload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateWorkload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateWorkload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateWorkload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateWorkload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateWorkload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateWorkload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateWorkload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateWorkload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateWorkload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateWorkload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

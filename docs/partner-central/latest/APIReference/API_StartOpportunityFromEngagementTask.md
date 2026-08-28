---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartOpportunityFromEngagementTask.html
---

# StartOpportunityFromEngagementTask
<a name="API_StartOpportunityFromEngagementTask"></a>

This action creates an opportunity from an existing engagement context. The task is asynchronous and orchestrates the process of converting engagement contextual information into a structured opportunity record within the partner's account.

## Request Syntax
<a name="API_StartOpportunityFromEngagementTask_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "ContextIdentifier": "{{string}}",
   "Identifier": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_StartOpportunityFromEngagementTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_StartOpportunityFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-request-Catalog"></a>
Specifies the catalog in which the opportunity creation task is executed. Acceptable values include `AWS` for production and `Sandbox` for testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_StartOpportunityFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-request-ClientToken"></a>
A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.
Type: String
Pattern: `.{1,255}`
Required: Yes

 ** [ContextIdentifier](#API_StartOpportunityFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-request-ContextIdentifier"></a>
The unique identifier of the engagement context from which to create the opportunity. This specifies the specific contextual information within the engagement that will be used for opportunity creation.
Type: String
Pattern: `[1-9][0-9]*`
Required: Yes

 ** [Identifier](#API_StartOpportunityFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-request-Identifier"></a>
The unique identifier of the engagement from which the opportunity creation task is to be initiated. This helps ensure that the task is applied to the correct engagement.
Type: String
Pattern: `(arn:.*|eng-[0-9a-z]{14})`
Required: Yes

 ** [Tags](#API_StartOpportunityFromEngagementTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-request-Tags"></a>
A map of the key-value pairs of the tag or tags to assign.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_StartOpportunityFromEngagementTask_ResponseSyntax"></a>

```
{
   "ContextId": "string",
   "EngagementId": "string",
   "Message": "string",
   "OpportunityId": "string",
   "ReasonCode": "string",
   "ResourceSnapshotJobId": "string",
   "StartTime": "string",
   "TaskArn": "string",
   "TaskId": "string",
   "TaskStatus": "string"
}
```

## Response Elements
<a name="API_StartOpportunityFromEngagementTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContextId](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-ContextId"></a>
The unique identifier of the engagement context used to create the opportunity.
Type: String
Pattern: `[1-9][0-9]*`

 ** [EngagementId](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-EngagementId"></a>
The unique identifier of the engagement from which the opportunity was created.
Type: String
Pattern: `eng-[0-9a-z]{14}`

 ** [Message](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-Message"></a>
If the task fails, this field contains a detailed message describing the failure and possible recovery steps.
Type: String

 ** [OpportunityId](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-OpportunityId"></a>
The unique identifier of the opportunity created as a result of the task. This field is populated when the task is completed successfully.
Type: String
Pattern: `O[0-9]{1,19}`

 ** [ReasonCode](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-ReasonCode"></a>
Indicates the reason for task failure using an enumerated code.
Type: String
Valid Values: `InvitationAccessDenied | InvitationValidationFailed | EngagementAccessDenied | OpportunityAccessDenied | ResourceSnapshotJobAccessDenied | ResourceSnapshotJobValidationFailed | ResourceSnapshotJobConflict | EngagementValidationFailed | EngagementConflict | OpportunitySubmissionFailed | EngagementInvitationConflict | InternalError | OpportunityValidationFailed | OpportunityConflict | ResourceSnapshotAccessDenied | ResourceSnapshotValidationFailed | ResourceSnapshotConflict | ServiceQuotaExceeded | RequestThrottled | ContextNotFound | CustomerProjectContextNotPermitted | DisqualifiedLeadNotPermitted`

 ** [ResourceSnapshotJobId](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-ResourceSnapshotJobId"></a>
The identifier of the resource snapshot job created as part of the opportunity creation process.
Type: String
Pattern: `job-[0-9a-z]{13}`

 ** [StartTime](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-StartTime"></a>
The timestamp indicating when the task was initiated. The format follows RFC 3339 section 5.6.
Type: Timestamp

 ** [TaskArn](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-TaskArn"></a>
The Amazon Resource Name (ARN) of the task, used for tracking and managing the task within AWS.
Type: String
Pattern: `arn:.*`

 ** [TaskId](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-TaskId"></a>
The unique identifier of the task, used to track the task's progress.
Type: String
Pattern: `.*task-[0-9a-z]{13}`

 ** [TaskStatus](#API_StartOpportunityFromEngagementTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartOpportunityFromEngagementTask-response-TaskStatus"></a>
Indicates the current status of the task.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`

## Errors
<a name="API_StartOpportunityFromEngagementTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error occurs when you don't have permission to perform the requested action.
You don’t have access to this action or resource. Review IAM policies or contact your AWS administrator for assistance.
 ** Reason **
The reason why access was denied for the requested operation.
HTTP Status Code: 400

 ** ConflictException **
This error occurs when the request can’t be processed due to a conflict with the target resource's current state, which could result from updating or deleting the resource.
Suggested action: Fetch the latest state of the resource, verify the state, and retry the request.
HTTP Status Code: 400

 ** InternalServerException **
This error occurs when the specified resource can’t be found or doesn't exist. Resource ID and type might be incorrect.
Suggested action: This is usually a transient error. Retry after the provided retry delay or a short interval. If the problem persists, contact AWS support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error occurs when the specified resource can't be found. The resource might not exist, or isn't visible with the current credentials.
Suggested action: Verify that the resource ID is correct and the resource is in the expected AWS region. Check IAM permissions for accessing the resource.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
This error occurs when the request would cause a service quota to be exceeded. Service quotas represent the maximum allowed use of a specific resource, and this error indicates that the request would surpass that limit.
Suggested action: Review the [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) for the resource, and either reduce usage or request a quota increase.
HTTP Status Code: 400

 ** ThrottlingException **
This error occurs when there are too many requests sent. Review the provided quotas and adapt your usage to avoid throttling.
This error occurs when there are too many requests sent. Review the provided [Quotas](https://docs.aws.amazon.com/partner-central/latest/selling-api/quotas.html) and retry after the provided delay.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service or business validation rules.
Suggested action: Review the error message, including the failed fields and reasons, to correct the request payload.
 ** ErrorList **
A list of issues that were discovered in the submitted request or the resource state.
 ** Reason **
The primary reason for this validation exception to occur.
+  *REQUEST\_VALIDATION\_FAILED:* The request format is not valid.

  Fix: Verify your request payload includes all required fields, uses correct data types and string formats.
+  *BUSINESS\_VALIDATION\_FAILED:* The requested change doesn't pass the business validation rules.

  Fix: Check that your change aligns with the business rules defined by AWS Partner Central.
HTTP Status Code: 400

## See Also
<a name="API_StartOpportunityFromEngagementTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/StartOpportunityFromEngagementTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

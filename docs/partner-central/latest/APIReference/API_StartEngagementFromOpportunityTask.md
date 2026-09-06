---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartEngagementFromOpportunityTask.html
---

# StartEngagementFromOpportunityTask
<a name="API_StartEngagementFromOpportunityTask"></a>

Similar to `StartEngagementByAcceptingInvitationTask`, this action is asynchronous and performs multiple steps before completion. This action orchestrates a comprehensive workflow that combines multiple API operations into a single task to create and initiate an engagement from an existing opportunity. It automatically executes a sequence of operations including `GetOpportunity`, `CreateEngagement` (if it doesn't exist), `CreateResourceSnapshot`, `CreateResourceSnapshotJob`, `CreateEngagementInvitation` (if not already invited/accepted), and `SubmitOpportunity`.

## Request Syntax
<a name="API_StartEngagementFromOpportunityTask_RequestSyntax"></a>

```
{
   "AwsSubmission": {
      "InvolvementType": "{{string}}",
      "Visibility": "{{string}}"
   },
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
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
<a name="API_StartEngagementFromOpportunityTask_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AwsSubmission](#API_StartEngagementFromOpportunityTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-request-AwsSubmission"></a>
Indicates the level of AWS involvement in the opportunity. This field helps track AWS participation throughout the engagement, such as providing technical support, deal assistance, and sales support.
Type: [AwsSubmission](API_AwsSubmission.md) object
Required: Yes

 ** [Catalog](#API_StartEngagementFromOpportunityTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-request-Catalog"></a>
Specifies the catalog in which the engagement is tracked. Acceptable values include `AWS` for production and `Sandbox` for testing environments.
Type: String
Pattern: `[a-zA-Z]+`
Required: Yes

 ** [ClientToken](#API_StartEngagementFromOpportunityTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-request-ClientToken"></a>
A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.
Type: String
Pattern: `.{1,255}`
Required: Yes

 ** [Identifier](#API_StartEngagementFromOpportunityTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-request-Identifier"></a>
The unique identifier of the opportunity from which the engagement task is to be initiated. This helps ensure that the task is applied to the correct opportunity.
Type: String
Pattern: `O[0-9]{1,19}`
Required: Yes

 ** [Tags](#API_StartEngagementFromOpportunityTask_RequestSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-request-Tags"></a>
A map of the key-value pairs of the tag or tags to assign.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_StartEngagementFromOpportunityTask_ResponseSyntax"></a>

```
{
   "EngagementId": "string",
   "EngagementInvitationId": "string",
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
<a name="API_StartEngagementFromOpportunityTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EngagementId](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-EngagementId"></a>
The identifier of the newly created Engagement. Only populated if TaskStatus is COMPLETE.
Type: String
Pattern: `eng-[0-9a-z]{14}`

 ** [EngagementInvitationId](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-EngagementInvitationId"></a>
The identifier of the new Engagement invitation. Only populated if TaskStatus is COMPLETE.
Type: String
Pattern: `engi-[0-9,a-z]{13}`

 ** [Message](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-Message"></a>
If the task fails, this field contains a detailed message describing the failure and possible recovery steps.
Type: String

 ** [OpportunityId](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-OpportunityId"></a>
Returns the original opportunity identifier passed in the request, which is the unique identifier for the opportunity created in the partner’s system.
Type: String
Pattern: `O[0-9]{1,19}`

 ** [ReasonCode](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-ReasonCode"></a>
Indicates the reason for task failure using an enumerated code.
Type: String
Valid Values: `InvitationAccessDenied | InvitationValidationFailed | EngagementAccessDenied | OpportunityAccessDenied | ResourceSnapshotJobAccessDenied | ResourceSnapshotJobValidationFailed | ResourceSnapshotJobConflict | EngagementValidationFailed | EngagementConflict | OpportunitySubmissionFailed | EngagementInvitationConflict | InternalError | OpportunityValidationFailed | OpportunityConflict | ResourceSnapshotAccessDenied | ResourceSnapshotValidationFailed | ResourceSnapshotConflict | ServiceQuotaExceeded | RequestThrottled | ContextNotFound | CustomerProjectContextNotPermitted | DisqualifiedLeadNotPermitted`

 ** [ResourceSnapshotJobId](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-ResourceSnapshotJobId"></a>
The identifier of the resource snapshot job created to add the opportunity resource snapshot to the Engagement. Only populated if TaskStatus is COMPLETE
Type: String
Pattern: `job-[0-9a-z]{13}`

 ** [StartTime](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-StartTime"></a>
The timestamp indicating when the task was initiated. The format follows RFC 3339 section 5.6.
Type: Timestamp

 ** [TaskArn](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-TaskArn"></a>
The Amazon Resource Name (ARN) of the task, used for tracking and managing the task within AWS.
Type: String
Pattern: `arn:.*`

 ** [TaskId](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-TaskId"></a>
The unique identifier of the task, used to track the task’s progress. This value follows a specific pattern: `^oit-[0-9a-z]{13}$`.
Type: String
Pattern: `.*task-[0-9a-z]{13}`

 ** [TaskStatus](#API_StartEngagementFromOpportunityTask_ResponseSyntax) **   <a name="AWSPartnerCentral-StartEngagementFromOpportunityTask-response-TaskStatus"></a>
Indicates the current status of the task. Valid values include `IN_PROGRESS`, `COMPLETE`, and `FAILED`.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`

## Errors
<a name="API_StartEngagementFromOpportunityTask_Errors"></a>

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
<a name="API_StartEngagementFromOpportunityTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)

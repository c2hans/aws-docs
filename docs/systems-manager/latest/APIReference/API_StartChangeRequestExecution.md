---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartChangeRequestExecution.html
---

# StartChangeRequestExecution
<a name="API_StartChangeRequestExecution"></a>

**Important**
 AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html).

Creates a change request for Change Manager. The Automation runbooks specified in the change request run only after all required approvals for the change request have been received.

## Request Syntax
<a name="API_StartChangeRequestExecution_RequestSyntax"></a>

```
{
   "AutoApprove": {{boolean}},
   "ChangeDetails": "{{string}}",
   "ChangeRequestName": "{{string}}",
   "ClientToken": "{{string}}",
   "DocumentName": "{{string}}",
   "DocumentVersion": "{{string}}",
   "Parameters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "Runbooks": [
      {
         "DocumentName": "{{string}}",
         "DocumentVersion": "{{string}}",
         "MaxConcurrency": "{{string}}",
         "MaxErrors": "{{string}}",
         "Parameters": {
            "{{string}}" : [ "{{string}}" ]
         },
         "TargetLocations": [
            {
               "Accounts": [ "{{string}}" ],
               "ExcludeAccounts": [ "{{string}}" ],
               "ExecutionRoleName": "{{string}}",
               "IncludeChildOrganizationUnits": {{boolean}},
               "Regions": [ "{{string}}" ],
               "TargetLocationAlarmConfiguration": {
                  "Alarms": [
                     {
                        "Name": "{{string}}"
                     }
                  ],
                  "IgnorePollAlarmFailure": {{boolean}}
               },
               "TargetLocationMaxConcurrency": "{{string}}",
               "TargetLocationMaxErrors": "{{string}}",
               "Targets": [
                  {
                     "Key": "{{string}}",
                     "Values": [ "{{string}}" ]
                  }
               ],
               "TargetsMaxConcurrency": "{{string}}",
               "TargetsMaxErrors": "{{string}}"
            }
         ],
         "TargetMaps": [
            {
               "{{string}}" : [ "{{string}}" ]
            }
         ],
         "TargetParameterName": "{{string}}",
         "Targets": [
            {
               "Key": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ]
      }
   ],
   "ScheduledEndTime": {{number}},
   "ScheduledTime": {{number}},
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_StartChangeRequestExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutoApprove](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-AutoApprove"></a>
Indicates whether the change request can be approved automatically without the need for manual approvals.
If `AutoApprovable` is enabled in a change template, then setting `AutoApprove` to `true` in `StartChangeRequestExecution` creates a change request that bypasses approver review.
Change Calendar restrictions are not bypassed in this scenario. If the state of an associated calendar is `CLOSED`, change freeze approvers must still grant permission for this change request to run. If they don't, the change won't be processed until the calendar state is again `OPEN`.
Type: Boolean
Required: No

 ** [ChangeDetails](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-ChangeDetails"></a>
User-provided details about the change. If no details are provided, content specified in the **Template information** section of the associated change template is added.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: No

 ** [ChangeRequestName](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-ChangeRequestName"></a>
The name of the change request associated with the runbook workflow to be run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [ClientToken](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-ClientToken"></a>
The user-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can't be reused.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: No

 ** [DocumentName](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-DocumentName"></a>
The name of the change template document to run during the runbook workflow.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** [DocumentVersion](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-DocumentVersion"></a>
The version of the change template document to run during the runbook workflow.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [Parameters](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-Parameters"></a>
A key-value map of parameters that match the declared parameters in the change template document.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [Runbooks](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-Runbooks"></a>
Information about the Automation runbooks that are run during the runbook workflow.
The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.
Type: Array of [Runbook](API_Runbook.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** [ScheduledEndTime](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-ScheduledEndTime"></a>
The time that the requester expects the runbook workflow related to the change request to complete. The time is an estimate only that the requester provides for reviewers.
Type: Timestamp
Required: No

 ** [ScheduledTime](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-ScheduledTime"></a>
The date and time specified in the change request to run the Automation runbooks.
The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.
Type: Timestamp
Required: No

 ** [Tags](#API_StartChangeRequestExecution_RequestSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-request-Tags"></a>
Optional metadata that you assign to a resource. You can specify a maximum of five tags for a change request. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a change request to identify an environment or target AWS Region. In this case, you could specify the following key-value pairs:
+  `Key=Environment,Value=Production`
+  `Key=Region,Value=us-east-2`
The `Array Members` maximum value is reported as 1000. This number includes capacity reserved for internal operations. When calling the `StartChangeRequestExecution` action, you can specify a maximum of 5 tags. You can, however, use the [AddTagsToResource](API_AddTagsToResource.md) action to add up to a total of 50 tags to an existing change request configuration.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

## Response Syntax
<a name="API_StartChangeRequestExecution_ResponseSyntax"></a>

```
{
   "AutomationExecutionId": "string"
}
```

## Response Elements
<a name="API_StartChangeRequestExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutomationExecutionId](#API_StartChangeRequestExecution_ResponseSyntax) **   <a name="systemsmanager-StartChangeRequestExecution-response-AutomationExecutionId"></a>
The unique ID of a runbook workflow operation. (A runbook workflow is a type of Automation operation.)
Type: String
Length Constraints: Fixed length of 36.

## Errors
<a name="API_StartChangeRequestExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AutomationDefinitionNotApprovedException **
Indicates that the Change Manager change template used in the change request was rejected or is still in a pending state.
HTTP Status Code: 400

 ** AutomationDefinitionNotFoundException **
An Automation runbook with the specified name couldn't be found.
HTTP Status Code: 400

 ** AutomationDefinitionVersionNotFoundException **
An Automation runbook with the specified name and version couldn't be found.
HTTP Status Code: 400

 ** AutomationExecutionLimitExceededException **
The number of simultaneously running Automation executions exceeded the allowable limit.
HTTP Status Code: 400

 ** IdempotentParameterMismatch **
Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidAutomationExecutionParametersException **
The supplied parameters for invoking the specified Automation runbook are incorrect. For example, they may not match the set of parameters permitted for the specified Automation document.
HTTP Status Code: 400

 ** NoLongerSupportedException **
The requested operation is no longer supported by Systems Manager.
HTTP Status Code: 400

## Examples
<a name="API_StartChangeRequestExecution_Examples"></a>

### Example
<a name="API_StartChangeRequestExecution_Example_1"></a>

This example illustrates one usage of StartChangeRequestExecution.

#### Sample Request
<a name="API_StartChangeRequestExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.StartChangeRequestExecution
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.12 Python/3.8.8 Windows/10 exe/AMD64 prompt/off command/ssm.start-change-request-execution
X-Amz-Date: 20240820T192759Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240820/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 1247

{
    "ChangeRequestName": "MyChangeRequest",
    "DocumentName": "AWS-HelloWorldChangeTemplate",
    "DocumentVersion": "$DEFAULT",
    "ScheduledTime": 1640833200,
    "ScheduledEndTime": 1640833500,
    "Tags": [
        {
            "Key": "Purpose",
            "Value": "Testing"
        }
    ],
    "Parameters": {
        "Approver": [
            "JohnDoe"
        ],
        "ApproverType": [
            "IamUser"
        ],
        "ApproverSnsTopicArn": [
            "arn:aws:sns:us-east-2:111122223333:MyNotificationTopic"
        ]
    },
    "Runbooks": [
        {
            "DocumentName": "AWS-HelloWorld",
            "DocumentVersion": "1",
            "MaxConcurrency": "1",
            "MaxErrors": "1",
            "Parameters": {
                "AutomationAssumeRole": [
                    "arn:aws:iam::111122223333:role/MyChangeManagerAssumeRole"
                ]
            }
        }
    ],
    "ChangeDetails": "### Document Name: HelloWorldChangeTemplate\n\n## What does this document do?\nThis change template demonstrates the feature set available for creating change templates for Change Manager. This template starts a Runbook workflow for the Automation document called AWS-HelloWorld.\n\n## Input Parameters\n* ApproverSnsTopicArn: (Required) Amazon Simple Notification Service ARN for approvers.\n* Approver: (Required) The name of the approver to send this request to.\n* ApproverType: (Required) The type of reviewer.\n  * Allowed Values: IamUser, IamGroup, IamRole, SSOGroup, SSOUser\n\n## Output Parameters\nThis document has no outputs \n"
}
```

#### Sample Response
<a name="API_StartChangeRequestExecution_Example_1_Response"></a>

```
{
    "AutomationExecutionId": "dddd1c6c-849d-4ee0-acc1-0be9dEXAMPLE"
}
```

## See Also
<a name="API_StartChangeRequestExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/StartChangeRequestExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/StartChangeRequestExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/StartChangeRequestExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/StartChangeRequestExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/StartChangeRequestExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/StartChangeRequestExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/StartChangeRequestExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/StartChangeRequestExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/StartChangeRequestExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/StartChangeRequestExecution)

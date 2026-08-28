---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartAutomationExecution.html
---

# StartAutomationExecution
<a name="API_StartAutomationExecution"></a>

Initiates execution of an Automation runbook.

## Request Syntax
<a name="API_StartAutomationExecution_RequestSyntax"></a>

```
{
   "AlarmConfiguration": {
      "Alarms": [
         {
            "Name": "{{string}}"
         }
      ],
      "IgnorePollAlarmFailure": {{boolean}}
   },
   "ClientToken": "{{string}}",
   "DocumentName": "{{string}}",
   "DocumentVersion": "{{string}}",
   "MaxConcurrency": "{{string}}",
   "MaxErrors": "{{string}}",
   "Mode": "{{string}}",
   "Parameters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
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
   "TargetLocationsURL": "{{string}}",
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
```

## Request Parameters
<a name="API_StartAutomationExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlarmConfiguration](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-AlarmConfiguration"></a>
The CloudWatch alarm you want to apply to your automation.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** [ClientToken](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-ClientToken"></a>
User-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can't be reused.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: No

 ** [DocumentName](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-DocumentName"></a>
The name of the SSM document to run. This can be a public document or a custom document. To run a shared document belonging to another account, specify the document ARN. For more information about how to use shared documents, see [Sharing SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html) in the * AWS Systems Manager User Guide*.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** [DocumentVersion](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-DocumentVersion"></a>
The version of the Automation runbook to use for this execution.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [MaxConcurrency](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-MaxConcurrency"></a>
The maximum number of targets allowed to run this task in parallel. You can specify a number, such as 10, or a percentage, such as 10%. The default value is `10`.
If both this parameter and the `TargetLocation:TargetsMaxConcurrency` are supplied, `TargetLocation:TargetsMaxConcurrency` takes precedence.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** [MaxErrors](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-MaxErrors"></a>
The number of errors that are allowed before the system stops running the automation on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops running the automation when the fourth error is received. If you specify 0, then the system stops running the automation on additional targets after the first error result is returned. If you run an automation on 50 resources and set max-errors to 10%, then the system stops running the automation on additional targets when the sixth error is received.
Executions that are already running an automation when max-errors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set max-concurrency to 1 so the executions proceed one at a time.
If this parameter and the `TargetLocation:TargetsMaxErrors` parameter are both supplied, `TargetLocation:TargetsMaxErrors` takes precedence.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** [Mode](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-Mode"></a>
The execution mode of the automation. Valid modes include the following: Auto and Interactive. The default mode is Auto.
Type: String
Valid Values: `Auto | Interactive`
Required: No

 ** [Parameters](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-Parameters"></a>
A key-value map of execution parameters, which match the declared parameters in the Automation runbook.
Type: String to array of strings map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [Tags](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-Tags"></a>
Optional metadata that you assign to a resource. You can specify a maximum of five tags for an automation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an automation to identify an environment or operating system. In this case, you could specify the following key-value pairs:
+  `Key=environment,Value=test`
+  `Key=OS,Value=Windows`
The `Array Members` maximum value is reported as 1000. This number includes capacity reserved for internal operations. When calling the `StartAutomationExecution` action, you can specify a maximum of 5 tags. You can, however, use the [AddTagsToResource](API_AddTagsToResource.md) action to add up to a total of 50 tags to an existing automation configuration.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

 ** [TargetLocations](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-TargetLocations"></a>
A location is a combination of AWS Regions and/or AWS accounts where you want to run the automation. Use this operation to start an automation in multiple AWS Regions and multiple AWS accounts. For more information, see [Running automations in multiple AWS Regions and accounts](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation-multiple-accounts-and-regions.html) in the * AWS Systems Manager User Guide*.
Type: Array of [TargetLocation](API_TargetLocation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [TargetLocationsURL](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-TargetLocationsURL"></a>
Specify a publicly accessible URL for a file that contains the `TargetLocations` body. Currently, only files in presigned Amazon S3 buckets are supported.
Type: String
Pattern: `^https:\/\/[-a-zA-Z0-9@:%._\+~#=]{1,253}\.s3(\.[a-z\d-]{9,16})?\.amazonaws\.com\/.{1,2000}`
Required: No

 ** [TargetMaps](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-TargetMaps"></a>
A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.
Type: Array of string to array of strings maps
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** [TargetParameterName](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-TargetParameterName"></a>
The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify targets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** [Targets](#API_StartAutomationExecution_RequestSyntax) **   <a name="systemsmanager-StartAutomationExecution-request-Targets"></a>
A key-value mapping to target resources. Required if you specify TargetParameterName.
If both this parameter and the `TargetLocation:Targets` parameter are supplied, `TargetLocation:Targets` takes precedence.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## Response Syntax
<a name="API_StartAutomationExecution_ResponseSyntax"></a>

```
{
   "AutomationExecutionId": "string"
}
```

## Response Elements
<a name="API_StartAutomationExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutomationExecutionId](#API_StartAutomationExecution_ResponseSyntax) **   <a name="systemsmanager-StartAutomationExecution-response-AutomationExecutionId"></a>
The unique ID of a newly scheduled automation execution.
Type: String
Length Constraints: Fixed length of 36.

## Errors
<a name="API_StartAutomationExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InvalidTarget **
The target isn't valid or doesn't exist. It might not be configured for Systems Manager or you might not have permission to perform the operation.
HTTP Status Code: 400

## Examples
<a name="API_StartAutomationExecution_Examples"></a>

### Example
<a name="API_StartAutomationExecution_Example_1"></a>

This example illustrates one usage of StartAutomationExecution.

#### Sample Request
<a name="API_StartAutomationExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.StartAutomationExecution
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T162110Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 86

{
    "DocumentName": "Example",
    "Parameters": {
        "InstanceId": [
            "i-02573cafcfEXAMPLE"
        ]
    }
}
```

#### Sample Response
<a name="API_StartAutomationExecution_Example_1_Response"></a>

```
{
    "AutomationExecutionId": "832a6fba-f4f0-4b2a-ab85-587adEXAMPLE"
}
```

## See Also
<a name="API_StartAutomationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/StartAutomationExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/StartAutomationExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/StartAutomationExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/StartAutomationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/StartAutomationExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/StartAutomationExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/StartAutomationExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/StartAutomationExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/StartAutomationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/StartAutomationExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

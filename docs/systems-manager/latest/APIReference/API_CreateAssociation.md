---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html
---

# CreateAssociation
<a name="API_CreateAssociation"></a>

A State Manager association defines the state that you want to maintain on your managed nodes. For example, an association can specify that anti-virus software must be installed and running on your managed nodes, or that certain ports must be closed. For static targets, the association specifies a schedule for when the configuration is reapplied. For dynamic targets, such as an AWS resource group or an AWS autoscaling group, State Manager, a tool in AWS Systems Manager applies the configuration when new managed nodes are added to the group. The association also specifies actions to take when applying the configuration. For example, an association for anti-virus software might run once a day. If the software isn't installed, then State Manager installs it. If the software is installed, but the service isn't running, then the association might instruct State Manager to start the service.

## Request Syntax
<a name="API_CreateAssociation_RequestSyntax"></a>

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
   "ApplyOnlyAtCronInterval": {{boolean}},
   "AssociationDispatchAssumeRole": "{{string}}",
   "AssociationName": "{{string}}",
   "AutomationTargetParameterName": "{{string}}",
   "CalendarNames": [ "{{string}}" ],
   "ComplianceSeverity": "{{string}}",
   "DocumentVersion": "{{string}}",
   "Duration": {{number}},
   "InstanceId": "{{string}}",
   "MaxConcurrency": "{{string}}",
   "MaxErrors": "{{string}}",
   "Name": "{{string}}",
   "OutputLocation": {
      "S3Location": {
         "OutputS3BucketName": "{{string}}",
         "OutputS3KeyPrefix": "{{string}}",
         "OutputS3Region": "{{string}}"
      }
   },
   "Parameters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "ScheduleExpression": "{{string}}",
   "ScheduleOffset": {{number}},
   "SyncCompliance": "{{string}}",
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
   "TargetMaps": [
      {
         "{{string}}" : [ "{{string}}" ]
      }
   ],
   "Targets": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlarmConfiguration](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-AlarmConfiguration"></a>
The details for the CloudWatch alarm you want to apply to an automation or command.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** [ApplyOnlyAtCronInterval](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-ApplyOnlyAtCronInterval"></a>
By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified and when target changes are detected. Specify `true` for `ApplyOnlyAtCronInterval`if you want the association to run only according to the schedule you specified.
For more information, see [Understanding when associations are applied to resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#state-manager-about-scheduling) and [>About target updates with Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#runbook-target-updates) in the * AWS Systems Manager User Guide*.
This parameter isn't supported for rate expressions.
Type: Boolean
Required: No

 ** [AssociationDispatchAssumeRole](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-AssociationDispatchAssumeRole"></a>
A role used by association to take actions on your behalf. State Manager will assume this role and call required APIs when dispatching configurations to nodes. If not specified, [ service-linked role for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html) will be used by default.
It is recommended that you define a custom IAM role so that you have full control of the permissions that State Manager has when taking actions on your behalf.
Service-linked role support in State Manager is being phased out. Associations relying on service-linked role may require updates in the future to continue functioning properly.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** [AssociationName](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-AssociationName"></a>
Specify a descriptive name for the association.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** [AutomationTargetParameterName](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-AutomationTargetParameterName"></a>
Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a tool in AWS Systems Manager.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** [CalendarNames](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-CalendarNames"></a>
The names of Amazon Resource Names (ARNs) of the Change Calendar type documents you want to gate your associations under. The associations only run when that change calendar is open. For more information, see [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Required: No

 ** [ComplianceSeverity](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-ComplianceSeverity"></a>
The severity level to assign to the association.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | UNSPECIFIED`
Required: No

 ** [DocumentVersion](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-DocumentVersion"></a>
The document version you want to associate with the targets. Can be a specific version or the default version.
State Manager doesn't support running associations that use a new version of a document if that document is shared from another account. State Manager always runs the `default` version of a document if shared from another account, even though the Systems Manager console shows that a new version was processed. If you want to run an association using a new version of a document shared form another account, you must set the document version to `default`.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** [Duration](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-Duration"></a>
The number of hours the association can run before it is canceled. Duration applies to associations that are currently running, and any pending and in progress commands on all targets. If a target was taken offline for the association to run, it is made available again immediately, without a reboot.
The `Duration` parameter applies only when both these conditions are true:
+ The association for which you specify a duration is cancelable according to the parameters of the SSM command document or Automation runbook associated with this execution.
+ The command specifies the ` [ApplyOnlyAtCronInterval](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html#systemsmanager-CreateAssociation-request-ApplyOnlyAtCronInterval) ` parameter, which means that the association doesn't run immediately after it is created, but only according to the specified schedule.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: No

 ** [InstanceId](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-InstanceId"></a>
The managed node ID.
 `InstanceId` has been deprecated. To specify a managed node ID for an association, use the `Targets` parameter. Requests that include the parameter `InstanceID` with Systems Manager documents (SSM documents) that use schema version 2.0 or later will fail. In addition, if you use the parameter `InstanceId`, you can't use the parameters `AssociationName`, `DocumentVersion`, `MaxErrors`, `MaxConcurrency`, `OutputLocation`, or `ScheduleExpression`. To use these parameters, you must use the `Targets` parameter.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** [MaxConcurrency](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-MaxConcurrency"></a>
The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new managed node starts and attempts to run an association while Systems Manager is running `MaxConcurrency` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for `MaxConcurrency`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** [MaxErrors](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-MaxErrors"></a>
The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set `MaxError` to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when `MaxErrors` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set `MaxConcurrency` to 1 so that executions proceed one at a time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** [Name](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-Name"></a>
The name of the SSM Command document or Automation runbook that contains the configuration information for the managed node.
You can specify AWS-predefined documents, documents you created, or a document that is shared with you from another AWS account.
For Systems Manager documents (SSM documents) that are shared with you from other AWS accounts, you must specify the complete SSM document ARN, in the following format:
 `arn:partition:ssm:region:account-id:document/document-name `
For example:
 `arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document`
For AWS-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, `AWS-ApplyPatchBaseline` or `My-Document`.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** [OutputLocation](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-OutputLocation"></a>
An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.
Type: [InstanceAssociationOutputLocation](API_InstanceAssociationOutputLocation.md) object
Required: No

 ** [Parameters](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-Parameters"></a>
The parameters for the runtime configuration of the document.
Type: String to array of strings map
Required: No

 ** [ScheduleExpression](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-ScheduleExpression"></a>
A cron expression when the association will be applied to the targets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [ScheduleOffset](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-ScheduleOffset"></a>
Number of days to wait after the scheduled day to run an association. For example, if you specified a cron schedule of `cron(0 0 ? * THU#2 *)`, you could specify an offset of 3 to run the association each Sunday after the second Thursday of the month. For more information about cron schedules for associations, see [Reference: Cron and rate expressions for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html) in the * AWS Systems Manager User Guide*.
To use offsets, you must specify the `ApplyOnlyAtCronInterval` parameter. This option tells the system not to run an association immediately after you create it.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.
Required: No

 ** [SyncCompliance](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-SyncCompliance"></a>
The mode for generating association compliance. You can specify `AUTO` or `MANUAL`. In `AUTO` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is `COMPLIANT`. If the association execution doesn't run successfully, the association is `NON-COMPLIANT`.
In `MANUAL` mode, you must specify the `AssociationId` as a parameter for the [PutComplianceItems](API_PutComplianceItems.md) API operation. In this case, compliance data isn't managed by State Manager. It is managed by your direct call to the [PutComplianceItems](API_PutComplianceItems.md) API operation.
By default, all associations use `AUTO` mode.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** [Tags](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-Tags"></a>
Adds or overwrites one or more tags for a State Manager association. *Tags* are metadata that you can assign to your AWS resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Maximum number of 1000 items.
Required: No

 ** [TargetLocations](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-TargetLocations"></a>
A location is a combination of AWS Regions and AWS accounts where you want to run the association. Use this action to create an association in multiple Regions and multiple accounts.
The `TargetLocationAlarmConfiguration` parameter is not supported by State Manager.
Type: Array of [TargetLocation](API_TargetLocation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** [TargetMaps](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-TargetMaps"></a>
A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.
Type: Array of string to array of strings maps
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** [Targets](#API_CreateAssociation_RequestSyntax) **   <a name="systemsmanager-CreateAssociation-request-Targets"></a>
The targets for the association. You can target managed nodes by using tags, AWS resource groups, all managed nodes in an AWS account, or individual managed node IDs. You can target all managed nodes in an AWS account by specifying the `InstanceIds` key with a value of `*`. For more information about choosing targets for an association, see [Understanding targets and rate controls in State Manager associations](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-targets-and-rate-controls.html) in the * AWS Systems Manager User Guide*.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## Response Syntax
<a name="API_CreateAssociation_ResponseSyntax"></a>

```
{
   "AssociationDescription": {
      "AlarmConfiguration": {
         "Alarms": [
            {
               "Name": "string"
            }
         ],
         "IgnorePollAlarmFailure": boolean
      },
      "ApplyOnlyAtCronInterval": boolean,
      "AssociationDispatchAssumeRole": "string",
      "AssociationId": "string",
      "AssociationName": "string",
      "AssociationVersion": "string",
      "AutomationTargetParameterName": "string",
      "CalendarNames": [ "string" ],
      "ComplianceSeverity": "string",
      "Date": number,
      "DocumentVersion": "string",
      "Duration": number,
      "InstanceId": "string",
      "LastExecutionDate": number,
      "LastSuccessfulExecutionDate": number,
      "LastUpdateAssociationDate": number,
      "MaxConcurrency": "string",
      "MaxErrors": "string",
      "Name": "string",
      "OutputLocation": {
         "S3Location": {
            "OutputS3BucketName": "string",
            "OutputS3KeyPrefix": "string",
            "OutputS3Region": "string"
         }
      },
      "Overview": {
         "AssociationStatusAggregatedCount": {
            "string" : number
         },
         "DetailedStatus": "string",
         "Status": "string"
      },
      "Parameters": {
         "string" : [ "string" ]
      },
      "ScheduleExpression": "string",
      "ScheduleOffset": number,
      "Status": {
         "AdditionalInfo": "string",
         "Date": number,
         "Message": "string",
         "Name": "string"
      },
      "SyncCompliance": "string",
      "TargetLocations": [
         {
            "Accounts": [ "string" ],
            "ExcludeAccounts": [ "string" ],
            "ExecutionRoleName": "string",
            "IncludeChildOrganizationUnits": boolean,
            "Regions": [ "string" ],
            "TargetLocationAlarmConfiguration": {
               "Alarms": [
                  {
                     "Name": "string"
                  }
               ],
               "IgnorePollAlarmFailure": boolean
            },
            "TargetLocationMaxConcurrency": "string",
            "TargetLocationMaxErrors": "string",
            "Targets": [
               {
                  "Key": "string",
                  "Values": [ "string" ]
               }
            ],
            "TargetsMaxConcurrency": "string",
            "TargetsMaxErrors": "string"
         }
      ],
      "TargetMaps": [
         {
            "string" : [ "string" ]
         }
      ],
      "Targets": [
         {
            "Key": "string",
            "Values": [ "string" ]
         }
      ],
      "TriggeredAlarms": [
         {
            "Name": "string",
            "State": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationDescription](#API_CreateAssociation_ResponseSyntax) **   <a name="systemsmanager-CreateAssociation-response-AssociationDescription"></a>
Information about the association.
Type: [AssociationDescription](API_AssociationDescription.md) object

## Errors
<a name="API_CreateAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociationAlreadyExists **
The specified association already exists.
HTTP Status Code: 400

 ** AssociationLimitExceeded **
You can have at most 2,000 active associations.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentVersion **
The document version isn't valid or doesn't exist.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** InvalidOutputLocation **
The output location isn't valid or doesn't exist.
HTTP Status Code: 400

 ** InvalidParameters **
You must specify values for all required parameters in the AWS Systems Manager document (SSM document). You can only supply values to parameters defined in the SSM document.
HTTP Status Code: 400

 ** InvalidSchedule **
The schedule is invalid. Verify your cron or rate expression and try again.
HTTP Status Code: 400

 ** InvalidTag **
The specified tag key or value isn't valid.
HTTP Status Code: 400

 ** InvalidTarget **
The target isn't valid or doesn't exist. It might not be configured for Systems Manager or you might not have permission to perform the operation.
HTTP Status Code: 400

 ** InvalidTargetMaps **
TargetMap parameter isn't valid.
HTTP Status Code: 400

 ** UnsupportedPlatformType **
The document doesn't support the platform type of the given managed node IDs. For example, you sent an document for a Windows managed node to a Linux node.
HTTP Status Code: 400

## Examples
<a name="API_CreateAssociation_Examples"></a>

### Example
<a name="API_CreateAssociation_Example_1"></a>

This example illustrates one usage of CreateAssociation.

#### Sample Request
<a name="API_CreateAssociation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.CreateAssociation
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T140427Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 67

{
    "Name": "AWS-UpdateSSMAgent",
    "InstanceId": "i-02573cafcfEXAMPLE"
}
```

#### Sample Response
<a name="API_CreateAssociation_Example_1_Response"></a>

```
{
    "AssociationDescription": {
        "ApplyOnlyAtCronInterval": false,
        "AssociationId": "f7d193fe-7722-4f2b-ac53-d8736EXAMPLE",
        "AssociationVersion": "1",
        "Date": 1585058668.255,
        "DocumentVersion": "$DEFAULT",
        "InstanceId": "i-02573cafcfEXAMPLE",
        "LastUpdateAssociationDate": 1585058668.255,
        "Name": "AWS-UpdateSSMAgent",
        "Overview": {
            "DetailedStatus": "Creating",
            "Status": "Pending"
        },
        "Status": {
            "Date": 1585058668.255,
            "Message": "Associated with AWS-UpdateSSMAgent",
            "Name": "Associated"
        },
        "Targets": [
            {
                "Key": "InstanceIds",
                "Values": [
                    "i-02573cafcfEXAMPLE"
                ]
            }
        ]
    }
}
```

## See Also
<a name="API_CreateAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreateAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreateAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreateAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreateAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreateAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreateAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreateAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateAssociation)

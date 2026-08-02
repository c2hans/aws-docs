---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociationBatchRequestEntry.html
---

# CreateAssociationBatchRequestEntry
<a name="API_CreateAssociationBatchRequestEntry"></a>

Describes the association of a AWS Systems Manager document (SSM document) and a managed node.

## Contents
<a name="API_CreateAssociationBatchRequestEntry_Contents"></a>

 ** Name **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-Name"></a>
The name of the SSM document that contains the configuration information for the managed node. You can specify Command or Automation runbooks.
You can specify AWS-predefined documents, documents you created, or a document that is shared with you from another account.
For SSM documents that are shared with you from other AWS accounts, you must specify the complete SSM document ARN, in the following format:
 `arn:aws:ssm:region:account-id:document/document-name `
For example:
 `arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document`
For AWS-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, `AWS-ApplyPatchBaseline` or `My-Document`.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

 ** AlarmConfiguration **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-AlarmConfiguration"></a>
The details for the CloudWatch alarm you want to apply to an automation or command.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** ApplyOnlyAtCronInterval **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-ApplyOnlyAtCronInterval"></a>
By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified and when target changes are detected. Specify `true` for `ApplyOnlyAtCronInterval` if you want the association to run only according to the schedule you specified.
For more information, see [Understanding when associations are applied to resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#state-manager-about-scheduling) and [>About target updates with Automation runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#runbook-target-updates) in the * AWS Systems Manager User Guide*.
This parameter isn't supported for rate expressions.
Type: Boolean
Required: No

 ** AssociationName **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-AssociationName"></a>
Specify a descriptive name for the association.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** AutomationTargetParameterName **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-AutomationTargetParameterName"></a>
Specify the target for the association. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a tool in AWS Systems Manager.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** CalendarNames **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-CalendarNames"></a>
The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under. The associations only run when that Change Calendar is open. For more information, see [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Required: No

 ** ComplianceSeverity **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-ComplianceSeverity"></a>
The severity level to assign to the association.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | UNSPECIFIED`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-DocumentVersion"></a>
The document version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** Duration **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-Duration"></a>
The number of hours the association can run before it is canceled. Duration applies to associations that are currently running, and any pending and in progress commands on all targets. If a target was taken offline for the association to run, it is made available again immediately, without a reboot.
The `Duration` parameter applies only when both these conditions are true:
+ The association for which you specify a duration is cancelable according to the parameters of the SSM command document or Automation runbook associated with this execution.
+ The command specifies the ` [ApplyOnlyAtCronInterval](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociationBatchRequestEntry.html#systemsmanager-Type-CreateAssociationBatchRequestEntry-ApplyOnlyAtCronInterval) ` parameter, which means that the association doesn't run immediately after it is created, but only according to the specified schedule.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: No

 ** InstanceId **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-InstanceId"></a>
The managed node ID.
 `InstanceId` has been deprecated. To specify a managed node ID for an association, use the `Targets` parameter. Requests that include the parameter `InstanceID` with Systems Manager documents (SSM documents) that use schema version 2.0 or later will fail. In addition, if you use the parameter `InstanceId`, you can't use the parameters `AssociationName`, `DocumentVersion`, `MaxErrors`, `MaxConcurrency`, `OutputLocation`, or `ScheduleExpression`. To use these parameters, you must use the `Targets` parameter.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** MaxConcurrency **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-MaxConcurrency"></a>
The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new managed node starts and attempts to run an association while Systems Manager is running `MaxConcurrency` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for `MaxConcurrency`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** MaxErrors **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-MaxErrors"></a>
The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set `MaxError` to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when `MaxErrors` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set `MaxConcurrency` to 1 so that executions proceed one at a time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** OutputLocation **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-OutputLocation"></a>
An S3 bucket where you want to store the results of this request.
Type: [InstanceAssociationOutputLocation](API_InstanceAssociationOutputLocation.md) object
Required: No

 ** Parameters **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-Parameters"></a>
A description of the parameters for a document.
Type: String to array of strings map
Required: No

 ** ScheduleExpression **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-ScheduleExpression"></a>
A cron expression that specifies a schedule when the association runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ScheduleOffset **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-ScheduleOffset"></a>
Number of days to wait after the scheduled day to run an association.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.
Required: No

 ** SyncCompliance **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-SyncCompliance"></a>
The mode for generating association compliance. You can specify `AUTO` or `MANUAL`. In `AUTO` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is `COMPLIANT`. If the association execution doesn't run successfully, the association is `NON-COMPLIANT`.
In `MANUAL` mode, you must specify the `AssociationId` as a parameter for the [PutComplianceItems](API_PutComplianceItems.md) API operation. In this case, compliance data isn't managed by State Manager, a tool in AWS Systems Manager. It is managed by your direct call to the [PutComplianceItems](API_PutComplianceItems.md) API operation.
By default, all associations use `AUTO` mode.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** TargetLocations **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-TargetLocations"></a>
Use this action to create an association in multiple Regions and multiple accounts.
Type: Array of [TargetLocation](API_TargetLocation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** TargetMaps **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-TargetMaps"></a>
A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.
Type: Array of string to array of strings maps
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Targets **   <a name="systemsmanager-Type-CreateAssociationBatchRequestEntry-Targets"></a>
The managed nodes targeted by the request.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_CreateAssociationBatchRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateAssociationBatchRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateAssociationBatchRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateAssociationBatchRequestEntry)

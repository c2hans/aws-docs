---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AssociationDescription.html
---

# AssociationDescription
<a name="API_AssociationDescription"></a>

Describes the parameters for a document.

## Contents
<a name="API_AssociationDescription_Contents"></a>

 ** AlarmConfiguration **   <a name="systemsmanager-Type-AssociationDescription-AlarmConfiguration"></a>
The details for the CloudWatch alarm you want to apply to an automation or command.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** ApplyOnlyAtCronInterval **   <a name="systemsmanager-Type-AssociationDescription-ApplyOnlyAtCronInterval"></a>
By default, when you create a new associations, the system runs it immediately after it is created and then according to the schedule you specified. Specify this option if you don't want an association to run immediately after you create it. This parameter isn't supported for rate expressions.
Type: Boolean
Required: No

 ** AssociationDispatchAssumeRole **   <a name="systemsmanager-Type-AssociationDescription-AssociationDispatchAssumeRole"></a>
A role used by association to take actions on your behalf. State Manager will assume this role and call required APIs when dispatching configurations to nodes. If not specified, [ service-linked role for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html) will be used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** AssociationId **   <a name="systemsmanager-Type-AssociationDescription-AssociationId"></a>
The association ID.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** AssociationName **   <a name="systemsmanager-Type-AssociationDescription-AssociationName"></a>
The association name.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** AssociationVersion **   <a name="systemsmanager-Type-AssociationDescription-AssociationVersion"></a>
The association version.
Type: String
Pattern: `([$]LATEST)|([1-9][0-9]*)`
Required: No

 ** AutomationTargetParameterName **   <a name="systemsmanager-Type-AssociationDescription-AutomationTargetParameterName"></a>
Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a tool in AWS Systems Manager.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** CalendarNames **   <a name="systemsmanager-Type-AssociationDescription-CalendarNames"></a>
The names or Amazon Resource Names (ARNs) of the Change Calendar type documents your associations are gated under. The associations only run when that change calendar is open. For more information, see [AWS Systems Manager Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar) in the * AWS Systems Manager User Guide*.
Type: Array of strings
Required: No

 ** ComplianceSeverity **   <a name="systemsmanager-Type-AssociationDescription-ComplianceSeverity"></a>
The severity level that is assigned to the association.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | UNSPECIFIED`
Required: No

 ** Date **   <a name="systemsmanager-Type-AssociationDescription-Date"></a>
The date when the association was made.
Type: Timestamp
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-AssociationDescription-DocumentVersion"></a>
The document version.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** Duration **   <a name="systemsmanager-Type-AssociationDescription-Duration"></a>
The number of hours that an association can run on specified targets. After the resulting cutoff time passes, associations that are currently running are cancelled, and no pending executions are started on remaining targets.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: No

 ** InstanceId **   <a name="systemsmanager-Type-AssociationDescription-InstanceId"></a>
The managed node ID.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** LastExecutionDate **   <a name="systemsmanager-Type-AssociationDescription-LastExecutionDate"></a>
The date on which the association was last run.
Type: Timestamp
Required: No

 ** LastSuccessfulExecutionDate **   <a name="systemsmanager-Type-AssociationDescription-LastSuccessfulExecutionDate"></a>
The last date on which the association was successfully run.
Type: Timestamp
Required: No

 ** LastUpdateAssociationDate **   <a name="systemsmanager-Type-AssociationDescription-LastUpdateAssociationDate"></a>
The date when the association was last updated.
Type: Timestamp
Required: No

 ** MaxConcurrency **   <a name="systemsmanager-Type-AssociationDescription-MaxConcurrency"></a>
The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.
If a new managed node starts and attempts to run an association while Systems Manager is running `MaxConcurrency` associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for `MaxConcurrency`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** MaxErrors **   <a name="systemsmanager-Type-AssociationDescription-MaxErrors"></a>
The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set `MaxError` to 10%, then the system stops sending the request when the sixth error is received.
Executions that are already running an association when `MaxErrors` is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set `MaxConcurrency` to 1 so that executions proceed one at a time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** Name **   <a name="systemsmanager-Type-AssociationDescription-Name"></a>
The name of the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: No

 ** OutputLocation **   <a name="systemsmanager-Type-AssociationDescription-OutputLocation"></a>
An S3 bucket where you want to store the output details of the request.
Type: [InstanceAssociationOutputLocation](API_InstanceAssociationOutputLocation.md) object
Required: No

 ** Overview **   <a name="systemsmanager-Type-AssociationDescription-Overview"></a>
Information about the association.
Type: [AssociationOverview](API_AssociationOverview.md) object
Required: No

 ** Parameters **   <a name="systemsmanager-Type-AssociationDescription-Parameters"></a>
A description of the parameters for a document.
Type: String to array of strings map
Required: No

 ** ScheduleExpression **   <a name="systemsmanager-Type-AssociationDescription-ScheduleExpression"></a>
A cron expression that specifies a schedule when the association runs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ScheduleOffset **   <a name="systemsmanager-Type-AssociationDescription-ScheduleOffset"></a>
Number of days to wait after the scheduled day to run an association.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.
Required: No

 ** Status **   <a name="systemsmanager-Type-AssociationDescription-Status"></a>
The association status.
Type: [AssociationStatus](API_AssociationStatus.md) object
Required: No

 ** SyncCompliance **   <a name="systemsmanager-Type-AssociationDescription-SyncCompliance"></a>
The mode for generating association compliance. You can specify `AUTO` or `MANUAL`. In `AUTO` mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is `COMPLIANT`. If the association execution doesn't run successfully, the association is `NON-COMPLIANT`.
In `MANUAL` mode, you must specify the `AssociationId` as a parameter for the [PutComplianceItems](API_PutComplianceItems.md) API operation. In this case, compliance data isn't managed by State Manager, a tool in AWS Systems Manager. It is managed by your direct call to the [PutComplianceItems](API_PutComplianceItems.md) API operation.
By default, all associations use `AUTO` mode.
Type: String
Valid Values: `AUTO | MANUAL`
Required: No

 ** TargetLocations **   <a name="systemsmanager-Type-AssociationDescription-TargetLocations"></a>
The combination of AWS Regions and AWS accounts where you want to run the association.
Type: Array of [TargetLocation](API_TargetLocation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** TargetMaps **   <a name="systemsmanager-Type-AssociationDescription-TargetMaps"></a>
A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.
Type: Array of string to array of strings maps
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Targets **   <a name="systemsmanager-Type-AssociationDescription-Targets"></a>
The managed nodes targeted by the request.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** TriggeredAlarms **   <a name="systemsmanager-Type-AssociationDescription-TriggeredAlarms"></a>
The CloudWatch alarm that was invoked during the association.
Type: Array of [AlarmStateInformation](API_AlarmStateInformation.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_AssociationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AssociationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AssociationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AssociationDescription)

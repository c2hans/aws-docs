---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Association.html
---

# Association
<a name="API_Association"></a>

Describes an association of a AWS Systems Manager document (SSM document) and a managed node.

## Contents
<a name="API_Association_Contents"></a>

 ** AssociationId **   <a name="systemsmanager-Type-Association-AssociationId"></a>
The ID created by the system when you create an association. An association is a binding between a document and a set of targets with a schedule.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** AssociationName **   <a name="systemsmanager-Type-Association-AssociationName"></a>
The association name.
Type: String
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** AssociationVersion **   <a name="systemsmanager-Type-Association-AssociationVersion"></a>
The association version.
Type: String
Pattern: `^(([$]LATEST)|([1-9][0-9]*))$`
Required: No

 ** DocumentVersion **   <a name="systemsmanager-Type-Association-DocumentVersion"></a>
The version of the document used in the association. If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the `apply-only-at-cron-interval` parameter.
State Manager doesn't support running associations that use a new version of a document if that document is shared from another account. State Manager always runs the `default` version of a document if shared from another account, even though the Systems Manager console shows that a new version was processed. If you want to run an association using a new version of a document shared form another account, you must set the document version to `default`.
Type: String
Pattern: `([$]LATEST|[$]DEFAULT|^[1-9][0-9]*$)`
Required: No

 ** Duration **   <a name="systemsmanager-Type-Association-Duration"></a>
The number of hours that an association can run on specified targets. After the resulting cutoff time passes, associations that are currently running are cancelled, and no pending executions are started on remaining targets.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: No

 ** InstanceId **   <a name="systemsmanager-Type-Association-InstanceId"></a>
The managed node ID.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: No

 ** LastExecutionDate **   <a name="systemsmanager-Type-Association-LastExecutionDate"></a>
The date on which the association was last run.
Type: Timestamp
Required: No

 ** Name **   <a name="systemsmanager-Type-Association-Name"></a>
The name of the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: No

 ** Overview **   <a name="systemsmanager-Type-Association-Overview"></a>
Information about the association.
Type: [AssociationOverview](API_AssociationOverview.md) object
Required: No

 ** ScheduleExpression **   <a name="systemsmanager-Type-Association-ScheduleExpression"></a>
A cron expression that specifies a schedule when the association runs. The schedule runs in Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ScheduleOffset **   <a name="systemsmanager-Type-Association-ScheduleOffset"></a>
Number of days to wait after the scheduled day to run an association.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 6.
Required: No

 ** TargetMaps **   <a name="systemsmanager-Type-Association-TargetMaps"></a>
A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.
Type: Array of string to array of strings maps
Array Members: Minimum number of 0 items. Maximum number of 300 items.
Map Entries: Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 50.
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** Targets **   <a name="systemsmanager-Type-Association-Targets"></a>
The managed nodes targeted by the request to create an association. You can target all managed nodes in an AWS account by specifying the `InstanceIds` key with a value of `*`.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_Association_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Association)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Association)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Association)

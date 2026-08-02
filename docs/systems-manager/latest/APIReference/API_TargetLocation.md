---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_TargetLocation.html
---

# TargetLocation
<a name="API_TargetLocation"></a>

The combination of AWS Regions and AWS accounts targeted by the current Automation execution.

## Contents
<a name="API_TargetLocation_Contents"></a>

 ** Accounts **   <a name="systemsmanager-Type-TargetLocation-Accounts"></a>
The AWS accounts targeted by the current Automation execution.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** ExcludeAccounts **   <a name="systemsmanager-Type-TargetLocation-ExcludeAccounts"></a>
 AWS accounts or organizational units to exclude as expanded targets.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5000 items.
Length Constraints: Minimum length of 6. Maximum length of 68.
Pattern: `^(ou-[a-z0-9]{4,32}-[a-z0-9]{8,32})|(\d{12})$`
Required: No

 ** ExecutionRoleName **   <a name="systemsmanager-Type-TargetLocation-ExecutionRoleName"></a>
The Automation execution role used by the currently running Automation. If not specified, the default value is `AWS-SystemsManager-AutomationExecutionRole`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@/-]+`
Required: No

 ** IncludeChildOrganizationUnits **   <a name="systemsmanager-Type-TargetLocation-IncludeChildOrganizationUnits"></a>
Indicates whether to include child organizational units (OUs) that are children of the targeted OUs. The default is `false`.
Type: Boolean
Required: No

 ** Regions **   <a name="systemsmanager-Type-TargetLocation-Regions"></a>
The AWS Regions targeted by the current Automation execution.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** TargetLocationAlarmConfiguration **   <a name="systemsmanager-Type-TargetLocation-TargetLocationAlarmConfiguration"></a>
The details for the CloudWatch alarm you want to apply to an automation or command.
Type: [AlarmConfiguration](API_AlarmConfiguration.md) object
Required: No

 ** TargetLocationMaxConcurrency **   <a name="systemsmanager-Type-TargetLocation-TargetLocationMaxConcurrency"></a>
The maximum number of AWS Regions and AWS accounts allowed to run the Automation concurrently. `TargetLocationMaxConcurrency` has a default value of 1.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** TargetLocationMaxErrors **   <a name="systemsmanager-Type-TargetLocation-TargetLocationMaxErrors"></a>
The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation. `TargetLocationMaxErrors` has a default value of 0.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

 ** Targets **   <a name="systemsmanager-Type-TargetLocation-Targets"></a>
A list of key-value mappings to target resources. If you specify values for this data type, you must also specify a value for `TargetParameterName`.
This `Targets` parameter takes precedence over the `StartAutomationExecution:Targets` parameter if both are supplied.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** TargetsMaxConcurrency **   <a name="systemsmanager-Type-TargetLocation-TargetsMaxConcurrency"></a>
The maximum number of targets allowed to run this task in parallel. This `TargetsMaxConcurrency` takes precedence over the `StartAutomationExecution:MaxConcurrency` parameter if both are supplied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[1-9][0-9]%|[1-9]%|100%)$`
Required: No

 ** TargetsMaxErrors **   <a name="systemsmanager-Type-TargetLocation-TargetsMaxErrors"></a>
The maximum number of errors that are allowed before the system stops running the automation on additional targets. This `TargetsMaxErrors` parameter takes precedence over the `StartAutomationExecution:MaxErrors` parameter if both are supplied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 7.
Pattern: `^([1-9][0-9]*|[0]|[1-9][0-9]%|[0-9]%|100%)$`
Required: No

## See Also
<a name="API_TargetLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/TargetLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/TargetLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/TargetLocation)

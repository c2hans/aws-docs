---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_MaintenanceWindowTarget.html
---

# MaintenanceWindowTarget
<a name="API_MaintenanceWindowTarget"></a>

The target registered with the maintenance window.

## Contents
<a name="API_MaintenanceWindowTarget_Contents"></a>

 ** Description **   <a name="systemsmanager-Type-MaintenanceWindowTarget-Description"></a>
A description for the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Name **   <a name="systemsmanager-Type-MaintenanceWindowTarget-Name"></a>
The name for the maintenance window target.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `^[a-zA-Z0-9_\-.]{3,128}$`
Required: No

 ** OwnerInformation **   <a name="systemsmanager-Type-MaintenanceWindowTarget-OwnerInformation"></a>
A user-provided value that will be included in any Amazon CloudWatch Events events that are raised while running tasks for these targets in this maintenance window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ResourceType **   <a name="systemsmanager-Type-MaintenanceWindowTarget-ResourceType"></a>
The type of target that is being registered with the maintenance window.
Type: String
Valid Values: `INSTANCE | RESOURCE_GROUP`
Required: No

 ** Targets **   <a name="systemsmanager-Type-MaintenanceWindowTarget-Targets"></a>
The targets, either managed nodes or tags.
Specify managed nodes using the following format:
 `Key=instanceids,Values=<instanceid1>,<instanceid2>`
Tags are specified using the following format:
 `Key=<tag name>,Values=<tag value>`.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** WindowId **   <a name="systemsmanager-Type-MaintenanceWindowTarget-WindowId"></a>
The ID of the maintenance window to register the target with.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: No

 ** WindowTargetId **   <a name="systemsmanager-Type-MaintenanceWindowTarget-WindowTargetId"></a>
The ID of the target.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: No

## See Also
<a name="API_MaintenanceWindowTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/MaintenanceWindowTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/MaintenanceWindowTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/MaintenanceWindowTarget)

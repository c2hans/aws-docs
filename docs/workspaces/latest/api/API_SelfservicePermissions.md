---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_SelfservicePermissions.html
---

# SelfservicePermissions
<a name="API_SelfservicePermissions"></a>

Describes the self-service permissions for a directory. For more information, see [Enable Self-Service WorkSpace Management Capabilities for Your Users](https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html).

## Contents
<a name="API_SelfservicePermissions_Contents"></a>

 ** ChangeComputeType **   <a name="WorkSpaces-Type-SelfservicePermissions-ChangeComputeType"></a>
Specifies whether users can change the compute type (bundle) for their WorkSpace.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** IncreaseVolumeSize **   <a name="WorkSpaces-Type-SelfservicePermissions-IncreaseVolumeSize"></a>
Specifies whether users can increase the volume size of the drives on their WorkSpace.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** RebuildWorkspace **   <a name="WorkSpaces-Type-SelfservicePermissions-RebuildWorkspace"></a>
Specifies whether users can rebuild the operating system of a WorkSpace to its original state.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** RestartWorkspace **   <a name="WorkSpaces-Type-SelfservicePermissions-RestartWorkspace"></a>
Specifies whether users can restart their WorkSpace.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** SwitchRunningMode **   <a name="WorkSpaces-Type-SelfservicePermissions-SwitchRunningMode"></a>
Specifies whether users can switch the running mode of their WorkSpace.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_SelfservicePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/SelfservicePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/SelfservicePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/SelfservicePermissions)

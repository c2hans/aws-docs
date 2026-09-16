---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceProperties.html
---

# WorkspaceProperties
<a name="API_WorkspaceProperties"></a>

Describes a WorkSpace.

## Contents
<a name="API_WorkspaceProperties_Contents"></a>

 ** ComputeTypeName **   <a name="WorkSpaces-Type-WorkspaceProperties-ComputeTypeName"></a>
The compute type. For more information, see [Amazon WorkSpaces Bundles](http://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles).
Type: String
Valid Values: `VALUE | STANDARD | PERFORMANCE | POWER | GRAPHICS | POWERPRO | GENERALPURPOSE_4XLARGE | GENERALPURPOSE_8XLARGE | GRAPHICSPRO | GRAPHICS_G4DN | GRAPHICSPRO_G4DN | GRAPHICS_G6_XLARGE | GRAPHICS_G6_2XLARGE | GRAPHICS_G6_4XLARGE | GRAPHICS_G6_8XLARGE | GRAPHICS_G6_16XLARGE | GRAPHICS_GR6_4XLARGE | GRAPHICS_GR6_8XLARGE | GRAPHICS_G6F_LARGE | GRAPHICS_G6F_XLARGE | GRAPHICS_G6F_2XLARGE | GRAPHICS_G6F_4XLARGE | GRAPHICS_GR6F_4XLARGE | GRAPHICS_G7_2XLARGE | GRAPHICS_G7_4XLARGE | GRAPHICS_G7_8XLARGE | GRAPHICS_G7_12XLARGE`
Required: No

 ** GlobalAccelerator **   <a name="WorkSpaces-Type-WorkspaceProperties-GlobalAccelerator"></a>
Indicates the Global Accelerator properties.
Type: [GlobalAcceleratorForWorkSpace](API_GlobalAcceleratorForWorkSpace.md) object
Required: No

 ** NestedVirtualizationEnabled **   <a name="WorkSpaces-Type-WorkspaceProperties-NestedVirtualizationEnabled"></a>
Specifies whether nested virtualization is enabled for the WorkSpace.
For more information, see [Nested virtualization for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/nested-virtualization.html).
Type: Boolean
Required: No

 ** OperatingSystemName **   <a name="WorkSpaces-Type-WorkspaceProperties-OperatingSystemName"></a>
The name of the operating system.
Type: String
Valid Values: `AMAZON_LINUX_2 | UBUNTU_18_04 | UBUNTU_20_04 | UBUNTU_22_04 | UNKNOWN | WINDOWS_10 | WINDOWS_11 | WINDOWS_7 | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | WINDOWS_SERVER_2025 | RHEL_8 | ROCKY_8`
Required: No

 ** Protocols **   <a name="WorkSpaces-Type-WorkspaceProperties-Protocols"></a>
The protocol. For more information, see [ Protocols for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-protocols.html).
+ Only available for WorkSpaces created with PCoIP bundles.
+ The `Protocols` property is case sensitive. Ensure you use `PCOIP` or `DCV` (formerly WSP).
+ Unavailable for Windows 7 WorkSpaces and WorkSpaces using GPU-based bundles (Graphics, GraphicsPro, Graphics.g4dn, GraphicsPro.g4dn, Graphics.g6, and Graphics.g7).
Type: Array of strings
Valid Values: `PCOIP | WSP`
Required: No

 ** RootVolumeSizeGib **   <a name="WorkSpaces-Type-WorkspaceProperties-RootVolumeSizeGib"></a>
The size of the root volume. For important information about how to modify the size of the root and user volumes, see [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html).
Type: Integer
Required: No

 ** RunningMode **   <a name="WorkSpaces-Type-WorkspaceProperties-RunningMode"></a>
The running mode. For more information, see [Manage the WorkSpace Running Mode](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html).
The `MANUAL` value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see [Amazon WorkSpaces Core](http://aws.amazon.com/workspaces/core/).
Review your running mode to ensure you are using one that is optimal for your needs and budget. For more information on switching running modes, see [ Can I switch between hourly and monthly billing?](http://aws.amazon.com/workspaces-family/workspaces/faqs/#:~:text=Can%20I%20switch%20between%20hourly%20and%20monthly%20billing%20on%20WorkSpaces%20Personal%3F)
Type: String
Valid Values: `AUTO_STOP | ALWAYS_ON | MANUAL`
Required: No

 ** RunningModeAutoStopTimeoutInMinutes **   <a name="WorkSpaces-Type-WorkspaceProperties-RunningModeAutoStopTimeoutInMinutes"></a>
The time after a user logs off when WorkSpaces are automatically stopped. Configured in 60-minute intervals.
Type: Integer
Required: No

 ** UserVolumeSizeGib **   <a name="WorkSpaces-Type-WorkspaceProperties-UserVolumeSizeGib"></a>
The size of the user storage. For important information about how to modify the size of the root and user volumes, see [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html).
Type: Integer
Required: No

## See Also
<a name="API_WorkspaceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspaceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspaceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspaceProperties)

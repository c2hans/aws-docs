---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkSpaceApplication.html
---

# WorkSpaceApplication
<a name="API_WorkSpaceApplication"></a>

Describes the WorkSpace application.

## Contents
<a name="API_WorkSpaceApplication_Contents"></a>

 ** ApplicationId **   <a name="WorkSpaces-Type-WorkSpaceApplication-ApplicationId"></a>
The identifier of the application.
Type: String
Pattern: `^wsa-[0-9a-z]{8,63}$`
Required: No

 ** Created **   <a name="WorkSpaces-Type-WorkSpaceApplication-Created"></a>
The time the application is created.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpaces-Type-WorkSpaceApplication-Description"></a>
The description of the WorkSpace application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** LicenseType **   <a name="WorkSpaces-Type-WorkSpaceApplication-LicenseType"></a>
The license availability for the applications.
Type: String
Valid Values: `LICENSED | UNLICENSED`
Required: No

 ** Name **   <a name="WorkSpaces-Type-WorkSpaceApplication-Name"></a>
The name of the WorkSpace application.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Owner **   <a name="WorkSpaces-Type-WorkSpaceApplication-Owner"></a>
The owner of the WorkSpace application.
Type: String
Pattern: `^\d{12}|AMAZON$`
Required: No

 ** State **   <a name="WorkSpaces-Type-WorkSpaceApplication-State"></a>
The status of WorkSpace application.
Type: String
Valid Values: `PENDING | ERROR | AVAILABLE | UNINSTALL_ONLY`
Required: No

 ** SupportedComputeTypeNames **   <a name="WorkSpaces-Type-WorkSpaceApplication-SupportedComputeTypeNames"></a>
The supported compute types of the WorkSpace application.
Type: Array of strings
Valid Values: `VALUE | STANDARD | PERFORMANCE | POWER | GRAPHICS | POWERPRO | GENERALPURPOSE_4XLARGE | GENERALPURPOSE_8XLARGE | GRAPHICSPRO | GRAPHICS_G4DN | GRAPHICSPRO_G4DN | GRAPHICS_G6_XLARGE | GRAPHICS_G6_2XLARGE | GRAPHICS_G6_4XLARGE | GRAPHICS_G6_8XLARGE | GRAPHICS_G6_16XLARGE | GRAPHICS_GR6_4XLARGE | GRAPHICS_GR6_8XLARGE | GRAPHICS_G6F_LARGE | GRAPHICS_G6F_XLARGE | GRAPHICS_G6F_2XLARGE | GRAPHICS_G6F_4XLARGE | GRAPHICS_GR6F_4XLARGE`
Required: No

 ** SupportedOperatingSystemNames **   <a name="WorkSpaces-Type-WorkSpaceApplication-SupportedOperatingSystemNames"></a>
The supported operating systems of the WorkSpace application.
Type: Array of strings
Valid Values: `AMAZON_LINUX_2 | UBUNTU_18_04 | UBUNTU_20_04 | UBUNTU_22_04 | UNKNOWN | WINDOWS_10 | WINDOWS_11 | WINDOWS_7 | WINDOWS_SERVER_2016 | WINDOWS_SERVER_2019 | WINDOWS_SERVER_2022 | WINDOWS_SERVER_2025 | RHEL_8 | ROCKY_8`
Required: No

## See Also
<a name="API_WorkSpaceApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkSpaceApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkSpaceApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkSpaceApplication)

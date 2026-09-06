---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_SoftwareAssociations.html
---

# SoftwareAssociations
<a name="API_SoftwareAssociations"></a>

The association between a license-included application and a resource.

## Contents
<a name="API_SoftwareAssociations_Contents"></a>

 ** DeploymentError **   <a name="WorkSpacesApplications-Type-SoftwareAssociations-DeploymentError"></a>
The error details for failed deployments of the license-included application.
Type: Array of [ErrorDetails](API_ErrorDetails.md) objects
Required: No

 ** SoftwareName **   <a name="WorkSpacesApplications-Type-SoftwareAssociations-SoftwareName"></a>
The name of the license-included application.
Possible values include the following:
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_64Bit
+ Microsoft\_Project\_2021\_Professional\_32Bit
+ Microsoft\_Project\_2021\_Professional\_64Bit
+ Microsoft\_Project\_2024\_Professional\_32Bit
+ Microsoft\_Project\_2024\_Professional\_64Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Project\_2021\_Standard\_32Bit
+ Microsoft\_Project\_2021\_Standard\_64Bit
+ Microsoft\_Project\_2024\_Standard\_32Bit
+ Microsoft\_Project\_2024\_Standard\_64Bit
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Status **   <a name="WorkSpacesApplications-Type-SoftwareAssociations-Status"></a>
The deployment status of the license-included application.
Type: String
Valid Values: `STAGED_FOR_INSTALLATION | PENDING_INSTALLATION | INSTALLED | STAGED_FOR_UNINSTALLATION | PENDING_UNINSTALLATION | FAILED_TO_INSTALL | FAILED_TO_UNINSTALL`
Required: No

## See Also
<a name="API_SoftwareAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/SoftwareAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/SoftwareAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/SoftwareAssociations)

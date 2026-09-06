---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchPermissionModifications.html
---

# LaunchPermissionModifications
<a name="API_LaunchPermissionModifications"></a>

Describes a launch permission modification.

## Contents
<a name="API_LaunchPermissionModifications_Contents"></a>

 ** Add.N **
The AWS account ID, organization ARN, or OU ARN to add to the list of launch permissions for the AMI.
Type: Array of [LaunchPermission](API_LaunchPermission.md) objects
Required: No

 ** Remove.N **
The AWS account ID, organization ARN, or OU ARN to remove from the list of launch permissions for the AMI.
Type: Array of [LaunchPermission](API_LaunchPermission.md) objects
Required: No

## See Also
<a name="API_LaunchPermissionModifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchPermissionModifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchPermissionModifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchPermissionModifications)

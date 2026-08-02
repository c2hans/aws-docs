---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolumePermissionModifications.html
---

# CreateVolumePermissionModifications
<a name="API_CreateVolumePermissionModifications"></a>

Describes modifications to the list of create volume permissions for a volume.

## Contents
<a name="API_CreateVolumePermissionModifications_Contents"></a>

 ** Add.N **
Adds the specified AWS account ID or group to the list.
Type: Array of [CreateVolumePermission](API_CreateVolumePermission.md) objects
Required: No

 ** Remove.N **
Removes the specified AWS account ID or group from the list.
Type: Array of [CreateVolumePermission](API_CreateVolumePermission.md) objects
Required: No

## See Also
<a name="API_CreateVolumePermissionModifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVolumePermissionModifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVolumePermissionModifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVolumePermissionModifications)

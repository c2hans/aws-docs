---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolumePermission.html
---

# CreateVolumePermission
<a name="API_CreateVolumePermission"></a>

Describes the user or group to be added or removed from the list of create volume permissions for a volume.

## Contents
<a name="API_CreateVolumePermission_Contents"></a>

 ** Group ** (request), ** group ** (response)
The group to be added or removed. The possible value is `all`.
Type: String
Valid Values: `all`
Required: No

 ** UserId ** (request), ** userId ** (response)
The ID of the AWS account to be added or removed.
Type: String
Required: No

## See Also
<a name="API_CreateVolumePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVolumePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVolumePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVolumePermission)

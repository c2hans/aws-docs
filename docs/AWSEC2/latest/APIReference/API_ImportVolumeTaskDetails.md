---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportVolumeTaskDetails.html
---

# ImportVolumeTaskDetails
<a name="API_ImportVolumeTaskDetails"></a>

Describes an import volume task.

## Contents
<a name="API_ImportVolumeTaskDetails_Contents"></a>

 ** availabilityZone **
The Availability Zone where the resulting volume will reside.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone where the resulting volume will reside.
Type: String
Required: No

 ** bytesConverted **
The number of bytes converted so far.
Type: Long
Required: No

 ** description **
The description you provided when starting the import volume task.
Type: String
Required: No

 ** image **
The image.
Type: [DiskImageDescription](API_DiskImageDescription.md) object
Required: No

 ** volume **
The volume.
Type: [DiskImageVolumeDescription](API_DiskImageVolumeDescription.md) object
Required: No

## See Also
<a name="API_ImportVolumeTaskDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImportVolumeTaskDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImportVolumeTaskDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImportVolumeTaskDetails)

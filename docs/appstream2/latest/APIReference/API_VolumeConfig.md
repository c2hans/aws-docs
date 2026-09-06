---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_VolumeConfig.html
---

# VolumeConfig
<a name="API_VolumeConfig"></a>

Configuration for the root volume of fleet instances and image builders. This allows you to customize the storage capacity beyond the default 200 GB.

## Contents
<a name="API_VolumeConfig_Contents"></a>

 ** VolumeSizeInGb **   <a name="WorkSpacesApplications-Type-VolumeConfig-VolumeSizeInGb"></a>
The size of the root volume in GB. Valid range is 200-500 GB. The default is 200 GB, which is included in the hourly instance rate. Additional storage beyond 200 GB incurs extra charges and applies to instances regardless of their running state.
Type: Integer
Required: No

## See Also
<a name="API_VolumeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/VolumeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/VolumeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/VolumeConfig)

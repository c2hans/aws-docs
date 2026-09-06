---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsMountPoint.html
---

# AwsMountPoint
<a name="API_AwsMountPoint"></a>

Details for a volume mount point that's used in a container definition.

## Contents
<a name="API_AwsMountPoint_Contents"></a>

 ** ContainerPath **   <a name="securityhub-Type-AwsMountPoint-ContainerPath"></a>
The path on the container to mount the host volume at.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceVolume **   <a name="securityhub-Type-AwsMountPoint-SourceVolume"></a>
The name of the volume to mount. Must be a volume name referenced in the `name` parameter of task definition `volume`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsMountPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsMountPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsMountPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsMountPoint)

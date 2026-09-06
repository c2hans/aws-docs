---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_MountSource.html
---

# MountSource
<a name="API_MountSource"></a>

The data source configuration for a mount. Specify exactly one of the following.

## Contents
<a name="API_MountSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3AccessPoint **   <a name="iotsitewise-Type-MountSource-s3AccessPoint"></a>
Configuration for a mount that reads from an Amazon S3 access point.
Type: [S3AccessPointSource](API_S3AccessPointSource.md) object
Required: No

## See Also
<a name="API_MountSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/MountSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/MountSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/MountSource)

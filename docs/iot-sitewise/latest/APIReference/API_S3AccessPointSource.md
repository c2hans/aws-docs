---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_S3AccessPointSource.html
---

# S3AccessPointSource
<a name="API_S3AccessPointSource"></a>

Configures a mount that reads from an Amazon S3 access point.

## Contents
<a name="API_S3AccessPointSource_Contents"></a>

 ** accessPointArn **   <a name="iotsitewise-Type-S3AccessPointSource-accessPointArn"></a>
The Amazon Resource Name (ARN) of the S3 access point.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 128.
Pattern: `arn:aws(-cn|-us-gov)?:s3:[a-z0-9-]*:\d{12}:accesspoint[/:][a-zA-Z0-9._-]+`
Required: Yes

 ** prefix **   <a name="iotsitewise-Type-S3AccessPointSource-prefix"></a>
An optional key prefix to scope the mount to a subset of objects at the access point.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_S3AccessPointSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/S3AccessPointSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/S3AccessPointSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/S3AccessPointSource)

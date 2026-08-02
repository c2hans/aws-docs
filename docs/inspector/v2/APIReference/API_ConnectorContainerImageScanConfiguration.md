---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ConnectorContainerImageScanConfiguration.html
---

# ConnectorContainerImageScanConfiguration
<a name="API_ConnectorContainerImageScanConfiguration"></a>

The container image scanning settings for a connector, including how long pushed and pulled images continue to be rescanned for vulnerabilities.

## Contents
<a name="API_ConnectorContainerImageScanConfiguration_Contents"></a>

 ** pullDuration **   <a name="inspector2-Type-ConnectorContainerImageScanConfiguration-pullDuration"></a>
The amount of time after a container image is last pulled from a repository during which Amazon Inspector continues to rescan the image for vulnerabilities. Valid values are `DAYS_3`, `DAYS_7`, `DAYS_14`, `DAYS_30`, `DAYS_60`, `DAYS_90`, and `DAYS_180`.
Type: String
Valid Values: `DAYS_3 | DAYS_7 | DAYS_14 | DAYS_30 | DAYS_60 | DAYS_90 | DAYS_180`
Required: No

 ** pushDuration **   <a name="inspector2-Type-ConnectorContainerImageScanConfiguration-pushDuration"></a>
The amount of time after a container image is pushed to a repository during which Amazon Inspector continues to rescan the image for vulnerabilities. Valid values are `LIFETIME`, `DAYS_3`, `DAYS_7`, `DAYS_14`, `DAYS_30`, `DAYS_60`, `DAYS_90`, and `DAYS_180`.
Type: String
Valid Values: `LIFETIME | DAYS_3 | DAYS_7 | DAYS_30 | DAYS_180 | DAYS_14 | DAYS_60 | DAYS_90`
Required: No

## See Also
<a name="API_ConnectorContainerImageScanConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ConnectorContainerImageScanConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ConnectorContainerImageScanConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ConnectorContainerImageScanConfiguration)

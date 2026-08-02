---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_ConfigListItem.html
---

# ConfigListItem
<a name="API_ConfigListItem"></a>

An item in a list of `Config` objects.

## Contents
<a name="API_ConfigListItem_Contents"></a>

 ** configArn **   <a name="groundstation-Type-ConfigListItem-configArn"></a>
ARN of a `Config`.
Type: String
Length Constraints: Minimum length of 82. Maximum length of 424.
Pattern: `arn:aws:groundstation:[-a-z0-9]{1,50}:[0-9]{12}:config/[a-z0-9]+(-[a-z0-9]+){0,4}/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/.{1,256})?`
Required: No

 ** configId **   <a name="groundstation-Type-ConfigListItem-configId"></a>
UUID of a `Config`.
Type: String
Required: No

 ** configType **   <a name="groundstation-Type-ConfigListItem-configType"></a>
Type of a `Config`.
Type: String
Valid Values: `antenna-downlink | antenna-downlink-demod-decode | tracking | dataflow-endpoint | antenna-uplink | uplink-echo | s3-recording | telemetry-sink`
Required: No

 ** name **   <a name="groundstation-Type-ConfigListItem-name"></a>
Name of a `Config`.
Type: String
Required: No

## See Also
<a name="API_ConfigListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/ConfigListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/ConfigListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/ConfigListItem)

---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_SourceConfiguration.html
---

# SourceConfiguration
<a name="API_SourceConfiguration"></a>

Configuration for a migration source environment.

## Contents
<a name="API_SourceConfiguration_Contents"></a>

 ** sourceEnvironment **   <a name="mgn-Type-SourceConfiguration-sourceEnvironment"></a>
The source environment type.
Type: String
Valid Values: `NSX | VSPHERE | FORTIGATE_FIREWALL | PALO_ALTO_FIREWALL | CISCO_ACI | LOGICAL_MODEL | MODELIZE_IT | AWS_DISCOVERY_COLLECTOR | PRE_MAPPED_MODEL`
Required: Yes

 ** sourceS3Configuration **   <a name="mgn-Type-SourceConfiguration-sourceS3Configuration"></a>
The S3 configuration for the source data.
Type: [SourceS3Configuration](API_SourceS3Configuration.md) object
Required: Yes

## See Also
<a name="API_SourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/SourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/SourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/SourceConfiguration)

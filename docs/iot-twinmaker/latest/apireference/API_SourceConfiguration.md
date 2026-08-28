---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_SourceConfiguration.html
---

# SourceConfiguration
<a name="API_SourceConfiguration"></a>

The source configuration.

## Contents
<a name="API_SourceConfiguration_Contents"></a>

 ** type **   <a name="tm-Type-SourceConfiguration-type"></a>
The source configuration type.
Type: String
Valid Values: `s3 | iotsitewise | iottwinmaker`
Required: Yes

 ** iotSiteWiseConfiguration **   <a name="tm-Type-SourceConfiguration-iotSiteWiseConfiguration"></a>
The source configuration IoT SiteWise configuration.
Type: [IotSiteWiseSourceConfiguration](API_IotSiteWiseSourceConfiguration.md) object
Required: No

 ** iotTwinMakerConfiguration **   <a name="tm-Type-SourceConfiguration-iotTwinMakerConfiguration"></a>
The source configuration IoT TwinMaker configuration.
Type: [IotTwinMakerSourceConfiguration](API_IotTwinMakerSourceConfiguration.md) object
Required: No

 ** s3Configuration **   <a name="tm-Type-SourceConfiguration-s3Configuration"></a>
The source configuration S3 configuration.
Type: [S3SourceConfiguration](API_S3SourceConfiguration.md) object
Required: No

## See Also
<a name="API_SourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/SourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/SourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/SourceConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

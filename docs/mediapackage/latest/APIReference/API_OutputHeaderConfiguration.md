---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_OutputHeaderConfiguration.html
---

# OutputHeaderConfiguration
<a name="API_OutputHeaderConfiguration"></a>

The settings for what common media server data (CMSD) headers AWS Elemental MediaPackage includes in responses to the CDN.

## Contents
<a name="API_OutputHeaderConfiguration_Contents"></a>

 ** PublishMQCS **   <a name="mediapackage-Type-OutputHeaderConfiguration-PublishMQCS"></a>
When true, AWS Elemental MediaPackage includes the MQCS in responses to the CDN. This setting is valid only when `InputType` is `CMAF`.
Type: Boolean
Required: No

## See Also
<a name="API_OutputHeaderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/OutputHeaderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/OutputHeaderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/OutputHeaderConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

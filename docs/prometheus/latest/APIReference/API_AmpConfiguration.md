---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_AmpConfiguration.html
---

# AmpConfiguration
<a name="API_AmpConfiguration"></a>

The `AmpConfiguration` structure defines the Amazon Managed Service for Prometheus instance a scraper should send metrics to.

## Contents
<a name="API_AmpConfiguration_Contents"></a>

 ** workspaceArn **   <a name="prometheus-Type-AmpConfiguration-workspaceArn"></a>
ARN of the Amazon Managed Service for Prometheus workspace.
Type: String
Pattern: `arn:aws[-a-z]*:aps:[-a-z0-9]+:[0-9]{12}:workspace/.+`
Required: Yes

## See Also
<a name="API_AmpConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/AmpConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/AmpConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/AmpConfiguration)

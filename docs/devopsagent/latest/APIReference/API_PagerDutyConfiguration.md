---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_PagerDutyConfiguration.html
---

# PagerDutyConfiguration
<a name="API_PagerDutyConfiguration"></a>

Configuration for Pagerduty integration.

## Contents
<a name="API_PagerDutyConfiguration_Contents"></a>

 ** customerEmail **   <a name="devopsagent-Type-PagerDutyConfiguration-customerEmail"></a>
Email to be used in Pagerduty API header
Type: String
Pattern: `[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}`
Required: Yes

 ** services **   <a name="devopsagent-Type-PagerDutyConfiguration-services"></a>
List of Pagerduty service available for the association.
Type: Array of strings
Required: Yes

## See Also
<a name="API_PagerDutyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/PagerDutyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/PagerDutyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/PagerDutyConfiguration)

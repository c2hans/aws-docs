---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_NetworkTrafficConfig.html
---

# NetworkTrafficConfig
<a name="API_NetworkTrafficConfig"></a>

The network traffic configuration for a pentest, including custom headers and traffic rules.

## Contents
<a name="API_NetworkTrafficConfig_Contents"></a>

 ** customHeaders **   <a name="securityagent-Type-NetworkTrafficConfig-customHeaders"></a>
The list of custom HTTP headers to include in network traffic during testing.
Type: Array of [CustomHeader](API_CustomHeader.md) objects
Required: No

 ** rules **   <a name="securityagent-Type-NetworkTrafficConfig-rules"></a>
The list of network traffic rules that control which URLs are allowed or denied during testing.
Type: Array of [NetworkTrafficRule](API_NetworkTrafficRule.md) objects
Required: No

## See Also
<a name="API_NetworkTrafficConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/NetworkTrafficConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/NetworkTrafficConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/NetworkTrafficConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

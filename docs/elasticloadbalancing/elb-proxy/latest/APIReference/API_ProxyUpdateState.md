---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ProxyUpdateState.html
---

# ProxyUpdateState

The state of a proxy update.

## Contents
<a name="API_ProxyUpdateState_Contents"></a>

 ** propagationStatus **   <a name="elasticloadbalancing-Type-ProxyUpdateState-propagationStatus"></a>
Whether the configuration submitted with the update was applied to all proxy nodes.
Type: String
Valid Values: `in-progress | complete | skipped | failed | cancelled`
Required: Yes

 ** validationStatus **   <a name="elasticloadbalancing-Type-ProxyUpdateState-validationStatus"></a>
Whether the configuration submitted with the update works. An update is valid once it is successfully applied to at least one proxy node.
Type: String
Valid Values: `not-validated | valid | invalid`
Required: Yes

 ** reasons **   <a name="elasticloadbalancing-Type-ProxyUpdateState-reasons"></a>
The reasons for the current state of the update.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ProxyUpdateState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/ProxyUpdateState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/ProxyUpdateState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/ProxyUpdateState)

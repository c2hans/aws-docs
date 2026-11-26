---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ProxyUpdateSummary.html
---

# ProxyUpdateSummary

Summary information about a proxy update.

## Contents
<a name="API_ProxyUpdateSummary_Contents"></a>

 ** propagationStatus **   <a name="elasticloadbalancing-Type-ProxyUpdateSummary-propagationStatus"></a>
Whether the configuration submitted with the update was applied to all proxy nodes.
Type: String
Valid Values: `in-progress | complete | skipped | failed | cancelled`
Required: Yes

 ** submittedAt **   <a name="elasticloadbalancing-Type-ProxyUpdateSummary-submittedAt"></a>
The date and time that the update was submitted.
Type: Timestamp
Required: Yes

 ** type **   <a name="elasticloadbalancing-Type-ProxyUpdateSummary-type"></a>
The type of the update.
Type: String
Valid Values: `update-proxy-configuration`
Required: Yes

 ** updateId **   <a name="elasticloadbalancing-Type-ProxyUpdateSummary-updateId"></a>
The ID of the update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** validationStatus **   <a name="elasticloadbalancing-Type-ProxyUpdateSummary-validationStatus"></a>
Whether the configuration submitted with the update works.
Type: String
Valid Values: `not-validated | valid | invalid`
Required: Yes

 ** completedAt **   <a name="elasticloadbalancing-Type-ProxyUpdateSummary-completedAt"></a>
The date and time that the update's propagation status became `complete`, `failed`, or `cancelled`. This value is absent while the update is `in-progress` or `skipped`.
Type: Timestamp
Required: No

 ** validatedAt **   <a name="elasticloadbalancing-Type-ProxyUpdateSummary-validatedAt"></a>
The date and time that the update was first successfully applied to a proxy node. This value is absent until the update is valid.
Type: Timestamp
Required: No

## See Also
<a name="API_ProxyUpdateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/ProxyUpdateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/ProxyUpdateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/ProxyUpdateSummary)

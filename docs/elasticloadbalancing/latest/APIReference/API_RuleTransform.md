---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RuleTransform.html
---

# RuleTransform
<a name="API_RuleTransform"></a>

Information about a transform to apply to requests that match a rule. Transforms are applied to requests before they are sent to targets.

## Contents
<a name="API_RuleTransform_Contents"></a>

 ** Type **
The type of transform.
+  `host-header-rewrite` - Rewrite the host header.
+  `url-rewrite` - Rewrite the request URL.
Type: String
Valid Values: `host-header-rewrite | url-rewrite`
Required: Yes

 ** HostHeaderRewriteConfig **
Information about a host header rewrite transform. This transform modifies the host header in an HTTP request. Specify only when `Type` is `host-header-rewrite`.
Type: [HostHeaderRewriteConfig](API_HostHeaderRewriteConfig.md) object
Required: No

 ** UrlRewriteConfig **
Information about a URL rewrite transform. This transform modifies the request URL. Specify only when `Type` is `url-rewrite`.
Type: [UrlRewriteConfig](API_UrlRewriteConfig.md) object
Required: No

## See Also
<a name="API_RuleTransform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/RuleTransform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/RuleTransform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/RuleTransform)

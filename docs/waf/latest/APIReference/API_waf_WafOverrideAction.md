---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_WafOverrideAction.html
---

# WafOverrideAction
<a name="API_waf_WafOverrideAction"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The action to take if any rule within the `RuleGroup` matches a request.

## Contents
<a name="API_waf_WafOverrideAction_Contents"></a>

 ** Type **   <a name="WAF-Type-waf_WafOverrideAction-Type"></a>
 `COUNT` overrides the action specified by the individual rule within a `RuleGroup` . If set to `NONE`, the rule's action will take place.
Type: String
Valid Values: `NONE | COUNT`
Required: Yes

## See Also
<a name="API_waf_WafOverrideAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/WafOverrideAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/WafOverrideAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/WafOverrideAction)

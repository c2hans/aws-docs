---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_wafRegional_Predicate.html
---

# Predicate
<a name="API_wafRegional_Predicate"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the [ByteMatchSet](API_wafRegional_ByteMatchSet.md), [IPSet](API_wafRegional_IPSet.md), [SqlInjectionMatchSet](API_wafRegional_SqlInjectionMatchSet.md), [XssMatchSet](API_wafRegional_XssMatchSet.md), [RegexMatchSet](API_wafRegional_RegexMatchSet.md), [GeoMatchSet](API_wafRegional_GeoMatchSet.md), and [SizeConstraintSet](API_wafRegional_SizeConstraintSet.md) objects that you want to add to a `Rule` and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.

## Contents
<a name="API_wafRegional_Predicate_Contents"></a>

 ** DataId **   <a name="WAF-Type-wafRegional_Predicate-DataId"></a>
A unique identifier for a predicate in a `Rule`, such as `ByteMatchSetId` or `IPSetId`. The ID is returned by the corresponding `Create` or `List` command.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** Negated **   <a name="WAF-Type-wafRegional_Predicate-Negated"></a>
Set `Negated` to `False` if you want AWS WAF to allow, block, or count requests based on the settings in the specified [ByteMatchSet](API_wafRegional_ByteMatchSet.md), [IPSet](API_wafRegional_IPSet.md), [SqlInjectionMatchSet](API_wafRegional_SqlInjectionMatchSet.md), [XssMatchSet](API_wafRegional_XssMatchSet.md), [RegexMatchSet](API_wafRegional_RegexMatchSet.md), [GeoMatchSet](API_wafRegional_GeoMatchSet.md), or [SizeConstraintSet](API_wafRegional_SizeConstraintSet.md). For example, if an `IPSet` includes the IP address `192.0.2.44`, AWS WAF will allow or block requests based on that IP address.
Set `Negated` to `True` if you want AWS WAF to allow or block a request based on the negation of the settings in the [ByteMatchSet](API_wafRegional_ByteMatchSet.md), [IPSet](API_wafRegional_IPSet.md), [SqlInjectionMatchSet](API_wafRegional_SqlInjectionMatchSet.md), [XssMatchSet](API_wafRegional_XssMatchSet.md), [RegexMatchSet](API_wafRegional_RegexMatchSet.md), [GeoMatchSet](API_wafRegional_GeoMatchSet.md), or [SizeConstraintSet](API_wafRegional_SizeConstraintSet.md). For example, if an `IPSet` includes the IP address `192.0.2.44`, AWS WAF will allow, block, or count requests based on all IP addresses *except* `192.0.2.44`.
Type: Boolean
Required: Yes

 ** Type **   <a name="WAF-Type-wafRegional_Predicate-Type"></a>
The type of predicate in a `Rule`, such as `ByteMatch` or `IPSet`.
Type: String
Valid Values: `IPMatch | ByteMatch | SqlInjectionMatch | GeoMatch | SizeConstraint | XssMatch | RegexMatch`
Required: Yes

## See Also
<a name="API_wafRegional_Predicate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-regional-2016-11-28/Predicate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-regional-2016-11-28/Predicate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-regional-2016-11-28/Predicate)

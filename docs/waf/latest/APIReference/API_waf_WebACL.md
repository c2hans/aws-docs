---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_WebACL.html
---

# WebACL
<a name="API_waf_WebACL"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Contains the `Rules` that identify the requests that you want to allow, block, or count. In a `WebACL`, you also specify a default action (`ALLOW` or `BLOCK`), and the action for each `Rule` that you add to a `WebACL`, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the `WebACL` with an Amazon CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one `Rule` to a `WebACL`, a request needs to match only one of the specifications to be allowed, blocked, or counted. For more information, see [UpdateWebACL](API_waf_UpdateWebACL.md).

## Contents
<a name="API_waf_WebACL_Contents"></a>

 ** DefaultAction **   <a name="WAF-Type-waf_WebACL-DefaultAction"></a>
The action to perform if none of the `Rules` contained in the `WebACL` match. The action is specified by the [WafAction](API_waf_WafAction.md) object.
Type: [WafAction](API_waf_WafAction.md) object
Required: Yes

 ** Rules **   <a name="WAF-Type-waf_WebACL-Rules"></a>
An array that contains the action for each `Rule` in a `WebACL`, the priority of the `Rule`, and the ID of the `Rule`.
Type: Array of [ActivatedRule](API_waf_ActivatedRule.md) objects
Required: Yes

 ** WebACLId **   <a name="WAF-Type-waf_WebACL-WebACLId"></a>
A unique identifier for a `WebACL`. You use `WebACLId` to get information about a `WebACL` (see [GetWebACL](API_waf_GetWebACL.md)), update a `WebACL` (see [UpdateWebACL](API_waf_UpdateWebACL.md)), and delete a `WebACL` from AWS WAF (see [DeleteWebACL](API_waf_DeleteWebACL.md)).
 `WebACLId` is returned by [CreateWebACL](API_waf_CreateWebACL.md) and by [ListWebACLs](API_waf_ListWebACLs.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: Yes

 ** MetricName **   <a name="WAF-Type-waf_WebACL-MetricName"></a>
A friendly name or description for the metrics for this `WebACL`. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default\_Action." You can't change `MetricName` after you create the `WebACL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="WAF-Type-waf_WebACL-Name"></a>
A friendly name or description of the `WebACL`. You can't change the name of a `WebACL` after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

 ** WebACLArn **   <a name="WAF-Type-waf_WebACL-WebACLArn"></a>
Tha Amazon Resource Name (ARN) of the web ACL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_waf_WebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/WebACL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/WebACL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/WebACL)

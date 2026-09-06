---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2WebAclDetails.html
---

# AwsWafv2WebAclDetails
<a name="API_AwsWafv2WebAclDetails"></a>

 Details about an AWS WAFv2 web Access Control List (ACL).

## Contents
<a name="API_AwsWafv2WebAclDetails_Contents"></a>

 ** Arn **   <a name="securityhub-Type-AwsWafv2WebAclDetails-Arn"></a>
 The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Capacity **   <a name="securityhub-Type-AwsWafv2WebAclDetails-Capacity"></a>
 The web ACL capacity units (WCUs) currently being used by this web ACL.
Type: Long
Required: No

 ** CaptchaConfig **   <a name="securityhub-Type-AwsWafv2WebAclDetails-CaptchaConfig"></a>
 Specifies how AWS WAF should handle CAPTCHA evaluations for rules that don't have their own `CaptchaConfig` settings.
Type: [AwsWafv2WebAclCaptchaConfigDetails](API_AwsWafv2WebAclCaptchaConfigDetails.md) object
Required: No

 ** DefaultAction **   <a name="securityhub-Type-AwsWafv2WebAclDetails-DefaultAction"></a>
 The action to perform if none of the Rules contained in the web ACL match.
Type: [AwsWafv2WebAclActionDetails](API_AwsWafv2WebAclActionDetails.md) object
Required: No

 ** Description **   <a name="securityhub-Type-AwsWafv2WebAclDetails-Description"></a>
 A description of the web ACL that helps with identification.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-AwsWafv2WebAclDetails-Id"></a>
 A unique identifier for the web ACL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ManagedbyFirewallManager **   <a name="securityhub-Type-AwsWafv2WebAclDetails-ManagedbyFirewallManager"></a>
 Indicates whether this web ACL is managed by AWS Firewall Manager.
Type: Boolean
Required: No

 ** Name **   <a name="securityhub-Type-AwsWafv2WebAclDetails-Name"></a>
 The name of the web ACL.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Rules **   <a name="securityhub-Type-AwsWafv2WebAclDetails-Rules"></a>
 The Rule statements used to identify the web requests that you want to allow, block, or count. Each rule includes one top-level statement that AWS WAF uses to identify matching web requests, and parameters that govern how AWS WAF handles them.
Type: Array of [AwsWafv2RulesDetails](API_AwsWafv2RulesDetails.md) objects
Required: No

 ** VisibilityConfig **   <a name="securityhub-Type-AwsWafv2WebAclDetails-VisibilityConfig"></a>
 Defines and enables Amazon CloudWatch metrics and web request sample collection.
Type: [AwsWafv2VisibilityConfigDetails](API_AwsWafv2VisibilityConfigDetails.md) object
Required: No

## See Also
<a name="API_AwsWafv2WebAclDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2WebAclDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2WebAclDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2WebAclDetails)

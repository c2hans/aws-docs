---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2WebAclActionDetails.html
---

# AwsWafv2WebAclActionDetails
<a name="API_AwsWafv2WebAclActionDetails"></a>

 Specifies the action that Amazon CloudFront or AWS WAF takes when a web request matches the conditions in the rule.

## Contents
<a name="API_AwsWafv2WebAclActionDetails_Contents"></a>

 ** Allow **   <a name="securityhub-Type-AwsWafv2WebAclActionDetails-Allow"></a>
 Specifies that AWS WAF should allow requests by default.
Type: [AwsWafv2ActionAllowDetails](API_AwsWafv2ActionAllowDetails.md) object
Required: No

 ** Block **   <a name="securityhub-Type-AwsWafv2WebAclActionDetails-Block"></a>
 Specifies that AWS WAF should block requests by default.
Type: [AwsWafv2ActionBlockDetails](API_AwsWafv2ActionBlockDetails.md) object
Required: No

## See Also
<a name="API_AwsWafv2WebAclActionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2WebAclActionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2WebAclActionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2WebAclActionDetails)

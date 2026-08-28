---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2WebAclCaptchaConfigDetails.html
---

# AwsWafv2WebAclCaptchaConfigDetails
<a name="API_AwsWafv2WebAclCaptchaConfigDetails"></a>

 Specifies how AWS WAF should handle CAPTCHA evaluations for rules that don't have their own `CaptchaConfig` settings.

## Contents
<a name="API_AwsWafv2WebAclCaptchaConfigDetails_Contents"></a>

 ** ImmunityTimeProperty **   <a name="securityhub-Type-AwsWafv2WebAclCaptchaConfigDetails-ImmunityTimeProperty"></a>
 Determines how long a CAPTCHA timestamp in the token remains valid after the client successfully solves a CAPTCHA puzzle.
Type: [AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails](API_AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails.md) object
Required: No

## See Also
<a name="API_AwsWafv2WebAclCaptchaConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2WebAclCaptchaConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2WebAclCaptchaConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2WebAclCaptchaConfigDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

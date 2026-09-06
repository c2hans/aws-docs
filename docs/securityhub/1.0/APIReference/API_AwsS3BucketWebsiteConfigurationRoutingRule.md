---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketWebsiteConfigurationRoutingRule.html
---

# AwsS3BucketWebsiteConfigurationRoutingRule
<a name="API_AwsS3BucketWebsiteConfigurationRoutingRule"></a>

A rule for redirecting requests to the website.

## Contents
<a name="API_AwsS3BucketWebsiteConfigurationRoutingRule_Contents"></a>

 ** Condition **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRoutingRule-Condition"></a>
Provides the condition that must be met in order to apply the routing rule.
Type: [AwsS3BucketWebsiteConfigurationRoutingRuleCondition](API_AwsS3BucketWebsiteConfigurationRoutingRuleCondition.md) object
Required: No

 ** Redirect **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRoutingRule-Redirect"></a>
Provides the rules to redirect the request if the condition in `Condition` is met.
Type: [AwsS3BucketWebsiteConfigurationRoutingRuleRedirect](API_AwsS3BucketWebsiteConfigurationRoutingRuleRedirect.md) object
Required: No

## See Also
<a name="API_AwsS3BucketWebsiteConfigurationRoutingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRoutingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRoutingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRoutingRule)

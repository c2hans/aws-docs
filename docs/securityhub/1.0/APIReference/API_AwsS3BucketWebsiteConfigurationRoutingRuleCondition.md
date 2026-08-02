---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketWebsiteConfigurationRoutingRuleCondition.html
---

# AwsS3BucketWebsiteConfigurationRoutingRuleCondition
<a name="API_AwsS3BucketWebsiteConfigurationRoutingRuleCondition"></a>

The condition that must be met in order to apply the routing rule.

## Contents
<a name="API_AwsS3BucketWebsiteConfigurationRoutingRuleCondition_Contents"></a>

 ** HttpErrorCodeReturnedEquals **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRoutingRuleCondition-HttpErrorCodeReturnedEquals"></a>
Indicates to redirect the request if the HTTP error code matches this value.
Type: String
Pattern: `.*\S.*`
Required: No

 ** KeyPrefixEquals **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRoutingRuleCondition-KeyPrefixEquals"></a>
Indicates to redirect the request if the key prefix matches this value.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketWebsiteConfigurationRoutingRuleCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRoutingRuleCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRoutingRuleCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRoutingRuleCondition)

---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsS3BucketWebsiteConfigurationRoutingRuleRedirect.html
---

# AwsS3BucketWebsiteConfigurationRoutingRuleRedirect
<a name="API_AwsS3BucketWebsiteConfigurationRoutingRuleRedirect"></a>

The rules to redirect the request if the condition in `Condition` is met.

## Contents
<a name="API_AwsS3BucketWebsiteConfigurationRoutingRuleRedirect_Contents"></a>

 ** Hostname **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRoutingRuleRedirect-Hostname"></a>
The host name to use in the redirect request.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HttpRedirectCode **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRoutingRuleRedirect-HttpRedirectCode"></a>
The HTTP redirect code to use in the response.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Protocol **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRoutingRuleRedirect-Protocol"></a>
The protocol to use to redirect the request. By default, uses the protocol from the original request.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplaceKeyPrefixWith **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRoutingRuleRedirect-ReplaceKeyPrefixWith"></a>
The object key prefix to use in the redirect request.
Cannot be provided if `ReplaceKeyWith` is present.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ReplaceKeyWith **   <a name="securityhub-Type-AwsS3BucketWebsiteConfigurationRoutingRuleRedirect-ReplaceKeyWith"></a>
The specific object key to use in the redirect request.
Cannot be provided if `ReplaceKeyPrefixWith` is present.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsS3BucketWebsiteConfigurationRoutingRuleRedirect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRoutingRuleRedirect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRoutingRuleRedirect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsS3BucketWebsiteConfigurationRoutingRuleRedirect)

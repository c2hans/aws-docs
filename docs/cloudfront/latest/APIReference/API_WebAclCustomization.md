---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_WebAclCustomization.html
---

# WebAclCustomization
<a name="API_WebAclCustomization"></a>

The AWS WAF web ACL customization specified for the distribution tenant.

## Contents
<a name="API_WebAclCustomization_Contents"></a>

 ** Action **   <a name="cloudfront-Type-WebAclCustomization-Action"></a>
The action for the AWS WAF web ACL customization. You can specify `override` to specify a separate AWS WAF web ACL for the distribution tenant. If you specify `disable`, the distribution tenant won't have AWS WAF web ACL protections and won't inherit from the multi-tenant distribution.
Type: String
Valid Values: `override | disable`
Required: Yes

 ** Arn **   <a name="cloudfront-Type-WebAclCustomization-Arn"></a>
The Amazon Resource Name (ARN) of the AWS WAF web ACL.
Type: String
Required: No

## See Also
<a name="API_WebAclCustomization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/WebAclCustomization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/WebAclCustomization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/WebAclCustomization)

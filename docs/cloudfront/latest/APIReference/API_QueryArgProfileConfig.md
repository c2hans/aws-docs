---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_QueryArgProfileConfig.html
---

# QueryArgProfileConfig
<a name="API_QueryArgProfileConfig"></a>

Configuration for query argument-profile mapping for field-level encryption.

## Contents
<a name="API_QueryArgProfileConfig_Contents"></a>

 ** ForwardWhenQueryArgProfileIsUnknown **   <a name="cloudfront-Type-QueryArgProfileConfig-ForwardWhenQueryArgProfileIsUnknown"></a>
Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.
Type: Boolean
Required: Yes

 ** QueryArgProfiles **   <a name="cloudfront-Type-QueryArgProfileConfig-QueryArgProfiles"></a>
Profiles specified for query argument-profile mapping for field-level encryption.
Type: [QueryArgProfiles](API_QueryArgProfiles.md) object
Required: No

## See Also
<a name="API_QueryArgProfileConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/QueryArgProfileConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/QueryArgProfileConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/QueryArgProfileConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

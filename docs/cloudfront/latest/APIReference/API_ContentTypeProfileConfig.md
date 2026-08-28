---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ContentTypeProfileConfig.html
---

# ContentTypeProfileConfig
<a name="API_ContentTypeProfileConfig"></a>

The configuration for a field-level encryption content type-profile mapping.

## Contents
<a name="API_ContentTypeProfileConfig_Contents"></a>

 ** ForwardWhenContentTypeIsUnknown **   <a name="cloudfront-Type-ContentTypeProfileConfig-ForwardWhenContentTypeIsUnknown"></a>
The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.
Type: Boolean
Required: Yes

 ** ContentTypeProfiles **   <a name="cloudfront-Type-ContentTypeProfileConfig-ContentTypeProfiles"></a>
The configuration for a field-level encryption content type-profile.
Type: [ContentTypeProfiles](API_ContentTypeProfiles.md) object
Required: No

## See Also
<a name="API_ContentTypeProfileConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ContentTypeProfileConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ContentTypeProfileConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ContentTypeProfileConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudfront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

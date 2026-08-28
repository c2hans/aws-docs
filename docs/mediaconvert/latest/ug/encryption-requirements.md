---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/encryption-requirements.html
---

# Requirements
<a name="encryption-requirements"></a>

When implementing content encryption for MediaConvert, refer to the following limitations and requirements:
+ Use the AWS Secure Packager and Encoder Key Exchange (SPEKE) API to facilitate integration with a digital rights management (DRM) system provider. For information about SPEKE, see [What is Secure Packager and Encoder Key Exchange?](https://docs.aws.amazon.com/speke/latest/documentation/what-is-speke.html)
+ Your DRM system provider must support SPEKE. For a list of DRM providers that support SPEKE, see the [Get on board with a DRM platform provider](https://docs.aws.amazon.com/speke/latest/documentation/customer-onboarding.html#choose-drm-provider) topic in the *SPEKE partner and customer guide*. Your DRM provider can help you set up DRM encryption use in MediaConvert.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

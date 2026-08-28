---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/setting-up-encryption.html
---

# (Optional) Set up encryption
<a name="setting-up-encryption"></a>

You can protect your content from unauthorized use through encryption. If your source is encrypted, AWS Elemental MediaConnect can decrypt it. In addition, the service can encrypt outputs and entitlements. AWS Elemental MediaConnect offers two options for encrypting content: static key and Secure Packager and Encoder Key Exchange (SPEKE). The steps to set up encryption depend on the type of encryption that you choose. For more information, see the following:
+ [Setting up static key encryption using AWS Elemental MediaConnect](encryption-static-key-set-up.md)
+ [Setting up SPEKE encryption using AWS Elemental MediaConnect](encryption-speke-set-up.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

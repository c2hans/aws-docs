---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/encryption-deploying-speke.html
---

# Deploying SPEKE
<a name="encryption-deploying-speke"></a>

Your digital rights management (DRM) system provider can help you get set up to use DRM encryption in MediaConvert. Generally, the provider gives you a SPEKE gateway to deploy in your AWS account in the same AWS Region where MediaConvert is running.

If you must build your own API Gateway to connect MediaConvert to your key service, you can use the [SPEKE Reference Server](https://github.com/awslabs/speke-reference-server) available on GitHub as a starting point.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

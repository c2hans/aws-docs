---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-access-token.html
---

# Working with AWS Secrets Manager access token authentication
<a name="channel-assembly-access-configuration-access-token"></a>

MediaTailor supports *Secrets Manager access token authentication*. With AWS Secrets Manager access token authentication, MediaTailor uses an AWS Key Management Service (AWS KMS) customer managed key and an AWS Secrets Manager secret that you create, own, and manage to authenticate requests to your origin.

In this section, we explain how Secrets Manager access token authentication works, and provide step-by-step information about how to configure Secrets Manager access token authentication. You can work with Secrets Manager access token authentication in the AWS Management Console or programmatically with AWS APIs.

**Topics**
+ [Configuring AWS Secrets Manager access token authentication](channel-assembly-access-configuration-access-configuring.md)
+ [Integrating with MediaPackage endpoints that use CDN authorization](channel-assembly-access-configuration-access-token-integrating-emp-cdn-auth.md)
+ [How MediaTailor Secrets Manager access token authentication works](channel-assembly-access-configuration-overview.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

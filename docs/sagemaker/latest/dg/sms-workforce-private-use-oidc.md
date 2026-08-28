---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-private-use-oidc.html
---

# OIDC IdP Workforces
<a name="sms-workforce-private-use-oidc"></a>

Create a private workforce using an OpenID Connect (OIDC) Identity Provider (IdP) when you want to manage and authenticate your workers using your own OIDC IdP. Individual worker credentials and other data will be kept private. Ground Truth and Amazon A2I will only have visibility into worker information you provide through the claims that you send to these services. To create a workforce using an OIDC IdP, your IdP must support *groups* because Ground Truth and Amazon A2I map one or more groups in your IdP to a work team. To learn more, see [Send Required and Optional Claims to Ground Truth and Amazon A2I](sms-workforce-create-private-oidc.md#sms-workforce-create-private-oidc-configure-idp).

If you are a new user of Ground Truth or Amazon A2I, you can test your worker UI and job workflow by creating a private work team and adding yourself as a worker. Use this work team when you create a labeling job or human review workflow. First, create a private OIDC IdP workforce using the instructions in [Create a Private Workforce (OIDC IdP)](sms-workforce-create-private-oidc.md). Next, refer to [Manage a Private Workforce (OIDC IdP)](sms-workforce-manage-private-oidc.md) to learn how to create a work team.

**Topics**
+ [Create a Private Workforce (OIDC IdP)](sms-workforce-create-private-oidc.md)
+ [Manage a Private Workforce (OIDC IdP)](sms-workforce-manage-private-oidc.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/identity-center-based-domains.html
---

# Identity Center-based domains
<a name="identity-center-based-domains"></a>

Identity Center-based domains use AWS IAM Identity Center for user authentication and management. These domains support single sign-on (SSO) through identity providers, and also support IAM credentials. They provide centralized user management capabilities. You can use the Amazon SageMaker management console to create either Amazon SageMaker unified domains or Amazon DataZone domains by using either quick setup or manual setup options.

Once your domain is created, you can navigate to the Amazon SageMaker Unified Studio (a browser-based web application) where you can use all your data and configured tools for analytics and AI.

**Topics**
+ [Create a Amazon SageMaker Unified Studio domain - quick setup](create-domain-sagemaker-unified-studio-quick.md)
+ [Create a Amazon SageMaker Unified Studio domain - manual setup](create-domain-sagemaker-unified-studio-manual.md)
+ [Create an Amazon DataZone domain](create-domain-datazone.md)
+ [Domain administration for Identity Center-based domains](access-domain-admin-portal-idc.md)
+ [Edit domains](edit-domain.md)
+ [Delete domains](delete-domain.md)
+ [Upgrade Amazon DataZone domains to Amazon SageMaker unified domains](upgrade-domain.md)
+ [Trusted identity propagation](trusted-identity-propagation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

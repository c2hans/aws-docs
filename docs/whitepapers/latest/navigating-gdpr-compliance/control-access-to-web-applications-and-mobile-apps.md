---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/control-access-to-web-applications-and-mobile-apps.html
---

# Control Access to Web Applications and Mobile Apps
<a name="control-access-to-web-applications-and-mobile-apps"></a>

AWS provides services for managing data access control within customer applications. If you need to add user login and access control features to your web applications and mobile apps, you can use [Amazon Cognito](https://aws.amazon.com/cognito/). Amazon Cognito user pools provide a secure user directory that scales to hundreds of millions of users. To protect the identity of the users, you can add multi-factor authentication (MFA) to your user pools. You can also use adaptive authentication, which uses a risk-based model to predict when you might need another authentication factor.

With [Amazon Cognito Identity Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html) (Federated Identities), you can see who accessed your resources and where the access originated (mobile app or web application). You can use this information to create IAM roles and policies that allow or deny access to a resource based on the type of access origin (mobile app or web application) and Identity Provider.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

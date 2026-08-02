---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/managing-users.html
---

# Managing users in Deadline Cloud
<a name="managing-users"></a>

AWS Deadline Cloud uses AWS IAM Identity Center to manage users and groups. IAM Identity Center is a cloud-based single sign-on service that can be integrated with your enterprise single-sign on (SSO) provider. With integration, users can sign in with their company account.

Deadline Cloud enables IAM Identity Center by default, and it is required to set up and use Deadline Cloud. An organization owner for your AWS Organizations is responsible for managing the users and groups that have access to your Deadline Cloud monitor. For more information, see [What is AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

How you manage users depends on your IAM Identity Center identity source configuration. The identity source defines where IAM Identity Center gets user information.

To bring a new artist, team, or vendor onto your farm, start with [Onboard users to your farm](onboarding.md).

**Topics**
+ [Onboard users to your farm](onboarding.md)
+ [Understanding your identity source](understanding-identity-source.md)
+ [Create and manage users with IAM Identity Center directory](manage-monitor-users_users.md)
+ [Manage users with an external identity provider](manage-users-external-idp.md)
+ [Restricting which users can access the monitor](restrict-user-management-visibility.md)
+ [Understanding access levels](manage-users-by-farm.md)

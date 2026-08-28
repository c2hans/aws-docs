---
source_url: https://docs.aws.amazon.com/repostprivate/latest/caguide/onboard-iam-identity-center.html
---

End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

# Onboard to re:Post Private through IAM Identity Center
<a name="onboard-iam-identity-center"></a>

re:Post Private integrates with AWS IAM Identity Center to provide identity federation for your workforce. Through IAM Identity Center, users are redirected to their existing company directory to sign in with their existing credentials. Then, they're seamlessly signed in to their private re:Post. This makes sure that security settings such as password policies and two-factor authentication are enforced. Using IAM Identity Center doesn’t impact your existing IAM configuration.

 If you don’t have an existing user directory or prefer not to federate, then IAM Identity Center offers an integrated user directory that you can use to create users and groups for re:Post Private. re:Post Private doesn’t support the use of IAM users and roles to assign permissions within a private re:Post. User permissions within a private re:Post are configured by an administrator on their private re:Post application.

 For more information about IAM Identity Center, see [ What is AWS IAM Identity Center (successor to AWS Single Sign-On)](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). For more information about getting started with IAM Identity Center, see [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html). To use IAM Identity Center, you must also have AWS Organizations activated for the account.

**Important**
re:Post Private supports only [organization instances of IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/organization-instances-identity-center.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS re:Post Private. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query repostprivate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

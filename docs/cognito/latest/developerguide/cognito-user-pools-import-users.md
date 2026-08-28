---
source_url: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-import-users.html
---

# Importing users into a user pool
<a name="cognito-user-pools-import-users"></a>

There are two ways you can import or migrate users from your existing user directory or user database into Amazon Cognito user pools. You can migrate users when they sign-in using Amazon Cognito for the first time with a user migration Lambda trigger. With this approach, users can continue using their existing passwords and will not have to reset them after the migration to your user pool. Alternatively, you can migrate users in bulk by uploading a CSV file containing the user profile attributes for all users. The following sections describe both these approaches.

**More resources**
+ [Approaches for migrating users to Amazon Cognito user pools](https://aws.amazon.com/blogs/security/approaches-for-migrating-users-to-amazon-cognito-user-pools/)
+ [AWS re:Inforce 2023 - Migrating to Amazon Cognito](https://www.youtube.com/watch?v=OkDj9uXWwCc)

**Topics**
+ [Importing users with a user migration Lambda trigger](cognito-user-pools-import-using-lambda.md)
+ [Importing users into user pools from a CSV file](cognito-user-pools-using-import-tool.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

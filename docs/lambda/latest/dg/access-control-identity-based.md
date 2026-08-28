---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/access-control-identity-based.html
---

# Identity-based IAM policies for Lambda
<a name="access-control-identity-based"></a>

You can use identity-based policies in AWS Identity and Access Management (IAM) to grant users in your account access to Lambda. Identity-based policies can apply to users, user groups, or roles. You can also grant users in another account permission to assume a role in your account and access your Lambda resources.

Lambda provides AWS managed policies that grant access to Lambda API actions and, in some cases, access to other AWS services used to develop and manage Lambda resources. Lambda updates these managed policies as needed to ensure that your users have access to new features when they're released.
+ [AWSLambda\_FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_FullAccess.html) – Grants full access to Lambda actions and other AWS services used to develop and maintain Lambda resources.
+ [AWSLambda\_ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambda_ReadOnlyAccess.html) – Grants read-only access to Lambda resources.
+ [AWSLambdaRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaRole.html) – Grants permissions to invoke Lambda functions.

AWS managed policies grant permission to API actions without restricting the Lambda functions or layers that a user can modify. For finer-grained control, you can create your own policies that limit the scope of a user's permissions. For information about granting layer access, see [Granting users access to a Lambda layer](permissions-user-layer.md).

**Topics**
+ [Granting users access to a Lambda function](permissions-user-function.md)
+ [Granting users access to a Lambda layer](permissions-user-layer.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

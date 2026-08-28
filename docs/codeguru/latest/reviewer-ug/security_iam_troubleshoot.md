---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/security_iam_troubleshoot.html
---

As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

# Troubleshooting CodeGuru Reviewer identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon CodeGuru Reviewer and IAM.

**Topics**
+ [I am not authorized to perform an action in CodeGuru Reviewer](#security_iam_troubleshoot-no-permissions)
+ [I am not authorized to perform iam:PassRole](#security_iam_troubleshoot-passrole)

## I am not authorized to perform an action in CodeGuru Reviewer
<a name="security_iam_troubleshoot-no-permissions"></a>

If the AWS Management Console tells you that you're not authorized to perform an action, you must contact your administrator for assistance.

The following example error occurs when the user `mateojackson` tries to use the console to view details about a code review, but does not have `codeguru-reviewer:{{DescribeCodeReview}}` permissions.

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform:
            codeguru-reviewer:{{DescribeCodeReview}} on resource: {{my-example-code-review}}
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `{{my-example-code-review}}` resource using the `codeguru-reviewer:{{DescribeCodeReview}}` action.

## I am not authorized to perform iam:PassRole
<a name="security_iam_troubleshoot-passrole"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to CodeGuru Reviewer.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in CodeGuru Reviewer. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

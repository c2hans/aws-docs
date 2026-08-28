---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/security-instance-profiles_find.html
---

# Find instance profiles used with AWS PCS
<a name="security-instance-profiles_find"></a>

1. If you don't know the exact names of your IAM roles for AWS PCS, use the following AWS CLI command to list the IAM roles that meet the AWS PCS name requirements.

   ```
   aws iam list-roles --query "Roles[?starts_with(RoleName, 'AWSPCS') || contains(Path, '/aws-pcs/')].[RoleName]" --output text
   ```

1. Use the following AWS CLI command to list the instance profiles associated with a specific IAM role. Replace {{role-name}} with the name of an IAM role that meets AWS PCS name requirements.

   ```
   aws iam list-instance-profiles-for-role --role-name {{role-name}}
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/iam-admin-policies.html
---

# Creating custom IAM policy statements to administer Amazon Neptune
<a name="iam-admin-policies"></a>

Administrative policy statements let you control what an IAM user can do to manage a Neptune database.

A Neptune administrative policy statement grants access to one or more [administrative actions](neptune-iam-admin-actions.md) and [administrative resources](iam-admin-resources.md) that Neptune supports. You can also use [Condition Keys](iam-admin-condition-keys.md) to make the administrative permissions more specific.

**Note**
Because Neptune shares functionality with Amazon RDS, administrative actions, resources, and service-specific condition keys in administrative policy statements use an `rds:` prefix by design.

**Topics**
+ [IAM actions for administering Amazon Neptune](neptune-iam-admin-actions.md)
+ [IAM resource types for administering Amazon Neptune](iam-admin-resources.md)
+ [IAM condition keys for administering Amazon Neptune](iam-admin-condition-keys.md)
+ [Creating IAM administrative policy statements for Amazon Neptune](iam-admin-policy-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

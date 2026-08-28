---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-resources.html
---

# IAM resource types for accessing data in Amazon Neptune
<a name="iam-data-resources"></a>

Data resources, like data actions, have a `neptune-db:` prefix.

In a Neptune data-access policy, you specify the DB cluster that you are giving access to in an ARN with the following format:

```
arn:aws:neptune-db:{{region}}:{{account-id}}:{{cluster-resource-id}}/*
```

Such a resource ARN contains the following parts:
+ `{{region}}` is the AWS Region for the Amazon Neptune DB cluster.
+ `{{account-id}}` is the AWS account number for the DB cluster.
+ `{{cluster-resource-id}}` is a resource id for the DB cluster.
**Important**
The `cluster-resource-id` is different from the cluster identifier. To find a cluster resource ID in the Neptune AWS Management Console, look in the **Configuration** section for the DB cluster in question.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

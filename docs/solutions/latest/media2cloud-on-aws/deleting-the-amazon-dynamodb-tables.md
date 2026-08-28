---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/deleting-the-amazon-dynamodb-tables.html
---

# Deleting the Amazon DynamoDB tables
<a name="deleting-the-amazon-dynamodb-tables"></a>

 This solution is configured to retain the DynamoDB tables if you decide to delete the AWS CloudFormation stack to prevent accidental data loss. After uninstalling the solution, you can manually delete the DynamoDB tables if you do not need to retain the data. Follow these steps:

1.  Sign in to the [Amazon DynamoDB console](https://console.aws.amazon.com/dynamodb/home).

1.  Choose **Tables** from the left navigation pane.

1.  Select the {{<stack-name>}} table and choose **Delete**.

 To delete the DynamoDB tables using AWS CLI, run the following command:

```
$ aws dynamodb delete-table {{<table-name>}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Media2Cloud on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

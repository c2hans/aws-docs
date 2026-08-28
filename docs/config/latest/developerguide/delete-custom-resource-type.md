---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/delete-custom-resource-type.html
---

# Delete Third-Party Resources from AWS Config using the AWS CLI
<a name="delete-custom-resource-type"></a>

Enter the following command to delete a third-party resource:

```
aws configservice delete-resource-config --resource-type MyCustomNamespace::Testing::WordPress --resource-id resource-002
```

If successful, the command executes with no additional output.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

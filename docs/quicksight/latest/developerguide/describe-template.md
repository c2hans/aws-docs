---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-template.html
---

# DescribeTemplate
<a name="describe-template"></a>

Use the `DescribeTemplate` operation to describe a template's metadata. To use this operation, you need the ID of the template that you want to describe. You can use the `ListTemplates` operation to list all templates and their corresponding template IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-template
    --aws-account-id {{AWSACCOUNTID}}
    --template-id {{TEMPLATEID}}
    --version-number {{VERSION}}
    --alias-name {{ALIAS}}
```

------

The parameter value for `alias-name` can be `$LATEST`.

For more information about the `DescribeTemplate` operation, see [DescribeTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTemplate.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

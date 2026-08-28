---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-template.html
---

# CreateTemplate
<a name="create-template"></a>

Use the `CreateTemplate` operation to create a template from an existing Quick Sight analysis or template. You can use the resulting template to create a dashboard.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-template
    --aws-account-id {{555555555555}}
    --template-id {{TEMPLATEID}}
    --source-entity {{SOURCEENTITY}}
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-template
    --cli-input-json file://{{createtemplate}}.json
```

------

You can to get the ID the dataset ID by using a `DescribeAnalysis`operation. The `ANALYSISID`is part of the analysis URL in Quick Sight. You can also use the `ListAnalyses` operation to get the ID.

For more information about the `CreateTemplate` operation, see [CreateTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTemplate.html) in the *Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

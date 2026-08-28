---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-validate.html
---

# Validate AWS SAM template files
<a name="serverless-sam-cli-using-validate"></a>

Validate your templates with `sam validate`. Currently, this command validates that the template provided is valid JSON / YAML. As with most AWS SAM CLI commands, it looks for a `template.[yaml|yml]` file in your current working directory by default. You can specify a different template file/location with the `-t` or `--template` option.

Example:

```
$ sam validate
{{<path-to-template>}}/template.yaml is a valid SAM Template
```

**Note**
The `sam validate` command requires AWS credentials to be configured. For more information, see [Configuring the AWS SAM CLI](using-sam-cli-configure.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

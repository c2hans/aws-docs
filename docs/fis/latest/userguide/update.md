---
source_url: https://docs.aws.amazon.com/fis/latest/userguide/update.html
---

# Update a target account configuration
<a name="update"></a>

You can update an existing target account configuration if you want to change the role ARN or description for the the account. When you update a target account configuration, the changes do not affect any running experiments that use the template.

**To update a target account configuration using the AWS Management Console**

1. Open the AWS FIS console at [https://console.aws.amazon.com/fis/](https://console.aws.amazon.com/fis/).

1. In the navigation pane, choose **Experiment templates**

1. Select the experiment template, and choose **Actions**, **Update experiment template**.

1. In the side panel, choose **Step 3, Configure service access**.

1. Modify the **target account configurations**, and choose **Update experiment template**.

1. Select **Step 5, Review and create**.

**To update a target account configuration using the CLI**
Run the [update-target-account-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/update-target-account-configuration.html) command to command, replacing the placeholder values in {{italics}} with your own values. The `--role-arn` and `--description` parameters are optional, and will not be updated if not included.

```
aws fis update-target-account-configuration --experiment-template-id {{EXTxxxxxxxxx}} --account-id {{111122223333}} --role-arn arn:aws:iam::{{111122223333}}:role/{{role-name}} --description {{"my description"}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

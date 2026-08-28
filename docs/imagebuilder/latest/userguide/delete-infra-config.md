---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/delete-infra-config.html
---

# Delete an infrastructure configuration
<a name="delete-infra-config"></a>

You can delete an infrastructure configuration that you no longer need. You can't delete an infrastructure configuration while an image pipeline references it. First update or delete the pipeline, and then delete the infrastructure configuration.

------
#### [ Console ]

To delete an infrastructure configuration from the Image Builder console, follow these steps:

**Delete infrastructure configuration**

1. To see a list of the infrastructure configurations created under your account, choose **Infrastructure configuration** from the navigation pane.

1. Select the check box next to **Configuration name** to select the infrastructure configuration that you want to delete.

1. At the top of the **Infrastructure configurations** panel, choose **Delete**.

1. To confirm the deletion, enter `Delete` in the box, and choose **Delete**.

------
#### [ AWS CLI ]

The following example shows how to delete an infrastructure configuration with the **[delete-infrastructure-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-infrastructure-configuration.html)** command in the AWS CLI.

```
aws imagebuilder delete-infrastructure-configuration --infrastructure-configuration-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:infrastructure-configuration/{{my-example-infrastructure-configuration}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/infrastructure-composer/latest/dg/composer-cfn-mode-create.html
---

# Create a new template in Infrastructure Composer in CloudFormation console mode
<a name="composer-cfn-mode-create"></a>

Follow the instructions in this topic to create a new template.

1. Go to the [CloudFormation console](https://console.aws.amazon.com/cloudformation) and log in.

1. Select **Infrastructure Composer** from the left-side navigation menu. This will open Infrastructure Composer in CloudFormation console mode.

1. Drag, drop, configure, and connect the resources ([cards](using-composer-cards-intro.md)) you need from the **Resources** pallete.
**Note**
See [How to compose](using-composer-basics.md) for details on using Infrastructure Composer, and note that Lambda-related cards (**Lambda Function** and **Lambda Layer**) require code builds and packaging solutions that are not available in Infrastructure Composer in CloudFormation console mode. These cards can be used in the [Infrastructure Composer console](https://aws.amazon.com/application-composer/) or the AWS Toolkit for Visual Studio Code. For information on using these tools, refer to [Where you can use Infrastructure Composer](using-composer.md).

1. Double click cards to use the **Resource properties** panel to specify how cards are configured.

1. [Connect your cards](using-composer-connecting.md) to specify your application’s event-driven workflow.

1. Select **Template** to view and edit your infrastructure code. Changes are automatically synced with your canvas view.

1. Once your template is ready to be exported into a stack, select **Create template**.

1. Select the **Confirm and export to CloudFormation** button. This will take you back to the create stack workflow with a message confirming your template was successfully imported.
**Note**
Only templates with resources in them can be exported.

1. In the **Create stack** workflow, select **Next**.

1. Provide a stack name, review any listed parameters, and select **Next**.
**Note**
The stack name must start with a letter and contain only letters, numbers, dashes.

1. Select **Next** after providing the following information:
   + Tags associated with the stack
   + Stack permissions
   + The stack's failure options
**Note**
For guidance on managing stacks, see [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html) in the *CloudFormation User Guide*.

1. Confirm your stack details are correct, check acknowledgements at the bottom of the page, and select the **Submit** button.

CloudFormation will begin creating the stack based on the data in your template.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Infrastructure Composer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query infrastructure-composer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

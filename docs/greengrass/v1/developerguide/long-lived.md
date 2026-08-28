---
source_url: https://docs.aws.amazon.com/greengrass/v1/developerguide/long-lived.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# Configure long-lived Lambda functions for AWS IoT Greengrass
<a name="long-lived"></a>

You are now ready to configure your Lambda function for AWS IoT Greengrass.

1. <a name="console-gg-groups"></a>In the AWS IoT console navigation pane, under **Manage**, expand **Greengrass devices**, and then choose **Groups (V1)**.

1. Under **Greengrass groups**, choose the group that you created in [Module 2](module2.md).

1. On the group configuration page, choose the **Lambda functions** tab, and then under **My Lambda functions**, choose **Add**.

1. For **Lambda function**, choose **Greengrass\_HelloWorld\_Counter**.

1. For **Lambda function version**, choose the alias to the version that you published.

1. For **Timeout (seconds)**, enter **25**. This Lambda function sleeps for 20 seconds before each invocation.

1. For **Pinned**, choose **True**.

1. Keep the default values for all other fields, and choose **Add Lambda function**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-delete.html
---

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

# Delete an AWS Mainframe Modernization application
<a name="applications-m2-delete"></a>

You can delete an AWS Mainframe Modernization application from an environment using the AWS Mainframe Modernization console.

These instructions assume that you have completed the steps in [Set up for AWS Mainframe Modernization](setting-up.md).

## Delete an application
<a name="applications-m2-delete-console"></a>

If you need to delete an AWS Mainframe Modernization application, and it is running, make sure that you stop it first. You can see the application status on the **Applications** page.

**To delete an application**

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/).

1. In the AWS Region selector, choose the Region where the application that you want to delete from the environment was created.

1. On the **Applications** page, choose the application that you want to delete from the environment, and then choose **Actions**.

1. (Optional) If the status of the application is `Running`, choose **Stop application**.

1. Choose **Delete from environment**.

The delete process starts immediately.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

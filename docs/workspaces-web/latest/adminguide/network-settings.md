---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/network-settings.html
---

# Configuring network settings for Amazon WorkSpaces Secure Browser
<a name="network-settings"></a>

To configuring network settings for WorkSpaces Secure Browser follow these steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home](https://console.aws.amazon.com/workspaces-web/home).

1. Choose **WorkSpaces Secure Browser**, then **Web portals**, and then choose **Create web portal**.

1. On the **Step 1: Specify networking connection** page, complete the following steps to connect your VPC to your web portal and configure your VPC and subnets.

   1. For **Networking details**, choose a VPC with a connection to the content you want your users to access with WorkSpaces Secure Browser.

   1. Choose up to three private subnets that meet the following requirements. For more information, see [Networking for Amazon WorkSpaces Secure Browser](setup-vpc.md).
      + You must choose a minimum of two private subnets to create a portal.
      + To ensure high availability for your web portal, we recommend you provide the maximum number of private subnets in unique availability zones for your VPC.

   1. Choose a security group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2_MaintenanceGatewayConsole-fgw.html
---

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Running Storage Gateway commands on the local console for an Amazon EC2 gateway
<a name="EC2_MaintenanceGatewayConsole-fgw"></a>

The AWS Storage Gateway console helps provide a secure environment for configuring and diagnosing issues with your gateway. Using the console commands, you can perform maintenance tasks such as saving routing tables or connecting to Support.

**To run a configuration or diagnostic command**

1. Log in to your gateway's local console. For instructions, see [Logging in to your Amazon EC2 gateway local console](EC2_MaintenanceConsoleWindow-fgw.md).

1. From the **AWS Appliance Activation - Configuration** main menu, enter the corresponding numeral to select **Gateway Console**.

1. From the gateway console command prompt, enter **h**.

   The console displays the **AVAILABLE COMMANDS** menu, which lists the available commands:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/filefsxw/EC2_MaintenanceGatewayConsole-fgw.html)

1. From the gateway console command prompt, enter the corresponding command for the function you want to use, and follow the instructions.

To learn about a command, enter **man** \+ {{command name}} at the command prompt.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query filegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

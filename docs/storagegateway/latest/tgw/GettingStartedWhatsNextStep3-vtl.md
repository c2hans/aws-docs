---
source_url: https://docs.aws.amazon.com/storagegateway/latest/tgw/GettingStartedWhatsNextStep3-vtl.html
---

# Where do I go from here?
<a name="GettingStartedWhatsNextStep3-vtl"></a>

After your Tape Gateway is in production, you can perform several maintenance tasks, such as adding and removing tapes, monitoring and optimizing gateway performance, and troubleshooting. For general information about these management tasks, see [Managing your Tape Gateway](managing-gateway-common.md).

You can perform some of the Tape Gateway maintenance tasks on the AWS Management Console, such as configuring your gateway's bandwidth rate limits and managing gateway software updates. If your Tape Gateway is deployed on-premises, you can perform some maintenance tasks on the gateway's local console. These include routing your Tape Gateway through a proxy and configuring your gateway to use a static IP address. If you are running your gateway as an Amazon EC2 instance, you can perform specific maintenance tasks on the Amazon EC2 console, such as adding and removing Amazon EBS volumes. For more information on maintaining your Tape Gateway, see [Managing your Tape Gateway](managing-gateway-common.md).

If you plan to deploy your gateway in production, you should take your real workload into consideration in determining the disk sizes. For information on how to determine real-world disk sizes, see [Managing local disks for your Storage Gateway](ManagingLocalStorage-common.md). Also, consider cleaning up if you don't plan to continue using your Tape Gateway. Cleaning up lets you avoid incurring charges. For information on cleanup, see [Cleaning up unecessary resources](best-practices.md#cleanup-vtl).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

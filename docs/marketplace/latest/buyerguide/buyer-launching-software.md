---
source_url: https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-launching-software.html
---

# Launching software in AWS Marketplace
<a name="buyer-launching-software"></a>

After buying software, you can launch Amazon Machine Images (AMIs) that contain it by using the 1-Choose Launch view in AWS Marketplace. You can also launch it using other Amazon Web Services (AWS) management tools, including the AWS Management Console, the Amazon Elastic Compute Cloud (Amazon EC2) console, Amazon EC2 APIs, or the AWS CloudFormation console.

With the 1-Choose Launch view, you can quickly review, modify, and then launch a single instance of the software with settings recommended by the software seller. The **Launch with EC2 Console** view provides an easy way to find the AMI identification number and other pertinent information that is required to launch the AMI using the AWS Management Console, Amazon EC2 APIs, or other management tools. The **Launch with EC2 Console** view also provides more configuration options than launching from the AWS Management Console, such as tagging an instance.

**Note**
If you're unable to access an instance type or AWS Region, it may not have been supported at the time the private offer was sent to you. Review your agreement details for more information. To obtain access to an instance or a Region, contact the seller and request an updated private offer. After you accept the new offer, you'll have access to the newly added instance or Region.

For AWS Marketplace products with complex topologies, the **Custom Launch** view provides a **Launch with CloudFormation Console** option that loads the product in the CloudFormation console with the appropriate CloudFormation template. You can then follow the steps in the CloudFormation console wizard to create the cluster of AMIs and associated AWS resources for that product.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

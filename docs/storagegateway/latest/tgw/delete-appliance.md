---
source_url: https://docs.aws.amazon.com/storagegateway/latest/tgw/delete-appliance.html
---

# Deleting your Storage Gateway Hardware Appliance
<a name="delete-appliance"></a>

**Note**
End of availability notice: As of May 12, 2025, the AWS Storage Gateway Hardware Appliance will no longer be offered. Existing customers with the AWS Storage Gateway Hardware Appliance can continue to use and receive support until May 2028. As an alternative, you can use the AWS Storage Gateway service to give your applications on-premises and in-cloud access to virtually unlimited cloud storage.

If you no longer need an Storage Gateway Hardware Appliance that you have already activated, you can delete the appliance completely from your AWS account.

**Note**
To move your appliance to a different AWS account or AWS Region, you must first delete it using the following procedure, then open the gateway's support channel and contact Support to perform a soft reset. For more information, see [Turning on Support access to help troubleshoot your gateway hosted on-premises](https://docs.aws.amazon.com/storagegateway/latest/tgw/troubleshooting-on-premises-gateway-issues.html#enable-support-access-on-premises).

**To delete your hardware appliance**

1. If you have installed a gateway on the hardware appliance, you must first remove the gateway before you can delete the appliance. For instructions on how to remove a gateway from your hardware appliance, see [Removing gateway software from your hardware appliance](appliance-remove-gateway.md).

1. On the Hardware page of the Storage Gateway console, choose the hardware appliance you want to delete.

1. For **Actions**, choose **Delete Appliance**. The confirmation dialog box appears.

1. Verify that you want to delete the specified hardware appliance, then type the word *delete* in the confirmation box and choose **Delete**.

   When you delete the hardware appliance, all resources associated with the gateway that is installed on the appliance are deleted, but the data on the hardware appliance itself is not deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

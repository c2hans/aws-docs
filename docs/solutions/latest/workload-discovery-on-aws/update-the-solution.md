---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

**Important**
Updating from v1.x.x to v2.x.x of Workload Discovery on AWS is not supported. We recommend that you to uninstall v1.x.x of this solution before installing v2.x.x.

To update from a 2.x.x deployment, follow these steps.

1. Download the solution’s [AWS CloudFormation template](https://s3.amazonaws.com/solutions-reference/workload-discovery-on-aws/latest/workload-discovery-on-aws.template).

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. Select the stack with the name provided during deployment and choose **Update**.

1. On the **Update stack** page, select **Replace current template**, then select **Upload a template file**, and upload the file downloaded in step 1.

1. Choose **Next**.

1. On the **Specify stack detail** page, under **Parameters**, review the parameters and modify them as necessary.

1. Choose **Next**.

1. On the **Configure stack options** page, under **Stack failure options**, ensure the **Behavior on provisioning failure** radio button is set to **Rollback all stack resources**.

1. choose **Next**.

1. On the **Review** page, review and confirm the settings. Select the boxes acknowledging that the template creates IAM resources and requires certain capabilities.

1. Choose **Update stack** to deploy the stack.

**Note**
If you deployed the solution in self-managed account discovery mode, you must update the global resources you deployed when following the steps in the [Import a Region](import-a-region.md) section.

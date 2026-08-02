---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-for-mutable-instances-in-the-hybrid-cloud-using-aws-systems-manager/design-multi-account-region.html
---

# Patching solution design for multiple AWS accounts and AWS Regions
<a name="design-multi-account-region"></a>

You can extend the automated patching solution to support servers that span multiple AWS accounts and multiple AWS Regions. The extended solution involves setting up the patch automation solution in each account through AWS CloudFormation StackSets in a shared services account, and configuring a resource data sync across the accounts with the shared services account.

## Automated process
<a name="multi-account-auto-process"></a>

The following diagram illustrates the architecture for this scenario. This architecture includes CloudFormation StackSets and an AWS shared service account.

![Reference architecture for patching mutable EC2 instances that span multiple accounts and Regions.](http://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-for-mutable-instances-in-the-hybrid-cloud-using-aws-systems-manager/images/guide-img/9c36bc8c-880d-42f7-8b76-ddf8e3d52477/images/e85f1289-2c4e-4f44-b489-a8136bddccf9.png)

The workflow is similar to the process described in the previous section, but involves the following additional steps, where the step numbers match the callouts in the diagram:

1. In the shared services account, an CloudFormation stack set is used to configure the S3 bucket for resource data sync through Systems Manager Inventory.

1. The CloudFormation stack set creates the stack with the `automate-patch` Lambda function, sets up the patch baselines, and sets up Systems Manager Inventory resource data sync on the application accounts, to synchronize resources in the shared services account.

1. The resource information in the application accounts is synchronized with the resource information in the shared services account.

1. Quick generates patch compliance reports, using the Amazon Athena dataset for the synchronized resource information.

## Architectural considerations and limitations
<a name="multi-account-considerations"></a>

### Maintenance window quotas per account
<a name="quota"></a>

The architecture illustrated and described in the previous section creates a maintenance window for each patch group. However, the quota for the number of maintenance windows per AWS account is 50 (assuming that you haven't requested a service quota increase). If you expect the number of patch groups to exceed 50 groups in a single AWS account, this architecture won't scale to meet your requirements.

If a service quota increase isn't sufficient for your needs, there are two options for managing this challenge: using predefined maintenance windows and using CloudWatch Events. Here are the advantages and disadvantages of each approach.

#### Option 1. Use predefined maintenance windows
<a name="option-1.-use-predefined-maintenance-windows.15808bc1-0df0-5565-985b-e761d7dad409"></a>
+ Define a list of maintenance windows with various time windows (for example, 15 to 20 maintenance windows per account).
+ The application teams choose the maintenance windows that suit them from the predefined list and tag the instances accordingly.
+ Update the automated patching solution to map the patch groups to the selected maintenance windows instead of creating new maintenance windows.

Pros:
+ Simplified management.

Cons:
+ Less flexibility for defining custom maintenance windows.
+ When multiple patch groups share maintenance windows and patch tasks, canceling a specific patch task for a specific patch group requires additional manual effort.

#### Option 2. Use CloudWatch Events to trigger patch tasks instead of using maintenance windows
<a name="option-2.-use-9999999999999999cwe--to-trigger-patch-tasks-instead-of-using-maintenance-windows.f5d955d8-de15-5c87-8163-15dbeb5a49d7"></a>
+ Instead of creating maintenance windows, use CloudWatch Events to trigger patch tasks based on the schedule and the patch groups.
+ In this scenario, each patch group is associated with a CloudWatch Events event instead of a maintenance window.
+ Update the automated patching solution to create events instead of maintenance windows.

Pros:
+ Scalable design.
+ Provides flexibility for defining custom maintenance windows.

Cons:
+ Maintenance windows provide additional functionality (such as duration and cutoff times) that aren't available with CloudWatch Events.

### Other considerations
<a name="other"></a>
+ The automated patching solution described in this section doesn't support Amazon EC2 instances that are shut down.
+ This process supports Amazon EC2 instances in public subnets. To patch instances in private subnets, you must deploy a [local patch repository like Windows Server Update Services (WSUS)](https://aws.amazon.com/blogs/mt/how-to-patch-windows-ec2-instances-in-private-subnets-using-aws-systems-manager/).
+ You must adjust the frequency for running the Lambda function so patch groups and maintenance windows are updated according to your required schedule.

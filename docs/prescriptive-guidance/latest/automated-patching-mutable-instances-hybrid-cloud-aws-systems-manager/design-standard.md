---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-mutable-instances-hybrid-cloud-aws-systems-manager/design-standard.html
---

# Patching solution design for mutable Amazon EC2 instances
<a name="design-standard"></a>

The patching process for mutable instances involves the following teams and actions:
+ The **application (DevOps) teams** define the patch groups for their servers based on application environment, OS type, or other criteria. They also define the maintenance windows specific to each patch group. This information is stored on the **Patch Group** and **Maintenance Window** tags of the Amazon EC2 application instances. During each patch cycle, the application teams prepare for patching, test the application after patching, and troubleshoot any issues with their applications and OS during patching.
+ The **security operations team** defines the patch baselines for various OS types that are used by the application teams, approve the patches, and make the patches available through Systems Manager Patch Manager.
+ The **automated patching solution** runs on a regular basis and deploys the patches defined in the patch baselines based on the user-defined patch groups and maintenance windows. The patch compliance information is obtained through a resource data sync in Systems Manager Inventory, and is used for patch compliance reporting through Quick dashboards.
+ The **governance and compliance teams** define the patching guidelines, define exception processes and mechanisms, and obtain the compliance reporting from Quick.

For detailed information about the key stakeholders involved in a successful OS patch management solution and their responsibilities, see the [Key stakeholders, roles, and responsibilities](stakeholders.md) section later in this guide.

## Automated process
<a name="standard-auto-process"></a>

The automated patching solution uses multiple AWS services that work in tandem to deploy the patches to the EC2 instances. This process involves AWS Config, AWS Lambda, Systems Manager, Amazon Simple Storage Service (Amazon S3), and Quick. The following diagram shows the reference architecture and workflow.

![Reference architecture and workflow for a standard mutable Amazon EC2 instance patching process.](http://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-mutable-instances-hybrid-cloud-aws-systems-manager/images/guide-img/9c36bc8c-880d-42f7-8b76-ddf8e3d52477/images/8a9dab85-84c7-4ffa-b27b-ac9b997ee237.png)

The workflow includes these steps, where the step numbers match the callouts in the diagram:

1. AWS Config continuously monitors for the following and sends notifications with the details of non-compliant instances and the configurations needed:
   + Patch tagging compliance on EC2 instances. AWS Config checks for instances that don't have **Patch Group** and **Maintenance Window** tags.
   + The AWS Identity and Access Management (IAM) instance profile with the Systems Manager role, which allows Systems Manager to manage the instances.

1. The Lambda function (we'll call it `automate-patch`) runs on a predefined schedule and collects the **Patch Group** and **Maintenance Window** information for all the servers.

1. The `automate-patch` function then creates or updates the appropriate patch groups and maintenance windows, associates the patch groups with the patch baselines, configures the patch scan, and deploys the patching task. Optionally, the `automate-patch` function also creates events in Amazon CloudWatch Events to notify users of impending patches.

1. Based on the maintenance windows, the events send patch notifications to the application teams with the details of the impending patching operation.

1. Patch Manager performs system patching based on the defined schedule and the patch groups.

1. A resource data sync in Systems Manager Inventory gathers the patching details and publishes them to an Amazon S3 bucket.

1. Patch compliance reporting and dashboards are built in Quick from the Amazon S3 bucket information.

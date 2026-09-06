---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-delete-ebs-volumes.html
---

# Delete unattached Amazon EBS volumes
<a name="ebs-delete-ebs-volumes"></a>

## Overview
<a name="delete-ebs-volumes-overview"></a>

Unattached (orphaned) EBS volumes can lead to unnecessary storage costs in your AWS environment. It's essential to incorporate the regular review and deletion of unused and unutilized EBS volumes as part of your AWS environment hygiene. It's a best practice to have a process in place to continually review the usage of EBS volumes. You can use the [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to review underutilized instances. This section helps you identify, manage, and delete EBS volumes that are unattached or underutilized.

## Amazon EBS
<a name="delete-ebs-volumes-ebs"></a>

[Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) is a block-level device that offers storage volumes for Amazon Elastic Compute Cloud (Amazon EC2) instances. EBS provides persistent storage, with the flexibility to attach and detach from EC2 instances. This means the lifecycle of EBS volumes persists even if an EC2 instance is terminated. The [DeleteOnTermination](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#preserving-volumes-on-termination) attribute is a feature that controls whether to preserve or delete attached EBS volumes upon instance termination. By default, the attribute is set to `True` for the root volume, resulting in deletion. It's set to `False` for other volumes, resulting in preservation.

## Cost impact
<a name="delete-ebs-volumes-cost"></a>

Unattached EBS volumes, also referred to as unused or orphaned volumes, incur the same charges as attached volumes based on the provisioned storage size and storage type. Although the average cost of Amazon EBS charges may seem minimal at $0.10 per GB-month, it's crucial to recognize that the accumulation of unused EBS volumes can result in significant costs over time.

For example, consider the ramifications of retaining 50 unused EBS volumes, each provisioned with a storage size of 100 GB, as the following table shows.

|
|
| Number of storage volumes | Volume type | Size | Total monthly cost |
| --- |--- |--- |--- |
| 50 volumes | gp2 ($0.10 USD) | 100 GB | 100 GB 50.00 EBS volumes months $0.10 USD = $500.00 USD |

The scenario from the preceding table yields a cost reduction of approximately $500 per month or $6,000 annually. This is an effective step toward cost reduction. Be sure to incorporate the deletion of unattached EBS volumes as a regular practice in your AWS environment hygiene.

## Cost optimization recommendations
<a name="delete-ebs-volumes-rec"></a>

You can use AWS to easily automate the deletion of unattached EBS volumes. For example, you can use AWS Lambda, AWS Config, Amazon CloudWatch, and AWS Systems Manager to define criteria for deleting unattached volumes based on age, tags, and other specifications. You can also use these AWS services to automate the cleanup process at scale.

To avoid unintended consequences, we recommend that you perform your due diligence before deleting unattached EBS volumes.

### Manage unattached EBS volumes
<a name="manage-unattached-ebs-volumes.40105de5-8e7b-5df8-a380-90747a6b07c4"></a>

We recommend that you consider the follow best practices:
+ **Meet compliance requirements** – Verify that the deletion of unattached EBS volumes complies with your organization's governance and compliance requirements.
+ **Set data backup and retention policies** – Before deleting an unattached EBS volume, back up any important data to another storage repository (for example, [Amazon S3](https://aws.amazon.com/pm/serv-s3/)). For data retention, [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html) are a more cost-effective way to retain data than EBS volumes, and they can restore the volume if needed in the future. For more information about effectively managing snapshots, see the [Modify Amazon EBS snapshots](ebs-migrate-gp2-gp3.md) section of this guide.
+ **Check for dependencies** – Check for any dependencies between unattached EBS volumes and other AWS resources. You can use the [AWS Management Console or an API](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-describing-volumes.html) to gather descriptive information about your EBS volumes, such as size, status, and associated resources. This is an important step to safeguard against deleting any temporarily unattached resources.
+ **Create a retention policy** – Establish a retention period for unattached EBS volumes. This can help you identify the appropriate time to delete unattached volumes, ensuring that your AWS environment remains optimized. For example, you can create an [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rule to initiate a Lambda function on a scheduled basis. The Lambda function can use the AWS SDK to actively identify any unattached EBS volumes, apply a tagging mechanism for easy tracking, and send out notifications when an unattached EBS volume reaches or exceeds a defined threshold.
+ **Tag unattached EBS volumes** – [Tagging](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) EBS volumes is a useful practice that can aid in organizing and identifying volumes based on attributes such as environment, application, or owner. This can be particularly helpful when deciding which unattached volumes to delete, because it enables you to quickly identify volumes that are no longer needed based on their tags.
+ **Ensure safe deletion** – Reviewing when an EBS volume was last attached can help you determine whether it's safe to delete the volume. For more information, see [How do I use AWS CLI commands to list the attachments or detachments history of a specific Amazon EBS volume?](https://repost.aws/knowledge-center/list-attachments-history-ebs-volume) in the AWS Knowledge Center.
+ **Identify underutilized EBS volumes** – Identifying and removing underutilized EBS volumes is a highly recommended practice for reducing storage costs and maintaining an optimized AWS environment. AWS Trusted Advisor and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ebs-recommendations.html) can help you identify underutilized EBS volumes and provide recommendations to reduce costs and improve efficiency. For example, see [Setting up automation for optimizing EBS volumes with AWS Trusted Advisor](https://github.com/aws/Trusted-Advisor-Tools/tree/master/UnderutilzedEBSVolumes) (GitHub), [Establishing a Trusted Advisor Organization (TAO) dashboard](https://catalog.workshops.aws/awscid/en-US/dashboards/advanced/trusted-advisor) (AWS Workshop Studio), and [Cost-optimizing Amazon EBS volumes using AWS Compute Optimizer](https://aws.amazon.com/blogs/storage/cost-optimizing-amazon-ebs-volumes-using-aws-compute-optimizer/) (AWS Storage Blog).

### Automate the cleaning of unattached EBS volumes
<a name="automate-the-cleaning-of-unattached-ebs-volumes.4d678739-47e5-5440-8be7-2cdbdf737bc7"></a>

We recommend that you consider the following tools to help you automate the cleaning of unattached EBS volumes:
+ [AWS APIs (DescribeVolumes)](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html) – You can filter and find unattached EBS volumes by using AWS SDKs or the AWS Command Line Interface (AWS CLI). You can save time and effort by automating this process with a script or a [Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) that runs on a schedule. A [sample script](https://github.com/aws-samples/aws-systems-manager-amazon-ebs-management/blob/master/opsCenterAgedEBSVolumeFinder.py) from GitHub demonstrates how this works. The script uses Lambda to analyze AWS CloudTrail logs and identify unattached EBS volumes.
+ [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) – This enables you to automate routine maintenance and remediation tasks in your infrastructure. To get started, [create an automation runbook](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-ref-ebs.html), which defines a series of steps to be executed in a specific order. For example, you can create a runbook that first creates a snapshot of the unattached EBS volume and then deletes the volume itself. This can help you automate tasks that would otherwise be time-consuming and error-prone if done manually.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) – This enables you to assess, audit, and track changes to your AWS resources over time. By capturing configuration changes, you can use AWS Config to evaluate compliance, governance, and resource utilization in your environment. For example, AWS Config can identify [unused EBS volumes](https://docs.aws.amazon.com/config/latest/developerguide/ec2-volume-inuse-check.html). Furthermore, you can associate AWS Systems Manager Automation with AWS Config to automatically remediate the deletion of unused EBS volumes.

## Additional resources
<a name="delete-ebs-volumes-resources"></a>
+ [Delete unused Amazon Elastic Block Store (Amazon EBS) volumes by using AWS Config and AWS Systems Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/delete-unused-amazon-elastic-block-store-amazon-ebs-volumes-by-using-aws-config-and-aws-systems-manager.html) (AWS Prescriptive Guidance)
+ [Controlling  your AWS costs by deleting unused Amazon EBS volumes](https://aws.amazon.com/blogs/mt/controlling-your-aws-costs-by-deleting-unused-amazon-ebs-volumes/) (AWS Cloud Operations & Migrations Blog)
+ [AWSConfigRemediation-DeleteUnusedEBSVolume](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-ebs-volume.html) (AWS Systems Manager Automation runbook reference)

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-mutable-instances-hybrid-cloud-aws-systems-manager/introduction.html
---

# Automated patching for mutable instances in the hybrid cloud using AWS Systems Manager
<a name="introduction"></a>

*Chandra Allaka and Khurram Nizami, Amazon Web Services*

This prescriptive guide describes an automated patching solution that uses AWS Systems Manager. You can use this solution to patch both your mutable (long-running) Amazon Elastic Compute Cloud (Amazon EC2) instances that span multiple AWS accounts and AWS Regions, and your on-premises instances.

This guide is for users who are involved in designing and building operational capabilities in a hybrid cloud environment to enable application teams to comply with their enterprise's patch policies. It provides you with a self-service mechanism to deploy pre-approved patches to your application servers.

This guide assumes a good understanding of the following AWS services and concepts:
+ [Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) – Provides a unified user interface for viewing operational data from multiple AWS services and automating operational tasks across your AWS resources.
+ [Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) – Provides visibility into your Amazon EC2 and on-premises computing environment. You can use Inventory to collect metadata from your managed instances.
+ [Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) – Automates the process of patching managed instances with security-related and other types of updates.
+ [Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) – Let you define a schedule for performing potentially disruptive actions on your instances, such as patching an operating system, updating drivers, or installing software or patches.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – Lets you run code without provisioning or managing servers.
+ [Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) – Lets you easily create and publish interactive dashboards, including machine learning (ML) Insights. You can access dashboards from any device and embed them into your applications, portals, and websites.
+ [Tagging](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) – Lets you assign metadata to your AWS resources in the form of tags. Each tag is a label consisting of a user-defined key and value. Tags can help you manage, identify, organize, search for, and filter resources.

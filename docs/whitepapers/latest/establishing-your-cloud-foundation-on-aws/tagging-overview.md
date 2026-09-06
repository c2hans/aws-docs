---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/tagging-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Overview
<a name="tagging-overview"></a>

Tagging enables you to assign metadata to the different resources in your environment. As metadata, tags allow you to assign additional labels to these resources for you to identify them according you your business needs. We recommend you define a tagging strategy for your environment, this will allow you to confidently and efficiently identify resources across your environment and teams.

It is important to define a strategy to tag your resources as soon as possible when establishing your Cloud Foundation on AWS, this will enable you to find resources and environments quickly, as your overall environment expands and matures. When defining your tagging strategy, you need to determine the right tags that will help you gather all of the information you will need in your environment for the following scenarios:

## Tags for workload and ownership
<a name="tags-workload"></a>

You can use tags to help you organize and display the resources that are owned by the same team or developer, as well as the resources that belong to the same workload across your environment. These tags can also help you identify what resources within a workload belong to a specific software development lifecycle (SDLC).

## Tags for cloud financial management
<a name="tags-cloud-management"></a>

 Being able to control how much you are spending on the cloud and what resources are incurring the costs in your environment can help you reduce your costs in the long term. Being able to create reports and view the resources associated with a specific tag will also enable you to create budgets and forecast your spend based on specific tags.

## Tags for regulatory scope definition and security risk management
<a name="tags-regulatory-scope"></a>

When your resources are identifiable through tags, you can filter resources during your automated infrastructure activities. For example, when deploying, updating, or deleting resources within your infrastructure. Additionally, you can use tags to stop or start an entire fleet of resources according to your business needs.

## Tags for operations and automation
<a name="tags-operations-automation"></a>

When your resources are identifiable through tags, you can filter resources during your automated infrastructure activities. For example, when deploying, updating, or deleting resources within your infrastructure. Additionally, you can use tags to stop or start an entire fleet of resources according to your business needs.

## Tags for operational support and disaster recovery
<a name="tags-disaster-recovery"></a>

You can use tags to identify the kind of support a group of resources may need, and as part of your incident management process. Tags can be assigned to resources when they are isolated, or when they are on standby before deleting them or archiving them. This can help your support teams to identify the resources within a workload that need to be worked on. Tags can also be used to identify the frequency your resources need to be backed up, and where the backup copies need to go or where to restore the backups.

## Tags for Attribute-based access control
<a name="tags-attribute-control"></a>

In addition to role-based access control (RBAC), tagging your resources enables you to define and enhance the security of your resources in the environment. You can limit access to certain resources for roles in different environments, and you can also use tags to grant a temporary elevated access to certain resources. For more information, refer to the [What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) documentation.

Authorization-based access control (ABAC) is not supported for all services. For information on what services support tags refer to, the [service table](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). In the table, locate the service and check the **Authorization based on tags** column. You can also select the service name for additional documentation on authorization and access control for the service.

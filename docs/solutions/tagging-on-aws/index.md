---
source_url: https://docs.aws.amazon.com/solutions/tagging-on-aws/index.html
---

# Guidance for Tagging on AWS

## Overview

Tagging is the act of assigning metadata to the different resources in your AWS environment for a variety of purposes, such as Attribute Based Access Control (ABAC), Cloud Financial Management, and automation (such as patching for selecttaggedinstances). Tagging can also be used to create new resource constructs for visibility or control (such as grouping together resources that make up a micro-service, application, or workload). Tagging is fundamental to providing enterprise-level visibility and control.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/tagging-on-aws.pdf)

![Architecture diagram](/images/solutions/tagging-on-aws/images/tagging-on-aws-1.png)

1. **Step 1**: (CF23 - S1) Define a tagging strategy: decide what the mandatory tags are, your tagging policy, and your tagging standards. Stakeholders across the company provide the information required to the Cloud team to standardize tagging.
1. **Step 2**: (CF23 - S2) Create tag policies in AWS Organizations and attach them to the relevant organizational units (OUs) and accounts to generate resource compliance reports and understand how resources are tagged in your environment.
1. **Step 3**: (CF23 - S2) AWS Systems Manager can help you tag resources through automations across your AWS environment. You can also use resource groups to bulk tag your resources across your environment.
1. **Step 4**: (CF23 - S3) Within your operations account, create a dashboard that can display the metadata assigned to your resources and act as a remediation mechanism.
## Implementation resources

### Implement a tagging strategy for your environment

Implement a tagging strategy for your environment

- Create tagging standards
- Define a set of mandatory and discretionary tags
- Define resource types that need to be tagged
- Publish tagging dictionary
- Define tags for ABAC

It is important to define a strategy to tag your resources as soon as possible when establishing your cloud foundation. This enables you to find resources and environments quickly, as your overall environment expands and matures. When defining your tagging strategy, you need to determine the right tags that will help you gather all of the information you will need in your environment for the following scenarios:

**Tags for workload and ownership:** You can use tags to help you organize and display the resources that are owned by the same team or developer, as well as the resources that belong to the same workload across your environment. These tags can also help you identify what resources within a workload belong to a specific software development life cycle (SDLC).

**Tags for cloud financial management:** The ability to control how much you are spending on the cloud and what resources are incurring the costs in your environment can help you reduce your costs in the long term. The ability to create reports and view the resources associated with a specific tag also enables you to create budgets and forecast your spend based on specific tags.

**Tags for regulatory scope definition and security risk management:** Some of the resources in your environment may handle confidential information, personal information, or data that is subject to a specific compliance framework. Assigning tags to identify these resources allows you to ensure that the correct access controls and security mechanisms are established and working as intended.

**Tags for operations and automation:** When your resources are identifiable through tags, you can filter resources during your automated infrastructure activities. For example, when deploying, updating, or deleting resources within your infrastructure. Additionally, you can use tags to stop or start an entire fleet of resources according to your business needs.

**Tags for operational support and disaster recovery:** You can use tags to identify the kind of support a group of resources may need, and as part of your incident management process. Tags can be assigned to resources when they are isolated, or when they are on standby before deleting them or archiving them. This can help your support teams to identify the resources within a workload that need to be worked on. Tags can also be used to identify the frequency your resources need to be backed up, and where the backup copies need to go or where to restore the backups.

**Tags for attribute-based access control:**  In addition to role-based access control (RBAC), tagging your resources enables you to define and enhance the security of your resources in the environment. When using tags for authorization (ABAC), you can further define under what conditions a resource or API can be accessed. For more information, refer to the [What is ABAC for AWS?](/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) documentation.

Authorization-based access control (ABAC) is not supported for all services. For information on what services support tags, refer to the service table. In the table, locate the service and check the Authorization based on tags column. You can also select the service name for additional documentation on authorization and access control for the service.

Build a tagging dictionary

As part of your tagging dictionary, you may define certain tags that can be used to access specific environment resources based on the tags attached to a role at a certain time. These tags can be used for a temporary escalation of privileges or for deploying changes through Infrastructure as Code (IaC) that other identities may not have access otherwise.

We recommend that you define and build a tagging dictionary where all these values are available for developers, cloud architects, and environment operators. To add, update, or remove values for each of the tags included in the tagging dictionary, you need to establishes processes where all the relevant stakeholders can provide their input when a tag becomes standard. This will ensure that all relevant stakeholders involved in the definition of the tags in your environment are aware of any changes they need to provision and deploy across their resources.

This tagging dictionary needs to be made available to builders and stakeholders, so tags can be applied consistently across the environment, and everyone is aware of requirements or errors that can be caused due to an incorrect used of tags in the environment. This includes missing tags and wrong or misspelled tag keys in your resources.

Create tagging standards

As you define your tagging strategy, a naming convention needs to be established for the different tags across your environment to ensure standardization and ability to identify resources based on their tags. The following are examples for tag key names and values:

- owner = SecOps
- cost-center = 5432
- financial-owner = Security

Define a set of mandatory and discretionary tags

When defining a tagging dictionary, it is important to delineate between mandatory and discretionary tags.

- **Mandatory tags** are the set of tags that every resource should have, regardless of its purpose. These tags will enable you to identify the necessary metadata to identify the resource.
- **Discretionary tags** are the set of tags that must be defined as part of your tagging strategy, so they are available to be assigned to resources that need them (for example, temporary elevation of permissions, or data sensitivity).

Additionally, you need to define what resources need to tagged, and define detection and enforcement mechanisms to ensure all the required resources have the mandatory tags. When building an environment with multiple accounts, every account in the environment should have the mandatory tags that allow you to identify what the purpose of the account is for and who is responsible for the resources in that account.

**Note:** When building your tag strategy personally identifiable information (PII) should not be used to label your resources, as tags are not encrypted and are visible across your environment. Codify these values so you can identify owners internally.

Recommended  **mandatory**** tags** :

**Owner: ** This tag indicates who is the owner and main user of the resource. This can be a team or an individual.

**BusinessUnitId: ** This tag identifies the business unit the resource belongs to.

**Environment: ** This tag indicates if the resources are being used for production or for non-production. (For example, development, test, or sandbox.)

**CostCenter: ** This tag specifies the budget or account that will be used to pay for the spend associated with the tag.

**DataClassification: ** This tag identifies if the resource contains, stores, or uses any type of special or sensitive data.

Recommended **discretionary****tags** :

**WorkloadId:** This tag identifies if the resource belongs to a specific workload. The value can be the workload ID or name.

**Compliance:** This tag identifies the resources that are subject to a specific compliance framework. (For example, PCI-DSS or HIPAA).

**Version:** This tag identifies the version of the environment, in case the same workload has more than one environment associated.

**WorkloadTier:** This tag identifies the type of workload the resources belong to. Some workload types examples are confidential, internal, or critical.

**Backup:** This tag identifies if the resource needs to be backed up based on the type of workload and the data that it manages.

**SLA:** This tag identifies SLA requirements.

**Lifespan:** This tag identifies the lifetime of the resources of the workload. If exceeded, these resources should be reviewed, replaced, or isolated.

Example tagging dictionary based on recommended mandatory and discretionary tags:

|  |  |  |  |
| --- | --- | --- | --- |
| Tag Key | Tag Purpose | Sample Tag Values | Observations |

|  |  |  |  |
| --- | --- | --- | --- |
| Tag Key | Tag Purpose | Sample Tag Values | Observations |
| Owner | This tag is used to indicate the owner of the resource. | SecurityLead, SecOps, Workload-1-Development-team | This value should represent a team or a title, given that humans come and go, but the function would remain within your environment. |
| BusinessUnitId | This tag indicates the business unit for the resource. | Finance, Retail, API-1, DevOps |
| Environment | This tag is used to indicate the lifecycle stage for the resource. | Sandbox, Dev, PreProd, QA, Prod, Testing |
| CostCenter | This tag is used to indicate the cost center associated with the resource. | FIN123, Retail-123, Sales-248, HR-333 |
| FinancialOwner | This tag is used to indicate the Financial Owner associated with the resource. | HR, SecurityLead, DevOps-3, Workload-1-Development-team | This value should represent a team or a title, given that humans come and go, but the function would remain within your environment. |
| Compliance | This tag is used to indicate if the resource is subject to any compliance requirement. | N/A, NIST, HIPAA, GDPR, |

Define resource types that need to be tagged

There are resources that always need to be tagged in your environment, because it is critical to have the identifiable information about the resources at all times. The resources in this category are meant to be persistent, and in some occasions, they act as resource containers for other resources. These resources include, but are not limited to, accounts, critical workloads, and shared infrastructure. For these resources, you should aim to tag a hundred percent of the resources, which will allow you to identify the spend, access, ownership, and permissions for the tagged resources.

However, as operational complexity increases and the level of automation to manage tags becomes more demanding, you may choose to not tag certain types of resources that are ephemeral. Ephemeral resources might run within a resource container that is properly tagged to allow you to identify and trace what happened within that environment, but enforcing the tags on these types of resources may not be necessary if they do not belong to critical workloads or applications.

Publish tagging dictionary

The tagging dictionary should be published and made readily available to builders and stakeholders, so tags can be applied consistently across the environment, and everyone is aware of requirements or errors that can be caused due to the incorrect usage of tags within the environment. This includes missing tags, and wrong or misspelled tag keys in your resources.

Define tags for attribute-based access control (ABAC)

As part of your tagging dictionary, you may have defined a series of tags that can be attached to roles or resources across your environment to grant  permissions to a specific set of resources or APIs. ABAC is an advanced authorization strategy we recommend you consider the right use cases to enhance your RBAC strategy to use tagging your environment, and sure you enforce the usage of the necessary guardrails to protect tags from unintended modification. Guardrails are governance rules for security, operations, and compliance that you can define and apply to align with your overall requirements. For more information, refer to Example service control policies and [What is ABAC for AWS?](/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) documentation.

### Enforce tagging across your environment and resources

Enforce tagging across your environment and resources

- Establish controls to ensure new resources are tagged on creation.
- Use Infrastructure as Code to easily deploy and maintain tags in your environment.
- Establish mechanisms to remediate non-compliant resources with your tagging strategy and automate these mechanisms when possible.

Because of the importance of tagging and the level of complexity, we recommended that you automate the tagging process when possible. This reduces the human error that can be introduced when tagging critical resources, and minimizes the number of resources that are not identifiable due to the lack of tags. When possible, creating tag policies in your organization can help you ensure that the tags assigned to resources have the correct value assigned.

Additionally, automation needs to be established in the environment to discover resources with missing tags or resources that are not compliant with the established tagging strategy. Once the resources have been identified, a report including these resources on the environment needs to be sent to the relevant stakeholders, to evaluate and make a decision to remediate the situation, if needed.

Based on the results of this report, if a situation where persistent resources that are identified as non-compliant or have missing tags is given, it should be remediated immediately. This can be done by assigning a default pre-defined tag value defined as part of your tagging strategy. If a pre-defined tag doesn’t exist, delete the non-compliant resources.

As part of your tagging strategy, it is important to implement preventative controls that ensure that disallow resources from being created if they do not have the appropriate tags (review the Establishing preventive controls across your environment section in the [Identity Management & Access Control Capability](/solutions/identity-management-and-access-control-on-aws/) ).

Establish controls to ensure new resources are tagged on creation

As you implement your tagging strategy, it is important to have a method to build, enforce, and maintain standardization within your environment. Tag policies are a type of policy that can help you standardize tag values based on defined tag keys across resources in your organization's accounts.

We consider the following tags mandatory, so we recommend using tag policies to help enforce the usage of the tag values according to our best practices. The following table is a sample that you can use to create your own tagging dictionary for the tags that are mandatory within your environment.

|  |  |  |  |
| --- | --- | --- | --- |
| Tag Key | Tag Purpose | Sample Tag Values | Observations |

|  |  |  |  |
| --- | --- | --- | --- |
| Tag Key | Tag Purpose | Sample Tag Values | Observations |
| Owner | Indicates the owner of the resource. | SecurityLead, SecOps, Workload-1-Development-team | This value should represent a team or a title, given that humans come and go, but the function remains within your environment. |
| Business Unit | Indicates the business unit for the resource. | Finance, Retail, API-1, DevOps |
| SDLC Stage | Indicates the lifecycle stage for the resource. | Sandbox, Dev, PreProd, QA, Prod, Testing |
| Cost Center | Indicates the cost center associated with the resource. | FIN123,Retail-123,Sales-248,HR-333 |
| Financial Owner | Indicates the Financial Owner associated with the resource. | HR, SecurityLead, DevOps-3, Workload-1-Development-team | This value should represent a team or a title, given that humans come and go, but the function remains within your environment. |
| Compliance Requirement | Indicates if the resource is subject to any compliance requirement. | N/A, NIST, HIPAA, GDPR, |

You can create tag policies to enforce the values you choose across your environment, and use the tag policies to prevent the creation of non-compliant resources. You can [create these tag policies](/organizations/latest/userguide/orgs_manage_policies_tag-policies-create.html) through the console, deploy them using IaC, in the AWS CLI, or one of the available SDKs. Using the sample dictionary defined previously, the following is a tag policy example that implements all the required tags:

{ "tags": { "Owner": { "tag_key": { "@@assign": "Owner" }, "tag_value": { "@@assign": [ "SecurityLead", "SecOps", "DevTeam1" ] }, "enforced_for": { "@@assign": [ "<service>:*" ] } }, "businessUnit": { "tag_key": { "@@assign": "BusinessUnit" }, "tag_value": { "@@assign": [ "Finance", "Retail" ] }, "enforced_for": { "@@assign": [ "<service>:*" ] } }, "costcenter": { "tag_key": { "@@assign": "CostCenter" }, "tag_value": { "@@assign": [ "100", "200" ] }, "enforced_for": { "@@assign": [ "<service>:*" ] } } ,"FinancialOwner": { "tag_key": { "@@assign": "FinancialOwner" }, "tag_value": { "@@assign": [ "SecOps", "HR" ] }, "enforced_for": { "@@assign": [ "<service>:*" ] } } ,"costcenter": { "tag_key": { "@@assign": "CostCenter" }, "tag_value": { "@@assign": [ "100", "200" ] }, "enforced_for": { "@@assign": [ "<service>:*" ] } } ,"compliance": { "tag_key": { "@@assign": "Compliance" }, "tag_value": { "@@assign": [ "NIST", "HIPAA", "GDPR" ] }, "enforced_for": { "@@assign": [ "<service>:*" ] } } }}

**Note:** Tag policies can be set to enforced or not enforced. Tag policies that are set to enforced prevent the instantiation of resources with non-compliant tag values. Tag policies that are not set to enforced allow the creation of the resource, but provide an organization level view of non-compliant resources. Refer to the evaluating organization-wide compliance section of the AWS Resource Groups user guide for more information on evaluating organization tag compliance.

After defining the tag policies in your environment you can use the Resource Group API to identify and correct non-compliant resources across your environment.

For resources that do not support tag policies, you can use preventive and detective controls to enforce tagging across your environment.

Preventive controls

Tagging policies enforce the use of defined tag values for defined tag keys. You can use Service Control Policies to prevent actions from being deployed in your environment when the expected tag keys are not included with the API calls. To achieve that, within your Service Control Policies to scope the permissions across your environment, you need to include a condition that will prevent the API call when the requested tag is not included in the resource. This is what it would look like to prevent an action when the CostCenter requested tag is not included within the call.

 "Condition": { "Null": { "aws:RequestTag/costcenter": "true" } }

These preventive controls can also be used to provide Attribute Based Access Control when certain tags are present within a Role or a User making AWS API calls to the service. This is something we will explore further in a later section within the [Identity Management & Access Control Capability](/solutions/identity-management-and-access-control-on-aws/) .

Tagging limitations and additional tags

In addition to the tags you define in your environment, specific services use tags to monitor and track resources created or managed through them. These tags are reserved and start with a prefix that contains aws:. Tags starting with that prefix can’t be manually created, updated, or deleted.

For a list of the different tagging limitations on AWS, review [tag naming limits and requirements](/general/latest/gr/aws_tagging.html#tag-conventions) .

Use infrastructure-as-code to deploy and maintain tags in your environment

We recommend enforcing tagging through Infrastructure as Code. This will automatically apply tags across your environment when creating resources as they are passed down directly from your templates, and pipelines. You can build preventive mechanisms to enforce the tags. Tools such as [cfn-guard](https://github.com/aws-cloudformation/cloudformation-guard) can help you check your IaC for compliance rules and enforce the required tags.

### Monitor the resources based on tags across your environment

Monitor resources based on tags across your environment

- Create dashboards, reports, and views based on tag groupings
- Monitor cloud spend based on tag groupings

Monitoring the spend, performance, and health of your cloud workloads and underlying infrastructure is essential for effectively managing your cloud environment. Tags enable you to categorize and group your resources in useful ways. By ensuring that you can group or filter by tags within your cost management, performance, logging, and infrastructure tooling, you can effectively monitor and manage distributed workloads with the ability to gain insights from different perspectives. For example, you could see the cost or performance of all SDLC instances of a specific application.

Create dashboards, reports, and views based on tag groupings

One of the benefits of an effective tagging strategy is being able to view data based on resources that are grouped by tags. You can use [resource groups](/ARG/latest/userguide/resource-groups.html) to organize your AWS resources. [AWS Resource Groups](/ARG/latest/userguide/resource-groups.html) is an AWS service that lets you manage and automate tasks on large numbers of resources at one time based.

Once resource groups are created, you can view metrics, alarms, and dashboards in Amazon CloudWatch based on your resource groups. To view resource group data in CloudWatch, refer to the [Focus on metrics and alarms in a resource group](/AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Resource_Group.html) section of the CloudWatch User Guide.

Monitor cloud spend based on tag groupings

Tags can enable you to organize your resources across your environment to help analyze and control how much you are spending on AWS, and determine what resources are incurring costs in your environment. You can create filter views and create reports for the resources associated with a specific tag, which also enables you to create budgets and forecast your spend based on specific tags.

[Cost Allocation Tags](/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) let you track your AWS costs on a detailed level. After you activate Cost Allocation Tags, AWS uses the cost allocation tags to organize your resource costs on your cost allocation report, to make it easier for you to categorize and track your AWS costs. AWS provides two types of cost allocation tags: **AWS generated tags and user-defined tags.**

To enable Cost Allocation Tags, activate [Cost Explorer](https://console.aws.amazon.com/cost-management/home#/dashboard) in your environment, which may take up to 24 hours if it is the first time you are visiting.

As you start creating and tagging resources, you can activate these tags as **Cost Allocation Tags** on the billing console, in the [Cost Allocation Tags](https://console.aws.amazon.com/billing/home#/tags) section. Once the tags are fully activated you can use the tags within [Cost Explorer](https://console.aws.amazon.com/cost-management/home#/dashboard) to create [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) or create different reports in Cost Explorer.

[Read usage guidelines](/solutions/guidance-disclaimers/)

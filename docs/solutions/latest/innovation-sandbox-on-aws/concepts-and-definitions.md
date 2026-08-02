---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

 **Sandbox environment**

A controlled, isolated environment where teams can experiment with AWS services without impacting production systems. It provides a safe space for learning, testing, and innovation.

 **Organizational Unit (OU)**

A grouping of AWS accounts that allows you to organize accounts into a hierarchy and apply policies. This solution creates dedicated OUs for active and recycled sandbox accounts.

 **Service Control Policies (SCPs)**

Policy documents that specify the maximum available permissions for accounts within an AWS Organization. They help enforce security boundaries and service restrictions across sandbox accounts.

 **Lease**

A lease is a temporary allocation of an AWS account to a user for a specified budget or lease duration to run innovation experiments. Leases can be created through two methods: user-initiated requests (traditional self-service model) or manager-initiated assignments (direct assignment model).

 **Lease template**

A lease template provides the ability to define conditions that govern the use of the account - such as approval for a user to use a given account, budget and threshold actions, lease duration and threshold actions, and template visibility controls. Admins and managers can create lease templates with public or private visibility settings, and sandbox users can request new sandbox leases by choosing from available public templates. Private templates are only accessible to administrators and managers for direct lease assignment purposes.

 **Blueprint**

A registered CloudFormation StackSet that deploys pre-configured infrastructure to sandbox accounts when you provision a lease. Blueprints enable administrators to provide users with ready-to-use environments containing standardized resources, tools, and configurations, eliminating manual setup time and ensuring consistency across sandbox accounts.

 **Template visibility**

A configuration setting that controls whether a lease template appears in the general template listing for user requests. Public templates are visible to all users for self-service lease requests, while private templates are only accessible to administrators and managers for direct lease assignment purposes.

 **Budget threshold**

A predefined customer-defined spending limit that triggers specific actions when reached. The solution uses thresholds to send alerts, stop resources, and prevent new resource creation.

 **Account recycling**

The process of cleaning up and reusing sandbox accounts when they reach customer-defined limits. This helps optimize account management and reduce administrative overhead.

 **AWS Nuke**

 [AWS-nuke](https://github.com/ekristen/aws-nuke) is an open-source tool designed for the purpose of cleaning up and deleting AWS resources in a systematic and automated way.

 **Guardrails**

Preventive or detective controls that protect your AWS environment. They help ensure sandbox accounts maintain security, compliance, and operational standards.

 **Hub Account**

A centralized AWS account that hosts the sandbox resources and configuration, and orchestrates actions across sandbox accounts.

 **Cost Report Group**

A configurable identifier used to categorize and aggregate sandbox costs for organizational reporting and chargeback purposes. Cost report groups enable administrators to attribute sandbox usage costs to specific departments, teams, or cost centers, facilitating accurate cost allocation and budget management across the organization.

 **Permission set**

A collection of administrator-defined policies that AWS IAM Identity Center uses to determine a user’s access permissions to AWS accounts.

 **Resource controls**

Mechanisms that manage AWS resource lifecycle, including creation, modification, and termination based on defined policies and budget thresholds.

 **Least privilege access**

A security principle where users and resources are granted the minimum permissions necessary to perform their tasks. The solution enforces this through automated policy deployment.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).

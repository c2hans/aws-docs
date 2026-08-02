---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automated-patching-for-mutable-instances-in-the-hybrid-cloud-using-aws-systems-manager/patch-management-overview.html
---

# Patch management overview
<a name="patch-management-overview"></a>

If you are involved in application or infrastructure operations, you understand the importance of an operating system (OS) patching solution that is flexible and scalable enough to meet the varied requirements from your application teams. In a typical organization, some application teams use an architecture that involves immutable instances whereas others deploy their applications on mutable instances.

Immutable instance patching involves applying the patches to the Amazon Machine Images (AMIs) that are used to provision the immutable Amazon EC2 application instances. Mutable instance patching involves an in-place patch deployment to running instances during a scheduled maintenance window.

This prescriptive guide describes how you can use AWS Systems Manager Patch Manager to patch mutable instances that span multiple AWS accounts and AWS Regions in an automated way, based on the maintenance windows and patch groups defined by the application teams on their servers through tags.

The guide describes an automated patching solution that uses AWS Lambda to automate patching configurations and scheduling, using Patch Manager and maintenance windows. Amazon Quick provides the necessary reporting and dashboard capabilities to report on patch compliance.

In addition, this guide describes a reference architecture for hybrid cloud environments. Users who run their applications in a hybrid cloud setup look for opportunities to consolidate, simplify, standardize, and optimize their patch management operations across AWS and their on-premises infrastructure. The guide explains how the automated patching solution for mutable instances can be extended to support hybrid cloud scenarios.

This guide describes:
+ Key user stories for patch management
+ The patching process
+ Patch management for mutable instances in a single account and single AWS Region; architectural considerations and limitations
+ Patch management for mutable instances in a multi-account, multi-Region environment; architectural considerations and limitations
+ Patch management for on-premises instances in a hybrid cloud environment; architectural considerations and limitations
+ Key stakeholders, roles, and responsibilities

**Note**
This guide describes an architecture for an automated solution (referred to as the *automated patching solution*) that you can implement to support your patch management requirements for mutable instances. It doesn't provide the code for building the solution.

## Terms and concepts
<a name="terms"></a>

|
|
| Term | Definition |
| --- |--- |
| Immutable instances | Immutable instances are Amazon EC2 server instances that do not undergo any changes while they're running. If changes are required, you create a new instance with the updated server image, redeploy the instance, and destroy the existing server image. |
| Patch baseline | A patch baseline is specific to an OS type and defines the patch list approved for installation on the instances. For more information, see [About predefined and custom patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baselines.html) in the Systems Manager documentation. |
| Patch group | A patch group represents the servers within an application environment that are targets of a specific patch baseline. Patch groups help ensure that the right patch baselines are deployed to the correct set of instances. They also help avoid deploying patches before they have been adequately tested. Patch groups are represented by the **Patch Group** tag. For more information, see [About patch groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-patchgroups.html) in the Systems Manager documentation. |
| Maintenance window | Maintenance windows let you define a schedule for performing potentially disruptive actions on instances, such as patching an operating system, updating drivers, or installing software or patches. Each maintenance window has a schedule, a maximum duration, a set of registered target instances, and a set of registered tasks. Maintenance windows are represented by the **Maintenance Window** tag. For more information, see [About patching schedules using maintenance windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-scheduletasks.html) in the Systems Manager documentation. |

## Key user stories
<a name="user-stories"></a>

The typical OS patching process involves three tasks:

1. Scanning the EC2 instances and the on-premises servers for applicable OS patches.

1. Grouping and patching the instances at a suitable time.

1. Reporting patching compliance across the server environment.

The following table lists the key user stories for patch management.

|
|
| Scenario | User role | Description |
| --- |--- |--- |
| **Patching mechanism** | Application dev/support teams | As an application team member who is responsible for OS patching, I need a mechanism to patch my long-running or mutable instances, so I can mitigate any OS security vulnerabilities and also ensure that the instances comply with the patching baseline defined by the security team. |
| **Patching solution** | Cloud service owner | As a cloud service owner who is responsible for providing cloud services to the application teams, I need to build an OS patching solution that supports multiple AWS accounts and AWS Regions as well as on-premises servers, so application teams can mitigate any OS security vulnerabilities and also stay compliant with the patching baseline defined by the security team. |
| **Patching compliance reporting** | Security operations manager | As a security operations manager who is responsible for ensuring patch compliance, I need detailed patch compliance reporting and information across the cloud landscape, so I can identify servers that are not compliant with the patch baseline and alert teams to implement the mitigation required. |
| **Definition of roles and responsibilities** | Cloud service owner | As a cloud service owner, I need to build a well-defined roles and responsibilities matrix that explains who does what in managing the hybrid cloud patching solution I built, so obligations for patching operations are published and met. |

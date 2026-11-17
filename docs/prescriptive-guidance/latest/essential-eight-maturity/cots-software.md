---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/cots-software.html
---

# Workload example: COTS software on Amazon EC2
<a name="cots-software"></a>

This workload is an example of [Theme 3: Manage mutable infrastructure with automation](theme-3.md).

The team created the workload that runs on Amazon EC2 manually by using the AWS Management Console. Developers manually update the system by logging in to the EC2 instances and updating the software.

For this workload, the cloud and application teams take the following actions to address the Essential Eight strategies.

## Application control
<a name="application-control.a8b6f9fd-1376-54d8-88f6-ca5d2cc79852"></a>
+ The cloud team configures their centralized Amazon Machine Image (AMI) pipeline to install and configure AWS Systems Manager Agent (SSM Agent), CloudWatch agent, and SELinux. They share the resulting AMI across all accounts in the organization.
+ The cloud team uses AWS Config rules to confirm that all running [EC2 instances are managed by Systems Manager](https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-managed-by-systems-manager.html) and have [SSM Agent, CloudWatch agent, and SELinux installed](https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-applications-required.html).
+ The cloud team sends Amazon CloudWatch Logs output to a centralized security information and event management (SIEM) solution that runs on Amazon OpenSearch Service.
+ The application team implements mechanisms to inspect and manage findings from AWS Config, GuardDuty, and Amazon Inspector. The cloud team implements their own mechanisms to catch any findings that the application team misses. For more guidance about creating a vulnerability management program to address findings, see [Building a scalable vulnerability management program on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/vulnerability-management/introduction.html).

## Patch applications
<a name="patch-applications.3249bace-a3d4-58d6-90b5-84a83dcb9dc1"></a>
+ The application team patches instances based on Amazon Inspector findings.
+ The cloud team patches the base AMI, and the application team receives an alert when that AMI changes.
+ The application team restricts direct access to their EC2 instances by configuring [security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) to allow traffic only on the ports that the workload requires.
+ The application team uses [Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to patch instances instead of logging in to individual instances.
+ To run arbitrary commands on groups of EC2 instances, the application team uses [Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html).
+ On the rare occasions when the application team needs direct access to an instance, they use [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html). This access approach uses federated identities and logs any session activity for audit purposes.

## Restrict administrative privileges
<a name="restrict-administrative-privileges.16e12730-a53e-5dc5-a93b-779420712bbc"></a>
+ The application team configures [security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html) to allow traffic only on the ports that the workload requires. This restricts direct access to Amazon EC2 instances and requires that users access EC2 instances through Session Manager.
+ The application team relies on the centralized cloud team's identity federation for rotation of credentials and centralized logging.
+ The application team creates a CloudTrail trail and CloudWatch filters.
+ The application team sets up Amazon SNS alerts for CodePipeline deployments and CloudFormation stack deletions.

## Patch operating systems
<a name="patch-operating-systems.54cc1d54-0875-518e-9169-cf478362b8bd"></a>
+ The cloud team patches the base AMI, and the application team receives an alert when that AMI changes. The application team deploys new instances by using this AMI, and then they use [State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html), a capability of Systems Manager, to install required software.
+ The application team uses Patch Manager to patch instances, instead of logging in to individual instances.
+ To run arbitrary commands on groups of EC2 instances, the application team uses Run Command.
+ On the rare occasions when the application team needs direct access, they use Session Manager.

## Multi-factor authentication
<a name="multi-factor-authentication.d18dffe7-82e3-5307-9d97-d66e87eca3bf"></a>
+ The application team relies on the centralized identity federation solution described in the [Core architecture](scenario.md#core-architecture) section. This solution enforces multi-factor authentication (MFA), logs authentications, and alerts on or automatically responds to suspicious MFA events.

## Regular backups
<a name="regular-backups.879aa6ee-b3e5-5a18-a3ea-f0d2bd747259"></a>
+ The application team creates an AWS Backup plan for its EC2 instances and Amazon Elastic Block Store (Amazon EBS) volumes.
+ The application team implements a mechanism to perform a backup restoration manually every month.

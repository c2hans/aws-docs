---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/containerised-web-service.html
---

# Workload example: Containerised web service

This workload is an example of [Theme 2: Manage immutable infrastructure through secure pipelines](theme-2.md).

The web service runs on Amazon ECS and uses a database in Amazon RDS. The application team defines these resources in an CloudFormation template. The application team creates containers with EC2 Image Builder and stores them in Amazon ECR. The application team deploys changes to the system through AWS CodePipeline. Only the application team can access this pipeline. When the application team makes a pull request for the code repository, the team follows the [two-person rule](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-5.2---implement-least-privilege-policies-for-source-and-downstream-systems..html).

For this workload, the application team takes the following actions to address the Essential Eight strategies.

## Application control
<a name="application-control.4c5a9820-02b0-5ee7-b468-b7e5875991c9"></a>
+ The application team enables [scanning for Amazon ECR container images in Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html).
+ The application team builds the File Access Policy Daemon (fapolicyd) security tool into the EC2 Image Builder pipeline. For more information, see [Implementing Application Control](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-hardening/implementing-application-control) on the Australian Cyber Security Centre (ACSC) website.
+ The application team configures the Amazon ECS task definition to log output to Amazon CloudWatch Logs.
+ The application team implements mechanisms to inspect and manage Amazon Inspector findings.

## Patch applications
<a name="patch-applications.eff2ad1f-7e1f-5d24-bbca-8264e2be31db"></a>
+ The application team enables scanning for Amazon ECR container images in Amazon Inspector and configures alerts for deprecated or vulnerable libraries.
+ The application team automates their responses to Amazon Inspector findings. New findings initiate their deployment pipeline through an Amazon EventBridge trigger, and CodePipeline is the target.
+ The application team enables AWS Config to track AWS resources for asset discovery.

## Restrict administrative privileges
<a name="restrict-administrative-privileges.a692b59f-185a-5b01-bafc-1bb391e5d2c4"></a>
+ The application team restricts access to production deployments through an approval rule on their deployment pipeline.
+ The application team relies on the centralized cloud team's identity federation for rotation of credentials and centralized logging.
+ The application team creates a CloudTrail trail and CloudWatch filters.
+ The application team sets up Amazon SNS alerts for CodePipeline deployments and CloudFormation stack deletions.

## Patch operating systems
<a name="patch-operating-systems.3afb2d8e-480a-5a3d-bfc5-85125a61d26c"></a>
+ The application team enables scanning for Amazon ECR container images in Amazon Inspector and configures alerts for operating system patch updates.
+ The application team automates their response to Amazon Inspector findings. New findings initiate their deployment pipeline through an EventBridge trigger, and CodePipeline is the target.
+ The application team subscribes to Amazon RDS event notifications to receive information about updates. They make a risk-based decision with their business owner about whether to apply these updates manually or let Amazon RDS apply them automatically.
+ The application team configures the Amazon RDS instance to be a multi-Availability Zone cluster to reduce the impact of maintenance events.

## Multi-factor authentication
<a name="multi-factor-authentication.d18dffe7-82e3-5307-9d97-d66e87eca3bf"></a>
+ The application team relies on the centralized identity federation solution described in the [Core architecture](scenario.md#core-architecture) section. This solution enforces multi-factor authentication (MFA), logs authentications, and alerts on or automatically responds to suspicious MFA events.

## Regular backups
<a name="regular-backups.48f2c510-f84c-5ba1-880b-ecd271e694d8"></a>
+ The application team configures AWS Backup to automate backup of the data in their Amazon RDS cluster.
+ The application team stores CloudFormation templates in a code repository.
+ The application team develops an automated pipeline to [create a copy of their workload in another Region and run automated tests](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/) (AWS blog post). After the automated tests run, the pipeline deletes the stack. This pipeline automatically runs once a month and validates the effectiveness of the recovery procedures.

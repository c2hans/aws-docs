---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/containerised-web-service.html
---

# Workload example: Containerised web service
<a name="containerised-web-service"></a>

This workload is an example of [Theme 2: Manage immutable infrastructure through secure pipelines](theme-2.md).

The web service runs on Amazon ECS and uses a database in Amazon RDS. The application team defines these resources in an CloudFormation template. Containers are created with EC2 Image Builder and stored in Amazon ECR. The application team deploys changes to the system through AWS CodePipeline. This pipeline is restricted to the application team. When the application team makes a pull request for the code repository, the [two-person rule](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-5.2---implement-least-privilege-policies-for-source-and-downstream-systems..html) is used.

For this workload, the application team takes the following actions to address the Essential Eight strategies.

## Application control
<a name="application-control.1af29084-c9d8-58b6-9e74-1c4c55cc2e3b"></a>
+ The application team enables [scanning for Amazon ECR container images in Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html).
+ The application team build the [File Access Policy Daemon (fapolicyd)](https://github.com/linux-application-whitelisting/fapolicyd/blob/main/README.md) security tool into the EC2 Image Builder pipeline. For more information, see [Implementing Application Control](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-hardening/implementing-application-control) on the ACSC website.
+ The application team configures the Amazon ECS task definition to log output to Amazon CloudWatch Logs.
+ The application team implements mechanisms to inspect and manage Amazon Inspector findings.

## Patch applications
<a name="patch-applications.eff2ad1f-7e1f-5d24-bbca-8264e2be31db"></a>
+ The application team enables scanning for Amazon ECR container images in Amazon Inspector and configures alerts for deprecated or vulnerable libraries.
+ The application team automates their responses to Amazon Inspector findings. New findings initiate their deployment pipeline through an Amazon EventBridge trigger, and CodePipeline is the target.
+ The application team enables AWS Config to track AWS resources for asset discovery.

## Restrict administrative privileges
<a name="restrict-administrative-privileges.0594df56-6aa9-56e0-8b4d-ea2943075c7c"></a>
+ The application team is already restricting access to production deployments through an approval rule on their deployment pipeline.
+ The application team relies on the centralised cloud team's identity federation for rotation of credentials and centralised logging.
+ The application team creates a CloudTrail trail and CloudWatch filters.
+ The application team sets up Amazon SNS alerts for CodePipeline deployments and CloudFormation stack deletions.

## Patch operating systems
<a name="patch-operating-systems.ac44d4af-bf45-51bd-b81e-6a8654ba5516"></a>
+ The application team enables scanning for Amazon ECR container images in Amazon Inspector and configures alerts for OS patch updates.
+ The application team automates their response to Amazon Inspector findings. New findings initiate their deployment pipeline through an EventBridge trigger, and CodePipeline is the target.
+ The application team subscribes to Amazon RDS event notifications so that they are informed about updates. They make a risk-based decision with their business owner about whether to apply these updates manually or let Amazon RDS apply them automatically.
+ The application team configures the Amazon RDS instance to be a multi-Availability Zone cluster in order to reduce the impact of maintenance events.

## Multi-factor authentication
<a name="multi-factor-authentication.b95e9783-b2e4-56a8-816d-eb65338f4cc9"></a>
+ The application team relies on the centralised identity federation solution described in the [Core architecture](scenario.md#core-architecture) section. This solution enforces MFA, logs authentications, and alerts on or automatically responds to suspicious MFA events.

## Regular backups
<a name="regular-backups.9d07c066-5a0e-537d-b4e2-4681bfad2e6e"></a>
+ The application team configures AWS Backup to automate backup of the data their Amazon RDS cluster.
+ The application team stores CloudFormation templates in a code repository.
+ The application team develops an automated pipeline to [create a copy of their workload in another Region and run automated tests](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/) (AWS blog post). After the automated tests run, the pipeline destroys the stack. This pipeline automatically runs once a month and validates the effectiveness of the recovery procedures.

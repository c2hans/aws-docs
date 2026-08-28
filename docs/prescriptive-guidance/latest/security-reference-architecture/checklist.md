---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/checklist.html
---

# AWS SRA best practices checklist
<a name="checklist"></a>

This section distills the AWS SRA best practices detailed throughout this guide into a checklist that you can follow as you build your version of the security architecture on AWS. Use this list as a reference point and not as a replacement for reviewing the guide. The checklist is grouped by AWS service. If you want to programmatically validate your existing AWS environment against the AWS SRA best practices checklist, you can use [SRA Verify](https://github.com/awslabs/sra-verify).

SRA Verify is a security assessment tool that helps you assess your organization's alignment to the AWS SRA across multiple AWS accounts and Regions. It directly maps to AWS SRA recommendations by providing automated checks that validate your implementation against the AWS SRA guidance. The tool helps you verify that your security services are properly configured according to the reference architecture. It provides detailed findings and actionable remediation steps to help ensure that your AWS environment follows security best practices. SRA Verify is designed to run in AWS CodeBuild in the organization audit (Security Tooling) account. You can also run it locally or extend it by using the SRA Verify library.

**Note**
SRA Verify contains checks for several services, but might not contain a check for every consideration of the AWS SRA. For more information, review the guides in the [AWS SRA library](about-sra-library.md).

## AWS Organizations
<a name="checklist-organizations"></a>
+ AWS Organizations is enabled with [all features](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all).
+ [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) are used to define access control guidelines for IAM principals.
+ [Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) (RCPs) are used to define access control guidelines for AWS resources.
+ [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) are used to centrally declare and enforce your desired configuration for a given AWS service at scale across your organization.
+ Three foundational OUs are created (Security, Infrastructure, and Workload) to group member accounts that provide foundation services.
+ The [Security Tooling account](security-tooling.md) is created under the Security OU. This account provides centralized management of AWS security services and other third-party security tools.
+ The [Log Archive account](log-archive.md) is created under the Security OU. This account provides a tightly controlled central log repository of AWS services and application logs.
+ The [Network account](network.md) is created under the Infrastructure OU. This account manages the gateway between your application and the broader internet. It isolates the networking services, configuration, and operation from the individual application workloads, security, and other infrastructure.
+ The [Shared Service account](shared-services.md) is created under the Infrastructure OU. This account supports the services that multiple applications and teams use to deliver their outcomes.
+ The [Application account](application.md) is created under the Workloads OU. This account  hosts the primary infrastructure and services to run and maintain an enterprise application. This guide provides a representation, but in the real world there will be multiple OUs and member accounts segregated by applications, development environments, and other security considerations.
+ Alternate contact information for billing, operations, and security for all member accounts are configured.

## AWS CloudTrail
<a name="checklist-cloudtrail"></a>
+ An organization trail is configured that enables delivery of CloudTrail management events in the management account and all member accounts in an AWS organization.
+ The organization trail is configured as multi-Region trail.
+ The organization trail is configured to capture events from global resources.
+ Additional trails to capture specific data events are configured as necessary to monitor sensitive AWS resource activities.
+ The Security Tooling account is set as a delegated administrator of the organization trail.
+ The organization trail is configured to be automatically enabled for all new member accounts.
+ The organization trail is configured to publish logs to a centralized S3 bucket that is hosted in the Log Archive account.
+ The organization trail has log file validation enabled to verify the integrity of log files.
+ The organization trail is integrated with CloudWatch Logs for retention of logs.
+ The organization trail is encrypted by using a customer managed key.
+ The central S3 bucket that is used for the log repository in the Log Archive account is encrypted with a customer managed key.
+ The central S3 bucket used for the log repository in the Log Archive account is configured with S3 Object Lock for immutability.
+ Versioning is enabled for the central S3 bucket that is used for the log repository in the Log Archive account.
+ The central S3 bucket that is used for the log repository in the Log Archive account has a [resource policy](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html#organizational-trail-prepare-confused-deputy) defined that restricts object upload only by organization trail through the resource Amazon Resource Name (ARN).

## AWS Security Hub CSPM
<a name="checklist-cspm"></a>
+ Security Hub CSPM is enabled for all member accounts and the management account.
+ AWS Config is enabled for all member accounts as a prerequisite for Security Hub CSPM.
+ The Security Tooling account is set as a delegated administrator of Security Hub CSPM.
+ Amazon GuardDuty and Amazon Detective have the same delegated administrator account as Security Hub CSPM for smooth service integration.
+ Central configuration is used to set up and manage Security Hub CSPM across multiple AWS accounts and AWS Regions.
+ All OU and member accounts are designated as *centrally managed* by the delegated administrator of Security Hub CSPM.
+ Security Hub CSPM is automatically enabled for all new member accounts.
+ Security Hub CSPM is automatically enabled for configuration of new standards.
+ Security Hub CSPM findings from all Regions are aggregated to a single home Region.
+ Security Hub CSPM findings from all member accounts are aggregated within the Security Tooling account.
+ The [AWS Foundational Best Practices](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html) (FSBP) standard in Security Hub CSPM is enabled for all member accounts.
+ The [CIS AWS Foundation Benchmark](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html) standard in Security Hub CSPM is enabled for all member accounts.
+ Other Security Hub CSPM standards are enabled as applicable.
+ Security Hub CSPM findings are consumed by Security Hub for exposure correlation.
+ A Security Hub CSPM automation rule is used to enrich findings with resource context.
+ The Security Hub CSPM automated response and remediation feature is used to create custom EventBridge rules to take automatic actions against specific findings.
+ An Amazon CloudWatch telemetry enablement rule is created to ingest Security Hub CSPM findings into CloudWatch, for the entire organization.

## AWS Config
<a name="checklist-config"></a>
+ The AWS Config recorder is enabled for all member accounts and the management account.
+ The AWS Config recorder is enabled for all Regions.
+ The AWS Config delivery channel S3 bucket is centralized in the Log Archive account.
+ The AWS Config delegated administrator account is set to the Security Tooling account.
+ AWS Config has an organization aggregator set up. The aggregator includes all Regions.
+ AWS Config conformance packs are deployed uniformly to all member accounts from the delegated administrator account.
+ AWS Config rule findings are automatically sent to Security Hub CSPM.

## Amazon GuardDuty
<a name="checklist-guardduty"></a>
+ GuardDuty detector is enabled for all member accounts and the management account.
+ GuardDuty detector is enabled for all Regions.
+ GuardDuty detector is automatically enabled for all new member accounts.
+ GuardDuty delegated administration is set to the Security Tooling account.
+ GuardDuty foundational data sources such as CloudTrail management events, VPC flow logs, and Route 53 Resolver DNS query logs are enabled.
+ GuardDuty S3 Protection is enabled.
+ GuardDuty Malware Protection for EBS volumes is enabled.
+ GuardDuty Malware Protection for S3 is enabled.
+ GuardDuty RDS Protection is enabled.
+ GuardDuty Lambda Protection is enabled.
+ GuardDuty EKS Protection is enabled.
+ GuardDuty EKS Runtime Monitoring is enabled.
+ GuardDuty findings automatically flow to Security Hub CSPM and Security Hub.
+ GuardDuty is integrated with Amazon Detective for finding investigation.
+ GuardDuty findings exported to Amazon S3 are encrypted with a customer managed KMS key.
+ GuardDuty Extended Threat Detection is enabled.
+ GuardDuty findings are exported to a central S3 bucket in the Log Archive account for retention and encrypted with a customer managed KMS key.

## IAM
<a name="checklist-iam"></a>
+ IAM users are not used.
+ Centralized management of root access for member accounts is enforced.
+ The centralized privileged root user task for management account is enforced from the delegated administrator.
+ Centralized root access management is delegated to the Security Tooling account.
+ All member account root credentials are removed.
+ All member and management AWS account password policies are set according to the organization's security standard.
+ IAM access advisor is used to review last used information for IAM groups, users, roles, and policies.
+ Permission boundaries are used to restrict maximum possible permissions for IAM roles.

## IAM Access Analyzer
<a name="checklist-iam-analyzer"></a>
+ IAM Access Analyzer is enabled for all member accounts and the management account.
+ The IAM Access Analyzer delegated administrator is set to the Security Tooling account.
+ The IAM Access Analyzer external access analyzer is configured with the organization zone of trust in every Region.
+ The IAM Access Analyzer external access analyzer is configured with the account zone of trust in every Region.
+ The IAM Access Analyzer internal access analyzer is configured with the organization zone of trust in every Region.
+ The IAM Access Analyzer internal access analyzer is configured with the account zone of trust in every Region.
+ The IAM Access Analyzer unused access analyzer for the current account is created.
+ The IAM Access Analyzer unused access analyzer for the current organization is created.

## Amazon Detective
<a name="checklist-detective"></a>
+ Detective is enabled for all member accounts.
+ Detective is automatically enabled for all new member accounts.
+ Detective is enabled for all Regions.
+ The Detective delegated administrator is set to the Security Tooling account.
+ The Detective, GuardDuty, and Security Hub CSPM delegated administrator is set to the same Security Tooling account.
+ Detective is integrated with Security Lake for storage and analysis of raw logs.
+ Detective is integrated with GuardDuty for ingesting findings.
+ Detective is ingesting Amazon EKS audit logs for analysis.
+ Detective is ingesting Security Hub CSPM logs for analysis.

## AWS Firewall Manager
<a name="checklist-firewall"></a>
+ Firewall Manager security policies are set.
+ The Firewall Manager delegated administrator is set to the Security Tooling account.
+ AWS Config is enabled as a prerequisite.
+ Multiple Firewall Manager administrators are set with restricted scope per OU, account, and Region.
+ A Firewall Manager AWS WAF security policy is defined.
+ A Firewall Manager AWS WAF centralized logging policy is defined.
+ A Firewall Manager Shield Advanced security policy is defined.
+ A Firewall Manager security group security policy is defined.
+ A Firewall Manager security policy is defined for AWS Network Firewall.
+ A Firewall Manager security policy is defined for Route 53 DNS Firewall.

## Amazon Inspector
<a name="checklist-inspector"></a>
+ Amazon Inspector is enabled for all member accounts.
+ Amazon Inspector is automatically enabled for any new member account.
+ The Amazon Inspector delegated administrator is set to the Security Tooling account.
+ Amazon Inspector EC2 vulnerability scanning is enabled.
+ Amazon Inspector ECR image vulnerability scanning is enabled.
+ Amazon Inspector Lambda function and layers vulnerability scanning is enabled.
+ Amazon Inspector Lambda code scanning is enabled.
+ Amazon Inspector code security scanning is enabled.

## Amazon Macie
<a name="checklist-macie"></a>
+ Macie is enabled for applicable member accounts.
+ Macie is automatically enabled for applicable new member accounts.
+ The Macie delegated administrator is set to the Security Tooling account.
+ Macie findings are exported to a central S3 bucket in the log Archive account.
+ S3 buckets that store Macie findings are encrypted with a customer managed key.
+ The Macie policy and classification policy are published to Security Hub CSPM.

## Amazon Security Lake
<a name="checklist-security-lake"></a>
+ Security Lake organization configuration is enabled.
+ The Security Lake delegated administrator is set to the Log Archive account.
+ The Security Lake organization configuration is enabled for new member accounts.
+ The Security Tooling account is set up as a data access subscriber to conduct analysis of logs.
+ The Security Tooling account is set up as a data query subscriber to conduct analysis of logs.
+ A CloudTrail management log source is enabled for Security Lake in all or specified active member accounts.
+ A VPC flow log source is enabled for Security Lake in all or specified active member accounts.
+ A Route 53 log source is enabled for Security Lake in all or specified active member accounts.
+ CloudTrail data event for an S3 log source is enabled for Security Lake in all or specified active member accounts.
+ A Lambda execution log source is enabled for Security Lake in all or specified active member accounts.
+ An Amazon EKS audit log source is enabled for Security Lake in all or specified active member accounts.
+ A Security Hub findings log source is enabled for Security Lake in all or specified active member accounts.
+ An AWS WAF log source is enabled for Security Lake in all or specified active member accounts.
+ Security Lake SQS queues in the delegated administrator account is encrypted with a customer managed key.
+ The Security Lake SQS dead-letter queue in the delegated administrator account is encrypted with a customer managed key.
+ The Security Lake S3 bucket is encrypted with a customer managed key.
+ The Security Lake S3 bucket has a resource policy that restricts direct access only by Security Lake.

## AWS WAF
<a name="checklist-waf"></a>
+ All CloudFront distributions are associated with AWS WAF.
+ All Amazon API Gateway REST APIs are associated with AWS WAF.
+ All Application Load Balancers are associated with AWS WAF.
+ All AWS AppSync GraphQL APIs are associated with AWS WAF.
+ All Amazon Cognito user pools are associated with AWS WAF.
+ All AWS App Runner services are associated with AWS WAF.
+ All AWS Verified Access instances are associated with AWS WAF.
+ All AWS Amplify applications are associated with AWS WAF.
+ AWS WAF logging is enabled.
+ AWS WAF logs are centralized in an S3 bucket in the Log Archive account.

## AWS Shield Advanced
<a name="checklist-shield"></a>
+ Shield Advanced subscription is enabled and set to auto-renew for all application accounts that have public-facing resources.
+ Shield Advanced is configured for all CloudFront distributions.
+ Shield Advanced is configured for all Application Load Balancers.
+ Shield Advanced is configured for all Elastic IP addresses associated with Network Load Balancers.
+ Shield Advanced is configured for all Elastic IP addresses associated with EC2 instances.
+ Shield Advanced is configured for all Route 53 hosted zones.
+ Shield Advanced is configured for all Elastic IP addresses.
+ Shield Advanced is configured for all Global Accelerators.
+ CloudWatch alarms are configured for CloudFront and Route 53 resources that are protected by Shield Advanced.
+ Shield Response Team (SRT) access is configured.
+ Shield Advanced proactive engagement is enabled.
+ Shield Advanced proactive engagement contacts are configured.
+ Shield Advanced protected resources have a custom AWS WAF rule configured.
+ Shield Advanced protected resources have automatic application-layer DDoS mitigation enabled.

## AWS Security Incident Response
<a name="checklist-incident-response"></a>
+ AWS Security Incident Response is enabled for the whole AWS organization.
+ The AWS Security Incident Response delegated administrator is set to the Security Tooling account.
+ The proactive response and alert triaging workflow is enabled.
+ AWS Customer Incident Response Team (CIRT) containment actions are authorized.

## AWS Audit Manager
<a name="checklist-audit"></a>
+ Audit Manager is enabled for all member accounts.
+ Audit Manager is automatically enabled for new member accounts.
+ The Audit Manager delegated administrator is set to the Security Tooling account.
+ AWS Config is enabled as prerequisite for Audit Manager.
+ A customer managed  key is used for data stored in Audit Manager.
+ The default assessment report destination is configured.

## AWS Security Hub
<a name="checklist-security-hub"></a>
+ AWS Security Hub is enabled for all member accounts and the management account.
+ The Security Tooling account is set as a delegated administrator for Security Hub.
+ Security Hub is configured to enable all Regions, OUs, and accounts automatically, including future Regions and accounts.
+ Cross-Region aggregation is set up to aggregate findings, resources, and trends from multiple Regions into a single home Region.
+ Security Hub CSPM, Amazon GuardDuty, Amazon Inspector, and Amazon Macie are enabled as building block services for Security Hub.
+ Security Hub coverage findings are used to validate that security services are uniformly enabled across all member accounts.
+ Findings are formatted in Open Cybersecurity Schema Framework (OCSF).
+ EventBridge integration is configured for automated response and remediation workflows.

## AWS Network Firewall
<a name="checklist-network-firewall"></a>
+ AWS Network Firewall is deployed in the inspection VPC within the Network account.
+ All traffic between VPCs passes through the inspection VPC for Network Firewall inspection.
+ The Network Firewall subnet is dedicated exclusively to firewall endpoints (no other workloads deployed in the firewall subnet).
+ Stateful inspection, intrusion prevention, and web filtering rules are configured.
+ Network Firewall activity is visible in real time through CloudWatch metrics.
+ Network Firewall logs are sent to Amazon S3, CloudWatch, or Amazon Data Firehose.
+ AWS Firewall Manager is used to centrally configure and deploy Network Firewall rules across the organization.
+ Firewall endpoints are deployed in every Availability Zone that contains protected subnets.

## Amazon Route 53 Resolver DNS Firewall
<a name="checklist-dns-firewall"></a>
+ DNS Firewall is used to prevent DNS exfiltration of data from VPCs that require DNS-level protection.
+ DNS Firewall rule groups are configured to block or allow queries to specific domains.
+ DNS Firewall blocks resolution requests to unauthorized private hosted zones, VPC endpoint names, and public or private EC2 instance names.
+ DNS Firewall rule groups are managed centrally through AWS Firewall Manager or AWS Resource Access Manager (AWS RAM).

## AWS Key Management Service
<a name="checklist-kms"></a>
+ Customer managed keys are used for encryption of all sensitive data at rest.
+ Separate KMS keys are created per service and per account where appropriate.
+ Key policies are defined to restrict usage to intended services and principals only.
+ Automatic annual key rotation is enabled for all customer managed symmetric keys.
+ Key administration is separated from key usage through distinct IAM permissions.
+ Key policies use condition keys (such as `kms:ViaService`) to restrict which services can use a key.
+ KMS key usage is audited through AWS CloudTrail.
+ AWS managed keys are acceptable only for non-sensitive or public-classified data.

## AWS Private Certificate Authority
<a name="checklist-private-ca"></a>
+ A private CA hierarchy (root CA and subordinate CAs) is created in the Security Tooling account.
+ The root CA is protected with stringent security controls in the Security Tooling account.
+ Subordinate CAs are shared with Application accounts through AWS RAM for issuing end-entity certificates.
+ Private certificates are used for internal application communications (TLS between services and load balancers).
+ Certificate lifecycle management (issuance, renewal, revocation) is automated through AWS Certificate Manager (ACM) integration.
+ CA hierarchy design follows the principle of limited revocable trust with separate CAs per domain of responsibility.

## AWS IAM Identity Center
<a name="checklist-sso"></a>
+ IAM Identity Center is enabled in the Org Management account.
+ Delegated administration for IAM Identity Center is configured to the Shared Services account.
+ IAM Identity Center is integrated with a corporate identity provider (IdP) via SAML 2.0 or SCIM.
+ Permission sets are centrally managed and provisioned to member accounts.
+ Multi-factor authentication (MFA) is enforced for all IAM Identity Center users.
+ Access to the delegated administrator account for IAM Identity Center is tightly controlled.
+ IAM Identity Center is used instead of IAM users for all human access to AWS accounts.
+ IAM Identity Center multi-Region replication is enabled for workforce identity management across multiple AWS Regions.

## AWS Systems Manager
<a name="checklist-systems-manager"></a>
+ Systems Manager is deployed across all member accounts using delegated administrator functionality.
+ All EC2 instances are registered as managed instances through SSM Agent.
+ Session Manager is used for interactive access to instances instead of SSH or RDP (no inbound ports required).
+ Patch Manager is used to automate patching for operating systems and applications.
+ Systems Manager Automation runbooks are used for standardized remediation actions.
+ Systems Manager Explorer is configured with cross-account data synchronization through AWS Organizations.
+ VPC endpoints are provisioned for Systems Manager to enable private network connectivity.
+ Compliance data from Systems Manager is integrated with AWS Config and Security Hub CSPM.

## AWS Secrets Manager
<a name="checklist-secrets-manager"></a>
+ All application credentials, database passwords, and API keys are stored in Secrets Manager (not hardcoded in code or environment variables).
+ Automatic rotation is configured for all secrets that support it.
+ Fine-grained IAM policies and resource-based policies control access to each secret.
+ Secrets are encrypted with customer managed KMS keys for sensitive workloads.
+ Secret access is monitored through AWS CloudTrail.
+ AWS Config rules are configured to detect changes to secrets.
+ Secrets Manager is integrated with Amazon Relational Database Service (Amazon RDS) for automatic database credential management.
+ Secrets are managed locally in the account closest to where they are used.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

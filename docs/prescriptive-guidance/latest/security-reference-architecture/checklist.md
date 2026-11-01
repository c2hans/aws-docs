---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/checklist.html
---

# AWS SRA best practices checklist
<a name="checklist"></a>

This section distills the AWS SRA best practices detailed throughout this guide into a checklist that you can follow as you build your version of the security architecture on AWS. Use this list as a reference point and not as a replacement for reviewing the guide. The checklist groups items by AWS service. If you want to programmatically validate your existing AWS environment against the AWS SRA best practices checklist, you can use [SRA Verify](https://github.com/awslabs/sra-verify).

SRA Verify is a security assessment tool that helps you assess your organization's alignment with the AWS SRA across multiple AWS accounts and Regions. It directly maps to AWS SRA recommendations by providing automated checks that validate your implementation against the AWS SRA guidance. The tool helps you verify that your security services follow the configuration requirements of the reference architecture. It provides detailed findings and actionable remediation steps to help ensure that your AWS environment follows security best practices. SRA Verify runs in AWS CodeBuild in the organization audit (Security Tooling) account. You can also run it locally or extend it by using the SRA Verify library.

**Note**
SRA Verify contains checks for several services, but might not contain a check for every consideration of the AWS SRA. For more information, review the guides in the [AWS SRA library](about-sra-library.md).

## AWS Organizations
<a name="checklist-organizations"></a>
+ AWS Organizations MUST be enabled with [all features](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all).
+ [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) MUST be used to define access control guidelines for IAM principals.
+ [Resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) (RCPs) MUST be used to define access control guidelines for AWS resources.
+ [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) MUST be used to centrally declare and enforce your desired configuration for a given AWS service at scale across your organization.
+ Three foundational OUs MUST be created (Security, Infrastructure, and Workloads) to group member accounts that provide foundation services.
+ The [Security Tooling account](security-tooling.md) MUST be created under the Security OU. This account provides centralized management of AWS security services and other third-party security tools.
+ The [Log Archive account](log-archive.md) MUST be created under the Security OU. This account provides a tightly controlled central log repository of AWS services and application logs.
+ The [Network account](network.md) SHOULD be created under the Infrastructure OU. This account manages the gateway between your application and the broader internet. It isolates the networking services, configuration, and operation from the individual application workloads, security, and other infrastructure.
+ The Shared Services account SHOULD be created under the Infrastructure OU. This account supports the services that multiple applications and teams use to deliver their outcomes.
+ The [Application account](application.md) MUST be created under the Workloads OU. This account hosts the primary infrastructure and services to run and maintain an enterprise application. This guide provides a representation, but in practice there will be multiple OUs and member accounts segregated by applications, development environments, and other security considerations.
+ Alternate contact information for billing, operations, and security for all member accounts MUST be configured.

## AWS CloudTrail
<a name="checklist-cloudtrail"></a>
+ An organization trail MUST be configured that enables delivery of CloudTrail management events in the management account and all member accounts in an AWS organization.
+ The organization trail MUST be configured as multi-Region trail.
+ The organization trail MUST be configured to capture events from global resources.
+ Additional trails to capture specific data events MAY be configured as necessary to monitor sensitive AWS resource activities.
+ The Security Tooling account MUST be set as a delegated administrator of the organization trail.
+ The organization trail MUST be configured to be automatically enabled for all new member accounts.
+ The organization trail MUST be configured to publish logs to a centralized S3 bucket that is hosted in the Log Archive account.
+ The organization trail MUST have log file validation enabled to verify the integrity of log files.
+ The organization trail MUST be integrated with CloudWatch Logs for monitoring, filtering and archival of logs.
+ The organization trail MUST be encrypted by using a customer managed key.
+ The central S3 bucket that is used for the log repository in the Log Archive account MUST be encrypted with a customer managed key.
+ The central S3 bucket used for the log repository in the Log Archive account SHOULD be configured with S3 Object Lock for immutability.
+ Versioning SHOULD be enabled for the central S3 bucket that is used for the log repository in the Log Archive account.
+ The central S3 bucket that is used for the log repository in the Log Archive account MUST have a [resource policy](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.html#organizational-trail-prepare-confused-deputy) defined that restricts object upload only by organization trail through the resource Amazon Resource Name (ARN).

## AWS Security Hub CSPM
<a name="checklist-cspm"></a>
+ Security Hub CSPM MUST be enabled for all member accounts and the management account.
+ AWS Config MUST be enabled for all member accounts as a prerequisite for Security Hub CSPM.
+ The Security Tooling account MUST be set as a delegated administrator of Security Hub CSPM.
+ Amazon GuardDuty and Amazon Detective SHOULD have the same delegated administrator account as Security Hub CSPM for seamless service integration.
+ Central configuration MUST be used to set up and manage Security Hub CSPM across multiple AWS accounts and AWS Regions.
+ All OU and member accounts SHOULD be designated as *centrally managed* by the delegated administrator of Security Hub CSPM.
+ Security Hub CSPM MUST be automatically enabled for all new member accounts.
+ Security Hub CSPM SHOULD be automatically enabled for configuration of new standards.
+ Security Hub CSPM findings from all Regions MUST be aggregated to a single home Region.
+ Security Hub CSPM findings from all member accounts MUST be aggregated within the Security Tooling account.
+ The [AWS Foundational Security Best Practices](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html) (FSBP) standard in Security Hub CSPM MUST be enabled for all member accounts.
+ The [CIS AWS Foundations Benchmark](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html) standard in Security Hub CSPM MUST be enabled for all member accounts.
+ Other Security Hub CSPM standards MAY be enabled as applicable.
+ Security Hub CSPM findings MUST be consumed by Security Hub for exposure correlation.
+ A Security Hub CSPM automation rule MAY be used to enrich findings with resource context.
+ The Security Hub CSPM automated response and remediation feature MAY be used to create custom EventBridge rules to take automatic actions against specific findings.
+ An Amazon CloudWatch telemetry enablement rule MAY be created to ingest Security Hub CSPM findings into CloudWatch, for the entire organization.
+ If using AWS and Microsoft Azure you MAY use Azure integration to monitor Microsoft Azure resources, extending risk analytics, cloud security posture management, vulnerability management, and security response management across both clouds.

## AWS Config
<a name="checklist-config"></a>
+ The AWS Config recorder MUST be enabled for all member accounts and the management account.
+ The AWS Config recorder MUST be enabled for all Regions.
+ The AWS Config delivery channel S3 bucket MUST be centralized in the Log Archive account.
+ The AWS Config delegated administrator account MUST be set to the Security Tooling account.
+ AWS Config MUST have an organization aggregator set up. The aggregator includes all Regions.
+ AWS Config conformance packs SHOULD be deployed uniformly to all member accounts from the delegated administrator account.
+ AWS Config rule findings MUST be automatically sent to Security Hub CSPM.

## Amazon GuardDuty
<a name="checklist-guardduty"></a>
+ GuardDuty detector MUST be enabled for all member accounts and the management account.
+ GuardDuty detector MUST be enabled for all Regions.
+ For multi-Region enablement, you SHOULD use AWS Organization Declarative policies for enablement
+ GuardDuty detector MUST be automatically enabled for all new member accounts using organization auto-enable feature
+ GuardDuty delegated administration MUST be set to the Security Tooling account.
+ GuardDuty foundational data sources such as CloudTrail management events, VPC flow logs, and Route 53 Resolver DNS query logs MUST be enabled.
+ GuardDuty S3 Protection SHOULD be enabled.
+ GuardDuty Malware Protection EBS volumes SHOULD be enabled.
+ GuardDuty Malware Protection for S3 SHOULD be enabled.
+ GuardDuty RDS Protection SHOULD be enabled.
+ GuardDuty Lambda Protection SHOULD be enabled.
+ GuardDuty EKS Protection SHOULD be enabled.
+ GuardDuty Runtime Monitoring SHOULD be enabled.
+ GuardDuty AI protection SHOULD be enabled.
+ GuardDuty findings automatically flow to Security Hub CSPM and Security Hub.
+ GuardDuty SHOULD be integrated with Amazon Detective for finding investigation.
+ GuardDuty findings exported to Amazon S3 MUST be encrypted with a customer managed KMS key.
+ GuardDuty Extended Threat Detection SHOULD be enabled (enabled by default as part of GuardDuty enablement) .
+ GuardDuty findings MUST be exported to a central S3 bucket in the Log Archive account for retention and encrypted with a customer managed KMS key.

## IAM
<a name="checklist-iam"></a>
+ IAM users MUST NOT be used.
+ Centralized management of root access for member accounts MUST be enforced.
+ The centralized privileged root user task for member account MUST be enforced from the delegated administrator.
+ Centralized root access management MUST be delegated to the Security Tooling account.
+ All member account root credentials SHOULD be removed.
+ All member and management AWS account password policies SHOULD be set according to the organization's security standard.
+ IAM access advisor SHOULD be used to review last used information for IAM groups, users, roles, and policies.
+ Permission boundaries SHOULD be used to restrict maximum possible permissions for IAM roles.

## IAM Access Analyzer
<a name="checklist-iam-analyzer"></a>
+ IAM Access Analyzer MUST be enabled for all member accounts and the management account.
+ The IAM Access Analyzer delegated administrator MUST be set to the Security Tooling account.
+ The IAM Access Analyzer external access analyzer MUST be configured with the organization zone of trust in every Region.
+ The IAM Access Analyzer external access analyzer SHOULD be configured with the account zone of trust in every Region.
+ The IAM Access Analyzer internal access analyzer SHOULD be configured with the organization zone of trust in every Region.
+ The IAM Access Analyzer internal access analyzer SHOULD be configured with the account zone of trust in every Region.
+ The IAM Access Analyzer unused access analyzer for the current account SHOULD be created.
+  IAM Access Analyzer unused access analyzer for the current organization MUST be created.

## Amazon Detective
<a name="checklist-detective"></a>
+ Detective SHOULD be enabled for all member accounts.
+ Detective SHOULD be automatically enabled for all new member accounts.
+ Detective SHOULD be enabled for all Regions.
+ The Detective delegated administrator MUST be set to the Security Tooling account.
+ The Detective, GuardDuty, and Security Hub CSPM delegated administrator SHOULD be set to the same Security Tooling account.
+ Detective SHOULD be integrated with Security Lake for storage and analysis of raw logs.
+ Detective SHOULD be integrated with GuardDuty for ingesting findings.
+ Detective SHOULD be ingesting Amazon EKS audit logs for analysis.
+ Detective SHOULD be ingesting Security Hub CSPM findings for analysis.

## AWS Firewall Manager
<a name="checklist-firewall"></a>
+ Firewall Manager security policies MUST be set.
+ The Firewall Manager delegated administrator MUST be set to the Security Tooling account.
+ AWS Config MUST be enabled as a prerequisite.
+ Multiple Firewall Manager administrators MAY be set with restricted scope per OU, account, and Region.
+ A Firewall Manager AWS WAF security policy SHOULD be defined.
+ A Firewall Manager AWS WAF centralized logging policy MUST be defined.
+ A Firewall Manager Shield Advanced security policy SHOULD be defined.
+ A Firewall Manager security group security policy MUST be defined.
+ A Firewall Manager security policy SHOULD be defined for AWS Network Firewall.
+ A Firewall Manager security policy SHOULD be defined for Route 53 DNS Firewall.

## Amazon Inspector
<a name="checklist-inspector"></a>
+ Amazon Inspector MUST be enabled for all member accounts.
+ Amazon Inspector MUST be automatically enabled for any new member account.
+ The Amazon Inspector delegated administrator MUST be set to the Security Tooling account.
+ Amazon Inspector EC2 vulnerability scanning SHOULD be enabled.
+ Amazon Inspector ECR image vulnerability scanning SHOULD be enabled.
+ Amazon Inspector Lambda function and layers vulnerability scanning SHOULD be enabled.
+ Amazon Inspector Lambda code scanning SHOULD be enabled.
+ Amazon Inspector code security scanning SHOULD be enabled.

## Amazon Macie
<a name="checklist-macie"></a>
+ Macie SHOULD be enabled for applicable member accounts.
+ The Macie delegated administrator MUST be set to the Security Tooling account.
+ Macie findings MUST be exported to a central S3 bucket in the log Archive account.
+ You MUST encrypt S3 buckets that store Macie findings with a customer managed key.
+ You MUST publish the Macie policy and classification policy to Security Hub CSPM.

## Amazon Security Lake
<a name="checklist-security-lake"></a>
+ Security Lake organization configuration SHOULD be enabled.
+ The Security Lake delegated administrator MUST be set to the Log Archive account.
+ The Security Lake organization configuration SHOULD be enabled for new member accounts.
+ The Security Tooling account SHOULD be set up as a data access subscriber to analyze logs.
+ The Security Tooling account SHOULD be set up as a data query subscriber to conduct analysis of logs.
+ A CloudTrail management log source MUST be enabled for Security Lake in all or specified active member accounts.
+ A VPC flow log source MUST be enabled for Security Lake in all or specified active member accounts.
+ An Amazon Route 53 log source MUST be enabled for Security Lake in all or specified active member accounts.
+ CloudTrail data event for an S3 log source SHOULD be enabled for Security Lake in all or specified active member accounts.
+ A Lambda execution log source SHOULD be enabled for Security Lake in all or specified active member accounts.
+ An Amazon EKS audit log source SHOULD be enabled for Security Lake in all or specified active member accounts.
+ A Security Hub findings log source MUST be enabled for Security Lake in all or specified active member accounts.
+ An AWS WAF log source SHOULD be enabled for Security Lake in all or specified active member accounts.
+ Security Lake SQS queues in the delegated administrator account MUST be encrypted with a customer managed key.
+ The Security Lake SQS dead-letter queue in the delegated administrator account MUST be encrypted with a customer managed key.
+ The Security Lake S3 bucket MUST be encrypted with a customer managed key.
+ The Security Lake S3 bucket MUST have a resource policy that restricts direct access only by Security Lake.

## AWS WAF
<a name="checklist-waf"></a>
+ All CloudFront distributions MUST be associated with AWS WAF.
+ All Amazon API Gateway REST APIs MUST be associated with AWS WAF.
+ All Application Load Balancers MUST be associated with AWS WAF.
+ All AWS AppSync GraphQL APIs MAY be associated with AWS WAF.
+ All Amazon Cognito user pools MAY be associated with AWS WAF.
+ All AWS App Runner services MAY be associated with AWS WAF.
+ All AWS Verified Access instances MAY be associated with AWS WAF.
+ All AWS Amplify applications MAY be associated with AWS WAF.
+ AWS WAF logging MUST be enabled.
+ AWS WAF logs MUST be stored in an S3 bucket in the Log Archive account.

## AWS Shield Advanced
<a name="checklist-shield"></a>
+ Shield Advanced subscription MUST be enabled and set to auto-renew for all application accounts that have public-facing resources.
+ Shield Advanced SHOULD be configured for all CloudFront distributions.
+ Shield Advanced SHOULD be configured for all Application Load Balancers.
+ Shield Advanced SHOULD be configured for all Elastic IP addresses associated with Network Load Balancers.
+ Shield Advanced SHOULD be configured for all Elastic IP addresses associated with EC2 instances.
+ Shield Advanced SHOULD be configured for all Route 53 hosted zones.
+ Shield Advanced SHOULD be configured for all Elastic IP addresses.
+ Shield Advanced SHOULD be configured for all Global Accelerators.
+ CloudWatch alarms MUST be configured for CloudFront and Route 53 resources that are protected by Shield Advanced.
+ Shield Response Team (SRT) access SHOULD be configured.
+ Shield Advanced proactive engagement SHOULD be enabled.
+ Shield Advanced proactive engagement contacts SHOULD be configured.
+ Shield Advanced protected resources MUST have a custom AWS WAF rule configured.
+ Shield Advanced protected resources (CloudFront and Application Load Balancers) SHOULD have automatic application-layer DDoS mitigation enabled.

## AWS Security Incident Response
<a name="checklist-incident-response"></a>
+ AWS Security Incident Response MUST be enabled for AWS organization.
+ The AWS Security Incident Response delegated administrator MUST be set to the Security Tooling account.
+ Enable the proactive response and alert triaging workflow.
+ AWS Customer Incident Response Team (CIRT) containment actions.

## AWS Audit Manager
<a name="checklist-audit"></a>
+ Audit Manager SHOULD be enabled for all member accounts (non longer available to new customers).
+ The Audit Manager delegated administrator MUST be set to the Security Tooling account.
+ AWS Config SHOULD be enabled as prerequisite for Audit Manager.
+ A customer managed  key MUST be used for data stored in Audit Manager.
+ The default assessment report destination SHOULD be configured.

## AWS Security Hub
<a name="checklist-security-hub"></a>
+ AWS Security Hub MUST be enabled for all member accounts and the management account.
+ The Security Tooling account MUST be set as a delegated administrator for Security Hub.
+ Security Hub MUST be configured to enable all Regions, OUs, and accounts automatically, including future Regions and accounts.
+ Cross-Region aggregation MUST be set up to aggregate findings, resources, and trends from multiple Regions into a single home Region.
+ Security Hub CSPM, Amazon GuardDuty, Amazon Inspector, and Amazon Macie SHOULD be enabled as building block services for Security Hub.
+ Network scanning opt-in feature of Security Hub MAY be used to perform active network reachability testing on your cloud resources.
+ Security Hub coverage findings SHOULD be used to validate that security services are uniformly enabled across all member accounts.
+ EventBridge integration SHOULD be configured for automated response and remediation workflows.

## AWS Network Firewall
<a name="checklist-network-firewall"></a>
+ AWS Network Firewall SHOULD be deployed in the inspection VPC within the Network account.
+ All traffic between VPCs SHOULD be routed through the inspection VPC for Network Firewall inspection.
+ The Network Firewall subnet SHOULD exclusively be used for firewall endpoints (do not deploy other workloads in the firewall subnet).
+ Stateful inspection, intrusion prevention, and web filtering rules SHOULD be configured.
+ Network Firewall activity in real time SHOULD be monitored through CloudWatch metrics.
+ Network Firewall logs SHOULD be sent to Amazon S3, CloudWatch, or Amazon Data Firehose.
+ AWS Firewall Manager SHOULD be used to centrally configure and deploy Network Firewall rules across the organization.
+ AWS Network Firewall endpoints MUST be deployed in every Availability Zone that contains protected subnets.

## Amazon Route 53 Resolver DNS Firewall
<a name="checklist-dns-firewall"></a>
+ DNS Firewall MUST be used to prevent DNS exfiltration of data from VPCs that require DNS-level protection.
+ DNS Firewall rule groups MUST be configured to block or allow queries to specific domains.
+ DNS Firewall MUST block resolution requests to unauthorized private hosted zones, VPC endpoint names, and public or private EC2 instance names.
+ DNS Firewall rule groups SHOULD be managed centrally through AWS Firewall Manager or AWS Resource Access Manager (AWS RAM).

## AWS Key Management Service
<a name="checklist-kms"></a>
+ Customer managed keys MUST be used to encrypt all sensitive data at rest.
+ Separate KMS keys SHOULD be used per service and per account where appropriate.
+ Key policies SHOULD be defined to restrict usage to intended services and principals only.
+ Automatic key rotation MUST be enabled for all customer managed symmetric keys.
+ Key administration SHOULD be separated from key usage through distinct IAM permissions.
+ Key policies SHOULD use condition keys (such as `kms:ViaService`) to restrict which services can use a key.
+ KMS key usage MUST be audited through AWS CloudTrail.
+ AWS managed keys SHOULD be used only for non-sensitive or public-classified data.

## AWS Private Certificate Authority
<a name="checklist-private-ca"></a>
+ Dedicated Root CA SHOULD be created in the Security Tooling account.
+ Subordinate CA hierarchy SHOULD be created in Workloads account.
+ The root CA MUST be protected with stringent security controls in the Security Tooling account.
+ Subordinate CAs SHOULD be shared with Application accounts through AWS RAM for issuing end-entity certificates.
+ Private certificates SHOULD be used for internal application communications (TLS between services and load balancers).
+ Certificate lifecycle management (issuance, renewal, revocation) SHOULD be automated through AWS Certificate Manager (ACM) integration.
+ CA hierarchy design MUST follow the principle of limited revocable trust with separate CAs per domain of responsibility.

## AWS IAM Identity Center
<a name="checklist-sso"></a>
+ IAM Identity Center SHOULD be enabled in the Org Management account.
+ Delegated administration for IAM Identity Center MUST be configured to the Shared Services account.
+ IAM Identity Center MUST be integrated with a corporate identity provider (IdP) via SAML 2.0 or SCIM.
+ Permission sets SHOULD be centrally managed and provisioned to member accounts.
+ Account access manager SHOULD be used to assign AWS account access to workforce identity
+ Multi-factor authentication (MFA) MUST be enforced for all IAM Identity Center users.
+ Delegated administrator account access for IAM Identity Center MUST be tightly controlled.
+ IAM Identity Center MUST be used instead of IAM users for all human access to AWS accounts.
+ IAM Identity Center multi-Region replication SHOULD be enabled for workforce identity management across multiple AWS Regions.

## AWS Systems Manager
<a name="checklist-systems-manager"></a>
+ Systems Manager across all member accounts SHOULD be using delegated administrator functionality.
+ All EC2 instances SHOULD be registered as managed instances through SSM Agent.
+ Session Manager SHOULD be used for interactive access to instances instead of SSH or RDP (no inbound ports required).
+ Use Patch Manager to automate patching for operating systems and applications.
+ Systems Manager Automation runbooks SHOULD be used for standardized remediation actions.
+ Systems Manager Explorer with cross-account data synchronization SHOULD be used through AWS Organizations.
+ Provision VPC endpoints for Systems Manager to enable private network connectivity.
+ Systems Manager SHOULD be integrated with AWS Config and Security Hub CSPM.

## AWS Secrets Manager
<a name="checklist-secrets-manager"></a>
+ All application credentials, database passwords, and API keys MUST be stored in Secrets Manager (not hardcoded in code or environment variables).
+ Automatic rotation MUST be configured for all secrets that support it.
+ Fine-grained IAM policies and resource-based policies MUST control access to each secret.
+ Secrets MUST be encrypted with customer managed KMS keys for sensitive workloads.
+ Secret access MUST be monitored through AWS CloudTrail.
+ Configure AWS Config rule to monitor secret usage
+ Secrets Manager SHOULD be integrated with Amazon Relational Database Service (Amazon RDS) for automatic database credential management.
+ Secrets SHOULD be managed locally in the account closest to where they are used.

## AWS Network Security Manager
<a name="aws-network-security-manager"></a>
+ AWS Network Security Manager OR AWS Firewall Manager SHOULD be enabled.
+ AWS Network Security Manager policies MUST be set.
+ AWS Network Security Manager MUST be delegated to Security Tooling account
+ You MUST monitor the synchronization status of your deployments to identify out-of-sync resources
+ AWS Network Security Manager resources - rules, templates, policies, scopes and deployments - SHOULD be versioned
+ You MAY enable auto-remediation to enable AWS Network Security Manager to remediate out-of-sync resources
+ You MAY enable multiple member accounts as Administrator account for AWS Network Security Manager
+ When using multiple Administrator accounts you MUST define the administrative scope (OU, account or firewall type) for each administrator
+ When using multiple Administrator accounts you MUST assign priority for each administrator to resolve policy enforcement conflicts.

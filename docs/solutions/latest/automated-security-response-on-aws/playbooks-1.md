---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/playbooks-1.html
---

# Playbooks
<a name="playbooks-1"></a>

This solution includes the playbook remediations for the security standards defined as part of the [Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html#cis1v2-standard), [CIS AWS Foundations Benchmark v1.4.0](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html#cis1v4-standard), [CIS AWS Foundations Benchmark v3.0.0](https://docs.aws.amazon.com/securityhub/latest/userguide/cis-aws-foundations-benchmark.html#cis3v0-standard), [AWS Foundational Security Best Practices (FSBP) v.1.0.0](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html), [Payment Card Industry Data Security Standard (PCI-DSS) v3.2.1](https://docs.aws.amazon.com/securityhub/latest/userguide/pci-standard.html), and [National Institute of Standards and Technology (NIST)](https://docs.aws.amazon.com/securityhub/latest/userguide/nist-standard.html).

If you have consolidated control findings enabled, then those controls are supported in all standards. If this feature is enabled, then only the SC playbook needs to be deployed. If not, then the playbooks are supported for the previously listed standards.

**Important**
Only deploy the playbooks for the enabled standards to avoid reaching service quotas.

For details on a specific remediation, refer to the Systems Manager automation document with the name deployed by the solution in your account. Go to the [AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/), then in the navigation pane choose **Documents**.

| Description | AWS FSBP | CIS v1.2.0 | PCI v3.2.1 | CIS v1.4.0 | NIST | CIS v3.0.0 | Security control ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  **Total Remediations**  | 63 | 34 | 29 | 33 | 65 | 19 | 90 |
|  **ASR-EnableAutoScalingGroupELBHealthCheck** <br />Auto Scaling groups associated with a load balancer should use load balancer health checks | Autoscaling.1 |  | Autoscaling.1 |  | Autoscaling.1 |  | Autoscaling.1 |
|  **ASR-ConfigureAutoScalingLaunchConfigToRequireIMDSv2** <br />Auto Scaling group launch configurations should configure EC2 instances to require Instance Metadata Service Version 2 (IMDSv2) |  |  |  |  | Autoscaling.3 |  | Autoscaling.3 |
|  **ASR-CreateCloudTrailMultiRegionTrail** <br />CloudTrail should be activated and configured with at least one multi-Region trail | CloudTrail.1 | 2.1 | CloudTrail.2 | 3.1 | CloudTrail.1 | 3.1 | CloudTrail.1 |
|  **ASR-EnableEncryption** <br />CloudTrail should have encryption at rest activated | CloudTrail.2 | 2.7 | CloudTrail.1 | 3.7 | CloudTrail.2 | 3.5 | CloudTrail.2 |
|  **ASR-EnableLogFileValidation** <br />Ensure CloudTrail log file validation is activated | CloudTrail.4 | 2.2 | CloudTrail.3 | 3.2 | CloudTrail.4 |  | CloudTrail.4 |
|  **ASR-EnableCloudTrailToCloudWatchLogging** <br />Ensure CloudTrail trails are integrated with Amazon CloudWatch Logs | CloudTrail.5 | 2.4 | CloudTrail.4 | 3.4 | CloudTrail.5 |  | CloudTrail.5 |
|  **ASR-ConfigureS3BucketLogging** <br />Ensure S3 bucket access logging is enabled on the CloudTrail S3 bucket |  | 2.6 |  | 3.6 |  | 3.4 | CloudTrail.7 |
|  **ASR-ReplaceCodeBuildClearTextCredentials** <br />CodeBuild project environment variables should not contain clear text credentials | CodeBuild.2 |  | CodeBuild.2 |  | CodeBuild.2 |  | CodeBuild.2 |
|  **ASR-EnableAWSConfig** <br />Ensure AWS Config is activated | Config.1 | 2.5 | Config.1 | 3.5 | Config.1 | 3.3 | Config.1 |
|  **ASR-MakeEBSSnapshotsPrivate** <br />Amazon EBS snapshots should not be publicly restorable | EC2.1 |  | EC2.1 |  | EC2.1 |  | EC2.1 |
|  **ASR-RemoveVPCDefaultSecurityGroupRules** <br />VPC default security group should prohibit inbound and outbound traffic | EC2.2 | 4.3 | EC2.2 | 5.3 | EC2.2 | 5.4 | EC2.2 |
|  **ASR-EnableVPCFlowLogs** <br />VPC flow logging should be enabled in all VPCs | EC2.6 | 2.9 | EC2.6 | 3.9 | EC2.6 | 3.7 | EC2.6 |
|  **ASR-EnableEbsEncryptionByDefault** <br />EBS default encryption should be activated | EC2.7 | 2.2.1 |  |  | EC2.7 | 2.2.1 | EC2.7 |
|  **ASR-RevokeUnrotatedKeys** <br />Users' access keys should be rotated every 90 days or less | IAM.3 | 1.4 |  | 1.14 | IAM.3 | 1.14 | IAM.3 |
|  **ASR-SetIAMPasswordPolicy** <br />IAM default password policy | IAM.7 | 1.5-1.11 | IAM.8 | 1.8 | IAM.7 | 1.8 | IAM.7 |
|  **ASR-RevokeUnusedIAMUserCredentials** <br />User credentials should be turned off if not used within 90 days | IAM.8 | 1.3 | IAM.7 |  | IAM.8 |  | IAM.8 |
|  **ASR-RevokeUnusedIAMUserCredentials** <br />User credentials should be turned off if not used within 45 days |  |  |  | 1.12 |  | 1.12 | IAM.22 |
|  **ASR-RemoveLambdaPublicAccess** <br />Lambda functions should prohibit public access | Lambda.1 |  | Lambda.1 |  | Lambda.1 |  | Lambda.1 |
|  **ASR-MakeRDSSnapshotPrivate** <br />RDS snapshots should prohibit public access | RDS.1 |  | RDS.1 |  | RDS.1 |  | RDS.1 |
|  **ASR-DisablePublicAccessToRDSInstance** <br />RDS DB Instances should prohibit public access | RDS.2 |  | RDS.2 |  | RDS.2 | 2.3.3 | RDS.2 |
|  **ASR-EncryptRDSSnapshot** <br />RDS cluster snapshots and database snapshots should be encrypted at rest | RDS.4 |  |  |  | RDS.4 |  | RDS.4 |
|  **ASR-EnableMultiAZOnRDSInstance** <br />RDS DB instances should be configured with multiple Availability Zones | RDS.5 |  |  |  | RDS.5 |  | RDS.5 |
|  **ASR-EnableEnhancedMonitoringOnRDSInstance** <br />Enhanced monitoring should be configured for RDS DB instances and clusters | RDS.6 |  |  |  | RDS.6 |  | RDS.6 |
|  **ASR-EnableRDSClusterDeletionProtection** <br />RDS clusters should have deletion protection activated | RDS.7 |  |  |  | RDS.7 |  | RDS.7 |
|  **ASR-EnableRDSInstanceDeletionProtection** <br />RDS DB instances should have deletion protection activated | RDS.8 |  |  |  | RDS.8 |  | RDS.8 |
|  **ASR-EnableMinorVersionUpgradeOnRDSDBInstance** <br />RDS automatic minor version upgrades should be activated | RDS.13 |  |  |  | RDS.13 | 2.3.2 | RDS.13 |
|  **ASR-EnableCopyTagsToSnapshotOnRDSCluster** <br />RDS DB clusters should be configured to copy tags to snapshots | RDS.16 |  |  |  | RDS.16 |  | RDS.16 |
|  **ASR-DisablePublicAccessToRedshiftCluster** <br />Amazon Redshift clusters should prohibit public access | Redshift.1 |  | Redshift.1 |  | Redshift.1 |  | Redshift.1 |
|  **ASR-EnableAutomaticSnapshotsOnRedshiftCluster** <br />Amazon Redshift clusters should have automatic snapshots activated | Redshift.3 |  |  |  | Redshift.3 |  | Redshift.3 |
|  **ASR-EnableRedshiftClusterAuditLogging** <br />Amazon Redshift clusters should have audit logging activated | Redshift.4 |  |  |  | Redshift.4 |  | Redshift.4 |
|  **ASR-EnableAutomaticVersionUpgradeOnRedshiftCluster** <br />Amazon Redshift should have automatic upgrades to major versions activated | Redshift.6 |  |  |  | Redshift.6 |  | Redshift.6 |
|  **ASR-ConfigureS3PublicAccessBlock** <br />S3 Block Public Access setting should be activated | S3.1 | 2.3 | S3.6 | 2.1.5.1 | S3.1 | 2.1.4 | S3.1 |
|  **ASR-ConfigureS3BucketPublicAccessBlock** <br />S3 buckets should prohibit public read access | S3.2 |  | S3.2 | 2.1.5.2 | S3.2 |  | S3.2 |
|  **ASR-ConfigureS3BucketPublicAccessBlock** <br />S3 buckets should prohibit public write access |  | S3.3 |  |  |  |  | S3.3 |
|  **ASR-EnableDefaultEncryptionS3** <br />S3 buckets should have server-side encryption activated | S3.4 |  | S3.4 | 2.1.1 | S3.4 |  | S3.4 |
|  **ASR-SetSSLBucketPolicy** <br />S3 buckets should require requests to use SSL | S3.5 |  | S3.5 | 2.1.2 | S3.5 | 2.1.1 | S3.5 |
|  **ASR-S3BlockDenylist** <br />Amazon S3 permissions granted to other AWS accounts in bucket policies should be restricted | S3.6 |  |  |  | S3.6 |  | S3.6 |
| S3 Block Public Access setting should be activated at the bucket level | S3.8 |  |  |  | S3.8 |  | S3.8 |
|  **ASR-ConfigureS3BucketPublicAccessBlock** <br />Ensure the S3 bucket CloudTrail logs to is not publicly accessible |  | 2.3 |  |  |  |  | CloudTrail.6 |
|  **ASR-CreateAccessLoggingBucket** <br />Ensure S3 bucket access logging is activated on the CloudTrail S3 bucket |  | 2.6 |  |  |  |  | CloudTrail.7 |
|  **ASR-EnableKeyRotation** <br />Ensure rotation for customer-created CMKs is activated |  | 2.8 | KMS.1 | 3.8 | KMS.4 | 3.6 | KMS.4 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for unauthorized API calls |  | 3.1 |  | 4.1 |  |  | Cloudwatch.1 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for AWS Management Console sign-in without MFA |  | 3.2 |  | 4.2 |  |  | Cloudwatch.2 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for usage of the "root" user |  | 3.3 | CW.1 | 4.3 |  |  | Cloudwatch.3 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for IAM policy changes |  | 3.4 |  | 4.4 |  |  | Cloudwatch.4 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for CloudTrail configuration changes |  | 3.5 |  | 4.5 |  |  | Cloudwatch.5 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for AWS Management Console authentication failures |  | 3.6 |  | 4.6 |  |  | Cloudwatch.6 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for disabling or scheduled deletion of customer created CMKs |  | 3.7 |  | 4.7 |  |  | Cloudwatch.7 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for S3 bucket policy changes |  | 3.8 |  | 4.8 |  |  | Cloudwatch.8 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for AWS Config configuration changes |  | 3.9 |  | 4.9 |  |  | Cloudwatch.9 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for security group changes |  | 3.10 |  | 4.10 |  |  | Cloudwatch.10 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for changes to Network Access Control Lists (NACL) |  | 3.11 |  | 4.11 |  |  | Cloudwatch.11 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for changes to network gateways |  | 3.12 |  | 4.12 |  |  | Cloudwatch.12 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for route table changes |  | 3.13 |  | 4.13 |  |  | Cloudwatch.13 |
|  **ASR-CreateLogMetricFilterAndAlarm** <br />Ensure a log metric filter and alarm exist for VPC changes |  | 3.14 |  | 4.14 |  |  | Cloudwatch.14 |
|  **AWS-DisablePublicAccessForSecurityGroup** <br />Ensure no security groups allow ingress from 0.0.0.0/0 to port 22 |  | 4.1 | EC2.5 |  | EC2.13 |  | EC2.13 |
|  **AWS-DisablePublicAccessForSecurityGroup** <br />Ensure no security groups allow ingress from 0.0.0.0/0 to port 3389 |  | 4.2 |  |  | EC2.14 |  | EC2.14 |
|  **ASR-ConfigureSNSTopicForStack**  | CloudFormation.1 |  |  |  | CloudFormation.1 |  | CloudFormation.1 |
|  **ASR-CreateIAMSupportRole**  |  | 1.20 |  | 1.17 |  | 1.17 | IAM.18 |
|  **ASR-DisablePublicIPAutoAssign** <br />Amazon EC2 subnets should not automatically assign public IP addresses | EC2.15 |  |  |  | EC2.15 |  | EC2.15 |
|  **ASR-EnableCloudTrailLogFileValidation**  | CloudTrail.4 | 2.2 | CloudTrail.3 | 3.2 |  |  | CloudTrail.4 |
|  **ASR-EnableEncryptionForSNSTopic**  | SNS.1 |  |  |  | SNS.1 |  | SNS.1 |
|  **ASR-EnableDeliveryStatusLoggingForSNSTopic** <br />Logging of delivery status should be enabled for notification messages sent to a topic | SNS.2 |  |  |  | SNS.2 |  | SNS.2 |
|  **ASR-EnableEncryptionForSQSQueue**  | SQS.1 |  |  |  | SQS.1 |  | SQS.1 |
|  **ASR-MakeRDSSnapshotPrivate** RDS snapshot should be private | RDS.1 |  | RDS.1 |  |  |  | RDS.1 |
|  **ASR-BlockSSMDocumentPublicAccess** <br />SSM Documents should not be public | SSM.4 |  |  |  | SSM.4 |  | SSM.4 |
|  **ASR-EnableCloudFrontDefaultRootObject** <br />CloudFront distributions should have a default root object configured | CloudFront.1 |  |  |  | CloudFront.1 |  | CloudFront.1 |
|  **ASR-SetCloudFrontOriginDomain** <br />CloudFront distributions should not point to non-existent S3 origins | CloudFront.12 |  |  |  | CloudFront.12 |  | CloudFront.12 |
|  **ASR-RemoveCodeBuildPrivilegedMode** <br />CodeBuild project environments should have a logging AWS Configuration | CodeBuild.5 |  |  |  | CodeBuild.5 |  | CodeBuild.5 |
|  **ASR-TerminateEC2Instance** <br />Stopped EC2 instances should be removed after a specified time period | EC2.4 |  |  |  | EC2.4 |  | EC2.4 |
|  **ASR-EnableIMDSV2OnInstance** <br />EC2 instances should use Instance Metadata Service Version 2 (IMDSv2) | EC2.8 |  |  |  | EC2.8 | 5.6 | EC2.8 |
|  **ASR-RevokeUnauthorizedInboudRules** <br />Security groups should only allow unrestricted incoming traffic for authorized ports | EC2.18 |  |  |  | EC2.18 |  | EC2.18 |
| INSERT TITLE HERE<br />Security groups should not allow unrestricted access to ports with high risk | EC2.19 |  |  |  | EC2.19 |  | EC2.19 |
|  **ASR-DisableTGWAutoAcceptSharedAttachments** <br />Amazon EC2 Transit Gateways should not automatically accept VPC attachment requests | EC2.23 |  |  |  | EC2.23 |  | EC2.23 |
|  **ASR-EnablePrivateRepositoryScanning** <br />ECR private repositories should have image scanning configured | ECR.1 |  |  |  | ECR.1 |  | ECR.1 |
|  **ASR-EnableGuardDuty** <br />GuardDuty should be enabled | GuardDuty.1 |  | GuardDuty.1 |  | GuardDuty.1 |  | GuardDuty.1 |
|  **ASR-ConfigureS3BucketLogging** <br />S3 bucket server access logging should be enabled | S3.9 |  |  |  | S3.9 |  | S3.9 |
|  **ASR-EnableBucketEventNotifications** <br />S3 buckets should have event notifications enabled | S3.11 |  |  |  | S3.11 |  | S3.11 |
|  **ASR-SetS3LifecyclePolicy** <br />S3 buckets should have lifecycle policies configured | S3.13 |  |  |  | S3.13 |  | S3.13 |
|  **ASR-EnableAutoSecretRotation** <br />Secrets Manager secrets should have automatic rotation enabled | SecretsManager.1 |  |  |  | SecretsManager.1 |  | SecretsManager.1 |
|  **ASR-RemoveUnusedSecret** <br />Remove unused Secrets Manager secrets | SecretsManager.3 |  |  |  | SecretsManager.3 |  | SecretsManager.3 |
|  **ASR-UpdateSecretRotationPeriod** <br />Secrets Manager secrets should be rotated within a specified number of days | SecretsManager.4 |  |  |  | SecretsManager.4 |  | SecretsManager.4 |
|  **ASR-EnableAPIGatewayCacheDataEncryption** <br />API Gateway REST API cache data should be encrypted at rest |  |  |  |  | APIGateway.5 |  | APIGateway.5 |
|  **ASR-SetLogGroupRetentionDays** <br />CloudWatch log groups should be retained for a specified time period |  |  |  |  | CloudWatch.16 |  | CloudWatch.16 |
|  **ASR-AttachServiceVPCEndpoint** <br />Amazon EC2 should be configured to use VPC endpoints that are created for the Amazon EC2 service | EC2.10 |  |  |  | EC2.10 |  | EC2.10 |
|  **ASR-TagGuardDutyResource** <br />GuardDuty filters should be tagged |  |  |  |  |  |  | GuardDuty.2 |
|  **ASR-TagGuardDutyResource** <br />GuardDuty detectors should be tagged |  |  |  |  |  |  | GuardDuty.4 |
|  **ASR-AttachSSMPermissionsToEC2** <br />Amazon EC2 instances should be managed by Systems Manager | SSM.1 |  | SSM.3 |  |  |  | SSM.1 |
|  **ASR-ConfigureLaunchConfigNoPublicIPDocument** <br />Amazon EC2 instances launched using Auto Scaling group launch configurations should not have public IP addresses |  |  |  |  | Autoscaling.5 |  | Autoscaling.5 |
|  **ASR-EnableAPIGatewayExecutionLogs**  | APIGateway.1 |  |  |  |  |  | APIGateway.1 |
|  **ASR-EnableMacie** <br />Amazon Macie should be enabled | Macie.1 |  |  |  | Macie.1 |  | Macie.1 |
|  **ASR-EnableAthenaWorkGroupLogging** <br />Athena workgroups should have logging enabled | Athena.4 |  |  |  |  |  | Athena.4 |
|  **ASR-EnforceHTTPSForALB** <br />Application Load Balancer should be configured to redirect all HTTP requests to HTTPS | ELB.1 |  | ELB.1 |  | ELB.1 |  | ELB.1 |
|  **ASR-LimitECSRootFilesystemAccess** <br />ECS containers should be limited to read-only access to root filesystems | ECS.5 |  |  |  | ECS.5 |  | ECS.5 |
|  **ASR-EnableElastiCacheBackups** <br />ElastiCache (Redis OSS) clusters should have automatic backups enabled | ElastiCache.1 |  |  |  | ElastiCache.1 |  | ElastiCache.1 |
|  **ASR-EnableElastiCacheVersionUpgrades** <br />ElastiCache clusters should have automatic minor version upgrades enabled | ElastiCache.2 |  |  |  | ElastiCache.2 |  | ElastiCache.2 |
|  **ASR-EnableElastiCacheReplicationGroupFailover** <br />ElastiCache replication groups should have automatic failover enabled | ElastiCache.3 |  |  |  | ElastiCache.3 |  | ElastiCache.3 |
|  **ASR-ConfigureDynamoDBAutoScaling** <br />DynamoDB tables should automatically scale capacity with demand | DynamoDB.1 |  |  |  | DynamoDB.1 |  | DynamoDB.1 |
|  **ASR-TagDynamoDBTableResource** <br />DynamoDB tables should be tagged |  |  |  |  |  |  | DynamoDB.5 |
|  **ASR-EnableDynamoDBDeletionProtection** <br />DynamoDB tables should have deletion protection enabled |  |  |  |  | DynamoDB.6 |  | DynamoDB.6 |

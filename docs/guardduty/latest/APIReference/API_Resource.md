---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

Contains information about the AWS resource associated with the activity that prompted GuardDuty to generate a finding.

## Contents
<a name="API_Resource_Contents"></a>

 ** accessKeyDetails **   <a name="guardduty-Type-Resource-accessKeyDetails"></a>
The IAM access key details (user information) of a user that engaged in the activity that prompted GuardDuty to generate a finding.
Type: [AccessKeyDetails](API_AccessKeyDetails.md) object
Required: No

 ** bedrockGuardrailDetails **   <a name="guardduty-Type-Resource-bedrockGuardrailDetails"></a>
Contains information about the Bedrock guardrail that was involved in a finding.
Type: [BedrockGuardrailDetails](API_BedrockGuardrailDetails.md) object
Required: No

 ** containerDetails **   <a name="guardduty-Type-Resource-containerDetails"></a>
Details of a container.
Type: [Container](API_Container.md) object
Required: No

 ** ebsSnapshotDetails **   <a name="guardduty-Type-Resource-ebsSnapshotDetails"></a>
Contains details about the EBS snapshot that was scanned.
Type: [EbsSnapshotDetails](API_EbsSnapshotDetails.md) object
Required: No

 ** ebsVolumeDetails **   <a name="guardduty-Type-Resource-ebsVolumeDetails"></a>
Contains list of scanned and skipped EBS volumes with details.
Type: [EbsVolumeDetails](API_EbsVolumeDetails.md) object
Required: No

 ** ec2ImageDetails **   <a name="guardduty-Type-Resource-ec2ImageDetails"></a>
Contains details about the EC2 image that was scanned.
Type: [Ec2ImageDetails](API_Ec2ImageDetails.md) object
Required: No

 ** ecsClusterDetails **   <a name="guardduty-Type-Resource-ecsClusterDetails"></a>
Contains information about the details of the ECS Cluster.
Type: [EcsClusterDetails](API_EcsClusterDetails.md) object
Required: No

 ** eksClusterDetails **   <a name="guardduty-Type-Resource-eksClusterDetails"></a>
Details about the EKS cluster involved in a Kubernetes finding.
Type: [EksClusterDetails](API_EksClusterDetails.md) object
Required: No

 ** instanceDetails **   <a name="guardduty-Type-Resource-instanceDetails"></a>
The information about the EC2 instance associated with the activity that prompted GuardDuty to generate a finding.
Type: [InstanceDetails](API_InstanceDetails.md) object
Required: No

 ** kubernetesDetails **   <a name="guardduty-Type-Resource-kubernetesDetails"></a>
Details about the Kubernetes user and workload involved in a Kubernetes finding.
Type: [KubernetesDetails](API_KubernetesDetails.md) object
Required: No

 ** lambdaDetails **   <a name="guardduty-Type-Resource-lambdaDetails"></a>
Contains information about the Lambda function that was involved in a finding.
Type: [LambdaDetails](API_LambdaDetails.md) object
Required: No

 ** modelDetails **   <a name="guardduty-Type-Resource-modelDetails"></a>
Contains information about the AI models involved in a finding.
Type: Array of [ModelDetail](API_ModelDetail.md) objects
Required: No

 ** rdsDbInstanceDetails **   <a name="guardduty-Type-Resource-rdsDbInstanceDetails"></a>
Contains information about the database instance to which an anomalous login attempt was made.
Type: [RdsDbInstanceDetails](API_RdsDbInstanceDetails.md) object
Required: No

 ** rdsDbUserDetails **   <a name="guardduty-Type-Resource-rdsDbUserDetails"></a>
Contains information about the user details through which anomalous login attempt was made.
Type: [RdsDbUserDetails](API_RdsDbUserDetails.md) object
Required: No

 ** rdsLimitlessDbDetails **   <a name="guardduty-Type-Resource-rdsLimitlessDbDetails"></a>
Contains information about the RDS Limitless database that was involved in a GuardDuty finding.
Type: [RdsLimitlessDbDetails](API_RdsLimitlessDbDetails.md) object
Required: No

 ** recoveryPointDetails **   <a name="guardduty-Type-Resource-recoveryPointDetails"></a>
Contains details about the backup recovery point that was scanned.
Type: [RecoveryPointDetails](API_RecoveryPointDetails.md) object
Required: No

 ** resourceType **   <a name="guardduty-Type-Resource-resourceType"></a>
The type of AWS resource.
Type: String
Required: No

 ** s3BucketDetails **   <a name="guardduty-Type-Resource-s3BucketDetails"></a>
Contains information on the S3 bucket.
Type: Array of [S3BucketDetail](API_S3BucketDetail.md) objects
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

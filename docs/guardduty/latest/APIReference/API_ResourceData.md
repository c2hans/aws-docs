---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ResourceData.html
---

# ResourceData
<a name="API_ResourceData"></a>

Contains information about the AWS resource that is associated with the activity that prompted GuardDuty to generate a finding.

## Contents
<a name="API_ResourceData_Contents"></a>

 ** accessKey **   <a name="guardduty-Type-ResourceData-accessKey"></a>
Contains information about the IAM access key details of a user that involved in the GuardDuty finding.
Type: [AccessKey](API_AccessKey.md) object
Required: No

 ** autoscalingAutoScalingGroup **   <a name="guardduty-Type-ResourceData-autoscalingAutoScalingGroup"></a>
Contains detailed information about the Auto Scaling Group associated with the activity that prompted GuardDuty to generate a finding.
Type: [AutoscalingAutoScalingGroup](API_AutoscalingAutoScalingGroup.md) object
Required: No

 ** cloudformationStack **   <a name="guardduty-Type-ResourceData-cloudformationStack"></a>
Contains detailed information about the CloudFormation stack associated with the activity that prompted GuardDuty to generate a finding.
Type: [CloudformationStack](API_CloudformationStack.md) object
Required: No

 ** container **   <a name="guardduty-Type-ResourceData-container"></a>
Contains detailed information about the container associated with the activity that prompted GuardDuty to generate a finding.
Type: [ContainerFindingResource](API_ContainerFindingResource.md) object
Required: No

 ** ec2Image **   <a name="guardduty-Type-ResourceData-ec2Image"></a>
Contains detailed information about the EC2 Image associated with the activity that prompted GuardDuty to generate a finding.
Type: [Ec2Image](API_Ec2Image.md) object
Required: No

 ** ec2Instance **   <a name="guardduty-Type-ResourceData-ec2Instance"></a>
Contains information about the Amazon EC2 instance.
Type: [Ec2Instance](API_Ec2Instance.md) object
Required: No

 ** ec2LaunchTemplate **   <a name="guardduty-Type-ResourceData-ec2LaunchTemplate"></a>
Contains detailed information about the EC2 launch template associated with the activity that prompted GuardDuty to generate a finding.
Type: [Ec2LaunchTemplate](API_Ec2LaunchTemplate.md) object
Required: No

 ** ec2NetworkInterface **   <a name="guardduty-Type-ResourceData-ec2NetworkInterface"></a>
Contains information about the elastic network interface of the Amazon EC2 instance.
Type: [Ec2NetworkInterface](API_Ec2NetworkInterface.md) object
Required: No

 ** ec2Vpc **   <a name="guardduty-Type-ResourceData-ec2Vpc"></a>
Contains detailed information about the EC2 VPC associated with the activity that prompted GuardDuty to generate a finding.
Type: [Ec2Vpc](API_Ec2Vpc.md) object
Required: No

 ** ecsCluster **   <a name="guardduty-Type-ResourceData-ecsCluster"></a>
Contains detailed information about the Amazon ECS cluster associated with the activity that prompted GuardDuty to generate a finding.
Type: [EcsCluster](API_EcsCluster.md) object
Required: No

 ** ecsTask **   <a name="guardduty-Type-ResourceData-ecsTask"></a>
Contains detailed information about the Amazon ECS task associated with the activity that prompted GuardDuty to generate a finding.
Type: [EcsTask](API_EcsTask.md) object
Required: No

 ** eksCluster **   <a name="guardduty-Type-ResourceData-eksCluster"></a>
Contains detailed information about the Amazon EKS cluster associated with the activity that prompted GuardDuty to generate a finding.
Type: [EksCluster](API_EksCluster.md) object
Required: No

 ** iamInstanceProfile **   <a name="guardduty-Type-ResourceData-iamInstanceProfile"></a>
Contains detailed information about the IAM instance profile associated with the activity that prompted GuardDuty to generate a finding.
Type: [IamInstanceProfileV2](API_IamInstanceProfileV2.md) object
Required: No

 ** kubernetesWorkload **   <a name="guardduty-Type-ResourceData-kubernetesWorkload"></a>
Contains detailed information about the Kubernetes workload associated with the activity that prompted GuardDuty to generate a finding.
Type: [KubernetesWorkload](API_KubernetesWorkload.md) object
Required: No

 ** s3Bucket **   <a name="guardduty-Type-ResourceData-s3Bucket"></a>
Contains information about the Amazon S3 bucket.
Type: [S3Bucket](API_S3Bucket.md) object
Required: No

 ** s3Object **   <a name="guardduty-Type-ResourceData-s3Object"></a>
Contains information about the Amazon S3 object.
Type: [S3Object](API_S3Object.md) object
Required: No

## See Also
<a name="API_ResourceData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ResourceData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ResourceData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ResourceData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

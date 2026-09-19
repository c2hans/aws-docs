---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ResourceV2.html
---

# ResourceV2
<a name="API_ResourceV2"></a>

Contains information about the AWS resource that is associated with the GuardDuty finding.

## Contents
<a name="API_ResourceV2_Contents"></a>

 ** resourceType **   <a name="guardduty-Type-ResourceV2-resourceType"></a>
The type of the AWS resource.
Type: String
Valid Values: `EC2_INSTANCE | EC2_NETWORK_INTERFACE | S3_BUCKET | S3_OBJECT | ACCESS_KEY | EKS_CLUSTER | KUBERNETES_WORKLOAD | CONTAINER | ECS_CLUSTER | ECS_TASK | AUTOSCALING_AUTO_SCALING_GROUP | IAM_INSTANCE_PROFILE | CLOUDFORMATION_STACK | EC2_LAUNCH_TEMPLATE | EC2_VPC | EC2_IMAGE | BEDROCK_CUSTOM_MODEL | BEDROCK_IMPORTED_MODEL | BEDROCK_PROVISIONED_MODEL | BEDROCK_CUSTOM_MODEL_DEPLOYMENT | BEDROCK_INFERENCE_PROFILE | BEDROCK_APPLICATION_INFERENCE_PROFILE | BEDROCK_PROMPT | BEDROCK_PROMPT_ROUTER | BEDROCK_GUARDRAIL | SAGEMAKER_ENDPOINT`
Required: Yes

 ** uid **   <a name="guardduty-Type-ResourceV2-uid"></a>
The unique identifier of the resource.
Type: String
Required: Yes

 ** accountId **   <a name="guardduty-Type-ResourceV2-accountId"></a>
The AWS account ID to which the resource belongs.
Type: String
Required: No

 ** cloudPartition **   <a name="guardduty-Type-ResourceV2-cloudPartition"></a>
The cloud partition within the AWS Region to which the resource belongs.
Type: String
Required: No

 ** data **   <a name="guardduty-Type-ResourceV2-data"></a>
Contains information about the AWS resource associated with the activity that prompted GuardDuty to generate a finding.
Type: [ResourceData](API_ResourceData.md) object
Required: No

 ** name **   <a name="guardduty-Type-ResourceV2-name"></a>
The name of the resource.
Type: String
Required: No

 ** region **   <a name="guardduty-Type-ResourceV2-region"></a>
The AWS Region where the resource belongs.
Type: String
Required: No

 ** service **   <a name="guardduty-Type-ResourceV2-service"></a>
The AWS service of the resource.
Type: String
Required: No

 ** tags **   <a name="guardduty-Type-ResourceV2-tags"></a>
Contains information about the tags associated with the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ResourceV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ResourceV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ResourceV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ResourceV2)

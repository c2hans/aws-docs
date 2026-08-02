---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DebugRuleConfiguration.html
---

# DebugRuleConfiguration
<a name="API_DebugRuleConfiguration"></a>

Configuration information for SageMaker Debugger rules for debugging. To learn more about how to configure the `DebugRuleConfiguration` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).

## Contents
<a name="API_DebugRuleConfiguration_Contents"></a>

 ** RuleConfigurationName **   <a name="sagemaker-Type-DebugRuleConfiguration-RuleConfigurationName"></a>
The name of the rule configuration. It must be unique relative to other rule configuration names.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** RuleEvaluatorImage **   <a name="sagemaker-Type-DebugRuleConfiguration-RuleEvaluatorImage"></a>
The Amazon Elastic Container (ECR) Image for the managed rule evaluation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** InstanceType **   <a name="sagemaker-Type-DebugRuleConfiguration-InstanceType"></a>
The instance type to deploy a custom rule for debugging a training job.
Type: String
Valid Values: `ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.r5d.large | ml.r5d.xlarge | ml.r5d.2xlarge | ml.r5d.4xlarge | ml.r5d.8xlarge | ml.r5d.12xlarge | ml.r5d.16xlarge | ml.r5d.24xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.p5.4xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge`
Required: No

 ** LocalPath **   <a name="sagemaker-Type-DebugRuleConfiguration-LocalPath"></a>
Path to local storage location for output of rules. Defaults to `/opt/ml/processing/output/rule/`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `.*`
Required: No

 ** RuleParameters **   <a name="sagemaker-Type-DebugRuleConfiguration-RuleParameters"></a>
Runtime configuration for rule container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

 ** S3OutputPath **   <a name="sagemaker-Type-DebugRuleConfiguration-S3OutputPath"></a>
Path to Amazon S3 storage location for rules.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** VolumeSizeInGB **   <a name="sagemaker-Type-DebugRuleConfiguration-VolumeSizeInGB"></a>
The size, in GB, of the ML storage volume attached to the processing instance.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_DebugRuleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DebugRuleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DebugRuleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DebugRuleConfiguration)

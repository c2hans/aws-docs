---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_InstanceConfig.html
---

# InstanceConfig
<a name="API_InstanceConfig"></a>

Configures the resource instances to use while running the Amazon Braket hybrid job on Amazon Braket.

## Contents
<a name="API_InstanceConfig_Contents"></a>

 ** instanceType **   <a name="braket-Type-InstanceConfig-instanceType"></a>
Configures the type of resource instances to use while running an Amazon Braket hybrid job.
Type: String
Valid Values: `ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5n.xlarge | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.p4d.24xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge`
Required: Yes

 ** volumeSizeInGb **   <a name="braket-Type-InstanceConfig-volumeSizeInGb"></a>
The size of the storage volume, in GB, to provision.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** instanceCount **   <a name="braket-Type-InstanceConfig-instanceCount"></a>
Configures the number of resource instances to use while running an Amazon Braket hybrid job on Amazon Braket. The default value is 1.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_InstanceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/InstanceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/InstanceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/InstanceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

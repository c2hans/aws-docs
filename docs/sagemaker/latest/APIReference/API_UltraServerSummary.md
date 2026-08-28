---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UltraServerSummary.html
---

# UltraServerSummary
<a name="API_UltraServerSummary"></a>

A summary of UltraServer resources and their current status.

## Contents
<a name="API_UltraServerSummary_Contents"></a>

 ** InstanceType **   <a name="sagemaker-Type-UltraServerSummary-InstanceType"></a>
The Amazon EC2 instance type used in the UltraServer.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.trn1.32xlarge | ml.trn2.48xlarge | ml.p6-b200.48xlarge | ml.p4de.24xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge`
Required: Yes

 ** UltraServerType **   <a name="sagemaker-Type-UltraServerSummary-UltraServerType"></a>
The type of UltraServer, such as ml.u-p6e-gb200x72.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ml.[a-z0-9\-.]+`
Required: Yes

 ** AvailableSpareInstanceCount **   <a name="sagemaker-Type-UltraServerSummary-AvailableSpareInstanceCount"></a>
The number of available spare instances in the UltraServers.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** UltraServerCount **   <a name="sagemaker-Type-UltraServerSummary-UltraServerCount"></a>
The number of UltraServers of this type.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** UnhealthyInstanceCount **   <a name="sagemaker-Type-UltraServerSummary-UnhealthyInstanceCount"></a>
The total number of instances across all UltraServers of this type that are currently in an unhealthy state.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_UltraServerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UltraServerSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UltraServerSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UltraServerSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

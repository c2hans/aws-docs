---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InstanceGroupHealthCheckConfiguration.html
---

# InstanceGroupHealthCheckConfiguration
<a name="API_InstanceGroupHealthCheckConfiguration"></a>

The configuration of deep health checks for an instance group.

**Note**
Overlapping deep health check configurations will be merged into a single operation.

## Contents
<a name="API_InstanceGroupHealthCheckConfiguration_Contents"></a>

 ** DeepHealthChecks **   <a name="sagemaker-Type-InstanceGroupHealthCheckConfiguration-DeepHealthChecks"></a>
A list of deep health checks to be performed.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `InstanceStress | InstanceConnectivity`
Required: Yes

 ** InstanceGroupName **   <a name="sagemaker-Type-InstanceGroupHealthCheckConfiguration-InstanceGroupName"></a>
The name of the instance group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`
Required: Yes

 ** InstanceIds **   <a name="sagemaker-Type-InstanceGroupHealthCheckConfiguration-InstanceIds"></a>
A list of Amazon Elastic Compute Cloud (EC2) instance IDs on which to perform deep health checks.
Leave this field blank to perform deep health checks on the entire instance group.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `i-[a-f0-9]{8}(?:[a-f0-9]{9})?`
Required: No

## See Also
<a name="API_InstanceGroupHealthCheckConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InstanceGroupHealthCheckConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InstanceGroupHealthCheckConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InstanceGroupHealthCheckConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterInstancePlacement.html
---

# ClusterInstancePlacement
<a name="API_ClusterInstancePlacement"></a>

Specifies the placement details for the node in the SageMaker HyperPod cluster, including the Availability Zone and the unique identifier (ID) of the Availability Zone.

## Contents
<a name="API_ClusterInstancePlacement_Contents"></a>

 ** AvailabilityZone **   <a name="sagemaker-Type-ClusterInstancePlacement-AvailabilityZone"></a>
The Availability Zone where the node in the SageMaker HyperPod cluster is launched.
Type: String
Pattern: `[a-z]{2}-[a-z]+-\d[a-z]`
Required: No

 ** AvailabilityZoneId **   <a name="sagemaker-Type-ClusterInstancePlacement-AvailabilityZoneId"></a>
The unique identifier (ID) of the Availability Zone where the node in the SageMaker HyperPod cluster is launched.
Type: String
Pattern: `[a-z]{3}\d-az\d`
Required: No

## See Also
<a name="API_ClusterInstancePlacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterInstancePlacement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterInstancePlacement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterInstancePlacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

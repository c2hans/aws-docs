---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EventMetadata.html
---

# EventMetadata
<a name="API_EventMetadata"></a>

Metadata associated with a cluster event, which may include details about various resource types.

## Contents
<a name="API_EventMetadata_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Cluster **   <a name="sagemaker-Type-EventMetadata-Cluster"></a>
Metadata specific to cluster-level events.
Type: [ClusterMetadata](API_ClusterMetadata.md) object
Required: No

 ** Instance **   <a name="sagemaker-Type-EventMetadata-Instance"></a>
Metadata specific to instance-level events.
Type: [InstanceMetadata](API_InstanceMetadata.md) object
Required: No

 ** InstanceGroup **   <a name="sagemaker-Type-EventMetadata-InstanceGroup"></a>
Metadata specific to instance group-level events.
Type: [InstanceGroupMetadata](API_InstanceGroupMetadata.md) object
Required: No

 ** InstanceGroupScaling **   <a name="sagemaker-Type-EventMetadata-InstanceGroupScaling"></a>
Metadata related to instance group scaling events.
Type: [InstanceGroupScalingMetadata](API_InstanceGroupScalingMetadata.md) object
Required: No

## See Also
<a name="API_EventMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EventMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EventMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EventMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

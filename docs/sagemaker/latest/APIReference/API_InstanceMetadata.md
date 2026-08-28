---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InstanceMetadata.html
---

# InstanceMetadata
<a name="API_InstanceMetadata"></a>

Metadata information about an instance in a HyperPod cluster.

## Contents
<a name="API_InstanceMetadata_Contents"></a>

 ** AdditionalEnis **   <a name="sagemaker-Type-InstanceMetadata-AdditionalEnis"></a>
Information about additional Elastic Network Interfaces (ENIs) associated with the instance.
Type: [AdditionalEnis](API_AdditionalEnis.md) object
Required: No

 ** CapacityReservation **   <a name="sagemaker-Type-InstanceMetadata-CapacityReservation"></a>
Information about the Capacity Reservation used by the instance.
Type: [CapacityReservation](API_CapacityReservation.md) object
Required: No

 ** CustomerEni **   <a name="sagemaker-Type-InstanceMetadata-CustomerEni"></a>
The ID of the customer-managed Elastic Network Interface (ENI) associated with the instance.
Type: String
Required: No

 ** FailureMessage **   <a name="sagemaker-Type-InstanceMetadata-FailureMessage"></a>
An error message describing why the instance creation or update failed, if applicable.
Type: String
Required: No

 ** InstanceRequirementsEniConfigurations **   <a name="sagemaker-Type-InstanceMetadata-InstanceRequirementsEniConfigurations"></a>
The ENI configurations for the instance types in the instance requirements, grouped by network interface category (for example, ENI-only or EFA with ENIs). At most one configuration per category.
Type: Array of [InstanceRequirementsEniConfiguration](API_InstanceRequirementsEniConfiguration.md) objects
Required: No

 ** LcsExecutionState **   <a name="sagemaker-Type-InstanceMetadata-LcsExecutionState"></a>
The execution state of the Lifecycle Script (LCS) for the instance.
Type: String
Required: No

 ** NodeLogicalId **   <a name="sagemaker-Type-InstanceMetadata-NodeLogicalId"></a>
The unique logical identifier of the node within the cluster. The ID used here is the same object as in the `BatchAddClusterNodes` API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]`
Required: No

## See Also
<a name="API_InstanceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InstanceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InstanceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InstanceMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

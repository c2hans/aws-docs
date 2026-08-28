---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails"></a>

A resource to assign to a container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails_Contents"></a>

 ** Type **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails-Type"></a>
The type of resource to assign to a container. Valid values are `GPU` or `InferenceAccelerator`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Value **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails-Value"></a>
The value for the specified resource type.
For `GPU`, the value is the number of physical GPUs the Amazon ECS container agent reserves for the container.
For `InferenceAccelerator`, the value should match the `DeviceName` attribute of an entry in `InferenceAccelerators`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

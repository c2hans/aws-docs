---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FindingTypeAggregation.html
---

# FindingTypeAggregation
<a name="API_FindingTypeAggregation"></a>

The details that define an aggregation based on finding type.

## Contents
<a name="API_FindingTypeAggregation_Contents"></a>

 ** findingType **   <a name="inspector2-Type-FindingTypeAggregation-findingType"></a>
The finding type to aggregate.
Type: String
Valid Values: `NETWORK_REACHABILITY | PACKAGE_VULNERABILITY | CODE_VULNERABILITY`
Required: No

 ** resourceType **   <a name="inspector2-Type-FindingTypeAggregation-resourceType"></a>
The resource type to aggregate.
Type: String
Valid Values: `AWS_EC2_INSTANCE | AWS_ECR_CONTAINER_IMAGE | AWS_LAMBDA_FUNCTION | CODE_REPOSITORY | Microsoft.Compute/virtualMachines | Microsoft.ContainerRegistry/registry/containerImage | Microsoft.Web/sites`
Required: No

 ** sortBy **   <a name="inspector2-Type-FindingTypeAggregation-sortBy"></a>
The value to sort results by.
Type: String
Valid Values: `CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-FindingTypeAggregation-sortOrder"></a>
The order to sort results by.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_FindingTypeAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FindingTypeAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FindingTypeAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FindingTypeAggregation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

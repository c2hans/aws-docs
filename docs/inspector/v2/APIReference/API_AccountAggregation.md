---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AccountAggregation.html
---

# AccountAggregation
<a name="API_AccountAggregation"></a>

An object that contains details about an aggregation response based on AWS accounts.

## Contents
<a name="API_AccountAggregation_Contents"></a>

 ** findingType **   <a name="inspector2-Type-AccountAggregation-findingType"></a>
The type of finding.
Type: String
Valid Values: `NETWORK_REACHABILITY | PACKAGE_VULNERABILITY | CODE_VULNERABILITY`
Required: No

 ** resourceType **   <a name="inspector2-Type-AccountAggregation-resourceType"></a>
The type of resource.
Type: String
Valid Values: `AWS_EC2_INSTANCE | AWS_ECR_CONTAINER_IMAGE | AWS_LAMBDA_FUNCTION | CODE_REPOSITORY | Microsoft.Compute/virtualMachines | Microsoft.ContainerRegistry/registry/containerImage | Microsoft.Web/sites`
Required: No

 ** sortBy **   <a name="inspector2-Type-AccountAggregation-sortBy"></a>
The value to sort by.
Type: String
Valid Values: `CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-AccountAggregation-sortOrder"></a>
The sort order (ascending or descending).
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_AccountAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AccountAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AccountAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AccountAggregation)

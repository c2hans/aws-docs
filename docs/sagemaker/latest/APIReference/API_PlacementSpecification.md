---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PlacementSpecification.html
---

# PlacementSpecification
<a name="API_PlacementSpecification"></a>

Specifies how instances should be placed on a specific UltraServer.

## Contents
<a name="API_PlacementSpecification_Contents"></a>

 ** InstanceCount **   <a name="sagemaker-Type-PlacementSpecification-InstanceCount"></a>
The number of ML compute instances required to be placed together on the same UltraServer. Minimum value of 1.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** UltraServerId **   <a name="sagemaker-Type-PlacementSpecification-UltraServerId"></a>
The unique identifier of the UltraServer where instances should be placed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_PlacementSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PlacementSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PlacementSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PlacementSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

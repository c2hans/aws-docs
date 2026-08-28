---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Stairs.html
---

# Stairs
<a name="API_Stairs"></a>

Defines the stairs traffic pattern for an Inference Recommender load test. This pattern type consists of multiple steps where the number of users increases at each step.

Specify either the stairs or phases traffic pattern.

## Contents
<a name="API_Stairs_Contents"></a>

 ** DurationInSeconds **   <a name="sagemaker-Type-Stairs-DurationInSeconds"></a>
Defines how long each traffic step should be.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** NumberOfSteps **   <a name="sagemaker-Type-Stairs-NumberOfSteps"></a>
Specifies how many steps to perform during traffic.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** UsersPerStep **   <a name="sagemaker-Type-Stairs-UsersPerStep"></a>
Specifies how many new users to spawn in each step.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3.
Required: No

## See Also
<a name="API_Stairs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Stairs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Stairs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Stairs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

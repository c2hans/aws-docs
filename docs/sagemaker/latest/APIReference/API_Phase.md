---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Phase.html
---

# Phase
<a name="API_Phase"></a>

Defines the traffic pattern.

## Contents
<a name="API_Phase_Contents"></a>

 ** DurationInSeconds **   <a name="sagemaker-Type-Phase-DurationInSeconds"></a>
Specifies how long a traffic phase should be. For custom load tests, the value should be between 120 and 3600. This value should not exceed `JobDurationInSeconds`.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** InitialNumberOfUsers **   <a name="sagemaker-Type-Phase-InitialNumberOfUsers"></a>
Specifies how many concurrent users to start with. The value should be between 1 and 3.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** SpawnRate **   <a name="sagemaker-Type-Phase-SpawnRate"></a>
Specified how many new users to spawn in a minute.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Phase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Phase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Phase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Phase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

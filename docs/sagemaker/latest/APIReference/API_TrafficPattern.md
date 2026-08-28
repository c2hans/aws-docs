---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrafficPattern.html
---

# TrafficPattern
<a name="API_TrafficPattern"></a>

Defines the traffic pattern of the load test.

## Contents
<a name="API_TrafficPattern_Contents"></a>

 ** Phases **   <a name="sagemaker-Type-TrafficPattern-Phases"></a>
Defines the phases traffic specification.
Type: Array of [Phase](API_Phase.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** Stairs **   <a name="sagemaker-Type-TrafficPattern-Stairs"></a>
Defines the stairs traffic pattern.
Type: [Stairs](API_Stairs.md) object
Required: No

 ** TrafficType **   <a name="sagemaker-Type-TrafficPattern-TrafficType"></a>
Defines the traffic patterns. Choose either `PHASES` or `STAIRS`.
Type: String
Valid Values: `PHASES | STAIRS`
Required: No

## See Also
<a name="API_TrafficPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrafficPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrafficPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrafficPattern)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_MultiMeasureAttributeMapping.html
---

# MultiMeasureAttributeMapping
<a name="API_MultiMeasureAttributeMapping"></a>

A mapping of a source event data field to a measure in a Timestream for LiveAnalytics record.

## Contents
<a name="API_MultiMeasureAttributeMapping_Contents"></a>

 ** MeasureValue **   <a name="eventbridge-Type-MultiMeasureAttributeMapping-MeasureValue"></a>
Dynamic path to the measurement attribute in the source event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** MeasureValueType **   <a name="eventbridge-Type-MultiMeasureAttributeMapping-MeasureValueType"></a>
Data type of the measurement attribute in the source event.
Type: String
Valid Values: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP`
Required: Yes

 ** MultiMeasureAttributeName **   <a name="eventbridge-Type-MultiMeasureAttributeMapping-MultiMeasureAttributeName"></a>
Target measure name to be used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_MultiMeasureAttributeMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/MultiMeasureAttributeMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/MultiMeasureAttributeMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/MultiMeasureAttributeMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge Pipes. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

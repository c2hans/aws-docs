---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_NumericQuestionPropertyValueAutomation.html
---

# NumericQuestionPropertyValueAutomation
<a name="API_NumericQuestionPropertyValueAutomation"></a>

Information about the property value used in automation of a numeric questions. Label values are associated with minimum and maximum values for the numeric question.
+ Sentiment scores have a minimum value of -5 and maximum value of 5.
+  Duration labels, such as `NON_TALK_TIME`, `CONTACT_DURATION`, `AGENT_INTERACTION_DURATION`, `CUSTOMER_HOLD_TIME` have a minimum value of 0 and maximum value of 63072000.
+ Percentages have a minimum value of 0 and maximum value of 100.
+  `NUMBER_OF_INTERRUPTIONS` has a minimum value of 0 and maximum value of 1000.

## Contents
<a name="API_NumericQuestionPropertyValueAutomation_Contents"></a>

 ** Label **   <a name="connect-Type-NumericQuestionPropertyValueAutomation-Label"></a>
The property label of the automation.
Type: String
Valid Values: `OVERALL_CUSTOMER_SENTIMENT_SCORE | OVERALL_AGENT_SENTIMENT_SCORE | CUSTOMER_SENTIMENT_SCORE_WITHOUT_AGENT | CUSTOMER_SENTIMENT_SCORE_WITH_AGENT | NON_TALK_TIME | NON_TALK_TIME_PERCENTAGE | NUMBER_OF_INTERRUPTIONS | CONTACT_DURATION | AGENT_INTERACTION_DURATION | CUSTOMER_HOLD_TIME | LONGEST_HOLD_DURATION | NUMBER_OF_HOLDS | AGENT_INTERACTION_AND_HOLD_DURATION`
Required: Yes

## See Also
<a name="API_NumericQuestionPropertyValueAutomation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/NumericQuestionPropertyValueAutomation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/NumericQuestionPropertyValueAutomation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/NumericQuestionPropertyValueAutomation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

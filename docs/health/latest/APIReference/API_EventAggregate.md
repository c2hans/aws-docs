---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EventAggregate.html
---

# EventAggregate
<a name="API_EventAggregate"></a>

The number of events of each issue type. Returned by the [DescribeEventAggregates](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventAggregates.html) operation.

## Contents
<a name="API_EventAggregate_Contents"></a>

 ** aggregateValue **   <a name="AWSHealth-Type-EventAggregate-aggregateValue"></a>
The issue type for the associated count.
Type: String
Required: No

 ** count **   <a name="AWSHealth-Type-EventAggregate-count"></a>
The number of events of the associated issue type.
Type: Integer
Required: No

## See Also
<a name="API_EventAggregate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EventAggregate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EventAggregate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EventAggregate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

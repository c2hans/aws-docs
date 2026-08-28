---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EntityAggregate.html
---

# EntityAggregate
<a name="API_EntityAggregate"></a>

The number of entities that are affected by one or more events. Returned by the [DescribeEntityAggregates](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEntityAggregates.html) operation.

## Contents
<a name="API_EntityAggregate_Contents"></a>

 ** count **   <a name="AWSHealth-Type-EntityAggregate-count"></a>
The number of entities that match the criteria for the specified events.
Type: Integer
Required: No

 ** eventArn **   <a name="AWSHealth-Type-EntityAggregate-eventArn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

 ** statuses **   <a name="AWSHealth-Type-EntityAggregate-statuses"></a>
The number of affected entities aggregated by the entity status codes.
Type: String to integer map
Valid Keys: `IMPAIRED | UNIMPAIRED | UNKNOWN | PENDING | RESOLVED`
Required: No

## See Also
<a name="API_EntityAggregate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EntityAggregate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EntityAggregate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EntityAggregate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

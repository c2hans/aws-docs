---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Event.html
---

# Event
<a name="API_Event"></a>

This data type is used as a response element in the [DescribeEvents](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeEvents.html) action.

## Contents
<a name="API_Event_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Date **
Specifies the date and time of the event.
Type: Timestamp
Required: No

 ** EventCategories.EventCategory.N **
Specifies the category for the event.
Type: Array of strings
Required: No

 ** Message **
Provides the text of this event.
Type: String
Required: No

 ** SourceArn **
The Amazon Resource Name (ARN) for the event.
Type: String
Required: No

 ** SourceIdentifier **
Provides the identifier for the source of the event.
Type: String
Required: No

 ** SourceType **
Specifies the source type for this event.
Type: String
Valid Values: `db-instance | db-parameter-group | db-security-group | db-snapshot | db-cluster | db-cluster-snapshot | custom-engine-version | db-proxy | blue-green-deployment | db-shard-group | zero-etl`
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/Event)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GroupingIdentifier.html
---

# GroupingIdentifier
<a name="API_GroupingIdentifier"></a>

A key-value pair that identifies how log groups are grouped in aggregate summaries.

## Contents
<a name="API_GroupingIdentifier_Contents"></a>

 ** key **   <a name="CWL-Type-GroupingIdentifier-key"></a>
The key that identifies the grouping characteristic. The format of the key uses dot notation. Examples are, `dataSource.Name`, `dataSource.Type`, and `dataSource.Format`.
Type: String
Required: No

 ** value **   <a name="CWL-Type-GroupingIdentifier-value"></a>
The value associated with the grouping characteristic. Examples are `amazon_vpc`, `flow`, and `OCSF`.
Type: String
Required: No

## See Also
<a name="API_GroupingIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GroupingIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GroupingIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GroupingIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

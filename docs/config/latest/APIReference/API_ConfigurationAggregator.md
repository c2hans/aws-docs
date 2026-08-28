---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationAggregator.html
---

# ConfigurationAggregator
<a name="API_ConfigurationAggregator"></a>

The details about the configuration aggregator, including information about source accounts, regions, and metadata of the aggregator.

## Contents
<a name="API_ConfigurationAggregator_Contents"></a>

 ** AccountAggregationSources **   <a name="config-Type-ConfigurationAggregator-AccountAggregationSources"></a>
Provides a list of source accounts and regions to be aggregated.
Type: Array of [AccountAggregationSource](API_AccountAggregationSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** AggregatorFilters **   <a name="config-Type-ConfigurationAggregator-AggregatorFilters"></a>
An object to filter the data you specify for an aggregator.
Type: [AggregatorFilters](API_AggregatorFilters.md) object
Required: No

 ** ConfigurationAggregatorArn **   <a name="config-Type-ConfigurationAggregator-ConfigurationAggregatorArn"></a>
The Amazon Resource Name (ARN) of the aggregator.
Type: String
Pattern: `arn:aws[a-z\-]*:config:[a-z\-\d]+:\d+:config-aggregator/config-aggregator-[a-z\d]+`
Required: No

 ** ConfigurationAggregatorName **   <a name="config-Type-ConfigurationAggregator-ConfigurationAggregatorName"></a>
The name of the aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: No

 ** CreatedBy **   <a name="config-Type-ConfigurationAggregator-CreatedBy"></a>
 AWS service that created the configuration aggregator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** CreationTime **   <a name="config-Type-ConfigurationAggregator-CreationTime"></a>
The time stamp when the configuration aggregator was created.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="config-Type-ConfigurationAggregator-LastUpdatedTime"></a>
The time of the last update.
Type: Timestamp
Required: No

 ** OrganizationAggregationSource **   <a name="config-Type-ConfigurationAggregator-OrganizationAggregationSource"></a>
Provides an organization and list of regions to be aggregated.
Type: [OrganizationAggregationSource](API_OrganizationAggregationSource.md) object
Required: No

## See Also
<a name="API_ConfigurationAggregator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigurationAggregator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigurationAggregator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigurationAggregator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

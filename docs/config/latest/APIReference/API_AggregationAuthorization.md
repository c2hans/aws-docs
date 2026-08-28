---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_AggregationAuthorization.html
---

# AggregationAuthorization
<a name="API_AggregationAuthorization"></a>

An object that represents the authorizations granted to aggregator accounts and regions.

## Contents
<a name="API_AggregationAuthorization_Contents"></a>

 ** AggregationAuthorizationArn **   <a name="config-Type-AggregationAuthorization-AggregationAuthorizationArn"></a>
The Amazon Resource Name (ARN) of the aggregation object.
Type: String
Required: No

 ** AuthorizedAccountId **   <a name="config-Type-AggregationAuthorization-AuthorizedAccountId"></a>
The 12-digit account ID of the account authorized to aggregate data.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** AuthorizedAwsRegion **   <a name="config-Type-AggregationAuthorization-AuthorizedAwsRegion"></a>
The region authorized to collect aggregated data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** CreationTime **   <a name="config-Type-AggregationAuthorization-CreationTime"></a>
The time stamp when the aggregation authorization was created.
Type: Timestamp
Required: No

## See Also
<a name="API_AggregationAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/AggregationAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/AggregationAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/AggregationAuthorization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

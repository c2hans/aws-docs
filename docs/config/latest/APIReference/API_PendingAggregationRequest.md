---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_PendingAggregationRequest.html
---

# PendingAggregationRequest
<a name="API_PendingAggregationRequest"></a>

An object that represents the account ID and region of an aggregator account that is requesting authorization but is not yet authorized.

## Contents
<a name="API_PendingAggregationRequest_Contents"></a>

 ** RequesterAccountId **   <a name="config-Type-PendingAggregationRequest-RequesterAccountId"></a>
The 12-digit account ID of the account requesting to aggregate data.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** RequesterAwsRegion **   <a name="config-Type-PendingAggregationRequest-RequesterAwsRegion"></a>
The region requesting to aggregate data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_PendingAggregationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/PendingAggregationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/PendingAggregationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/PendingAggregationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

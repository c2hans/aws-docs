---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingAggregationAccountDetails.html
---

# FindingAggregationAccountDetails
<a name="API_FindingAggregationAccountDetails"></a>

Contains information about the findings for an AWS account in an organization unused access analyzer.

## Contents
<a name="API_FindingAggregationAccountDetails_Contents"></a>

 ** account **   <a name="accessanalyzer-Type-FindingAggregationAccountDetails-account"></a>
The ID of the AWS account for which unused access finding details are provided.
Type: String
Required: No

 ** details **   <a name="accessanalyzer-Type-FindingAggregationAccountDetails-details"></a>
Provides the number of active findings for each type of unused access for the specified AWS account.
Type: String to integer map
Required: No

 ** numberOfActiveFindings **   <a name="accessanalyzer-Type-FindingAggregationAccountDetails-numberOfActiveFindings"></a>
The number of active unused access findings for the specified AWS account.
Type: Integer
Required: No

## See Also
<a name="API_FindingAggregationAccountDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingAggregationAccountDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingAggregationAccountDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingAggregationAccountDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

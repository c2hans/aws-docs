---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisCheckAggregation.html
---

# CisCheckAggregation
<a name="API_CisCheckAggregation"></a>

A CIS check.

## Contents
<a name="API_CisCheckAggregation_Contents"></a>

 ** scanArn **   <a name="inspector2-Type-CisCheckAggregation-scanArn"></a>
The scan ARN for the CIS check scan ARN.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/cis-scan/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** accountId **   <a name="inspector2-Type-CisCheckAggregation-accountId"></a>
The account ID for the CIS check.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** checkDescription **   <a name="inspector2-Type-CisCheckAggregation-checkDescription"></a>
The description for the CIS check.
Type: String
Required: No

 ** checkId **   <a name="inspector2-Type-CisCheckAggregation-checkId"></a>
The check ID for the CIS check.
Type: String
Required: No

 ** level **   <a name="inspector2-Type-CisCheckAggregation-level"></a>
The CIS check level.
Type: String
Valid Values: `LEVEL_1 | LEVEL_2`
Required: No

 ** platform **   <a name="inspector2-Type-CisCheckAggregation-platform"></a>
The CIS check platform.
Type: String
Required: No

 ** statusCounts **   <a name="inspector2-Type-CisCheckAggregation-statusCounts"></a>
The CIS check status counts.
Type: [StatusCounts](API_StatusCounts.md) object
Required: No

 ** title **   <a name="inspector2-Type-CisCheckAggregation-title"></a>
The CIS check title.
Type: String
Required: No

## See Also
<a name="API_CisCheckAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisCheckAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisCheckAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisCheckAggregation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

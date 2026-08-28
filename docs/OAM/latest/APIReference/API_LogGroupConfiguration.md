---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_LogGroupConfiguration.html
---

# LogGroupConfiguration
<a name="API_LogGroupConfiguration"></a>

This structure contains the `Filter` parameter which you can use to specify which log groups are to share log events from this source account to the monitoring account.

## Contents
<a name="API_LogGroupConfiguration_Contents"></a>

 ** Filter **   <a name="OAM-Type-LogGroupConfiguration-Filter"></a>
Use this field to specify which log groups are to share their log events with the monitoring account. Use the term `LogGroupName` and one or more of the following operands. Use single quotation marks (') around log group names. The matching of log group names is case sensitive. Each filter has a limit of five conditional operands. Conditional operands are `AND` and `OR`.
+  `=` and `!=`
+  `AND`
+  `OR`
+  `LIKE` and `NOT LIKE`. These can be used only as prefix searches. Include a `%` at the end of the string that you want to search for and include.
+  `IN` and `NOT IN`, using parentheses `( )`
Examples:
+  `LogGroupName IN ('This-Log-Group', 'Other-Log-Group')` includes only the log groups with names `This-Log-Group` and `Other-Log-Group`.
+  `LogGroupName NOT IN ('Private-Log-Group', 'Private-Log-Group-2')` includes all log groups except the log groups with names `Private-Log-Group` and `Private-Log-Group-2`.
+  `LogGroupName LIKE 'aws/lambda/%' OR LogGroupName LIKE 'AWSLogs%'` includes all log groups that have names that start with `aws/lambda/` or `AWSLogs`.
If you are updating a link that uses filters, you can specify `*` as the only value for the `filter` parameter to delete the filter and share all log groups with the monitoring account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## See Also
<a name="API_LogGroupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/LogGroupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/LogGroupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/LogGroupConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Observability Access Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query OAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

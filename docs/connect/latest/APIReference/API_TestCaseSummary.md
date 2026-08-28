---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TestCaseSummary.html
---

# TestCaseSummary
<a name="API_TestCaseSummary"></a>

Contains summary information about a test case.

## Contents
<a name="API_TestCaseSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-TestCaseSummary-Arn"></a>
The Amazon Resource Name (ARN) of the test case.
Type: String
Required: No

 ** Id **   <a name="connect-Type-TestCaseSummary-Id"></a>
The identifier of the test case.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-TestCaseSummary-LastModifiedRegion"></a>
The region in which the test case was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-TestCaseSummary-LastModifiedTime"></a>
The time at which the test case was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-TestCaseSummary-Name"></a>
The name of the test case.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Status **   <a name="connect-Type-TestCaseSummary-Status"></a>
The status of the test case.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

## See Also
<a name="API_TestCaseSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TestCaseSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TestCaseSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TestCaseSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

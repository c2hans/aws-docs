---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TestCaseExecution.html
---

# TestCaseExecution
<a name="API_TestCaseExecution"></a>

Contains information about a test case execution.

## Contents
<a name="API_TestCaseExecution_Contents"></a>

 ** EndTime **   <a name="connect-Type-TestCaseExecution-EndTime"></a>
The timestamp when the test case execution ended.
Type: Timestamp
Required: No

 ** StartTime **   <a name="connect-Type-TestCaseExecution-StartTime"></a>
The timestamp when the test case execution started.
Type: Timestamp
Required: No

 ** Tags **   <a name="connect-Type-TestCaseExecution-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** TestCaseExecutionId **   <a name="connect-Type-TestCaseExecution-TestCaseExecutionId"></a>
The identifier of the test case execution.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** TestCaseExecutionStatus **   <a name="connect-Type-TestCaseExecution-TestCaseExecutionStatus"></a>
The status of the test case execution.
Type: String
Valid Values: `INITIATED | PASSED | FAILED | IN_PROGRESS | STOPPED`
Required: No

 ** TestCaseId **   <a name="connect-Type-TestCaseExecution-TestCaseId"></a>
The identifier of the test case.
Type: String
Length Constraints: Maximum length of 500.
Required: No

## See Also
<a name="API_TestCaseExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TestCaseExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TestCaseExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TestCaseExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

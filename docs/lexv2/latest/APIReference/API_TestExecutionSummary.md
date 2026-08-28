---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestExecutionSummary.html
---

# TestExecutionSummary
<a name="API_TestExecutionSummary"></a>

Summarizes metadata about the test execution.

## Contents
<a name="API_TestExecutionSummary_Contents"></a>

 ** apiMode **   <a name="lexv2-Type-TestExecutionSummary-apiMode"></a>
Specifies whether the API mode for the test execution is streaming or non-streaming.
Type: String
Valid Values: `Streaming | NonStreaming`
Required: No

 ** creationDateTime **   <a name="lexv2-Type-TestExecutionSummary-creationDateTime"></a>
The date and time at which the test execution was created.
Type: Timestamp
Required: No

 ** lastUpdatedDateTime **   <a name="lexv2-Type-TestExecutionSummary-lastUpdatedDateTime"></a>
The date and time at which the test execution was last updated.
Type: Timestamp
Required: No

 ** target **   <a name="lexv2-Type-TestExecutionSummary-target"></a>
Contains information about the bot used for the test execution..
Type: [TestExecutionTarget](API_TestExecutionTarget.md) object
Required: No

 ** testExecutionId **   <a name="lexv2-Type-TestExecutionSummary-testExecutionId"></a>
The unique identifier of the test execution.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** testExecutionModality **   <a name="lexv2-Type-TestExecutionSummary-testExecutionModality"></a>
Specifies whether the data used for the test execution is written or spoken.
Type: String
Valid Values: `Text | Audio`
Required: No

 ** testExecutionStatus **   <a name="lexv2-Type-TestExecutionSummary-testExecutionStatus"></a>
The current status of the test execution.
Type: String
Valid Values: `Pending | Waiting | InProgress | Completed | Failed | Stopping | Stopped`
Required: No

 ** testSetId **   <a name="lexv2-Type-TestExecutionSummary-testSetId"></a>
The unique identifier of the test set used in the test execution.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: No

 ** testSetName **   <a name="lexv2-Type-TestExecutionSummary-testSetName"></a>
The name of the test set used in the test execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

## See Also
<a name="API_TestExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestExecutionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

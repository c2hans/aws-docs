---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableStatus.html
---

# TableStatus
<a name="API_TableStatus"></a>

A structure containing information about the state of an asynchronous change to a table.

## Contents
<a name="API_TableStatus_Contents"></a>

 ** Action **   <a name="Glue-Type-TableStatus-Action"></a>
Indicates which action was called on the table, currently only `CREATE` or `UPDATE`.
Type: String
Valid Values: `UPDATE | CREATE`
Required: No

 ** Details **   <a name="Glue-Type-TableStatus-Details"></a>
A `StatusDetails` object with information about the requested change.
Type: [StatusDetails](API_StatusDetails.md) object
Required: No

 ** Error **   <a name="Glue-Type-TableStatus-Error"></a>
An error that will only appear when the state is "FAILED". This is a parent level exception message, there may be different `Error`s for each dialect.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** RequestedBy **   <a name="Glue-Type-TableStatus-RequestedBy"></a>
The ARN of the user who requested the asynchronous change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** RequestTime **   <a name="Glue-Type-TableStatus-RequestTime"></a>
An ISO 8601 formatted date string indicating the time that the change was initiated.
Type: Timestamp
Required: No

 ** State **   <a name="Glue-Type-TableStatus-State"></a>
A generic status for the change in progress, such as QUEUED, IN\_PROGRESS, SUCCESS, or FAILED.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | SUCCESS | STOPPED | FAILED`
Required: No

 ** UpdatedBy **   <a name="Glue-Type-TableStatus-UpdatedBy"></a>
The ARN of the user to last manually alter the asynchronous change (requesting cancellation, etc).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** UpdateTime **   <a name="Glue-Type-TableStatus-UpdateTime"></a>
An ISO 8601 formatted date string indicating the time that the state was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_TableStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Statement.html
---

# Statement
<a name="API_Statement"></a>

The statement or request for a particular action to occur in a session.

## Contents
<a name="API_Statement_Contents"></a>

 ** Code **   <a name="Glue-Type-Statement-Code"></a>
The execution code of the statement.
Type: String
Required: No

 ** CompletedOn **   <a name="Glue-Type-Statement-CompletedOn"></a>
The unix time and date that the job definition was completed.
Type: Long
Required: No

 ** Id **   <a name="Glue-Type-Statement-Id"></a>
The ID of the statement.
Type: Integer
Required: No

 ** Output **   <a name="Glue-Type-Statement-Output"></a>
The output in JSON.
Type: [StatementOutput](API_StatementOutput.md) object
Required: No

 ** Progress **   <a name="Glue-Type-Statement-Progress"></a>
The code execution progress.
Type: Double
Required: No

 ** StartedOn **   <a name="Glue-Type-Statement-StartedOn"></a>
The unix time and date that the job definition was started.
Type: Long
Required: No

 ** State **   <a name="Glue-Type-Statement-State"></a>
The state while request is actioned.
Type: String
Valid Values: `WAITING | RUNNING | AVAILABLE | CANCELLING | CANCELLED | ERROR`
Required: No

## See Also
<a name="API_Statement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Statement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Statement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Statement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ViewValidation.html
---

# ViewValidation
<a name="API_ViewValidation"></a>

A structure that contains information for an analytical engine to validate a view, prior to persisting the view metadata. Used in the case of direct `UpdateTable` or `CreateTable` API calls.

## Contents
<a name="API_ViewValidation_Contents"></a>

 ** Dialect **   <a name="Glue-Type-ViewValidation-Dialect"></a>
The dialect of the query engine.
Type: String
Valid Values: `REDSHIFT | ATHENA | SPARK`
Required: No

 ** DialectVersion **   <a name="Glue-Type-ViewValidation-DialectVersion"></a>
The version of the dialect of the query engine. For example, 3.0.0.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Error **   <a name="Glue-Type-ViewValidation-Error"></a>
An error associated with the validation.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** State **   <a name="Glue-Type-ViewValidation-State"></a>
The state of the validation.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | SUCCESS | STOPPED | FAILED`
Required: No

 ** UpdateTime **   <a name="Glue-Type-ViewValidation-UpdateTime"></a>
The time of the last update.
Type: Timestamp
Required: No

 ** ViewValidationText **   <a name="Glue-Type-ViewValidation-ViewValidationText"></a>
The `SELECT` query that defines the view, as provided by the customer.
Type: String
Length Constraints: Maximum length of 409600.
Required: No

## See Also
<a name="API_ViewValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ViewValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ViewValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ViewValidation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

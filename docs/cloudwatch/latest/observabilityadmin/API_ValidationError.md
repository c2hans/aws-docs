---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_ValidationError.html
---

# ValidationError
<a name="API_ValidationError"></a>

Represents a detailed validation error with message, reason, and field mapping for comprehensive error reporting.

## Contents
<a name="API_ValidationError_Contents"></a>

 ** FieldMap **   <a name="cwoa-Type-ValidationError-FieldMap"></a>
A mapping of field names to specific validation issues within the configuration.
Type: String to string map
Required: No

 ** Message **   <a name="cwoa-Type-ValidationError-Message"></a>
The error message describing the validation issue.
Type: String
Required: No

 ** Reason **   <a name="cwoa-Type-ValidationError-Reason"></a>
The reason code or category for the validation error.
Type: String
Required: No

## See Also
<a name="API_ValidationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/ValidationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/ValidationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/ValidationError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

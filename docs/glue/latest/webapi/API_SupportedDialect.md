---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SupportedDialect.html
---

# SupportedDialect
<a name="API_SupportedDialect"></a>

A structure specifying the dialect and dialect version used by the query engine.

## Contents
<a name="API_SupportedDialect_Contents"></a>

 ** Dialect **   <a name="Glue-Type-SupportedDialect-Dialect"></a>
The dialect of the query engine.
Type: String
Valid Values: `REDSHIFT | ATHENA | SPARK`
Required: No

 ** DialectVersion **   <a name="Glue-Type-SupportedDialect-DialectVersion"></a>
The version of the dialect of the query engine. For example, 3.0.0.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_SupportedDialect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SupportedDialect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SupportedDialect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SupportedDialect)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

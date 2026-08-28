---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Location.html
---

# Location
<a name="API_Location"></a>

A union that identifies the location to instrument. Specify a `CodeLocation` for code-level instrumentation.

## Contents
<a name="API_Location_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CodeLocation **   <a name="applicationsignals-Type-Location-CodeLocation"></a>
A code location for code-level instrumentation, including language, code unit, class, method, file path, and optional line number.
Type: [CodeLocation](API_CodeLocation.md) object
Required: No

## See Also
<a name="API_Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/Location)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

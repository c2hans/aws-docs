---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_SelectionConfig.html
---

# SelectionConfig
<a name="API_SelectionConfig"></a>

Defines how operations are selected for a service-level SLO.

## Contents
<a name="API_SelectionConfig_Contents"></a>

 ** Type **   <a name="applicationsignals-Type-SelectionConfig-Type"></a>
The strategy for selecting operations to include in a service-level SLO.
+  `EXPLICIT` — You provide a specific list of operations in the `Components` field of `CompositeSliConfig`.
+  `PREFIX` — You provide a prefix string in the `Pattern` field of `SelectionConfig`, and all operations whose names start with the prefix are included.
+  `REGEX` — You provide a regular expression in the `Pattern` field of `SelectionConfig`, and all operations whose names match the pattern are included.
Type: String
Valid Values: `EXPLICIT | PREFIX | REGEX`
Required: Yes

 ** Pattern **   <a name="applicationsignals-Type-SelectionConfig-Pattern"></a>
A prefix string or regular expression that specifies which operations to include in a service-level SLO. When `SelectionType` is `PREFIX`, this value is a prefix string that matches the beginning of operation names. When `SelectionType` is `REGEX`, this value is a regular expression that matches operation names.
Type: String
Pattern: `.+`
Required: No

## See Also
<a name="API_SelectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/SelectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/SelectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/SelectionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

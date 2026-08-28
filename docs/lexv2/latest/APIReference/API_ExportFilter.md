---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ExportFilter.html
---

# ExportFilter
<a name="API_ExportFilter"></a>

Filters the response form the [ListExports](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListExports.html) operation

## Contents
<a name="API_ExportFilter_Contents"></a>

 ** name **   <a name="lexv2-Type-ExportFilter-name"></a>
The name of the field to use for filtering.
Type: String
Valid Values: `ExportResourceType`
Required: Yes

 ** operator **   <a name="lexv2-Type-ExportFilter-operator"></a>
The operator to use for the filter. Specify EQ when the `ListExports` operation should return only resource types that equal the specified value. Specify CO when the `ListExports` operation should return resource types that contain the specified value.
Type: String
Valid Values: `CO | EQ`
Required: Yes

 ** values **   <a name="lexv2-Type-ExportFilter-values"></a>
The values to use to filter the response. The values must be `Bot`, `BotLocale`, or `CustomVocabulary`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9a-zA-Z_()\s-]+$`
Required: Yes

## See Also
<a name="API_ExportFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ExportFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ExportFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ExportFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CustomVocabularyExportSpecification.html
---

# CustomVocabularyExportSpecification
<a name="API_CustomVocabularyExportSpecification"></a>

Provides the parameters required for exporting a custom vocabulary.

## Contents
<a name="API_CustomVocabularyExportSpecification_Contents"></a>

 ** botId **   <a name="lexv2-Type-CustomVocabularyExportSpecification-botId"></a>
The identifier of the bot that contains the custom vocabulary to export.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

 ** botVersion **   <a name="lexv2-Type-CustomVocabularyExportSpecification-botVersion"></a>
The version of the bot that contains the custom vocabulary to export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: Yes

 ** localeId **   <a name="lexv2-Type-CustomVocabularyExportSpecification-localeId"></a>
The locale of the bot that contains the custom vocabulary to export.
Type: String
Required: Yes

## See Also
<a name="API_CustomVocabularyExportSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/CustomVocabularyExportSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/CustomVocabularyExportSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/CustomVocabularyExportSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

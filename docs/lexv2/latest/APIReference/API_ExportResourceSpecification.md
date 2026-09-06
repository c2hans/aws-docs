---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ExportResourceSpecification.html
---

# ExportResourceSpecification
<a name="API_ExportResourceSpecification"></a>

Provides information about the bot or bot locale that you want to export. You can specify the `botExportSpecification` or the `botLocaleExportSpecification`, but not both.

## Contents
<a name="API_ExportResourceSpecification_Contents"></a>

 ** botExportSpecification **   <a name="lexv2-Type-ExportResourceSpecification-botExportSpecification"></a>
Parameters for exporting a bot.
Type: [BotExportSpecification](API_BotExportSpecification.md) object
Required: No

 ** botLocaleExportSpecification **   <a name="lexv2-Type-ExportResourceSpecification-botLocaleExportSpecification"></a>
Parameters for exporting a bot locale.
Type: [BotLocaleExportSpecification](API_BotLocaleExportSpecification.md) object
Required: No

 ** customVocabularyExportSpecification **   <a name="lexv2-Type-ExportResourceSpecification-customVocabularyExportSpecification"></a>
The parameters required to export a custom vocabulary.
Type: [CustomVocabularyExportSpecification](API_CustomVocabularyExportSpecification.md) object
Required: No

 ** testSetExportSpecification **   <a name="lexv2-Type-ExportResourceSpecification-testSetExportSpecification"></a>
Specifications for the test set that is exported as a resource.
Type: [TestSetExportSpecification](API_TestSetExportSpecification.md) object
Required: No

## See Also
<a name="API_ExportResourceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ExportResourceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ExportResourceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ExportResourceSpecification)

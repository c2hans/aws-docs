---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ImportResourceSpecification.html
---

# ImportResourceSpecification
<a name="API_ImportResourceSpecification"></a>

Provides information about the bot or bot locale that you want to import. You can specify the `botImportSpecification` or the `botLocaleImportSpecification`, but not both.

## Contents
<a name="API_ImportResourceSpecification_Contents"></a>

 ** botImportSpecification **   <a name="lexv2-Type-ImportResourceSpecification-botImportSpecification"></a>
Parameters for importing a bot.
Type: [BotImportSpecification](API_BotImportSpecification.md) object
Required: No

 ** botLocaleImportSpecification **   <a name="lexv2-Type-ImportResourceSpecification-botLocaleImportSpecification"></a>
Parameters for importing a bot locale.
Type: [BotLocaleImportSpecification](API_BotLocaleImportSpecification.md) object
Required: No

 ** customVocabularyImportSpecification **   <a name="lexv2-Type-ImportResourceSpecification-customVocabularyImportSpecification"></a>
Provides the parameters required for importing a custom vocabulary.
Type: [CustomVocabularyImportSpecification](API_CustomVocabularyImportSpecification.md) object
Required: No

 ** testSetImportResourceSpecification **   <a name="lexv2-Type-ImportResourceSpecification-testSetImportResourceSpecification"></a>
Specifications for the test set that is imported.
Type: [TestSetImportResourceSpecification](API_TestSetImportResourceSpecification.md) object
Required: No

## See Also
<a name="API_ImportResourceSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ImportResourceSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ImportResourceSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ImportResourceSpecification)

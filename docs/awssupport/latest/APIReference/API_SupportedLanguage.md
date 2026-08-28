---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_SupportedLanguage.html
---

# SupportedLanguage
<a name="API_SupportedLanguage"></a>

 A JSON-formatted object that contains the available ISO 639-1 language `code`, `language` name and langauge `display` value. The language code is what should be used in the [CreateCase](API_CreateCase.md) call.

## Contents
<a name="API_SupportedLanguage_Contents"></a>

 ** code **   <a name="AWSSupport-Type-SupportedLanguage-code"></a>
 2 digit ISO 639-1 code. e.g. `en`
Type: String

 ** display **   <a name="AWSSupport-Type-SupportedLanguage-display"></a>
 Language display value e.g. `ENGLISH`
Type: String

 ** language **   <a name="AWSSupport-Type-SupportedLanguage-language"></a>
 Full language description e.g. `ENGLISH`
Type: String

## See Also
<a name="API_SupportedLanguage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/SupportedLanguage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/SupportedLanguage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/SupportedLanguage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

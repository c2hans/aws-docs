---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_TranslationName.html
---

# TranslationName
<a name="API_geoplaces_TranslationName"></a>

A translation or alternative name for an address component.

## Contents
<a name="API_geoplaces_TranslationName_Contents"></a>

 ** Type **   <a name="location-Type-geoplaces_TranslationName-Type"></a>
The type of translation name. Valid values are `Abbreviation`, `AreaCode`, `BaseName`, `Exonym`, `Shortened`, and `Synonym`.
Type: String
Valid Values: `Abbreviation | AreaCode | BaseName | Exonym | Shortened | Synonym`
Required: Yes

 ** Value **   <a name="location-Type-geoplaces_TranslationName-Value"></a>
The translated or alternative name value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** Language **   <a name="location-Type-geoplaces_TranslationName-Language"></a>
A [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language code for the translation name.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** Primary **   <a name="location-Type-geoplaces_TranslationName-Primary"></a>
If `true`, indicates this is the primary name variant for the given language.
Type: Boolean
Required: No

 ** Transliterated **   <a name="location-Type-geoplaces_TranslationName-Transliterated"></a>
If `true`, indicates this name is a transliterated version rather than a native script translation.
Type: Boolean
Required: No

## See Also
<a name="API_geoplaces_TranslationName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/TranslationName)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/TranslationName)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/TranslationName)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

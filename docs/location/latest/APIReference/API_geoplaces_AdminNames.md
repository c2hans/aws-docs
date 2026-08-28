---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AdminNames.html
---

# AdminNames
<a name="API_geoplaces_AdminNames"></a>

The official administrative names for an address component, returned when `AddressNamesMode` is set to `Administrative`.

## Contents
<a name="API_geoplaces_AdminNames_Contents"></a>

 ** Names **   <a name="location-Type-geoplaces_AdminNames-Names"></a>
A list of translation names for the administrative address component, including name variants and translations in available languages.
Type: Array of [TranslationName](API_geoplaces_TranslationName.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** Preference **   <a name="location-Type-geoplaces_AdminNames-Preference"></a>
Indicates the preference level of the administrative name. Valid values are `Primary` and `Alternative`.
Type: String
Valid Values: `Alternative | Primary`
Required: No

## See Also
<a name="API_geoplaces_AdminNames_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/AdminNames)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/AdminNames)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/AdminNames)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

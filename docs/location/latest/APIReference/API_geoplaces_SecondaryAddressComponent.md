---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SecondaryAddressComponent.html
---

# SecondaryAddressComponent
<a name="API_geoplaces_SecondaryAddressComponent"></a>

Components that correspond to secondary identifiers on an address. The only component type supported currently is Unit.

## Contents
<a name="API_geoplaces_SecondaryAddressComponent_Contents"></a>

 ** Number **   <a name="location-Type-geoplaces_SecondaryAddressComponent-Number"></a>
Number that uniquely identifies a secondary address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Required: Yes

 ** Designator **   <a name="location-Type-geoplaces_SecondaryAddressComponent-Designator"></a>
The designator of the secondary address component.
Example: `Apt`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Required: No

## See Also
<a name="API_geoplaces_SecondaryAddressComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SecondaryAddressComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SecondaryAddressComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SecondaryAddressComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_ValidateAddressActionOptions.html
---

# ValidateAddressActionOptions
<a name="API_geojobs_ValidateAddressActionOptions"></a>

Options specific to address validation jobs.

## Contents
<a name="API_geojobs_ValidateAddressActionOptions_Contents"></a>

 ** AdditionalFeatures **   <a name="location-Type-geojobs_ValidateAddressActionOptions-AdditionalFeatures"></a>
A list of optional additional parameters that can be requested for each result.
Values:
+  `Position` - Return the position coordinates of the address if available. This feature is only available in the United States, Canada, and Australia, and incurs additional costs. For more information, see [Amazon Location Service pricing](http://aws.amazon.com/location/pricing/).
+  `CountrySpecificAttributes` - Return additional information about the address specific to the country of origin.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `Position | CountrySpecificAttributes`
Required: No

## See Also
<a name="API_geojobs_ValidateAddressActionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geojobs-2020-11-19/ValidateAddressActionOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geojobs-2020-11-19/ValidateAddressActionOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geojobs-2020-11-19/ValidateAddressActionOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

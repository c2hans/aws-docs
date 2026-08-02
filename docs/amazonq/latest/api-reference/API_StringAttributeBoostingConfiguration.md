---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StringAttributeBoostingConfiguration.html
---

# StringAttributeBoostingConfiguration
<a name="API_StringAttributeBoostingConfiguration"></a>

Provides information on boosting `STRING` type document attributes.

**Note**
For `STRING` and `STRING_LIST` type document attributes to be used for boosting on the console and the API, they must be enabled for search using the [DocumentAttributeConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeConfiguration.html) object of the [UpdateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIndex.html) API. If you haven't enabled searching on these attributes, you can't boost attributes of these data types on either the console or the API.

For more information on how boosting document attributes work in Amazon Q Business, see [Boosting using document attributes](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/metadata-boosting.html).

## Contents
<a name="API_StringAttributeBoostingConfiguration_Contents"></a>

 ** boostingLevel **   <a name="qbusiness-Type-StringAttributeBoostingConfiguration-boostingLevel"></a>
Specifies the priority tier ranking of boosting applied to document attributes. For version 2, this parameter indicates the relative ranking between boosted fields (ONE being highest priority, TWO being second highest, etc.) and determines the order in which attributes influence document ranking in search results. For version 1, this parameter specifies the boosting intensity. For version 2, boosting intensity (VERY HIGH, HIGH, MEDIUM, LOW, NONE) are not supported. Note that in version 2, you are not allowed to boost on only one field and make this value TWO.
Type: String
Valid Values: `NONE | LOW | MEDIUM | HIGH | VERY_HIGH | ONE | TWO`
Required: Yes

 ** attributeValueBoosting **   <a name="qbusiness-Type-StringAttributeBoostingConfiguration-attributeValueBoosting"></a>
Specifies specific values of a `STRING` type document attribute being boosted. When using `NativeIndexConfiguration` version 2, you can specify up to five values in order of priority.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Valid Values: `LOW | MEDIUM | HIGH | VERY_HIGH | ONE | TWO | THREE | FOUR | FIVE`
Required: No

## See Also
<a name="API_StringAttributeBoostingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/StringAttributeBoostingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/StringAttributeBoostingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/StringAttributeBoostingConfiguration)

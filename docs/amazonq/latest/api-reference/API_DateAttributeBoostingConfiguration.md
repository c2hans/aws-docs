---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DateAttributeBoostingConfiguration.html
---

# DateAttributeBoostingConfiguration
<a name="API_DateAttributeBoostingConfiguration"></a>

Provides information on boosting `DATE` type document attributes.

For more information on how boosting document attributes work in Amazon Q Business, see [Boosting using document attributes](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/metadata-boosting.html).

## Contents
<a name="API_DateAttributeBoostingConfiguration_Contents"></a>

 ** boostingLevel **   <a name="qbusiness-Type-DateAttributeBoostingConfiguration-boostingLevel"></a>
Specifies the priority tier ranking of boosting applied to document attributes. For version 2, this parameter indicates the relative ranking between boosted fields (ONE being highest priority, TWO being second highest, etc.) and determines the order in which attributes influence document ranking in search results. For version 1, this parameter specifies the boosting intensity. For version 2, boosting intensity (VERY HIGH, HIGH, MEDIUM, LOW, NONE) are not supported. Note that in version 2, you are not allowed to boost on only one field and make this value TWO.
Type: String
Valid Values: `NONE | LOW | MEDIUM | HIGH | VERY_HIGH | ONE | TWO`
Required: Yes

 ** boostingDurationInSeconds **   <a name="qbusiness-Type-DateAttributeBoostingConfiguration-boostingDurationInSeconds"></a>
Specifies the duration, in seconds, of a boost applies to a `DATE` type document attribute.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 999999999.
Required: No

## See Also
<a name="API_DateAttributeBoostingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DateAttributeBoostingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DateAttributeBoostingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DateAttributeBoostingConfiguration)

---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_FoodType.html
---

# FoodType
<a name="API_geoplaces_FoodType"></a>

List of `Food` types offered by this result.

## Contents
<a name="API_geoplaces_FoodType_Contents"></a>

 ** LocalizedName **   <a name="location-Type-geoplaces_FoodType-LocalizedName"></a>
Localized name of the food type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Id **   <a name="location-Type-geoplaces_FoodType-Id"></a>
The Food Type Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Primary **   <a name="location-Type-geoplaces_FoodType-Primary"></a>
Boolean which indicates if this food type is the primary offered by the place. For example, if a location serves fast food, but also dessert, he primary would likely be fast food.
Type: Boolean
Required: No

## See Also
<a name="API_geoplaces_FoodType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/FoodType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/FoodType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/FoodType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

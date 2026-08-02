---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_RecommenderSchemaField.html
---

# RecommenderSchemaField
<a name="API_connect-customer-profiles_RecommenderSchemaField"></a>

Defines a column in a recommender schema, including the target field name and optional feature and content type settings for training.

## Contents
<a name="API_connect-customer-profiles_RecommenderSchemaField_Contents"></a>

 ** TargetFieldName **   <a name="connect-Type-connect-customer-profiles_RecommenderSchemaField-TargetFieldName"></a>
The name of the target field in the dataset, such as `Location.City` or `Attributes.MealTime`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** ContentType **   <a name="connect-Type-connect-customer-profiles_RecommenderSchemaField-ContentType"></a>
The data type of the column value. Valid values are `String` and `Number`. The default value is `String`.
Type: String
Valid Values: `STRING | NUMBER`
Required: No

 ** FeatureType **   <a name="connect-Type-connect-customer-profiles_RecommenderSchemaField-FeatureType"></a>
How the column is treated for model training. Valid values are `CATEGORICAL` and `TEXTUAL`.
Type: String
Valid Values: `TEXTUAL | CATEGORICAL`
Required: No

## See Also
<a name="API_connect-customer-profiles_RecommenderSchemaField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RecommenderSchemaField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RecommenderSchemaField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RecommenderSchemaField)

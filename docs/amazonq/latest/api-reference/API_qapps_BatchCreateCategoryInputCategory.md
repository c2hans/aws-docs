---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_BatchCreateCategoryInputCategory.html
---

# BatchCreateCategoryInputCategory
<a name="API_qapps_BatchCreateCategoryInputCategory"></a>

The category object to be created.

## Contents
<a name="API_qapps_BatchCreateCategoryInputCategory_Contents"></a>

 ** title **   <a name="qbusiness-Type-qapps_BatchCreateCategoryInputCategory-title"></a>
The name of the category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*`
Required: Yes

 ** color **   <a name="qbusiness-Type-qapps_BatchCreateCategoryInputCategory-color"></a>
The color to be associated with a category. The color must be a hexadecimal value of either 3 or 6 digits.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 7.
Pattern: `#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})`
Required: No

 ** id **   <a name="qbusiness-Type-qapps_BatchCreateCategoryInputCategory-id"></a>
The unique identifier to be associated with a category. If you don't include a value, the category is automatically assigned a unique identifier.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: No

## See Also
<a name="API_qapps_BatchCreateCategoryInputCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/BatchCreateCategoryInputCategory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/BatchCreateCategoryInputCategory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/BatchCreateCategoryInputCategory)

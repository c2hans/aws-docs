---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_Category.html
---

# Category
<a name="API_qapps_Category"></a>

A category used to classify and filter library items for Amazon Q Apps.

## Contents
<a name="API_qapps_Category_Contents"></a>

 ** id **   <a name="qbusiness-Type-qapps_Category-id"></a>
The unique identifier of the category.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_Category-title"></a>
The title or name of the category.
Type: String
Required: Yes

 ** appCount **   <a name="qbusiness-Type-qapps_Category-appCount"></a>
The number of published Amazon Q Apps associated with a category
Type: Integer
Required: No

 ** color **   <a name="qbusiness-Type-qapps_Category-color"></a>
The color of the category
Type: String
Required: No

## See Also
<a name="API_qapps_Category_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/Category)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/Category)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/Category)

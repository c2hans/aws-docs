---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_BatchPermissionsRequestEntry.html
---

# BatchPermissionsRequestEntry
<a name="API_BatchPermissionsRequestEntry"></a>

A permission to a resource granted by batch operation to the principal.

## Contents
<a name="API_BatchPermissionsRequestEntry_Contents"></a>

 ** Id **   <a name="lakeformation-Type-BatchPermissionsRequestEntry-Id"></a>
A unique identifier for the batch permissions request entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Condition **   <a name="lakeformation-Type-BatchPermissionsRequestEntry-Condition"></a>
A Lake Formation condition, which applies to permissions and opt-ins that contain an expression.
Type: [Condition](API_Condition.md) object
Required: No

 ** Permissions **   <a name="lakeformation-Type-BatchPermissionsRequestEntry-Permissions"></a>
The permissions to be granted.
Type: Array of strings
Valid Values: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | DESCRIBE | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS | CREATE_LF_TAG | ASSOCIATE | GRANT_WITH_LF_TAG_EXPRESSION | CREATE_LF_TAG_EXPRESSION | CREATE_CATALOG | SUPER_USER`
Required: No

 ** PermissionsWithGrantOption **   <a name="lakeformation-Type-BatchPermissionsRequestEntry-PermissionsWithGrantOption"></a>
Indicates if the option to pass permissions is granted.
Type: Array of strings
Valid Values: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | DESCRIBE | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS | CREATE_LF_TAG | ASSOCIATE | GRANT_WITH_LF_TAG_EXPRESSION | CREATE_LF_TAG_EXPRESSION | CREATE_CATALOG | SUPER_USER`
Required: No

 ** Principal **   <a name="lakeformation-Type-BatchPermissionsRequestEntry-Principal"></a>
The principal to be granted a permission.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

 ** Resource **   <a name="lakeformation-Type-BatchPermissionsRequestEntry-Resource"></a>
The resource to which the principal is to be granted a permission.
Type: [Resource](API_Resource.md) object
Required: No

## See Also
<a name="API_BatchPermissionsRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/BatchPermissionsRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/BatchPermissionsRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/BatchPermissionsRequestEntry)

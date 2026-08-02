---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_PrincipalResourcePermissions.html
---

# PrincipalResourcePermissions
<a name="API_PrincipalResourcePermissions"></a>

The permissions granted or revoked on a resource.

## Contents
<a name="API_PrincipalResourcePermissions_Contents"></a>

 ** AdditionalDetails **   <a name="lakeformation-Type-PrincipalResourcePermissions-AdditionalDetails"></a>
This attribute can be used to return any additional details of `PrincipalResourcePermissions`. Currently returns only as a AWS RAM resource share ARN.
Type: [DetailsMap](API_DetailsMap.md) object
Required: No

 ** Condition **   <a name="lakeformation-Type-PrincipalResourcePermissions-Condition"></a>
A Lake Formation condition, which applies to permissions and opt-ins that contain an expression.
Type: [Condition](API_Condition.md) object
Required: No

 ** LastUpdated **   <a name="lakeformation-Type-PrincipalResourcePermissions-LastUpdated"></a>
The date and time when the resource was last updated.
Type: Timestamp
Required: No

 ** LastUpdatedBy **   <a name="lakeformation-Type-PrincipalResourcePermissions-LastUpdatedBy"></a>
The user who updated the record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Permissions **   <a name="lakeformation-Type-PrincipalResourcePermissions-Permissions"></a>
The permissions to be granted or revoked on the resource.
Type: Array of strings
Valid Values: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | DESCRIBE | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS | CREATE_LF_TAG | ASSOCIATE | GRANT_WITH_LF_TAG_EXPRESSION | CREATE_LF_TAG_EXPRESSION | CREATE_CATALOG | SUPER_USER`
Required: No

 ** PermissionsWithGrantOption **   <a name="lakeformation-Type-PrincipalResourcePermissions-PermissionsWithGrantOption"></a>
Indicates whether to grant the ability to grant permissions (as a subset of permissions granted).
Type: Array of strings
Valid Values: `ALL | SELECT | ALTER | DROP | DELETE | INSERT | DESCRIBE | CREATE_DATABASE | CREATE_TABLE | DATA_LOCATION_ACCESS | CREATE_LF_TAG | ASSOCIATE | GRANT_WITH_LF_TAG_EXPRESSION | CREATE_LF_TAG_EXPRESSION | CREATE_CATALOG | SUPER_USER`
Required: No

 ** Principal **   <a name="lakeformation-Type-PrincipalResourcePermissions-Principal"></a>
The Data Lake principal to be granted or revoked permissions.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

 ** Resource **   <a name="lakeformation-Type-PrincipalResourcePermissions-Resource"></a>
The resource where permissions are to be granted or revoked.
Type: [Resource](API_Resource.md) object
Required: No

## See Also
<a name="API_PrincipalResourcePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/PrincipalResourcePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/PrincipalResourcePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/PrincipalResourcePermissions)

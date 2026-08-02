---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DataLakeSettings.html
---

# DataLakeSettings
<a name="API_DataLakeSettings"></a>

A structure representing a list of AWS Lake Formation principals designated as data lake administrators and lists of principal permission entries for default create database and default create table permissions.

## Contents
<a name="API_DataLakeSettings_Contents"></a>

 ** AllowExternalDataFiltering **   <a name="lakeformation-Type-DataLakeSettings-AllowExternalDataFiltering"></a>
Whether to allow Amazon EMR clusters to access data managed by Lake Formation.
If true, you allow Amazon EMR clusters to access data in Amazon S3 locations that are registered with Lake Formation.
If false or null, no Amazon EMR clusters will be able to access data in Amazon S3 locations that are registered with Lake Formation.
For more information, see [(Optional) Allow external data filtering](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-LF-setup.html#external-data-filter).
Type: Boolean
Required: No

 ** AllowFullTableExternalDataAccess **   <a name="lakeformation-Type-DataLakeSettings-AllowFullTableExternalDataAccess"></a>
Whether to allow a third-party query engine to get data access credentials without session tags when a caller has full data access permissions.
Type: Boolean
Required: No

 ** AuthorizedSessionTagValueList **   <a name="lakeformation-Type-DataLakeSettings-AuthorizedSessionTagValueList"></a>
Lake Formation relies on a privileged process secured by Amazon EMR or the third party integrator to tag the user's role while assuming it. Lake Formation will publish the acceptable key-value pair, for example key = "LakeFormationTrustedCaller" and value = "TRUE" and the third party integrator must properly tag the temporary security credentials that will be used to call Lake Formation's administrative APIs.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** CreateDatabaseDefaultPermissions **   <a name="lakeformation-Type-DataLakeSettings-CreateDatabaseDefaultPermissions"></a>
Specifies whether access control on newly created database is managed by Lake Formation permissions or exclusively by IAM permissions.
A null value indicates access control by Lake Formation permissions. A value that assigns ALL to IAM\_ALLOWED\_PRINCIPALS indicates access control by IAM permissions. This is referred to as the setting "Use only IAM access control," and is for backward compatibility with the AWS Glue permission model implemented by IAM permissions.
The only permitted values are an empty array or an array that contains a single JSON object that grants ALL to IAM\_ALLOWED\_PRINCIPALS.
For more information, see [Changing the Default Security Settings for Your Data Lake](https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html).
Type: Array of [PrincipalPermissions](API_PrincipalPermissions.md) objects
Required: No

 ** CreateTableDefaultPermissions **   <a name="lakeformation-Type-DataLakeSettings-CreateTableDefaultPermissions"></a>
Specifies whether access control on newly created table is managed by Lake Formation permissions or exclusively by IAM permissions.
A null value indicates access control by Lake Formation permissions. A value that assigns ALL to IAM\_ALLOWED\_PRINCIPALS indicates access control by IAM permissions. This is referred to as the setting "Use only IAM access control," and is for backward compatibility with the AWS Glue permission model implemented by IAM permissions.
The only permitted values are an empty array or an array that contains a single JSON object that grants ALL to IAM\_ALLOWED\_PRINCIPALS.
For more information, see [Changing the Default Security Settings for Your Data Lake](https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html).
Type: Array of [PrincipalPermissions](API_PrincipalPermissions.md) objects
Required: No

 ** DataLakeAdmins **   <a name="lakeformation-Type-DataLakeSettings-DataLakeAdmins"></a>
A list of AWS Lake Formation principals. Supported principals are IAM users or IAM roles.
Type: Array of [DataLakePrincipal](API_DataLakePrincipal.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** ExternalDataFilteringAllowList **   <a name="lakeformation-Type-DataLakeSettings-ExternalDataFilteringAllowList"></a>
A list of the account IDs of AWS accounts with Amazon EMR clusters that are to perform data filtering.>
Type: Array of [DataLakePrincipal](API_DataLakePrincipal.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** Parameters **   <a name="lakeformation-Type-DataLakeSettings-Parameters"></a>
A key-value map that provides an additional configuration on your data lake. CROSS\_ACCOUNT\_VERSION is the key you can configure in the Parameters field. Accepted values for the CrossAccountVersion key are 1, 2, 3, and 4.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** ReadOnlyAdmins **   <a name="lakeformation-Type-DataLakeSettings-ReadOnlyAdmins"></a>
A list of AWS Lake Formation principals with only view access to the resources, without the ability to make changes. Supported principals are IAM users or IAM roles.
Type: Array of [DataLakePrincipal](API_DataLakePrincipal.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** TrustedResourceOwners **   <a name="lakeformation-Type-DataLakeSettings-TrustedResourceOwners"></a>
A list of the resource-owning account IDs that the caller's account can use to share their user access details (user ARNs). The user ARNs can be logged in the resource owner's CloudTrail log.
You may want to specify this property when you are in a high-trust boundary, such as the same team or company.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_DataLakeSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DataLakeSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DataLakeSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DataLakeSettings)

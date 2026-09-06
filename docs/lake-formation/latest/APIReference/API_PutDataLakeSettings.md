---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_PutDataLakeSettings.html
---

# PutDataLakeSettings
<a name="API_PutDataLakeSettings"></a>

Sets the list of data lake administrators who have admin privileges on all resources managed by AWS Lake Formation. For more information on admin privileges, see [Granting Lake Formation Permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/lake-formation-permissions.html).

This API replaces the current list of data lake admins with the new list being passed. To add an admin, fetch the current list and add the new admin to that list and pass that list in this API.

## Request Syntax
<a name="API_PutDataLakeSettings_RequestSyntax"></a>

```
POST /PutDataLakeSettings HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}",
   "DataLakeSettings": {
      "AllowExternalDataFiltering": {{boolean}},
      "AllowFullTableExternalDataAccess": {{boolean}},
      "AuthorizedSessionTagValueList": [ "{{string}}" ],
      "CreateDatabaseDefaultPermissions": [
         {
            "Permissions": [ "{{string}}" ],
            "Principal": {
               "DataLakePrincipalIdentifier": "{{string}}"
            }
         }
      ],
      "CreateTableDefaultPermissions": [
         {
            "Permissions": [ "{{string}}" ],
            "Principal": {
               "DataLakePrincipalIdentifier": "{{string}}"
            }
         }
      ],
      "DataLakeAdmins": [
         {
            "DataLakePrincipalIdentifier": "{{string}}"
         }
      ],
      "ExternalDataFilteringAllowList": [
         {
            "DataLakePrincipalIdentifier": "{{string}}"
         }
      ],
      "Parameters": {
         "{{string}}" : "{{string}}"
      },
      "ReadOnlyAdmins": [
         {
            "DataLakePrincipalIdentifier": "{{string}}"
         }
      ],
      "TrustedResourceOwners": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_PutDataLakeSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutDataLakeSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_PutDataLakeSettings_RequestSyntax) **   <a name="lakeformation-PutDataLakeSettings-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [DataLakeSettings](#API_PutDataLakeSettings_RequestSyntax) **   <a name="lakeformation-PutDataLakeSettings-request-DataLakeSettings"></a>
A structure representing a list of Lake Formation principals designated as data lake administrators.
Type: [DataLakeSettings](API_DataLakeSettings.md) object
Required: Yes

## Response Syntax
<a name="API_PutDataLakeSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutDataLakeSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutDataLakeSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_PutDataLakeSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/PutDataLakeSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/PutDataLakeSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/PutDataLakeSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/PutDataLakeSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/PutDataLakeSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/PutDataLakeSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/PutDataLakeSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/PutDataLakeSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/PutDataLakeSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/PutDataLakeSettings)

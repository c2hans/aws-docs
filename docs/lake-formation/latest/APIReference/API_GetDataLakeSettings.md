---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetDataLakeSettings.html
---

# GetDataLakeSettings
<a name="API_GetDataLakeSettings"></a>

Retrieves the list of the data lake administrators of a AWS Lake Formation-managed data lake.

## Request Syntax
<a name="API_GetDataLakeSettings_RequestSyntax"></a>

```
POST /GetDataLakeSettings HTTP/1.1
Content-type: application/json

{
   "CatalogId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetDataLakeSettings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDataLakeSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetDataLakeSettings_RequestSyntax) **   <a name="lakeformation-GetDataLakeSettings-request-CatalogId"></a>
The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## Response Syntax
<a name="API_GetDataLakeSettings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataLakeSettings": {
      "AllowExternalDataFiltering": boolean,
      "AllowFullTableExternalDataAccess": boolean,
      "AuthorizedSessionTagValueList": [ "string" ],
      "CreateDatabaseDefaultPermissions": [
         {
            "Permissions": [ "string" ],
            "Principal": {
               "DataLakePrincipalIdentifier": "string"
            }
         }
      ],
      "CreateTableDefaultPermissions": [
         {
            "Permissions": [ "string" ],
            "Principal": {
               "DataLakePrincipalIdentifier": "string"
            }
         }
      ],
      "DataLakeAdmins": [
         {
            "DataLakePrincipalIdentifier": "string"
         }
      ],
      "ExternalDataFilteringAllowList": [
         {
            "DataLakePrincipalIdentifier": "string"
         }
      ],
      "Parameters": {
         "string" : "string"
      },
      "ReadOnlyAdmins": [
         {
            "DataLakePrincipalIdentifier": "string"
         }
      ],
      "TrustedResourceOwners": [ "string" ]
   }
}
```

## Response Elements
<a name="API_GetDataLakeSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataLakeSettings](#API_GetDataLakeSettings_ResponseSyntax) **   <a name="lakeformation-GetDataLakeSettings-response-DataLakeSettings"></a>
A structure representing a list of Lake Formation principals designated as data lake administrators.
Type: [DataLakeSettings](API_DataLakeSettings.md) object

## Errors
<a name="API_GetDataLakeSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

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
<a name="API_GetDataLakeSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/GetDataLakeSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/GetDataLakeSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/GetDataLakeSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/GetDataLakeSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/GetDataLakeSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/GetDataLakeSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/GetDataLakeSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/GetDataLakeSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/GetDataLakeSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/GetDataLakeSettings)

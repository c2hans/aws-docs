---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListLakeFormationOptIns.html
---

# ListLakeFormationOptIns
<a name="API_ListLakeFormationOptIns"></a>

Retrieve the current list of resources and principals that are opt in to enforce Lake Formation permissions.

## Request Syntax
<a name="API_ListLakeFormationOptIns_RequestSyntax"></a>

```
POST /ListLakeFormationOptIns HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Principal": {
      "DataLakePrincipalIdentifier": "{{string}}"
   },
   "Resource": {
      "Catalog": {
         "Id": "{{string}}"
      },
      "Database": {
         "CatalogId": "{{string}}",
         "Name": "{{string}}"
      },
      "DataCellsFilter": {
         "DatabaseName": "{{string}}",
         "Name": "{{string}}",
         "TableCatalogId": "{{string}}",
         "TableName": "{{string}}"
      },
      "DataLocation": {
         "CatalogId": "{{string}}",
         "ResourceArn": "{{string}}"
      },
      "LFTag": {
         "CatalogId": "{{string}}",
         "TagKey": "{{string}}",
         "TagValues": [ "{{string}}" ]
      },
      "LFTagExpression": {
         "CatalogId": "{{string}}",
         "Name": "{{string}}"
      },
      "LFTagPolicy": {
         "CatalogId": "{{string}}",
         "Expression": [
            {
               "TagKey": "{{string}}",
               "TagValues": [ "{{string}}" ]
            }
         ],
         "ExpressionName": "{{string}}",
         "ResourceType": "{{string}}"
      },
      "Table": {
         "CatalogId": "{{string}}",
         "DatabaseName": "{{string}}",
         "Name": "{{string}}",
         "TableWildcard": {
         }
      },
      "TableWithColumns": {
         "CatalogId": "{{string}}",
         "ColumnNames": [ "{{string}}" ],
         "ColumnWildcard": {
            "ExcludedColumnNames": [ "{{string}}" ]
         },
         "DatabaseName": "{{string}}",
         "Name": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_ListLakeFormationOptIns_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLakeFormationOptIns_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListLakeFormationOptIns_RequestSyntax) **   <a name="lakeformation-ListLakeFormationOptIns-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListLakeFormationOptIns_RequestSyntax) **   <a name="lakeformation-ListLakeFormationOptIns-request-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String
Required: No

 ** [Principal](#API_ListLakeFormationOptIns_RequestSyntax) **   <a name="lakeformation-ListLakeFormationOptIns-request-Principal"></a>
The AWS Lake Formation principal. Supported principals are IAM users or IAM roles.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

 ** [Resource](#API_ListLakeFormationOptIns_RequestSyntax) **   <a name="lakeformation-ListLakeFormationOptIns-request-Resource"></a>
A structure for the resource.
Type: [Resource](API_Resource.md) object
Required: No

## Response Syntax
<a name="API_ListLakeFormationOptIns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LakeFormationOptInsInfoList": [
      {
         "Condition": {
            "Expression": "string"
         },
         "LastModified": number,
         "LastUpdatedBy": "string",
         "Principal": {
            "DataLakePrincipalIdentifier": "string"
         },
         "Resource": {
            "Catalog": {
               "Id": "string"
            },
            "Database": {
               "CatalogId": "string",
               "Name": "string"
            },
            "DataCellsFilter": {
               "DatabaseName": "string",
               "Name": "string",
               "TableCatalogId": "string",
               "TableName": "string"
            },
            "DataLocation": {
               "CatalogId": "string",
               "ResourceArn": "string"
            },
            "LFTag": {
               "CatalogId": "string",
               "TagKey": "string",
               "TagValues": [ "string" ]
            },
            "LFTagExpression": {
               "CatalogId": "string",
               "Name": "string"
            },
            "LFTagPolicy": {
               "CatalogId": "string",
               "Expression": [
                  {
                     "TagKey": "string",
                     "TagValues": [ "string" ]
                  }
               ],
               "ExpressionName": "string",
               "ResourceType": "string"
            },
            "Table": {
               "CatalogId": "string",
               "DatabaseName": "string",
               "Name": "string",
               "TableWildcard": {
               }
            },
            "TableWithColumns": {
               "CatalogId": "string",
               "ColumnNames": [ "string" ],
               "ColumnWildcard": {
                  "ExcludedColumnNames": [ "string" ]
               },
               "DatabaseName": "string",
               "Name": "string"
            }
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLakeFormationOptIns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LakeFormationOptInsInfoList](#API_ListLakeFormationOptIns_ResponseSyntax) **   <a name="lakeformation-ListLakeFormationOptIns-response-LakeFormationOptInsInfoList"></a>
A list of principal-resource pairs that have Lake Formation permissins enforced.
Type: Array of [LakeFormationOptInsInfo](API_LakeFormationOptInsInfo.md) objects

 ** [NextToken](#API_ListLakeFormationOptIns_ResponseSyntax) **   <a name="lakeformation-ListLakeFormationOptIns-response-NextToken"></a>
A continuation token, if this is not the first call to retrieve this list.
Type: String

## Errors
<a name="API_ListLakeFormationOptIns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListLakeFormationOptIns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ListLakeFormationOptIns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ListLakeFormationOptIns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ListLakeFormationOptIns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ListLakeFormationOptIns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ListLakeFormationOptIns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ListLakeFormationOptIns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ListLakeFormationOptIns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ListLakeFormationOptIns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ListLakeFormationOptIns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ListLakeFormationOptIns)

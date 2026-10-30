---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListRLSPolicyAttachments.html
---

# ListRLSPolicyAttachments
<a name="API_ListRLSPolicyAttachments"></a>

Lists the row-level security policy attachments in the Data Catalog. You can filter the results by resource, principal, or policy name.

## Request Syntax
<a name="API_ListRLSPolicyAttachments_RequestSyntax"></a>

```
POST /ListRLSPolicyAttachments HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PolicyName": "{{string}}",
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
      "RLSPolicy": {
         "CatalogId": "{{string}}",
         "Name": "{{string}}"
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
<a name="API_ListRLSPolicyAttachments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListRLSPolicyAttachments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRLSPolicyAttachments_RequestSyntax) **   <a name="lakeformation-ListRLSPolicyAttachments-request-MaxResults"></a>
The maximum number of attachments to return in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListRLSPolicyAttachments_RequestSyntax) **   <a name="lakeformation-ListRLSPolicyAttachments-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [PolicyName](#API_ListRLSPolicyAttachments_RequestSyntax) **   <a name="lakeformation-ListRLSPolicyAttachments-request-PolicyName"></a>
If specified, returns only the attachments for the row-level security policy with this name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Principal](#API_ListRLSPolicyAttachments_RequestSyntax) **   <a name="lakeformation-ListRLSPolicyAttachments-request-Principal"></a>
If specified, returns only the attachments for the given principal.
Type: [DataLakePrincipal](API_DataLakePrincipal.md) object
Required: No

 ** [Resource](#API_ListRLSPolicyAttachments_RequestSyntax) **   <a name="lakeformation-ListRLSPolicyAttachments-request-Resource"></a>
If specified, returns only the attachments for the given resource.
Type: [Resource](API_Resource.md) object
Required: No

## Response Syntax
<a name="API_ListRLSPolicyAttachments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RLSPolicyAttachments": [
      {
         "CatalogId": "string",
         "Condition": {
            "Expression": "string"
         },
         "DefaultRLSPolicy": boolean,
         "PolicyName": "string",
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
            "RLSPolicy": {
               "CatalogId": "string",
               "Name": "string"
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
   ]
}
```

## Response Elements
<a name="API_ListRLSPolicyAttachments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRLSPolicyAttachments_ResponseSyntax) **   <a name="lakeformation-ListRLSPolicyAttachments-response-NextToken"></a>
A continuation token, if not all attachments have been returned.
Type: String

 ** [RLSPolicyAttachments](#API_ListRLSPolicyAttachments_ResponseSyntax) **   <a name="lakeformation-ListRLSPolicyAttachments-response-RLSPolicyAttachments"></a>
A list of `RLSPolicyAttachment` structures.
Type: Array of [RLSPolicyAttachment](API_RLSPolicyAttachment.md) objects

## Errors
<a name="API_ListRLSPolicyAttachments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListRLSPolicyAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/ListRLSPolicyAttachments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/ListRLSPolicyAttachments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/ListRLSPolicyAttachments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/ListRLSPolicyAttachments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/ListRLSPolicyAttachments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/ListRLSPolicyAttachments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/ListRLSPolicyAttachments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/ListRLSPolicyAttachments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/ListRLSPolicyAttachments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/ListRLSPolicyAttachments)

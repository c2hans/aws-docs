---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetCatalogs.html
---

# GetCatalogs
<a name="API_GetCatalogs"></a>

Retrieves all catalogs defined in a catalog in the AWS Glue Data Catalog. For a Redshift-federated catalog use case, this operation returns the list of catalogs mapped to Redshift databases in the Redshift namespace catalog.

## Request Syntax
<a name="API_GetCatalogs_RequestSyntax"></a>

```
{
   "IncludeRoot": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ParentCatalogId": "{{string}}",
   "Recursive": {{boolean}}
}
```

## Request Parameters
<a name="API_GetCatalogs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IncludeRoot](#API_GetCatalogs_RequestSyntax) **   <a name="Glue-GetCatalogs-request-IncludeRoot"></a>
Whether to list the default catalog in the account and region in the response. Defaults to `false`. When `true` and `ParentCatalogId = NULL | AWS Account ID`, all catalogs and the default catalog are enumerated in the response.
When the `ParentCatalogId` is not equal to null, and this attribute is passed as `false` or `true`, an `InvalidInputException` is thrown.
Type: Boolean
Required: No

 ** [MaxResults](#API_GetCatalogs_RequestSyntax) **   <a name="Glue-GetCatalogs-request-MaxResults"></a>
The maximum number of catalogs to return in one response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetCatalogs_RequestSyntax) **   <a name="Glue-GetCatalogs-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [ParentCatalogId](#API_GetCatalogs_RequestSyntax) **   <a name="Glue-GetCatalogs-request-ParentCatalogId"></a>
The ID of the parent catalog in which the catalog resides. If none is provided, the AWS Account Number is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Recursive](#API_GetCatalogs_RequestSyntax) **   <a name="Glue-GetCatalogs-request-Recursive"></a>
Whether to list all catalogs across the catalog hierarchy, starting from the `ParentCatalogId`. Defaults to `false` . When `true`, all catalog objects in the `ParentCatalogID` hierarchy are enumerated in the response.
Type: Boolean
Required: No

## Response Syntax
<a name="API_GetCatalogs_ResponseSyntax"></a>

```
{
   "CatalogList": [
      {
         "AllowFullTableExternalDataAccess": "string",
         "CatalogId": "string",
         "CatalogProperties": {
            "CustomProperties": {
               "string" : "string"
            },
            "DataLakeAccessProperties": {
               "CatalogType": "string",
               "DataLakeAccess": boolean,
               "DataTransferRole": "string",
               "KmsKey": "string",
               "ManagedWorkgroupName": "string",
               "ManagedWorkgroupStatus": "string",
               "RedshiftDatabaseName": "string",
               "StatusMessage": "string"
            },
            "IcebergOptimizationProperties": {
               "Compaction": {
                  "string" : "string"
               },
               "LastUpdatedTime": number,
               "OrphanFileDeletion": {
                  "string" : "string"
               },
               "Retention": {
                  "string" : "string"
               },
               "RoleArn": "string"
            }
         },
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
         "CreateTime": number,
         "Description": "string",
         "FederatedCatalog": {
            "ConnectionName": "string",
            "ConnectionType": "string",
            "Identifier": "string"
         },
         "Name": "string",
         "Parameters": {
            "string" : "string"
         },
         "ResourceArn": "string",
         "TargetRedshiftCatalog": {
            "CatalogArn": "string"
         },
         "UpdateTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetCatalogs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CatalogList](#API_GetCatalogs_ResponseSyntax) **   <a name="Glue-GetCatalogs-response-CatalogList"></a>
An array of `Catalog` objects. A list of `Catalog` objects from the specified parent catalog.
Type: Array of [Catalog](API_Catalog.md) objects

 ** [NextToken](#API_GetCatalogs_ResponseSyntax) **   <a name="Glue-GetCatalogs-response-NextToken"></a>
A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.
Type: String

## Errors
<a name="API_GetCatalogs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** FederationSourceException **
A federation source failed.
 ** FederationSourceErrorCode **
The error code of the problem.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** FederationSourceRetryableException **
A federation source failed, but the operation may be retried.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetCatalogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetCatalogs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetCatalogs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetCatalogs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetCatalogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetCatalogs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetCatalogs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetCatalogs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetCatalogs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetCatalogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetCatalogs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

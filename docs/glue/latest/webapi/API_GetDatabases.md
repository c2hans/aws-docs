---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetDatabases.html
---

# GetDatabases
<a name="API_GetDatabases"></a>

Retrieves all databases defined in a given Data Catalog.

## Request Syntax
<a name="API_GetDatabases_RequestSyntax"></a>

```
{
   "AttributesToGet": [ "{{string}}" ],
   "CatalogId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceShareType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDatabases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributesToGet](#API_GetDatabases_RequestSyntax) **   <a name="Glue-GetDatabases-request-AttributesToGet"></a>
Specifies the database fields returned by the `GetDatabases` call. This parameter doesn’t accept an empty list. The request must include the `NAME`.
Type: Array of strings
Valid Values: `NAME | TARGET_DATABASE`
Required: No

 ** [CatalogId](#API_GetDatabases_RequestSyntax) **   <a name="Glue-GetDatabases-request-CatalogId"></a>
The ID of the Data Catalog from which to retrieve `Databases`. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [MaxResults](#API_GetDatabases_RequestSyntax) **   <a name="Glue-GetDatabases-request-MaxResults"></a>
The maximum number of databases to return in one response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetDatabases_RequestSyntax) **   <a name="Glue-GetDatabases-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

 ** [ResourceShareType](#API_GetDatabases_RequestSyntax) **   <a name="Glue-GetDatabases-request-ResourceShareType"></a>
Allows you to specify that you want to list the databases shared with your account. The allowable values are `FEDERATED`, `FOREIGN` or `ALL`.
+ If set to `FEDERATED`, will list the federated databases (referencing an external entity) shared with your account.
+ If set to `FOREIGN`, will list the databases shared with your account.
+ If set to `ALL`, will list the databases shared with your account, as well as the databases in yor local account.
Type: String
Valid Values: `FOREIGN | ALL | FEDERATED`
Required: No

## Response Syntax
<a name="API_GetDatabases_ResponseSyntax"></a>

```
{
   "DatabaseList": [
      {
         "CatalogId": "string",
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
         "FederatedDatabase": {
            "ConnectionName": "string",
            "ConnectionType": "string",
            "Identifier": "string"
         },
         "LocationUri": "string",
         "Name": "string",
         "Parameters": {
            "string" : "string"
         },
         "TargetDatabase": {
            "CatalogId": "string",
            "DatabaseName": "string",
            "Region": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetDatabases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatabaseList](#API_GetDatabases_ResponseSyntax) **   <a name="Glue-GetDatabases-response-DatabaseList"></a>
A list of `Database` objects from the specified catalog.
Type: Array of [Database](API_Database.md) objects

 ** [NextToken](#API_GetDatabases_ResponseSyntax) **   <a name="Glue-GetDatabases-response-NextToken"></a>
A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.
Type: String

## Errors
<a name="API_GetDatabases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_GetDatabases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetDatabases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetDatabases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetDatabases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetDatabases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetDatabases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetDatabases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetDatabases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetDatabases)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetDatabases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetDatabases)

---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetEntityRecords.html
---

# GetEntityRecords
<a name="API_GetEntityRecords"></a>

This API is used to query preview data from a given connection type or from a native Amazon S3 based AWS Glue Data Catalog.

Returns records as an array of JSON blobs. Each record is formatted using Jackson JsonNode based on the field type defined by the `DescribeEntity` API.

Spark connectors generate schemas according to the same data type mapping as in the `DescribeEntity` API. Spark connectors convert data to the appropriate data types matching the schema when returning rows.

## Request Syntax
<a name="API_GetEntityRecords_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "ConnectionName": "{{string}}",
   "ConnectionOptions": {
      "{{string}}" : "{{string}}"
   },
   "DataStoreApiVersion": "{{string}}",
   "EntityName": "{{string}}",
   "FilterPredicate": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "OrderBy": "{{string}}",
   "SelectedFields": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetEntityRecords_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-CatalogId"></a>
The catalog ID of the catalog that contains the connection. This can be null, By default, the AWS Account ID is the catalog ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ConnectionName](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-ConnectionName"></a>
The name of the connection that contains the connection type credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ConnectionOptions](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-ConnectionOptions"></a>
Connector options that are required to query the data.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[\w]*`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `[\S]*`
Required: No

 ** [DataStoreApiVersion](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-DataStoreApiVersion"></a>
The API version of the SaaS connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9.-]*`
Required: No

 ** [EntityName](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-EntityName"></a>
Name of the entity that we want to query the preview data from the given connection type.
Type: String
Required: Yes

 ** [FilterPredicate](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-FilterPredicate"></a>
A filter predicate that you can apply in the query request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: No

 ** [Limit](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-Limit"></a>
Limits the number of records fetched with the request.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** [NextToken](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-NextToken"></a>
A continuation token, included if this is a continuation call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/:_]*`
Required: No

 ** [OrderBy](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-OrderBy"></a>
A parameter that orders the response preview data.
Type: String
Required: No

 ** [SelectedFields](#API_GetEntityRecords_RequestSyntax) **   <a name="Glue-GetEntityRecords-request-SelectedFields"></a>
 List of fields that we want to fetch as part of preview data.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Required: No

## Response Syntax
<a name="API_GetEntityRecords_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Records": [ JSON value ]
}
```

## Response Elements
<a name="API_GetEntityRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetEntityRecords_ResponseSyntax) **   <a name="Glue-GetEntityRecords-response-NextToken"></a>
A continuation token, present if the current segment is not the last.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/:_]*`

 ** [Records](#API_GetEntityRecords_ResponseSyntax) **   <a name="Glue-GetEntityRecords-response-Records"></a>
A list of the requested objects.
Type: Array of JSON values

## Errors
<a name="API_GetEntityRecords_Errors"></a>

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

 ** GlueEncryptionException **
An encryption operation failed.
 ** Message **
The message describing the problem.
HTTP Status Code: 400

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

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetEntityRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetEntityRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetEntityRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetEntityRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetEntityRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetEntityRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetEntityRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetEntityRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetEntityRecords)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetEntityRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetEntityRecords)

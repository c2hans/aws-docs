---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DescribeEntity.html
---

# DescribeEntity
<a name="API_DescribeEntity"></a>

Provides details regarding the entity used with the connection type, with a description of the data model for each field in the selected entity.

 The response includes all the fields which make up the entity.

## Request Syntax
<a name="API_DescribeEntity_RequestSyntax"></a>

```
{
   "CatalogId": "{{string}}",
   "ConnectionName": "{{string}}",
   "DataStoreApiVersion": "{{string}}",
   "EntityName": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEntity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CatalogId](#API_DescribeEntity_RequestSyntax) **   <a name="Glue-DescribeEntity-request-CatalogId"></a>
The catalog ID of the catalog that contains the connection. This can be null, By default, the AWS Account ID is the catalog ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [ConnectionName](#API_DescribeEntity_RequestSyntax) **   <a name="Glue-DescribeEntity-request-ConnectionName"></a>
The name of the connection that contains the connection type credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [DataStoreApiVersion](#API_DescribeEntity_RequestSyntax) **   <a name="Glue-DescribeEntity-request-DataStoreApiVersion"></a>
The version of the API used for the data store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9.-]*`
Required: No

 ** [EntityName](#API_DescribeEntity_RequestSyntax) **   <a name="Glue-DescribeEntity-request-EntityName"></a>
The name of the entity that you want to describe from the connection type.
Type: String
Required: Yes

 ** [NextToken](#API_DescribeEntity_RequestSyntax) **   <a name="Glue-DescribeEntity-request-NextToken"></a>
A continuation token, included if this is a continuation call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/:_]*`
Required: No

## Response Syntax
<a name="API_DescribeEntity_ResponseSyntax"></a>

```
{
   "Fields": [
      {
         "CustomProperties": {
            "string" : "string"
         },
         "Description": "string",
         "FieldName": "string",
         "FieldType": "string",
         "IsCreateable": boolean,
         "IsDefaultOnCreate": boolean,
         "IsFilterable": boolean,
         "IsNullable": boolean,
         "IsPartitionable": boolean,
         "IsPrimaryKey": boolean,
         "IsRetrievable": boolean,
         "IsUpdateable": boolean,
         "IsUpsertable": boolean,
         "Label": "string",
         "NativeDataType": "string",
         "ParentField": "string",
         "SupportedFilterOperators": [ "string" ],
         "SupportedValues": [ "string" ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeEntity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Fields](#API_DescribeEntity_ResponseSyntax) **   <a name="Glue-DescribeEntity-response-Fields"></a>
Describes the fields for that connector entity. This is the list of `Field` objects. `Field` is very similar to column in a database. The `Field` object has information about different properties associated with fields in the connector.
Type: Array of [Field](API_Field.md) objects

 ** [NextToken](#API_DescribeEntity_ResponseSyntax) **   <a name="Glue-DescribeEntity-response-NextToken"></a>
A continuation token, present if the current segment is not the last.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[-a-zA-Z0-9+=/:_]*`

## Errors
<a name="API_DescribeEntity_Errors"></a>

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
<a name="API_DescribeEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/DescribeEntity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/DescribeEntity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DescribeEntity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/DescribeEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DescribeEntity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/DescribeEntity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/DescribeEntity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/DescribeEntity)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/DescribeEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DescribeEntity)

---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ListIntegrationTableProperties.html
---

# ListIntegrationTableProperties
<a name="API_ListIntegrationTableProperties"></a>

Lists the integration table properties in your account. This operation supports filtering and pagination.

## Request Syntax
<a name="API_ListIntegrationTableProperties_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "Marker": "{{string}}",
   "MaxRecords": {{number}}
}
```

## Request Parameters
<a name="API_ListIntegrationTableProperties_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListIntegrationTableProperties_RequestSyntax) **   <a name="Glue-ListIntegrationTableProperties-request-Filters"></a>
A list of filters. Supported filter keys are `SourceArn`, `TargetArn`, `SourceTableName`, and `TargetTableName`.
Type: Array of [IntegrationTablePropertiesFilter](API_IntegrationTablePropertiesFilter.md) objects
Required: No

 ** [Marker](#API_ListIntegrationTableProperties_RequestSyntax) **   <a name="Glue-ListIntegrationTableProperties-request-Marker"></a>
The pagination token for the next page of results. The initial value is `null`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [MaxRecords](#API_ListIntegrationTableProperties_RequestSyntax) **   <a name="Glue-ListIntegrationTableProperties-request-MaxRecords"></a>
The maximum number of records to return in the response.
Type: Integer
Required: No

## Response Syntax
<a name="API_ListIntegrationTableProperties_ResponseSyntax"></a>

```
{
   "IntegrationTablePropertiesList": [
      {
         "ResourceArn": "string",
         "SourceTableConfig": {
            "Fields": [ "string" ],
            "FilterPredicate": "string",
            "PrimaryKey": [ "string" ],
            "RecordUpdateField": "string"
         },
         "TableName": "string",
         "TargetTableConfig": {
            "IntegrationArn": "string",
            "PartitionSpec": [
               {
                  "ConversionSpec": "string",
                  "FieldName": "string",
                  "FunctionSpec": "string"
               }
            ],
            "TargetTableName": "string",
            "UnnestSpec": "string"
         }
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_ListIntegrationTableProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IntegrationTablePropertiesList](#API_ListIntegrationTableProperties_ResponseSyntax) **   <a name="Glue-ListIntegrationTableProperties-response-IntegrationTablePropertiesList"></a>
A list of integration table properties meeting the filter criteria.
Type: Array of [IntegrationTableProperties](API_IntegrationTableProperties.md) objects

 ** [Marker](#API_ListIntegrationTableProperties_ResponseSyntax) **   <a name="Glue-ListIntegrationTableProperties-response-Marker"></a>
The pagination token for the next page. Returns `null` if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_ListIntegrationTableProperties_Errors"></a>

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

 ** InternalServerException **
An internal server error occurred.
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
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ValidationException **
A value could not be validated.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ListIntegrationTableProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ListIntegrationTableProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ListIntegrationTableProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ListIntegrationTableProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ListIntegrationTableProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ListIntegrationTableProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ListIntegrationTableProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ListIntegrationTableProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ListIntegrationTableProperties)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ListIntegrationTableProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ListIntegrationTableProperties)

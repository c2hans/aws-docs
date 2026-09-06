---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetIntegrationTableProperties.html
---

# GetIntegrationTableProperties
<a name="API_GetIntegrationTableProperties"></a>

This API is used to retrieve optional override properties for the tables that need to be replicated. These properties can include properties for filtering and partition for source and target tables.

## Request Syntax
<a name="API_GetIntegrationTableProperties_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "TableName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetIntegrationTableProperties_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_GetIntegrationTableProperties_RequestSyntax) **   <a name="Glue-GetIntegrationTableProperties-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the target table for which to retrieve integration table properties. Currently, this API only supports retrieving properties for target tables, and the provided ARN should be the ARN of the target table in the AWS Glue Data Catalog. Support for retrieving integration table properties for source connections (using the connection ARN) is not yet implemented and will be added in a future release.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [TableName](#API_GetIntegrationTableProperties_RequestSyntax) **   <a name="Glue-GetIntegrationTableProperties-request-TableName"></a>
The name of the table to be replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Response Syntax
<a name="API_GetIntegrationTableProperties_ResponseSyntax"></a>

```
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
```

## Response Elements
<a name="API_GetIntegrationTableProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceArn](#API_GetIntegrationTableProperties_ResponseSyntax) **   <a name="Glue-GetIntegrationTableProperties-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the target table for which to retrieve integration table properties. Currently, this API only supports retrieving properties for target tables, and the provided ARN should be the ARN of the target table in the AWS Glue Data Catalog. Support for retrieving integration table properties for source connections (using the connection ARN) is not yet implemented and will be added in a future release.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.

 ** [SourceTableConfig](#API_GetIntegrationTableProperties_ResponseSyntax) **   <a name="Glue-GetIntegrationTableProperties-response-SourceTableConfig"></a>
A structure for the source table configuration.
Type: [SourceTableConfig](API_SourceTableConfig.md) object

 ** [TableName](#API_GetIntegrationTableProperties_ResponseSyntax) **   <a name="Glue-GetIntegrationTableProperties-response-TableName"></a>
The name of the table to be replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

 ** [TargetTableConfig](#API_GetIntegrationTableProperties_ResponseSyntax) **   <a name="Glue-GetIntegrationTableProperties-response-TargetTableConfig"></a>
A structure for the target table configuration.
Type: [TargetTableConfig](API_TargetTableConfig.md) object

## Errors
<a name="API_GetIntegrationTableProperties_Errors"></a>

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
<a name="API_GetIntegrationTableProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetIntegrationTableProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetIntegrationTableProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetIntegrationTableProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetIntegrationTableProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetIntegrationTableProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetIntegrationTableProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetIntegrationTableProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetIntegrationTableProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetIntegrationTableProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetIntegrationTableProperties)

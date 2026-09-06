---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateIntegrationTableProperties.html
---

# UpdateIntegrationTableProperties
<a name="API_UpdateIntegrationTableProperties"></a>

This API is used to provide optional override properties for the tables that need to be replicated. These properties can include properties for filtering and partitioning for the source and target tables. To set both source and target properties the same API need to be invoked with the AWS Glue connection ARN as `ResourceArn` with `SourceTableConfig`, and the AWS Glue database ARN as `ResourceArn` with `TargetTableConfig` respectively.

The override will be reflected across all the integrations using same `ResourceArn` and source table.

## Request Syntax
<a name="API_UpdateIntegrationTableProperties_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "SourceTableConfig": {
      "Fields": [ "{{string}}" ],
      "FilterPredicate": "{{string}}",
      "PrimaryKey": [ "{{string}}" ],
      "RecordUpdateField": "{{string}}"
   },
   "TableName": "{{string}}",
   "TargetTableConfig": {
      "PartitionSpec": [
         {
            "ConversionSpec": "{{string}}",
            "FieldName": "{{string}}",
            "FunctionSpec": "{{string}}"
         }
      ],
      "TargetTableName": "{{string}}",
      "UnnestSpec": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateIntegrationTableProperties_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_UpdateIntegrationTableProperties_RequestSyntax) **   <a name="Glue-UpdateIntegrationTableProperties-request-ResourceArn"></a>
The connection ARN of the source, or the database ARN of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** [SourceTableConfig](#API_UpdateIntegrationTableProperties_RequestSyntax) **   <a name="Glue-UpdateIntegrationTableProperties-request-SourceTableConfig"></a>
A structure for the source table configuration.
Type: [SourceTableConfig](API_SourceTableConfig.md) object
Required: No

 ** [TableName](#API_UpdateIntegrationTableProperties_RequestSyntax) **   <a name="Glue-UpdateIntegrationTableProperties-request-TableName"></a>
The name of the table to be replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [TargetTableConfig](#API_UpdateIntegrationTableProperties_RequestSyntax) **   <a name="Glue-UpdateIntegrationTableProperties-request-TargetTableConfig"></a>
A structure for the target table configuration.
Type: [TargetTableConfig](API_TargetTableConfig.md) object
Required: No

## Response Elements
<a name="API_UpdateIntegrationTableProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateIntegrationTableProperties_Errors"></a>

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
<a name="API_UpdateIntegrationTableProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateIntegrationTableProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateIntegrationTableProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateIntegrationTableProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateIntegrationTableProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateIntegrationTableProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateIntegrationTableProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateIntegrationTableProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateIntegrationTableProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateIntegrationTableProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateIntegrationTableProperties)

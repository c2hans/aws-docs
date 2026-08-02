---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetMapping.html
---

# GetMapping
<a name="API_GetMapping"></a>

Creates mappings.

## Request Syntax
<a name="API_GetMapping_RequestSyntax"></a>

```
{
   "Location": {
      "DynamoDB": [
         {
            "Name": "{{string}}",
            "Param": {{boolean}},
            "Value": "{{string}}"
         }
      ],
      "Jdbc": [
         {
            "Name": "{{string}}",
            "Param": {{boolean}},
            "Value": "{{string}}"
         }
      ],
      "S3": [
         {
            "Name": "{{string}}",
            "Param": {{boolean}},
            "Value": "{{string}}"
         }
      ]
   },
   "Sinks": [
      {
         "DatabaseName": "{{string}}",
         "TableName": "{{string}}"
      }
   ],
   "Source": {
      "DatabaseName": "{{string}}",
      "TableName": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetMapping_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Location](#API_GetMapping_RequestSyntax) **   <a name="Glue-GetMapping-request-Location"></a>
Parameters for the mapping.
Type: [Location](API_Location.md) object
Required: No

 ** [Sinks](#API_GetMapping_RequestSyntax) **   <a name="Glue-GetMapping-request-Sinks"></a>
A list of target tables.
Type: Array of [CatalogEntry](API_CatalogEntry.md) objects
Required: No

 ** [Source](#API_GetMapping_RequestSyntax) **   <a name="Glue-GetMapping-request-Source"></a>
Specifies the source table.
Type: [CatalogEntry](API_CatalogEntry.md) object
Required: Yes

## Response Syntax
<a name="API_GetMapping_ResponseSyntax"></a>

```
{
   "Mapping": [
      {
         "SourcePath": "string",
         "SourceTable": "string",
         "SourceType": "string",
         "TargetPath": "string",
         "TargetTable": "string",
         "TargetType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Mapping](#API_GetMapping_ResponseSyntax) **   <a name="Glue-GetMapping-response-Mapping"></a>
A list of mappings to the specified targets.
Type: Array of [MappingEntry](API_MappingEntry.md) objects

## Errors
<a name="API_GetMapping_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
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

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetMapping)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetMapping)

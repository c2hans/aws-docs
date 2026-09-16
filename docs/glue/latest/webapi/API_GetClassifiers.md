---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetClassifiers.html
---

# GetClassifiers
<a name="API_GetClassifiers"></a>

Lists all classifier objects in the Data Catalog.

## Request Syntax
<a name="API_GetClassifiers_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetClassifiers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_GetClassifiers_RequestSyntax) **   <a name="Glue-GetClassifiers-request-MaxResults"></a>
The size of the list to return (optional).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetClassifiers_RequestSyntax) **   <a name="Glue-GetClassifiers-request-NextToken"></a>
An optional continuation token.
Type: String
Required: No

## Response Syntax
<a name="API_GetClassifiers_ResponseSyntax"></a>

```
{
   "Classifiers": [
      {
         "CsvClassifier": {
            "AllowSingleColumn": boolean,
            "ContainsHeader": "string",
            "CreationTime": number,
            "CustomDatatypeConfigured": boolean,
            "CustomDatatypes": [ "string" ],
            "Delimiter": "string",
            "DisableValueTrimming": boolean,
            "Header": [ "string" ],
            "LastUpdated": number,
            "Name": "string",
            "QuoteSymbol": "string",
            "Serde": "string",
            "Version": number
         },
         "GrokClassifier": {
            "Classification": "string",
            "CreationTime": number,
            "CustomPatterns": "string",
            "GrokPattern": "string",
            "LastUpdated": number,
            "Name": "string",
            "Version": number
         },
         "JsonClassifier": {
            "CreationTime": number,
            "JsonPath": "string",
            "LastUpdated": number,
            "Name": "string",
            "Version": number
         },
         "XMLClassifier": {
            "Classification": "string",
            "CreationTime": number,
            "LastUpdated": number,
            "Name": "string",
            "RowTag": "string",
            "Version": number
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetClassifiers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Classifiers](#API_GetClassifiers_ResponseSyntax) **   <a name="Glue-GetClassifiers-response-Classifiers"></a>
The requested list of classifier objects.
Type: Array of [Classifier](API_Classifier.md) objects

 ** [NextToken](#API_GetClassifiers_ResponseSyntax) **   <a name="Glue-GetClassifiers-response-NextToken"></a>
A continuation token.
Type: String

## Errors
<a name="API_GetClassifiers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetClassifiers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetClassifiers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetClassifiers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetClassifiers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetClassifiers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetClassifiers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetClassifiers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetClassifiers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetClassifiers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetClassifiers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetClassifiers)

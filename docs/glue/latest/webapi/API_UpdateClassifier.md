---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateClassifier.html
---

# UpdateClassifier
<a name="API_UpdateClassifier"></a>

Modifies an existing classifier (a `GrokClassifier`, an `XMLClassifier`, a `JsonClassifier`, or a `CsvClassifier`, depending on which field is present).

## Request Syntax
<a name="API_UpdateClassifier_RequestSyntax"></a>

```
{
   "CsvClassifier": {
      "AllowSingleColumn": {{boolean}},
      "ContainsHeader": "{{string}}",
      "CustomDatatypeConfigured": {{boolean}},
      "CustomDatatypes": [ "{{string}}" ],
      "Delimiter": "{{string}}",
      "DisableValueTrimming": {{boolean}},
      "Header": [ "{{string}}" ],
      "Name": "{{string}}",
      "QuoteSymbol": "{{string}}",
      "Serde": "{{string}}"
   },
   "GrokClassifier": {
      "Classification": "{{string}}",
      "CustomPatterns": "{{string}}",
      "GrokPattern": "{{string}}",
      "Name": "{{string}}"
   },
   "JsonClassifier": {
      "JsonPath": "{{string}}",
      "Name": "{{string}}"
   },
   "XMLClassifier": {
      "Classification": "{{string}}",
      "Name": "{{string}}",
      "RowTag": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateClassifier_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CsvClassifier](#API_UpdateClassifier_RequestSyntax) **   <a name="Glue-UpdateClassifier-request-CsvClassifier"></a>
A `CsvClassifier` object with updated fields.
Type: [UpdateCsvClassifierRequest](API_UpdateCsvClassifierRequest.md) object
Required: No

 ** [GrokClassifier](#API_UpdateClassifier_RequestSyntax) **   <a name="Glue-UpdateClassifier-request-GrokClassifier"></a>
A `GrokClassifier` object with updated fields.
Type: [UpdateGrokClassifierRequest](API_UpdateGrokClassifierRequest.md) object
Required: No

 ** [JsonClassifier](#API_UpdateClassifier_RequestSyntax) **   <a name="Glue-UpdateClassifier-request-JsonClassifier"></a>
A `JsonClassifier` object with updated fields.
Type: [UpdateJsonClassifierRequest](API_UpdateJsonClassifierRequest.md) object
Required: No

 ** [XMLClassifier](#API_UpdateClassifier_RequestSyntax) **   <a name="Glue-UpdateClassifier-request-XMLClassifier"></a>
An `XMLClassifier` object with updated fields.
Type: [UpdateXMLClassifierRequest](API_UpdateXMLClassifierRequest.md) object
Required: No

## Response Elements
<a name="API_UpdateClassifier_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateClassifier_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
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

 ** VersionMismatchException **
There was a version conflict.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_UpdateClassifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateClassifier)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateClassifier)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateClassifier)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateClassifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateClassifier)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateClassifier)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateClassifier)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateClassifier)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateClassifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateClassifier)

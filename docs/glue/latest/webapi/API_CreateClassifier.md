---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateClassifier.html
---

# CreateClassifier
<a name="API_CreateClassifier"></a>

Creates a classifier in the user's account. This can be a `GrokClassifier`, an `XMLClassifier`, a `JsonClassifier`, or a `CsvClassifier`, depending on which field of the request is present.

## Request Syntax
<a name="API_CreateClassifier_RequestSyntax"></a>

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
<a name="API_CreateClassifier_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CsvClassifier](#API_CreateClassifier_RequestSyntax) **   <a name="Glue-CreateClassifier-request-CsvClassifier"></a>
A `CsvClassifier` object specifying the classifier to create.
Type: [CreateCsvClassifierRequest](API_CreateCsvClassifierRequest.md) object
Required: No

 ** [GrokClassifier](#API_CreateClassifier_RequestSyntax) **   <a name="Glue-CreateClassifier-request-GrokClassifier"></a>
A `GrokClassifier` object specifying the classifier to create.
Type: [CreateGrokClassifierRequest](API_CreateGrokClassifierRequest.md) object
Required: No

 ** [JsonClassifier](#API_CreateClassifier_RequestSyntax) **   <a name="Glue-CreateClassifier-request-JsonClassifier"></a>
A `JsonClassifier` object specifying the classifier to create.
Type: [CreateJsonClassifierRequest](API_CreateJsonClassifierRequest.md) object
Required: No

 ** [XMLClassifier](#API_CreateClassifier_RequestSyntax) **   <a name="Glue-CreateClassifier-request-XMLClassifier"></a>
An `XMLClassifier` object specifying the classifier to create.
Type: [CreateXMLClassifierRequest](API_CreateXMLClassifierRequest.md) object
Required: No

## Response Elements
<a name="API_CreateClassifier_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateClassifier_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
A resource to be created or added already exists.
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

## See Also
<a name="API_CreateClassifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateClassifier)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateClassifier)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateClassifier)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateClassifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateClassifier)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateClassifier)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateClassifier)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateClassifier)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateClassifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateClassifier)

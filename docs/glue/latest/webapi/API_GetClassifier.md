---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetClassifier.html
---

# GetClassifier
<a name="API_GetClassifier"></a>

Retrieve a classifier by name.

## Request Syntax
<a name="API_GetClassifier_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetClassifier_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_GetClassifier_RequestSyntax) **   <a name="Glue-GetClassifier-request-Name"></a>
Name of the classifier to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetClassifier_ResponseSyntax"></a>

```
{
   "Classifier": {
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
}
```

## Response Elements
<a name="API_GetClassifier_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Classifier](#API_GetClassifier_ResponseSyntax) **   <a name="Glue-GetClassifier-response-Classifier"></a>
The requested classifier.
Type: [Classifier](API_Classifier.md) object

## Errors
<a name="API_GetClassifier_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
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
<a name="API_GetClassifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetClassifier)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetClassifier)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetClassifier)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetClassifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetClassifier)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetClassifier)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetClassifier)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetClassifier)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetClassifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetClassifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

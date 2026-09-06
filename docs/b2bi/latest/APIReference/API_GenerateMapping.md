---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GenerateMapping.html
---

# GenerateMapping
<a name="API_GenerateMapping"></a>

Takes sample input and output documents and uses Amazon Bedrock to generate a mapping automatically. Depending on the accuracy and other factors, you can then edit the mapping for your needs.

**Note**
Before you can use the AI-assisted feature for AWS B2B Data Interchange you must enable models in Amazon Bedrock. For details, see [AI-assisted template mapping prerequisites](https://docs.aws.amazon.com/b2bi/latest/userguide/ai-assisted-mapping.html#ai-assist-prereq) in the * AWS B2B Data Interchange User guide*.

To generate a mapping, perform the following steps:

1. Start with an X12 EDI document to use as the input.

1. Call `TestMapping` using your EDI document.

1. Use the output from the `TestMapping` operation as either input or output for your GenerateMapping call, along with your sample file.

## Request Syntax
<a name="API_GenerateMapping_RequestSyntax"></a>

```
{
   "inputFileContent": "{{string}}",
   "mappingType": "{{string}}",
   "outputFileContent": "{{string}}"
}
```

## Request Parameters
<a name="API_GenerateMapping_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [inputFileContent](#API_GenerateMapping_RequestSyntax) **   <a name="b2bi-GenerateMapping-request-inputFileContent"></a>
Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a starting point for the mapping.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5000000.
Required: Yes

 ** [mappingType](#API_GenerateMapping_RequestSyntax) **   <a name="b2bi-GenerateMapping-request-mappingType"></a>
Specify the mapping type: either `JSONATA` or `XSLT.`
Type: String
Valid Values: `JSONATA | XSLT`
Required: Yes

 ** [outputFileContent](#API_GenerateMapping_RequestSyntax) **   <a name="b2bi-GenerateMapping-request-outputFileContent"></a>
Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a target for the mapping.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5000000.
Required: Yes

## Response Syntax
<a name="API_GenerateMapping_ResponseSyntax"></a>

```
{
   "mappingAccuracy": number,
   "mappingTemplate": "string"
}
```

## Response Elements
<a name="API_GenerateMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [mappingAccuracy](#API_GenerateMapping_ResponseSyntax) **   <a name="b2bi-GenerateMapping-response-mappingAccuracy"></a>
Returns a percentage that estimates the accuracy of the generated mapping.
Type: Float
Valid Range: Minimum value of 0.0. Maximum value of 1.0.

 ** [mappingTemplate](#API_GenerateMapping_ResponseSyntax) **   <a name="b2bi-GenerateMapping-response-mappingTemplate"></a>
Returns a mapping template based on your inputs.
Type: String

## Errors
<a name="API_GenerateMapping_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.
 ** retryAfterSeconds **
The server attempts to retry a command that was throttled.
HTTP Status Code: 400

 ** ValidationException **
When you use Transformer APIs, `TestConversion`, or `TestParsing`, the service throws a validation exception if a rule is configured incorrectly. For example, a validation exception occurs when:
+ A rule references an element that doesn't exist in the selected transaction set
+ An element length rule specifies a minimum length less than 0
If your custom validation rules are configured correctly but the EDI validation fails due to those rules, this is expected behavior and doesn't result in a `ValidationException`.
For all other API operations, a validation exception occurs when a Trading Partner object can't be validated against a request from another object. This can happen during:
+ Standard EDI validation
+ Custom validation rule evaluation, such as when:
  + Element lengths don't meet specified constraints
  + Code list validations contain invalid codes
  + Required elements are missing based on your element requirement rules
HTTP Status Code: 400

## See Also
<a name="API_GenerateMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/GenerateMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/GenerateMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/GenerateMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/GenerateMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/GenerateMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/GenerateMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/GenerateMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/GenerateMapping)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/GenerateMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/GenerateMapping)

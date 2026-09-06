---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TestConversion.html
---

# TestConversion
<a name="API_TestConversion"></a>

This operation mimics the latter half of a typical Outbound EDI request. It takes an input JSON/XML in the B2Bi shape as input, converts it to an X12 EDI string, and return that string.

## Request Syntax
<a name="API_TestConversion_RequestSyntax"></a>

```
{
   "source": {
      "fileFormat": "{{string}}",
      "inputFile": { ... }
   },
   "target": {
      "advancedOptions": {
         "x12": {
            "splitOptions": {
               "splitBy": "{{string}}"
            },
            "validationOptions": {
               "validationRules": [
                  { ... }
               ]
            }
         }
      },
      "fileFormat": "{{string}}",
      "formatDetails": { ... },
      "outputSampleFile": { ... }
   }
}
```

## Request Parameters
<a name="API_TestConversion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [source](#API_TestConversion_RequestSyntax) **   <a name="b2bi-TestConversion-request-source"></a>
Specify the source file for an outbound EDI request.
Type: [ConversionSource](API_ConversionSource.md) object
Required: Yes

 ** [target](#API_TestConversion_RequestSyntax) **   <a name="b2bi-TestConversion-request-target"></a>
Specify the format (X12 is the only currently supported format), and other details for the conversion target.
Type: [ConversionTarget](API_ConversionTarget.md) object
Required: Yes

## Response Syntax
<a name="API_TestConversion_ResponseSyntax"></a>

```
{
   "convertedFileContent": "string",
   "validationMessages": [ "string" ]
}
```

## Response Elements
<a name="API_TestConversion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [convertedFileContent](#API_TestConversion_ResponseSyntax) **   <a name="b2bi-TestConversion-response-convertedFileContent"></a>
Returns the converted file content.
Type: String

 ** [validationMessages](#API_TestConversion_ResponseSyntax) **   <a name="b2bi-TestConversion-response-validationMessages"></a>
Returns an array of validation messages that AWS B2B Data Interchange generates during the conversion process. These messages include both standard EDI validation results and custom validation messages when custom validation rules are configured. Custom validation messages provide detailed feedback on element length constraints, code list validations, and element requirement checks applied during the outbound EDI generation process.
Type: Array of strings

## Errors
<a name="API_TestConversion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.
HTTP Status Code: 400

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
<a name="API_TestConversion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/TestConversion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/TestConversion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/TestConversion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/TestConversion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/TestConversion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/TestConversion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/TestConversion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/TestConversion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/TestConversion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/TestConversion)

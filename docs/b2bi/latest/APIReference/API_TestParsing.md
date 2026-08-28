---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TestParsing.html
---

# TestParsing
<a name="API_TestParsing"></a>

Parses the input EDI (electronic data interchange) file. The input file has a file size limit of 250 KB.

## Request Syntax
<a name="API_TestParsing_RequestSyntax"></a>

```
{
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
   "ediType": { ... },
   "fileFormat": "{{string}}",
   "inputFile": {
      "bucketName": "{{string}}",
      "key": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_TestParsing_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [advancedOptions](#API_TestParsing_RequestSyntax) **   <a name="b2bi-TestParsing-request-advancedOptions"></a>
Specifies advanced options for parsing the input EDI file. These options allow for more granular control over the parsing process, including split options for X12 files.
Type: [AdvancedOptions](API_AdvancedOptions.md) object
Required: No

 ** [ediType](#API_TestParsing_RequestSyntax) **   <a name="b2bi-TestParsing-request-ediType"></a>
Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.
Type: [EdiType](API_EdiType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [fileFormat](#API_TestParsing_RequestSyntax) **   <a name="b2bi-TestParsing-request-fileFormat"></a>
Specifies that the currently supported file formats for EDI transformations are `JSON` and `XML`.
Type: String
Valid Values: `XML | JSON | NOT_USED`
Required: Yes

 ** [inputFile](#API_TestParsing_RequestSyntax) **   <a name="b2bi-TestParsing-request-inputFile"></a>
Specifies an `S3Location` object, which contains the Amazon S3 bucket and prefix for the location of the input file.
Type: [S3Location](API_S3Location.md) object
Required: Yes

## Response Syntax
<a name="API_TestParsing_ResponseSyntax"></a>

```
{
   "parsedFileContent": "string",
   "parsedSplitFileContents": [ "string" ],
   "validationMessages": [ "string" ]
}
```

## Response Elements
<a name="API_TestParsing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [parsedFileContent](#API_TestParsing_ResponseSyntax) **   <a name="b2bi-TestParsing-response-parsedFileContent"></a>
Returns the contents of the input file being tested, parsed according to the specified EDI (electronic data interchange) type.
Type: String

 ** [parsedSplitFileContents](#API_TestParsing_ResponseSyntax) **   <a name="b2bi-TestParsing-response-parsedSplitFileContents"></a>
Returns an array of parsed file contents when the input file is split according to the specified split options. Each element in the array represents a separate split file's parsed content.
Type: Array of strings

 ** [validationMessages](#API_TestParsing_ResponseSyntax) **   <a name="b2bi-TestParsing-response-validationMessages"></a>
Returns an array of validation messages generated during EDI validation. These messages provide detailed information about validation errors, warnings, or confirmations based on the configured X12 validation rules such as element length constraints, code list validations, and element requirement checks. This field is populated when the `TestParsing` API validates EDI documents.
Type: Array of strings

## Errors
<a name="API_TestParsing_Errors"></a>

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

## Examples
<a name="API_TestParsing_Examples"></a>

### Example
<a name="API_TestParsing_Example_1"></a>

The following example parses the sample input file.

#### Sample Request
<a name="API_TestParsing_Example_1_Request"></a>

```
{
    "ediType": {
        "x12Details": {
            "transactionSet": "X12_110",
            "version": "VERSION_4010"
        }
    },
    "fileFormat": "JSON",
    "inputFile": {
        "bucketName": "amzn-s3-demo-bucket",
        "key": "sampleFile.txt"
    }
}
```

#### Sample Response
<a name="API_TestParsing_Example_1_Response"></a>

```
{
    "parsedFileContent": "<Sample parsed file content>"
}
```

### Example
<a name="API_TestParsing_Example_2"></a>

The following example parses the sample input file with EDI splitting enabled.

#### Sample Request
<a name="API_TestParsing_Example_2_Request"></a>

```
{
    "ediType": {
        "x12Details": {
            "transactionSet": "X12_110",
            "version": "VERSION_4010"
        }
    },
    "fileFormat": "JSON",
    "inputFile": {
        "bucketName": "amzn-s3-demo-bucket",
        "key": "input/batch-file.edi"
    },
    "advancedOptions": {
        "x12": {
            "splitOptions": {
                "splitBy": "TRANSACTION"
            }
        }
    }
}
```

#### Sample Response
<a name="API_TestParsing_Example_2_Response"></a>

```
{
    "parsedFileContent": ""
}
```

## See Also
<a name="API_TestParsing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/TestParsing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/TestParsing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/TestParsing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/TestParsing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/TestParsing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/TestParsing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/TestParsing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/TestParsing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/TestParsing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/TestParsing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

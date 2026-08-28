---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TestMapping.html
---

# TestMapping
<a name="API_TestMapping"></a>

Maps the input file according to the provided template file. The API call downloads the file contents from the Amazon S3 location, and passes the contents in as a string, to the `inputFileContent` parameter.

## Request Syntax
<a name="API_TestMapping_RequestSyntax"></a>

```
{
   "fileFormat": "{{string}}",
   "inputFileContent": "{{string}}",
   "mappingTemplate": "{{string}}"
}
```

## Request Parameters
<a name="API_TestMapping_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [fileFormat](#API_TestMapping_RequestSyntax) **   <a name="b2bi-TestMapping-request-fileFormat"></a>
Specifies that the currently supported file formats for EDI transformations are `JSON` and `XML`.
Type: String
Valid Values: `XML | JSON | NOT_USED`
Required: Yes

 ** [inputFileContent](#API_TestMapping_RequestSyntax) **   <a name="b2bi-TestMapping-request-inputFileContent"></a>
Specify the contents of the EDI (electronic data interchange) XML or JSON file that is used as input for the transform.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5000000.
Required: Yes

 ** [mappingTemplate](#API_TestMapping_RequestSyntax) **   <a name="b2bi-TestMapping-request-mappingTemplate"></a>
Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.
This parameter is available for backwards compatibility. Use the [Mapping](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html) data type instead.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350000.
Required: Yes

## Response Syntax
<a name="API_TestMapping_ResponseSyntax"></a>

```
{
   "mappedFileContent": "string"
}
```

## Response Elements
<a name="API_TestMapping_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [mappedFileContent](#API_TestMapping_ResponseSyntax) **   <a name="b2bi-TestMapping-response-mappedFileContent"></a>
Returns a string for the mapping that can be used to identify the mapping. Similar to a fingerprint
Type: String

## Errors
<a name="API_TestMapping_Errors"></a>

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
<a name="API_TestMapping_Examples"></a>

### Example
<a name="API_TestMapping_Example_1"></a>

The following example maps the sample input string, using the JSONata mapping template `$`.

#### Sample Request
<a name="API_TestMapping_Example_1_Request"></a>

```
{
    "fileFormat": "JSON",
    "inputFileContent": "<sample input string>",
    "mappingTemplate": "$"
}
```

#### Sample Response
<a name="API_TestMapping_Example_1_Response"></a>

```
{
    "mappedFileContent": "<mapped sample content >"
}
```

## See Also
<a name="API_TestMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/TestMapping)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/TestMapping)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/TestMapping)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/TestMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/TestMapping)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/TestMapping)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/TestMapping)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/TestMapping)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/TestMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/TestMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

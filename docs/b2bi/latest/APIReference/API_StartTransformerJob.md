---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_StartTransformerJob.html
---

# StartTransformerJob
<a name="API_StartTransformerJob"></a>

Runs a job, using a transformer, to parse input EDI (electronic data interchange) file into the output structures used by AWS B2B Data Interchange.

If you only want to transform EDI (electronic data interchange) documents, you don't need to create profiles, partnerships or capabilities. Just create and configure a transformer, and then run the `StartTransformerJob` API to process your files.

**Note**
The system stores transformer jobs for 30 days. During that period, you can run [GetTransformerJob](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetTransformerJob.html) and supply its `transformerId` and `transformerJobId` to return details of the job.

## Request Syntax
<a name="API_StartTransformerJob_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "inputFile": {
      "bucketName": "{{string}}",
      "key": "{{string}}"
   },
   "outputLocation": {
      "bucketName": "{{string}}",
      "key": "{{string}}"
   },
   "transformerId": "{{string}}"
}
```

## Request Parameters
<a name="API_StartTransformerJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartTransformerJob_RequestSyntax) **   <a name="b2bi-StartTransformerJob-request-clientToken"></a>
Reserved for future use.
Type: String
Required: No

 ** [inputFile](#API_StartTransformerJob_RequestSyntax) **   <a name="b2bi-StartTransformerJob-request-inputFile"></a>
Specifies the location of the input file for the transformation. The location consists of an Amazon S3 bucket and prefix.
Type: [S3Location](API_S3Location.md) object
Required: Yes

 ** [outputLocation](#API_StartTransformerJob_RequestSyntax) **   <a name="b2bi-StartTransformerJob-request-outputLocation"></a>
Specifies the location of the output file for the transformation. The location consists of an Amazon S3 bucket and prefix.
Type: [S3Location](API_S3Location.md) object
Required: Yes

 ** [transformerId](#API_StartTransformerJob_RequestSyntax) **   <a name="b2bi-StartTransformerJob-request-transformerId"></a>
Specifies the system-assigned unique identifier for the transformer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Response Syntax
<a name="API_StartTransformerJob_ResponseSyntax"></a>

```
{
   "transformerJobId": "string"
}
```

## Response Elements
<a name="API_StartTransformerJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [transformerJobId](#API_StartTransformerJob_ResponseSyntax) **   <a name="b2bi-StartTransformerJob-response-transformerJobId"></a>
Returns the unique, system-generated identifier for a transformer run.
Type: String
Length Constraints: Fixed length of 25.
Pattern: `[a-zA-Z0-9_-]+`

## Errors
<a name="API_StartTransformerJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.
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
<a name="API_StartTransformerJob_Examples"></a>

### Example
<a name="API_StartTransformerJob_Example_1"></a>

The following example starts the processing for the specified input and output files.

#### Sample Request
<a name="API_StartTransformerJob_Example_1_Request"></a>

```
{
    "clientToken": "foo",
    "inputFile": {
        "bucketName": "amzn-s3-demo-bucket",
        "key": "input/inputFile.txt"
    },
    "outputLocation": {
        "bucketName": "amzn-s3-demo-bucket",
        "key": "output/"
    },
    "transformerId": "tr-1234abcd5678efghj"
}
```

#### Sample Response
<a name="API_StartTransformerJob_Example_1_Response"></a>

```
{
    "transformerJobId": "tj-zzzz9999yyyy8888xxxx77"
}
```

## See Also
<a name="API_StartTransformerJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/StartTransformerJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/StartTransformerJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/StartTransformerJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/StartTransformerJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/StartTransformerJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/StartTransformerJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/StartTransformerJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/StartTransformerJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/StartTransformerJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/StartTransformerJob)

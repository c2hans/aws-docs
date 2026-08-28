---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateStarterMappingTemplate.html
---

# CreateStarterMappingTemplate
<a name="API_CreateStarterMappingTemplate"></a>

 AWS B2B Data Interchange uses a mapping template in JSONata or XSLT format to transform a customer input file into a JSON or XML file that can be converted to EDI.

If you provide a sample EDI file with the same structure as the EDI files that you wish to generate, then the service can generate a mapping template. The starter template contains placeholder values which you can replace with JSONata or XSLT expressions to take data from your input file and insert it into the JSON or XML file that is used to generate the EDI.

If you do not provide a sample EDI file, then the service can generate a mapping template based on the EDI settings in the `templateDetails` parameter.

 Currently, we only support generating a template that can generate the input to produce an Outbound X12 EDI file.

## Request Syntax
<a name="API_CreateStarterMappingTemplate_RequestSyntax"></a>

```
{
   "mappingType": "{{string}}",
   "outputSampleLocation": {
      "bucketName": "{{string}}",
      "key": "{{string}}"
   },
   "templateDetails": { ... }
}
```

## Request Parameters
<a name="API_CreateStarterMappingTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [mappingType](#API_CreateStarterMappingTemplate_RequestSyntax) **   <a name="b2bi-CreateStarterMappingTemplate-request-mappingType"></a>
Specify the format for the mapping template: either JSONATA or XSLT.
Type: String
Valid Values: `JSONATA | XSLT`
Required: Yes

 ** [outputSampleLocation](#API_CreateStarterMappingTemplate_RequestSyntax) **   <a name="b2bi-CreateStarterMappingTemplate-request-outputSampleLocation"></a>
Specify the location of the sample EDI file that is used to generate the mapping template.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** [templateDetails](#API_CreateStarterMappingTemplate_RequestSyntax) **   <a name="b2bi-CreateStarterMappingTemplate-request-templateDetails"></a>
 Describes the details needed for generating the template. Specify the X12 transaction set and version for which the template is used: currently, we only support X12.
Type: [TemplateDetails](API_TemplateDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateStarterMappingTemplate_ResponseSyntax"></a>

```
{
   "mappingTemplate": "string"
}
```

## Response Elements
<a name="API_CreateStarterMappingTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [mappingTemplate](#API_CreateStarterMappingTemplate_ResponseSyntax) **   <a name="b2bi-CreateStarterMappingTemplate-response-mappingTemplate"></a>
Returns a string that represents the mapping template.
Type: String

## Errors
<a name="API_CreateStarterMappingTemplate_Errors"></a>

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
<a name="API_CreateStarterMappingTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/CreateStarterMappingTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/CreateStarterMappingTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/CreateStarterMappingTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/CreateStarterMappingTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/CreateStarterMappingTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/CreateStarterMappingTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/CreateStarterMappingTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/CreateStarterMappingTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/CreateStarterMappingTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/CreateStarterMappingTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

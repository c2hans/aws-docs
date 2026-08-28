---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_TestRenderTemplate.html
---

# TestRenderTemplate
<a name="API_TestRenderTemplate"></a>

Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_TestRenderTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TemplateData **
A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.
Type: String
Length Constraints: Maximum length of 262144.
Required: Yes

 ** TemplateName **
The name of the template to render.
Type: String
Required: Yes

## Response Elements
<a name="API_TestRenderTemplate_ResponseElements"></a>

The following element is returned by the service.

 ** RenderedTemplate **
The complete MIME message rendered by applying the data in the TemplateData parameter to the template specified in the TemplateName parameter.
Type: String

## Errors
<a name="API_TestRenderTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRenderingParameter **
Indicates that one or more of the replacement values you provided is invalid. This error may occur when the TemplateData object contains invalid JSON.
HTTP Status Code: 400

 ** MissingRenderingAttribute **
Indicates that one or more of the replacement values for the specified template was not specified. Ensure that the TemplateData object contains references to all of the replacement tags in the specified template.
HTTP Status Code: 400

 ** TemplateDoesNotExist **
Indicates that the Template object you specified does not exist in your Amazon SES account.
HTTP Status Code: 400

## See Also
<a name="API_TestRenderTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/TestRenderTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/TestRenderTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/TestRenderTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/TestRenderTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/TestRenderTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/TestRenderTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/TestRenderTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/TestRenderTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/TestRenderTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/TestRenderTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

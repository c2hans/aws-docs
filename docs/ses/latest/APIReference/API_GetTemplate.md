---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_GetTemplate.html
---

# GetTemplate
<a name="API_GetTemplate"></a>

Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify.

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_GetTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TemplateName **
The name of the template to retrieve.
Type: String
Required: Yes

## Response Elements
<a name="API_GetTemplate_ResponseElements"></a>

The following element is returned by the service.

 ** Template **
The content of the email, composed of a subject line and either an HTML part or a text-only part.
Type: [Template](API_Template.md) object

## Errors
<a name="API_GetTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** TemplateDoesNotExist **
Indicates that the Template object you specified does not exist in your Amazon SES account.
HTTP Status Code: 400

## See Also
<a name="API_GetTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/GetTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/GetTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/GetTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/GetTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/GetTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/GetTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/GetTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/GetTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/GetTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/GetTemplate)

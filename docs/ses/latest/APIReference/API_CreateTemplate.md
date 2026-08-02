---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateTemplate.html
---

# CreateTemplate
<a name="API_CreateTemplate"></a>

Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single operation. For more information, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-api.html).

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_CreateTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Template **
The content of the email, composed of a subject line and either an HTML part or a text-only part.
Type: [Template](API_Template.md) object
Required: Yes

## Errors
<a name="API_CreateTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExists **
Indicates that a resource could not be created because of a naming conflict.
 ** Name **
Indicates that a resource could not be created because the resource name already exists.
HTTP Status Code: 400

 ** InvalidTemplate **
Indicates that the template that you specified could not be rendered. This issue may occur when a template refers to a partial that does not exist.
HTTP Status Code: 400

 ** LimitExceeded **
Indicates that a resource could not be created because of service limits. For a list of Amazon SES limits, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/limits.html).
HTTP Status Code: 400

## See Also
<a name="API_CreateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/CreateTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/CreateTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/CreateTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/CreateTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/CreateTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/CreateTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/CreateTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/CreateTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/CreateTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/CreateTemplate)

---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ListTemplates.html
---

# ListTemplates
<a name="API_ListTemplates"></a>

Lists the email templates present in your Amazon SES account in the current AWS Region.

You can execute this operation no more than once per second.

## Request Parameters
<a name="API_ListTemplates_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** MaxItems **
The maximum number of templates to return. This value must be at least 1 and less than or equal to 100. If more than 100 items are requested, the page size will automatically set to 100. If you do not specify a value, 10 is the default page size.
Type: Integer
Required: No

 ** NextToken **
A token returned from a previous call to `ListTemplates` to indicate the position in the list of email templates.
Type: String
Required: No

## Response Elements
<a name="API_ListTemplates_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
A token indicating that there are additional email templates available to be listed. Pass this token to a subsequent call to `ListTemplates` to retrieve the next set of email templates within your page size.
Type: String

 **TemplatesMetadata.member.N**
An array the contains the name and creation time stamp for each template in your Amazon SES account.
Type: Array of [TemplateMetadata](API_TemplateMetadata.md) objects

## Errors
<a name="API_ListTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/ListTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/ListTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ListTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/ListTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ListTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/ListTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/ListTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/ListTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/ListTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ListTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

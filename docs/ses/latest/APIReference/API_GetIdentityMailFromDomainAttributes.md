---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityMailFromDomainAttributes.html
---

# GetIdentityMailFromDomainAttributes
<a name="API_GetIdentityMailFromDomainAttributes"></a>

Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains).

This operation is throttled at one request per second and can only get custom MAIL FROM attributes for up to 100 identities at a time.

## Request Parameters
<a name="API_GetIdentityMailFromDomainAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Identities.member.N**
A list of one or more identities.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_GetIdentityMailFromDomainAttributes_ResponseElements"></a>

The following element is returned by the service.

 **MailFromDomainAttributes** MailFromDomainAttributes.entry.N.key (key)MailFromDomainAttributes.entry.N.value (value)
A map of identities to custom MAIL FROM attributes.
Type: String to [IdentityMailFromDomainAttributes](API_IdentityMailFromDomainAttributes.md) object map

## Errors
<a name="API_GetIdentityMailFromDomainAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIdentityMailFromDomainAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/GetIdentityMailFromDomainAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/GetIdentityMailFromDomainAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/GetIdentityMailFromDomainAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/GetIdentityMailFromDomainAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/GetIdentityMailFromDomainAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/GetIdentityMailFromDomainAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/GetIdentityMailFromDomainAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/GetIdentityMailFromDomainAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/GetIdentityMailFromDomainAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/GetIdentityMailFromDomainAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

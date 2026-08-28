---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityDkimAttributes.html
---

# GetIdentityDkimAttributes
<a name="API_GetIdentityDkimAttributes"></a>

Returns the current status of Easy DKIM signing for an entity. For domain name identities, this operation also returns the DKIM tokens that are required for Easy DKIM signing, and whether Amazon SES has successfully verified that these tokens have been published.

This operation takes a list of identities as input and returns the following information for each:
+ Whether Easy DKIM signing is enabled or disabled.
+ A set of DKIM tokens that represent the identity. If the identity is an email address, the tokens represent the domain of that address.
+ Whether Amazon SES has successfully verified the DKIM tokens published in the domain's DNS. This information is only returned for domain name identities, not for email addresses.

This operation is throttled at one request per second and can only get DKIM attributes for up to 100 identities at a time.

For more information about creating DNS records using DKIM tokens, go to the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy-managing.html).

## Request Parameters
<a name="API_GetIdentityDkimAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Identities.member.N**
A list of one or more verified identities - email addresses, domains, or both.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_GetIdentityDkimAttributes_ResponseElements"></a>

The following element is returned by the service.

 **DkimAttributes** DkimAttributes.entry.N.key (key)DkimAttributes.entry.N.value (value)
The DKIM attributes for an email address or a domain.
Type: String to [IdentityDkimAttributes](API_IdentityDkimAttributes.md) object map

## Errors
<a name="API_GetIdentityDkimAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIdentityDkimAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/GetIdentityDkimAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/GetIdentityDkimAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/GetIdentityDkimAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/GetIdentityDkimAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/GetIdentityDkimAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/GetIdentityDkimAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/GetIdentityDkimAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/GetIdentityDkimAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/GetIdentityDkimAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/GetIdentityDkimAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

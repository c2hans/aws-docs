---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_Certificate.html
---

# Certificate
<a name="API_Certificate"></a>

The certificate.

## Contents
<a name="API_Certificate_Contents"></a>

 ** body **   <a name="workspacesweb-Type-Certificate-body"></a>
The body of the certificate.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: No

 ** issuer **   <a name="workspacesweb-Type-Certificate-issuer"></a>
The entity that issued the certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

 ** notValidAfter **   <a name="workspacesweb-Type-Certificate-notValidAfter"></a>
The certificate is not valid after this date.
Type: Timestamp
Required: No

 ** notValidBefore **   <a name="workspacesweb-Type-Certificate-notValidBefore"></a>
The certificate is not valid before this date.
Type: Timestamp
Required: No

 ** subject **   <a name="workspacesweb-Type-Certificate-subject"></a>
The entity the certificate belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: No

 ** thumbprint **   <a name="workspacesweb-Type-Certificate-thumbprint"></a>
A hexadecimal identifier for the certificate.
Type: String
Length Constraints: Fixed length of 64.
Pattern: `[A-Fa-f0-9]{64}`
Required: No

## See Also
<a name="API_Certificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/Certificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/Certificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/Certificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

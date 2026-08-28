---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_CertificateBasedAuthProperties.html
---

# CertificateBasedAuthProperties
<a name="API_CertificateBasedAuthProperties"></a>

Describes the properties of the certificate-based authentication you want to use with your WorkSpaces.

## Contents
<a name="API_CertificateBasedAuthProperties_Contents"></a>

 ** CertificateAuthorityArn **   <a name="WorkSpaces-Type-CertificateBasedAuthProperties-CertificateAuthorityArn"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager Private CA resource.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: No

 ** Status **   <a name="WorkSpaces-Type-CertificateBasedAuthProperties-Status"></a>
The status of the certificate-based authentication properties.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

## See Also
<a name="API_CertificateBasedAuthProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/CertificateBasedAuthProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/CertificateBasedAuthProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/CertificateBasedAuthProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

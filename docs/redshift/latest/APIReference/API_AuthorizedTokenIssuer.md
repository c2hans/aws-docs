---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_AuthorizedTokenIssuer.html
---

# AuthorizedTokenIssuer
<a name="API_AuthorizedTokenIssuer"></a>

The authorized token issuer for the Amazon Redshift IAM Identity Center application.

## Contents
<a name="API_AuthorizedTokenIssuer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AuthorizedAudiencesList.member.N **
The list of audiences for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.
Type: Array of strings
Length Constraints: Maximum length of 2147483647.
Required: No

 ** TrustedTokenIssuerArn **
The ARN for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_AuthorizedTokenIssuer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AuthorizedTokenIssuer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AuthorizedTokenIssuer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AuthorizedTokenIssuer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

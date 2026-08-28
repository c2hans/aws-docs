---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_PolicyInformation.html
---

# PolicyInformation
<a name="API_PolicyInformation"></a>

Defines the X.509 `CertificatePolicies` extension.

## Contents
<a name="API_PolicyInformation_Contents"></a>

 ** CertPolicyId **   <a name="privateca-Type-PolicyInformation-CertPolicyId"></a>
Specifies the object identifier (OID) of the certificate policy under which the certificate was issued. For more information, see NIST's definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
Required: Yes

 ** PolicyQualifiers **   <a name="privateca-Type-PolicyInformation-PolicyQualifiers"></a>
Modifies the given `CertPolicyId` with a qualifier. AWS Private CA supports the certification practice statement (CPS) qualifier.
Type: Array of [PolicyQualifierInfo](API_PolicyQualifierInfo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

## See Also
<a name="API_PolicyInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/PolicyInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/PolicyInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/PolicyInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query privateca` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

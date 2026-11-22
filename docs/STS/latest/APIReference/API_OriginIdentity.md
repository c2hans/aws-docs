---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_OriginIdentity.html
---

# OriginIdentity

The session's `aws:OriginIdentity/Subject`, `aws:OriginIdentity/SubjectType`, `aws:OriginIdentity/Issuer` and `aws:OriginIdentity/FederatedProviderArn` keys. A member is absent when the session does not have the key.

## Contents
<a name="API_OriginIdentity_Contents"></a>

 ** FederatedProviderArn **
The value of the `aws:OriginIdentity/FederatedProviderArn` key: the ARN of the IAM identity provider that the request federated through.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]+`
Required: No

 ** Issuer **
The value of the `aws:OriginIdentity/Issuer` key. For `AssumeRoleWithWebIdentity`, this is the `iss` claim of the token without the `https://` prefix. For `AssumeRoleWithSAML`, this is a hash of the key that signed the SAML assertion, not the `Issuer` element of the assertion.
Type: String
Required: No

 ** Subject **
The value of the `aws:OriginIdentity/Subject` key: the end user's identifier, taken from the token claim that the context provider maps as the subject.
Type: String
Required: No

 ** SubjectType **
The value of the `aws:OriginIdentity/SubjectType` key, which indicates whether the end user is a person (`user`) or a non-human caller such as an application or service (`workload`).
Type: String
Required: No

## See Also
<a name="API_OriginIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/OriginIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/OriginIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/OriginIdentity)

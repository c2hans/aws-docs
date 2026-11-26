---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ClientCertificateIdentityFilter.html
---

# ClientCertificateIdentityFilter

Describes a client certificate identity filter.

## Contents
<a name="API_ClientCertificateIdentityFilter_Contents"></a>

 ** Action **
The action to take when the client certificate matches the filter. The only supported action is `accept`.
Type: String
Valid Values: `accept`
Required: Yes

 ** Field **
The client certificate field to match. The possible values are:
+  `subject-cn` – The common name in the certificate subject.
+  `subject-ou` – The organizational unit in the certificate subject.
+  `san-dns` – A DNS name in the subject alternative name (SAN).
+  `san-uri` – A URI in the subject alternative name (SAN).
If the client certificate doesn't contain the field, the filter doesn't match. If the field has multiple values, the filter matches if it matches any one of the values.
Type: String
Valid Values: `subject-cn | subject-ou | san-dns | san-uri`
Required: Yes

 ** MatchType **
The match type. The possible values are `exact` and `prefix`.
For the `subject-cn`, `subject-ou`, and `san-dns` fields, matching is case-insensitive. For the `san-uri` field, the scheme and host are matched case-insensitively, and the rest of the URI is matched case-sensitively.
Type: String
Valid Values: `exact | prefix`
Required: Yes

 ** Value **
The value to match. The value must be 1–256 printable ASCII characters.
If the field is `san-uri`, the value must begin with a letter. Before the first colon, the value can contain only letters, digits, plus signs (\+), hyphens (-), or periods (.). If the match type is `exact`, the value must contain a colon. For example, `spiffe://example.com/workload` is a valid value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_ClientCertificateIdentityFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ClientCertificateIdentityFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ClientCertificateIdentityFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ClientCertificateIdentityFilter)

---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_TipConfiguration.html
---

# TipConfiguration
<a name="API_TipConfiguration"></a>

The trusted identity propagation (TIP) settings of a profile. When you enable TIP, sessions from the profile include the identity from the certificate in `aws:OriginIdentity` condition keys, which callers can't set.

## Contents
<a name="API_TipConfiguration_Contents"></a>

 ** status **   <a name="rolesanywhere-Type-TipConfiguration-status"></a>
Specifies whether you use trusted identity propagation (TIP) for the profile. This field supports the following values:
+  `ENABLED` – Sessions from the profile include the `aws:OriginIdentity` condition keys.
+  `DISABLED` – Sessions from the profile don't include these keys.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** subjectSource **   <a name="rolesanywhere-Type-TipConfiguration-subjectSource"></a>
The certificate field whose value becomes the subject, `aws:OriginIdentity/Subject`. This field supports the following values:
+  `x509Subject/CN` (default) – The common name (CN) in the certificate's Subject.
+  `x509SAN/URI` – The first URI in the certificate's Subject Alternative Name (SAN) extension.
The profile's attribute mappings must include a rule for this field, and the default attribute mappings include one for each value. If the certificate has no value for the field, `CreateSession` denies the request.
Type: String
Valid Values: `x509SAN/URI | x509Subject/CN`
Required: No

 ** subjectType **   <a name="rolesanywhere-Type-TipConfiguration-subjectType"></a>
Specifies whether the certificates for the profile identify workloads or people. This field supports the following values:
+  `workload` – The certificates identify workloads.
+  `user` – The certificates identify people.
Sessions include the value in `aws:OriginIdentity/SubjectType`. If you omit this field, sessions don't include that key.
Type: String
Valid Values: `user | workload`
Required: No

## See Also
<a name="API_TipConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/TipConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/TipConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/TipConfiguration)

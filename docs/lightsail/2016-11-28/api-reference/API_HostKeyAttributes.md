---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_HostKeyAttributes.html
---

# HostKeyAttributes
<a name="API_HostKeyAttributes"></a>

Describes the public SSH host keys or the RDP certificate.

## Contents
<a name="API_HostKeyAttributes_Contents"></a>

 ** algorithm **   <a name="Lightsail-Type-HostKeyAttributes-algorithm"></a>
The SSH host key algorithm or the RDP certificate format.
For SSH host keys, the algorithm may be `ssh-rsa`, `ecdsa-sha2-nistp256`, `ssh-ed25519`, etc. For RDP certificates, the algorithm is always `x509-cert`.
Type: String
Required: No

 ** fingerprintSHA1 **   <a name="Lightsail-Type-HostKeyAttributes-fingerprintSHA1"></a>
The SHA-1 fingerprint of the returned SSH host key or RDP certificate.
+ Example of an SHA-1 SSH fingerprint:

   `SHA1:1CHH6FaAaXjtFOsR/t83vf91SR0`
+ Example of an SHA-1 RDP fingerprint:

   `af:34:51:fe:09:f0:e0:da:b8:4e:56:ca:60:c2:10:ff:38:06:db:45`
Type: String
Required: No

 ** fingerprintSHA256 **   <a name="Lightsail-Type-HostKeyAttributes-fingerprintSHA256"></a>
The SHA-256 fingerprint of the returned SSH host key or RDP certificate.
+ Example of an SHA-256 SSH fingerprint:

   `SHA256:KTsMnRBh1IhD17HpdfsbzeGA4jOijm5tyXsMjKVbB8o`
+ Example of an SHA-256 RDP fingerprint:

   `03:9b:36:9f:4b:de:4e:61:70:fc:7c:c9:78:e7:d2:1a:1c:25:a8:0c:91:f6:7c:e4:d6:a0:85:c8:b4:53:99:68`
Type: String
Required: No

 ** notValidAfter **   <a name="Lightsail-Type-HostKeyAttributes-notValidAfter"></a>
The returned RDP certificate is not valid after this point in time.
This value is listed only for RDP certificates.
Type: Timestamp
Required: No

 ** notValidBefore **   <a name="Lightsail-Type-HostKeyAttributes-notValidBefore"></a>
The returned RDP certificate is valid after this point in time.
This value is listed only for RDP certificates.
Type: Timestamp
Required: No

 ** publicKey **   <a name="Lightsail-Type-HostKeyAttributes-publicKey"></a>
The public SSH host key or the RDP certificate.
Type: String
Required: No

 ** witnessedAt **   <a name="Lightsail-Type-HostKeyAttributes-witnessedAt"></a>
The time that the SSH host key or RDP certificate was recorded by Lightsail.
Type: Timestamp
Required: No

## See Also
<a name="API_HostKeyAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/HostKeyAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/HostKeyAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/HostKeyAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

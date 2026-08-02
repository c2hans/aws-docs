---
source_url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html
---

# Supported protocols and ciphers between viewers and CloudFront
<a name="secure-connections-supported-viewer-protocols-ciphers"></a>

When you [require HTTPS between viewers and your CloudFront distribution](DownloadDistValuesCacheBehavior.md#DownloadDistValuesViewerProtocolPolicy), you must choose a [security policy](DownloadDistValuesGeneral.md#DownloadDistValues-security-policy), which determines the following settings:
+ The minimum SSL/TLS protocol that CloudFront uses to communicate with viewers.
+ The ciphers that CloudFront can use to encrypt the communication with viewers.

To choose a security policy, specify the applicable value for [Security policy (minimum SSL/TLS version)](DownloadDistValuesGeneral.md#DownloadDistValues-security-policy). The following table lists the protocols and ciphers that CloudFront can use for each security policy.

A viewer must support at least one of the supported ciphers to establish an HTTPS connection with CloudFront. CloudFront chooses a cipher in the listed order from among the ciphers that the viewer supports. See also [OpenSSL, s2n, and RFC cipher names](#secure-connections-openssl-rfc-cipher-names).

<table>
<thead>
  <tr><th></th><th colspan="9">Security policy</th></tr>
  <tr><th></th><th>SSLv3</th><th>TLSv1</th><th>TLSv1\_2016</th><th>TLSv1.1\_2016</th><th>TLSv1.2\_2018</th><th>TLSv1.2\_2019</th><th>TLSv1.2\_2021</th><th>TLSv1.2\_2025</th><th>TLSv1.3\_2025</th></tr>
</thead>
<tbody>
  <tr><td colspan="10">Supported SSL/TLS protocols</td></tr>
  <tr><td>TLSv1.3</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLSv1.2</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>TLSv1.1</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>TLSv1</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>SSLv3</td><td>♦</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td colspan="10">Supported TLSv1.3 ciphers</td></tr>
  <tr><td>TLS\_AES\_128\_GCM\_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_AES\_256\_GCM\_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_CHACHA20\_POLY1305\_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td>♦</td></tr>
  <tr><td colspan="10">Supported ECDSA ciphers</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-GCM-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES256-GCM-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>ECDHE-ECDSA-CHACHA20-POLY1305</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td colspan="10">Supported RSA ciphers</td></tr>
  <tr><td>ECDHE-RSA-AES128-GCM-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-RSA-AES256-GCM-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td></tr>
  <tr><td>ECDHE-RSA-CHACHA20-POLY1305</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES128-GCM-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES256-GCM-SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES128-SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES256-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>AES128-SHA</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>DES-CBC3-SHA</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>RC4-MD5</td><td>♦</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>

## OpenSSL, s2n, and RFC cipher names
<a name="secure-connections-openssl-rfc-cipher-names"></a>

OpenSSL and [s2n](https://github.com/awslabs/s2n) use different names for ciphers than the TLS standards use ([RFC 2246](https://tools.ietf.org/html/rfc2246), [RFC 4346](https://tools.ietf.org/html/rfc4346), [RFC 5246](https://tools.ietf.org/html/rfc5246), and [RFC 8446](https://tools.ietf.org/html/rfc8446)). The following table maps the OpenSSL and s2n names to the RFC name for each cipher.

CloudFront supports both classical and quantum-safe key exchanges. For classical key exchanges using elliptic curves, CloudFront supports the following:
+ `prime256v1`
+ `X25519`
+ `secp384r1`

For quantum-safe key exchanges, CloudFront supports the following:
+ `X25519MLKEM768`
+ `SecP256r1MLKEM768`
**Note**
Quantum-safe key exchanges are only supported with TLS 1.3. TLS 1.2 and earlier versions do not support quantum-safe key exchanges.

  For more information, see the following topics:
  + [Post-Quantum Cryptography](https://aws.amazon.com/security/post-quantum-cryptography/)
  + [Cryptography algorithms and AWS services](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/aws-cryptography-services.html#algorithms)
  + [Hybrid key exchange in TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/)

For more information about certificate requirements for CloudFront, see [Requirements for using SSL/TLS certificates with CloudFront](cnames-and-https-requirements.md).

<table>
<thead>
  <tr><th>OpenSSL and s2n cipher name</th><th>RFC cipher name</th></tr>
</thead>
<tbody>
  <tr><td colspan="2">Supported TLSv1.3 ciphers</td></tr>
  <tr><td>TLS\_AES\_128\_GCM\_SHA256</td><td>TLS\_AES\_128\_GCM\_SHA256</td></tr>
  <tr><td>TLS\_AES\_256\_GCM\_SHA384</td><td>TLS\_AES\_256\_GCM\_SHA384</td></tr>
  <tr><td>TLS\_CHACHA20\_POLY1305\_SHA256</td><td>TLS\_CHACHA20\_POLY1305\_SHA256</td></tr>
  <tr><td colspan="2">Supported ECDSA ciphers</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-GCM-SHA256</td><td>TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA256</td><td>TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256</td></tr>
  <tr><td>ECDHE-ECDSA-AES128-SHA</td><td>TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-GCM-SHA384</td><td>TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384</td></tr>
  <tr><td>ECDHE-ECDSA-CHACHA20-POLY1305</td><td>TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA384</td><td>TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384</td></tr>
  <tr><td>ECDHE-ECDSA-AES256-SHA</td><td>TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA</td></tr>
  <tr><td colspan="2">Supported RSA ciphers</td></tr>
  <tr><td>ECDHE-RSA-AES128-GCM-SHA256</td><td>TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256</td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA256</td><td>TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256 </td></tr>
  <tr><td>ECDHE-RSA-AES128-SHA</td><td>TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA</td></tr>
  <tr><td>ECDHE-RSA-AES256-GCM-SHA384</td><td>TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384 </td></tr>
  <tr><td>ECDHE-RSA-CHACHA20-POLY1305</td><td>TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256</td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA384</td><td>TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384 </td></tr>
  <tr><td>ECDHE-RSA-AES256-SHA</td><td>TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA</td></tr>
  <tr><td>AES128-GCM-SHA256</td><td>TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256</td></tr>
  <tr><td>AES256-GCM-SHA384</td><td>TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384</td></tr>
  <tr><td>AES128-SHA256</td><td>TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256</td></tr>
  <tr><td>AES256-SHA</td><td>TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA</td></tr>
  <tr><td>AES128-SHA</td><td>TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA</td></tr>
  <tr><td>DES-CBC3-SHA </td><td>TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA </td></tr>
  <tr><td>RC4-MD5</td><td>TLS\_RSA\_WITH\_RC4\_128\_MD5</td></tr>
</tbody>
</table>

## Supported signature schemes between viewers and CloudFront
<a name="secure-connections-viewer-signature-schemes"></a>

CloudFront supports the following signature schemes for connections between viewers and CloudFront.

<table>
<thead>
  <tr><th></th><th colspan="9">Security policy</th></tr>
  <tr><th>Signature schemes</th><th>SSLv3</th><th>TLSv1</th><th>TLSv1\_2016</th><th>TLSv1.1\_2016</th><th>TLSv1.2\_2018</th><th>TLSv1.2\_2019</th><th> TLSv1.2\_2021</th><th>TLSv1.2\_2025</th><th>TLSv1.3\_2025</th></tr>
</thead>
<tbody>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PSS\_PSS\_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PSS\_PSS\_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PSS\_PSS\_SHA512</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PSS\_RSAE\_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PSS\_RSAE\_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PSS\_RSAE\_SHA512</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA512</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA224</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA512</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA224</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_ECDSA\_SECP256R1\_SHA256</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_ECDSA\_SECP384R1\_SHA384</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_RSA\_PKCS1\_SHA1</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
  <tr><td>TLS\_SIGNATURE\_SCHEME\_ECDSA\_SHA1</td><td>♦</td><td>♦</td><td>♦</td><td>♦</td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>

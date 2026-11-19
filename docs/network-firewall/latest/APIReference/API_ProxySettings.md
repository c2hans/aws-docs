---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ProxySettings.html
---

# ProxySettings

The proxy settings of a proxy mode firewall: the ports and protocols on which the firewall's proxy listens for traffic, and optionally your own domain name and certificate.

## Contents
<a name="API_ProxySettings_Contents"></a>

 ** ListenerProperties **   <a name="networkfirewall-Type-ProxySettings-ListenerProperties"></a>
The listeners of the firewall's proxy. Specify at least one listener, and at most one HTTP listener and one HTTPS listener. Each listener needs a port from 1 to 65535, and the two listeners must use different ports.
If you don't specify listeners when you create the firewall, the firewall listens for HTTP on port 3128 and HTTPS on port 8443.
Type: Array of [ListenerProperty](API_ListenerProperty.md) objects
Required: Yes

 ** CertificateArn **   <a name="networkfirewall-Type-ProxySettings-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate that the firewall's HTTPS proxy listener presents to clients. The certificate must be an AWS Certificate Manager (ACM) certificate in the same account and Region as the firewall. Its subject alternative names must cover `DomainName`, either exactly or with a wildcard that matches exactly one label. For example, `*.example.com` covers `proxy.example.com`. If you don't specify this, Network Firewall uses a certificate that it manages for a domain name that it generates.
You manage and renew the certificate in ACM, and Network Firewall uses renewed certificates automatically. While the firewall uses the certificate, you can't delete it from ACM. Your clients must trust the certificate's certificate authority.
If you specify `CertificateArn`, you must also specify `DomainName`. You can set them only when you create the firewall. When you call `UpdateProxySettings`, specify the same values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** DomainName **   <a name="networkfirewall-Type-ProxySettings-DomainName"></a>
The domain name that your clients use to reach the firewall's proxy. The name must have at least two labels and at most 253 characters. It can't contain a wildcard or use the `proxy-id.nfw.region.amazonaws.com` format, and the certificate in `CertificateArn` must cover it. If you don't specify this, Network Firewall generates a domain name.
Network Firewall creates the Route 53 private hosted zones that resolve this name to the firewall endpoints, so you don't need to configure DNS. A VPC can have only one private hosted zone with a given name. If a VPC that the firewall serves already has one with this name, Network Firewall can't set up the Availability Zones in that VPC.
If you specify `DomainName`, you must also specify `CertificateArn`. You can set them only when you create the firewall. When you call `UpdateProxySettings`, specify the same values.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `^[A-Za-z0-9][A-Za-z0-9.-]*$`
Required: No

## See Also
<a name="API_ProxySettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ProxySettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ProxySettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ProxySettings)

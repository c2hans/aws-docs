---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/security-data-protection.html
---

# Data protection in ELB for Envoy

ELB for Envoy protects your proxy configuration both at rest and in transit.

At rest, ELB for Envoy encrypts your proxy's configuration file and configuration archive. By default, the service encrypts this content with an AWS owned key, and no setup is required. To control the key instead, supply a customer managed key in AWS KMS. For instructions, see [Encrypt a proxy configuration with a customer managed key](proxy-encryption.md).

Proxy metadata, such as the proxy's name, tags, and attributes, isn't encrypted with a customer managed key.

In transit, you terminate TLS in your Envoy configuration. You control the certificates and protocols that the proxy presents to clients. For more information about presenting a certificate from AWS Certificate Manager (ACM), see [Terminate TLS with an ACM certificate](tls-acm-certificate.md).

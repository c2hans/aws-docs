---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/elbproxy/quotas.html
---

# Quotas for Elastic Load Balancing for Envoy

The following table lists the quotas for ELB for Envoy.

| Quota | Default | Adjustable |
| --- | --- | --- |
| Proxies per Region per account | 25 | Yes |
| Availability Zones per proxy | At least 2 | No |
| Configuration file size | 128 KB | No |
| Configuration archive size | 10 MB compressed, 50 MB uncompressed | No |
| Configuration archive entries | 50 | No |
| AWS Certificate Manager (ACM) certificates per proxy | 25 | Yes |
| Proxies per ACM certificate | 100 | No |
| Proxies per AWS WAF web ACL | 100 | Yes |

You can request an increase for an adjustable quota through Service Quotas.

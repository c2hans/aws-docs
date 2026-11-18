---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/load-balancer-limits.html
---

# Quotas for Amazon Route 53 Global Resolver
<a name="load-balancer-limits"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for Amazon Route 53 Global Resolver, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **Amazon Route 53 Global Resolver**.

To request a quota increase, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

Your AWS account has the following quotas related to Amazon Route 53 Global Resolver.

## Soft quotas
<a name="soft-quotas"></a>

The following table describes quotas in Amazon Route 53 Global Resolver that can be increased. For information about changing quotas, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

For some customers, your account quota might be below these published quotas. If you believe that you encountered a *Resource limit exceeded* error wrongfully, use the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home) to request quota increases.

| Resource | Default quota |
| --- | --- |
| Global resolvers per account | 10 |
| DNS views per global resolver | 5 |
| DNS views per account | 50 |
| Domain lists per account | 1,000 |
| Domains per domain list | 100,000 |
| Domains in a file imported from S3 | 100,000 |
| Firewall rules per DNS view | 100 |
| Access tokens per global resolver | 100,000 |
| ACL rulesAccess Source rules per global resolver | 5,000 |
| ACL ruleAccess Source rule CIDR size per global resolver | 65,000 |
| Private hosted zones per DNS view | 1,000 |
| Control plane API requests per account | 10 requests per second |
| Control plane token API requests per account | 50 requests per second |
| DNS queries (Do53) per global resolver per Region | 500,000 queries per second |
| DNS queries (DoH, DoT) per global resolver per Region | 100,000 queries per second |

## Hard quotas
<a name="hard-quotas"></a>

The following table describes quotas in Amazon Route 53 Global Resolver that can't be increased.

| Resource or operation | Quota |
| --- | --- |
| Domains per API request | 1,000 |
| Access token size | 64 bytes |
| Firewall rule priority value limit | 100,000 |
| Log delivery configurations per (global resolver, destination type, Region) | 1 |

**Note**
DNS query rate limits are based on the capacity of the underlying infrastructure and may vary based on query complexity and Regional availability.

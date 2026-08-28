---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_CreateLbCookieStickinessPolicy_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateLbCookieStickinessPolicy` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_CreateLbCookieStickinessPolicy_section"></a>

The following code examples show how to use `CreateLbCookieStickinessPolicy`.

------
#### [ CLI ]

**AWS CLI**
**To generate a duration-based stickiness policy for your HTTPS load balancer**
This example generates a stickiness policy with sticky session lifetimes controlled by the specified expiration period.
Command:

```
aws elb create-lb-cookie-stickiness-policy --load-balancer-name {{my-load-balancer}} --policy-name {{my-duration-cookie-policy}} --cookie-expiration-period {{60}}
```
+  For API details, see [CreateLbCookieStickinessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-lb-cookie-stickiness-policy.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a stickiness policy with sticky session lifetimes controlled by the specified expiration period (in seconds).**

```
New-ELBLBCookieStickinessPolicy -LoadBalancerName my-load-balancer -PolicyName my-duration-cookie-policy -CookieExpirationPeriod 60
```
**Example 2: This example creates a stickiness policy with sticky session lifetimes controlled by the by the lifetime of the browser (user-agent).**

```
New-ELBLBCookieStickinessPolicy -LoadBalancerName my-load-balancer -PolicyName my-duration-cookie-policy
```
+  For API details, see [CreateLbCookieStickinessPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a stickiness policy with sticky session lifetimes controlled by the specified expiration period (in seconds).**

```
New-ELBLBCookieStickinessPolicy -LoadBalancerName my-load-balancer -PolicyName my-duration-cookie-policy -CookieExpirationPeriod 60
```
**Example 2: This example creates a stickiness policy with sticky session lifetimes controlled by the by the lifetime of the browser (user-agent).**

```
New-ELBLBCookieStickinessPolicy -LoadBalancerName my-load-balancer -PolicyName my-duration-cookie-policy
```
+  For API details, see [CreateLbCookieStickinessPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

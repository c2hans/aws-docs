---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_CreateAppCookieStickinessPolicy_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateAppCookieStickinessPolicy` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_CreateAppCookieStickinessPolicy_section"></a>

The following code examples show how to use `CreateAppCookieStickinessPolicy`.

------
#### [ CLI ]

**AWS CLI**
**To generate a stickiness policy for your HTTPS load balancer**
This example generates a stickiness policy that follows the sticky session lifetimes of the application-generated cookie.
Command:

```
aws elb create-app-cookie-stickiness-policy --load-balancer-name {{my-load-balancer}} --policy-name {{my-app-cookie-policy}} --cookie-name {{my-app-cookie}}
```
+  For API details, see [CreateAppCookieStickinessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-app-cookie-stickiness-policy.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a stickiness policy that follows the sticky session lifetimes of the specified application-generated cookie.**

```
New-ELBAppCookieStickinessPolicy -LoadBalancerName my-load-balancer -PolicyName my-app-cookie-policy -CookieName my-app-cookie
```
+  For API details, see [CreateAppCookieStickinessPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a stickiness policy that follows the sticky session lifetimes of the specified application-generated cookie.**

```
New-ELBAppCookieStickinessPolicy -LoadBalancerName my-load-balancer -PolicyName my-app-cookie-policy -CookieName my-app-cookie
```
+  For API details, see [CreateAppCookieStickinessPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_SetLoadBalancerPoliciesOfListener_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `SetLoadBalancerPoliciesOfListener` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_SetLoadBalancerPoliciesOfListener_section"></a>

The following code examples show how to use `SetLoadBalancerPoliciesOfListener`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To replace the policies associated with a listener**
The following `set-load-balancer-policies-of-listener` example replaces the policies that are currently associated with the specified listener.

```
aws elb set-load-balancer-policies-of-listener \
    --load-balancer-name {{my-load-balancer}} \
    --load-balancer-port {{443}} \
    --policy-names {{my-SSLNegotiation-policy}}
```
This command produces no output.
For more information, see [Update the SSL negotiation configuration of your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html) in the *Classic Load Balancers Guide*.
**Example 2: To remove all policies associated with your listener**
The following `set-load-balancer-policies-of-listener` example removes all policies that are currently associated with the specified listener.

```
aws elb set-load-balancer-policies-of-listener \
    --load-balancer-name {{my-load-balancer}} \
    --load-balancer-port {{443}} \
    --policy-names {{[]}}
```
This command produces no output.
To confirm that the policies are removed from the load balancer, use the `describe-load-balancer-policies` command.
For more information, see [Update the SSL negotiation configuration of your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html) in the *Classic Load Balancers Guide*.
+  For API details, see [SetLoadBalancerPoliciesOfListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-policies-of-listener.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example replaces the policies for the specified listener with the specified policy.**

```
Set-ELBLoadBalancerPolicyOfListener -LoadBalancerName my-load-balancer -LoadBalancerPort 443 -PolicyName my-SSLNegotiation-policy
```
**Example 2: This example removes all policies associated with the specified listener.**

```
Set-ELBLoadBalancerPolicyOfListener -LoadBalancerName my-load-balancer -LoadBalancerPort 443
```
+  For API details, see [SetLoadBalancerPoliciesOfListener](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example replaces the policies for the specified listener with the specified policy.**

```
Set-ELBLoadBalancerPolicyOfListener -LoadBalancerName my-load-balancer -LoadBalancerPort 443 -PolicyName my-SSLNegotiation-policy
```
**Example 2: This example removes all policies associated with the specified listener.**

```
Set-ELBLoadBalancerPolicyOfListener -LoadBalancerName my-load-balancer -LoadBalancerPort 443
```
+  For API details, see [SetLoadBalancerPoliciesOfListener](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

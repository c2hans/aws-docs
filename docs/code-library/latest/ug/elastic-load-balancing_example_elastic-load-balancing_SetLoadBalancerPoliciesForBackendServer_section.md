---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_SetLoadBalancerPoliciesForBackendServer_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `SetLoadBalancerPoliciesForBackendServer` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_SetLoadBalancerPoliciesForBackendServer_section"></a>

The following code examples show how to use `SetLoadBalancerPoliciesForBackendServer`.

------
#### [ CLI ]

**AWS CLI**
**To replace the policies associated with a port for a backend instance**
This example replaces the policies that are currently associated with the specified port.
Command:

```
aws elb set-load-balancer-policies-for-backend-server --load-balancer-name {{my-load-balancer}} --instance-port {{80}} --policy-names {{my-ProxyProtocol-policy}}
```
**To remove all policies that are currently associated with a port on your backend instance**
This example removes all policies associated with the specified port.
Command:

```
aws elb set-load-balancer-policies-for-backend-server --load-balancer-name {{my-load-balancer}} --instance-port {{80}} --policy-names {{[]}}
```
To confirm that the policies are removed, use the `describe-load-balancer-policies` command.
+  For API details, see [SetLoadBalancerPoliciesForBackendServer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-policies-for-backend-server.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example replaces the policies for the specified port with the specified policy.**

```
Set-ELBLoadBalancerPolicyForBackendServer -LoadBalancerName my-load-balancer -InstancePort 80 -PolicyName my-ProxyProtocol-policy
```
**Example 2: This example removes all policies associated with the specified port.**

```
Set-ELBLoadBalancerPolicyForBackendServer -LoadBalancerName my-load-balancer -InstancePort 80
```
+  For API details, see [SetLoadBalancerPoliciesForBackendServer](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example replaces the policies for the specified port with the specified policy.**

```
Set-ELBLoadBalancerPolicyForBackendServer -LoadBalancerName my-load-balancer -InstancePort 80 -PolicyName my-ProxyProtocol-policy
```
**Example 2: This example removes all policies associated with the specified port.**

```
Set-ELBLoadBalancerPolicyForBackendServer -LoadBalancerName my-load-balancer -InstancePort 80
```
+  For API details, see [SetLoadBalancerPoliciesForBackendServer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

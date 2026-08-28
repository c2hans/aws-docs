---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_CreateLoadBalancerListeners_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateLoadBalancerListeners` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_CreateLoadBalancerListeners_section"></a>

The following code examples show how to use `CreateLoadBalancerListeners`.

------
#### [ CLI ]

**AWS CLI**
**To create HTTP listeners for a load balancer**
This example creates a listener for your load balancer at port 80 using the HTTP protocol.
Command:

```
aws elb create-load-balancer-listeners --load-balancer-name {{my-load-balancer}} --listeners {{"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"}}
```
**To create HTTPS listeners for a load balancer**
This example creates a listener for your load balancer at port 443 using the HTTPS protocol.
Command:

```
aws elb create-load-balancer-listeners --load-balancer-name {{my-load-balancer}} --listeners {{"Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTP,InstancePort=80"}}
```
+  For API details, see [CreateLoadBalancerListeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-listeners.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds an HTTPS listener to the specified load balancer.**

```
$httpsListener = New-Object Amazon.ElasticLoadBalancing.Model.Listener
$httpsListener.Protocol = "https"
$httpsListener.LoadBalancerPort = 443
$httpsListener.InstanceProtocol = "https"
$httpsListener.InstancePort = 443
$httpsListener.SSLCertificateId="arn:aws:iam::123456789012:server-certificate/my-server-cert"
New-ELBLoadBalancerListener -LoadBalancerName my-load-balancer -Listener $httpsListener
```
+  For API details, see [CreateLoadBalancerListeners](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds an HTTPS listener to the specified load balancer.**

```
$httpsListener = New-Object Amazon.ElasticLoadBalancing.Model.Listener
$httpsListener.Protocol = "https"
$httpsListener.LoadBalancerPort = 443
$httpsListener.InstanceProtocol = "https"
$httpsListener.InstancePort = 443
$httpsListener.SSLCertificateId="arn:aws:iam::123456789012:server-certificate/my-server-cert"
New-ELBLoadBalancerListener -LoadBalancerName my-load-balancer -Listener $httpsListener
```
+  For API details, see [CreateLoadBalancerListeners](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

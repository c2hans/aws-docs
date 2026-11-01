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
**Example 1: To create HTTP listeners for a load balancer**
The following `create-load-balancer-listeners` example creates a listener for your load balancer at port 80 using the HTTP protocol.

```
aws elb create-load-balancer-listeners \
    --load-balancer-name {{my-load-balancer}} \
    --listeners {{"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"}}
```
This command produces no output.
For more information, see [Listeners for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html) in the *Classic Load Balancers User Guide*.
**Example 2: To create HTTPS listeners for a load balancer**
The following `create-load-balancer-listeners` example creates a listener for your load balancer at port 443 using the HTTPS protocol.

```
aws elb create-load-balancer-listeners \
    --load-balancer-name {{my-load-balancer}} \
    --listeners {{"Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTP,InstancePort=80"}}
```
This command produces no output.
For more information, see [Configure an HTTPS listener for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-add-or-delete-listeners.html) in the *Classic Load Balancers User Guide*.
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

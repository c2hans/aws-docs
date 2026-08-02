---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_CreateLoadBalancer_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateLoadBalancer` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_CreateLoadBalancer_section"></a>

The following code examples show how to use `CreateLoadBalancer`.

------
#### [ CLI ]

**AWS CLI**
**To create an HTTP load balancer**
This example creates a load balancer with an HTTP listener in a VPC.
Command:

```
aws elb create-load-balancer --load-balancer-name {{my-load-balancer}} --listeners {{"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"}} --subnets {{subnet-15aaab61}} --security-groups {{sg-a61988c3}}
```
Output:

```
{
    "DNSName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com"
}
```
This example creates a load balancer with an HTTP listener in EC2-Classic.
Command:

```
aws elb create-load-balancer --load-balancer-name {{my-load-balancer}} --listeners {{"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"}} --availability-zones {{us-west-2a}} {{us-west-2b}}
```
Output:

```
{
    "DNSName": "my-load-balancer-123456789.us-west-2.elb.amazonaws.com"
}
```
**To create an HTTPS load balancer**
This example creates a load balancer with an HTTPS listener in a VPC.
Command:

```
aws elb create-load-balancer --load-balancer-name {{my-load-balancer}} --listeners {{"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"}} {{"Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTP,InstancePort=80,SSLCertificateId=arn:aws:iam::123456789012:server-certificate/my-server-cert"}} --subnets {{subnet-15aaab61}} --security-groups {{sg-a61988c3}}
```
Output:

```
{
    "DNSName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com"
}
```
This example creates a load balancer with an HTTPS listener in EC2-Classic.
Command:

```
aws elb create-load-balancer --load-balancer-name {{my-load-balancer}} --listeners {{"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"}} {{"Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTP,InstancePort=80,SSLCertificateId=arn:aws:iam::123456789012:server-certificate/my-server-cert"}} --availability-zones {{us-west-2a}} {{us-west-2b}}
```
Output:

```
{
    "DNSName": "my-load-balancer-123456789.us-west-2.elb.amazonaws.com"
}
```
**To create an internal load balancer**
This example creates an internal load balancer with an HTTP listener in a VPC.
Command:

```
aws elb create-load-balancer --load-balancer-name {{my-load-balancer}} --listeners {{"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"}} --scheme {{internal}} --subnets {{subnet-a85db0df}} --security-groups {{sg-a61988c3}}
```
Output:

```
{
    "DNSName": "internal-my-load-balancer-123456789.us-west-2.elb.amazonaws.com"
}
```
+  For API details, see [CreateLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a load balancer with an HTTP listener in a VPC.**

```
$httpListener = New-Object Amazon.ElasticLoadBalancing.Model.Listener
$httpListener.Protocol = "http"
$httpListener.LoadBalancerPort = 80
$httpListener.InstanceProtocol = "http"
$httpListener.InstancePort = 80
New-ELBLoadBalancer -LoadBalancerName my-vpc-load-balancer -SecurityGroup sg-a61988c3 -Subnet subnet-15aaab61 -Listener $httpListener

my-vpc-load-balancer-1234567890.us-west-2.elb.amazonaws.com
```
**Example 2: This example creates a load balancer with an HTTP listener in EC2-Classic.**

```
New-ELBLoadBalancer -LoadBalancerName my-classic-load-balancer -AvailabilityZone us-west-2a` -Listener $httpListener
```
**Output:**

```
my-classic-load-balancer-123456789.us-west-2.elb.amazonaws.com
```
**Example 3: This example creates a load balancer with an HTTPS listener.**

```
$httpsListener = New-Object Amazon.ElasticLoadBalancing.Model.Listener
$httpsListener.Protocol = "https"
$httpsListener.LoadBalancerPort = 443
$httpsListener.InstanceProtocol = "http"
$httpsListener.InstancePort = 80
$httpsListener.SSLCertificateId="arn:aws:iam::123456789012:server-certificate/my-server-cert"
New-ELBLoadBalancer -LoadBalancerName my-load-balancer -AvailabilityZone us-west-2a -Listener $httpsListener

my-load-balancer-123456789.us-west-2.elb.amazonaws.com
```
+  For API details, see [CreateLoadBalancer](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a load balancer with an HTTP listener in a VPC.**

```
$httpListener = New-Object Amazon.ElasticLoadBalancing.Model.Listener
$httpListener.Protocol = "http"
$httpListener.LoadBalancerPort = 80
$httpListener.InstanceProtocol = "http"
$httpListener.InstancePort = 80
New-ELBLoadBalancer -LoadBalancerName my-vpc-load-balancer -SecurityGroup sg-a61988c3 -Subnet subnet-15aaab61 -Listener $httpListener

my-vpc-load-balancer-1234567890.us-west-2.elb.amazonaws.com
```
**Example 2: This example creates a load balancer with an HTTP listener in EC2-Classic.**

```
New-ELBLoadBalancer -LoadBalancerName my-classic-load-balancer -AvailabilityZone us-west-2a` -Listener $httpListener
```
**Output:**

```
my-classic-load-balancer-123456789.us-west-2.elb.amazonaws.com
```
**Example 3: This example creates a load balancer with an HTTPS listener.**

```
$httpsListener = New-Object Amazon.ElasticLoadBalancing.Model.Listener
$httpsListener.Protocol = "https"
$httpsListener.LoadBalancerPort = 443
$httpsListener.InstanceProtocol = "http"
$httpsListener.InstancePort = 80
$httpsListener.SSLCertificateId="arn:aws:iam::123456789012:server-certificate/my-server-cert"
New-ELBLoadBalancer -LoadBalancerName my-load-balancer -AvailabilityZone us-west-2a -Listener $httpsListener

my-load-balancer-123456789.us-west-2.elb.amazonaws.com
```
+  For API details, see [CreateLoadBalancer](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

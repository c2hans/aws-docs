---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DescribeLoadBalancers_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeLoadBalancers` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DescribeLoadBalancers_section"></a>

The following code examples show how to use `DescribeLoadBalancers`.

------
#### [ CLI ]

**AWS CLI**
**To describe your load balancers**
This example describes all of your load balancers.
Command:

```
aws elb describe-load-balancers
```
**To describe one of your load balancers**
This example describes the specified load balancer.
Command:

```
aws elb describe-load-balancers --load-balancer-name {{my-load-balancer}}
```
The following example response is for an HTTPS load balancer in a VPC.
Output:

```
{
  "LoadBalancerDescriptions": [
    {
      "Subnets": [
          "subnet-15aaab61"
      ],
      "CanonicalHostedZoneNameID": "Z3DZXE0EXAMPLE",
      "CanonicalHostedZoneName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com",
      "ListenerDescriptions": [
          {
              "Listener": {
                  "InstancePort": 80,
                  "LoadBalancerPort": 80,
                  "Protocol": "HTTP",
                  "InstanceProtocol": "HTTP"
              },
              "PolicyNames": []
          },
          {
              "Listener": {
                  "InstancePort": 443,
                  "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-cert",
                  "LoadBalancerPort": 443,
                  "Protocol": "HTTPS",
                  "InstanceProtocol": "HTTPS"
              },
              "PolicyNames": [
                  "ELBSecurityPolicy-2015-03"
              ]
          }
      ],
      "HealthCheck": {
          "HealthyThreshold": 2,
          "Interval": 30,
          "Target": "HTTP:80/png",
          "Timeout": 3,
          "UnhealthyThreshold": 2
      },
      "VPCId": "vpc-a01106c2",
      "BackendServerDescriptions": [
          {
              "InstancePort": 80,
              "PolicyNames": [
                  "my-ProxyProtocol-policy"
              ]
          }
      ],
      "Instances": [
          {
              "InstanceId": "i-207d9717"
          },
          {
              "InstanceId": "i-afefb49b"
          }
      ],
      "DNSName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com",
      "SecurityGroups": [
          "sg-a61988c3"
      ],
      "Policies": {
          "LBCookieStickinessPolicies": [
              {
                  "PolicyName": "my-duration-cookie-policy",
                  "CookieExpirationPeriod": 60
              }
          ],
          "AppCookieStickinessPolicies": [],
          "OtherPolicies": [
              "my-PublicKey-policy",
              "my-authentication-policy",
              "my-SSLNegotiation-policy",
              "my-ProxyProtocol-policy",
              "ELBSecurityPolicy-2015-03"
          ]
      },
      "LoadBalancerName": "my-load-balancer",
      "CreatedTime": "2015-03-19T03:24:02.650Z",
      "AvailabilityZones": [
          "us-west-2a"
      ],
      "Scheme": "internet-facing",
      "SourceSecurityGroup": {
          "OwnerAlias": "123456789012",
          "GroupName": "my-elb-sg"
      }
    }
  ]
}
```
+  For API details, see [DescribeLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancers.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the names of your load balancers.**

```
Get-ELBLoadBalancer | format-table -property LoadBalancerName
```
**Output:**

```
LoadBalancerName
----------------
my-load-balancer
my-other-load-balancer
my-internal-load-balancer
```
**Example 2: This example describes the specified load balancer.**

```
Get-ELBLoadBalancer -LoadBalancerName my-load-balancer
```
**Output:**

```
AvailabilityZones         : {us-west-2a, us-west-2b}
BackendServerDescriptions : {Amazon.ElasticLoadBalancing.Model.BackendServerDescription}
CanonicalHostedZoneName   : my-load-balancer-1234567890.us-west-2.elb.amazonaws.com
CanonicalHostedZoneNameID : Z3DZXE0EXAMPLE
CreatedTime               : 4/11/2015 12:12:45 PM
DNSName                   : my-load-balancer-1234567890.us-west-2.elb.amazonaws.com
HealthCheck               : Amazon.ElasticLoadBalancing.Model.HealthCheck
Instances                 : {i-207d9717, i-afefb49b}
ListenerDescriptions      : {Amazon.ElasticLoadBalancing.Model.ListenerDescription}
LoadBalancerName          : my-load-balancer
Policies                  : Amazon.ElasticLoadBalancing.Model.Policies
Scheme                    : internet-facing
SecurityGroups            : {sg-a61988c3}
SourceSecurityGroup       : Amazon.ElasticLoadBalancing.Model.SourceSecurityGroup
Subnets                   : {subnet-15aaab61}
VPCId                     : vpc-a01106c2
```
**Example 3: This example describes all your load balancers in the current AWS region.**

```
Get-ELBLoadBalancer
```
**Example 4: This example describes all your load balancers across all available AWS Regions.**

```
Get-AWSRegion | % { Get-ELBLoadBalancer -Region $_ }
```
+  For API details, see [DescribeLoadBalancers](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the names of your load balancers.**

```
Get-ELBLoadBalancer | format-table -property LoadBalancerName
```
**Output:**

```
LoadBalancerName
----------------
my-load-balancer
my-other-load-balancer
my-internal-load-balancer
```
**Example 2: This example describes the specified load balancer.**

```
Get-ELBLoadBalancer -LoadBalancerName my-load-balancer
```
**Output:**

```
AvailabilityZones         : {us-west-2a, us-west-2b}
BackendServerDescriptions : {Amazon.ElasticLoadBalancing.Model.BackendServerDescription}
CanonicalHostedZoneName   : my-load-balancer-1234567890.us-west-2.elb.amazonaws.com
CanonicalHostedZoneNameID : Z3DZXE0EXAMPLE
CreatedTime               : 4/11/2015 12:12:45 PM
DNSName                   : my-load-balancer-1234567890.us-west-2.elb.amazonaws.com
HealthCheck               : Amazon.ElasticLoadBalancing.Model.HealthCheck
Instances                 : {i-207d9717, i-afefb49b}
ListenerDescriptions      : {Amazon.ElasticLoadBalancing.Model.ListenerDescription}
LoadBalancerName          : my-load-balancer
Policies                  : Amazon.ElasticLoadBalancing.Model.Policies
Scheme                    : internet-facing
SecurityGroups            : {sg-a61988c3}
SourceSecurityGroup       : Amazon.ElasticLoadBalancing.Model.SourceSecurityGroup
Subnets                   : {subnet-15aaab61}
VPCId                     : vpc-a01106c2
```
**Example 3: This example describes all your load balancers in the current AWS region.**

```
Get-ELBLoadBalancer
```
**Example 4: This example describes all your load balancers across all available AWS Regions.**

```
Get-AWSRegion | % { Get-ELBLoadBalancer -Region $_ }
```
+  For API details, see [DescribeLoadBalancers](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

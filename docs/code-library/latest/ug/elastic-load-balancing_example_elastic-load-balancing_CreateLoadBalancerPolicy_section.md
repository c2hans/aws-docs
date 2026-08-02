---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_CreateLoadBalancerPolicy_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateLoadBalancerPolicy` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_CreateLoadBalancerPolicy_section"></a>

The following code examples show how to use `CreateLoadBalancerPolicy`.

------
#### [ CLI ]

**AWS CLI**
**To create a policy that enables Proxy Protocol on a load balancer**
This example creates a policy that enables Proxy Protocol on the specified load balancer.
Command:

```
aws elb create-load-balancer-policy --load-balancer-name {{my-load-balancer}} --policy-name {{my-ProxyProtocol-policy}} --policy-type-name {{ProxyProtocolPolicyType}} --policy-attributes {{AttributeName=ProxyProtocol,AttributeValue=true}}
```
**To create an SSL negotiation policy using the recommended security policy**
This example creates an SSL negotiation policy for the specified HTTPS load balancer using the recommended security policy.
Command:

```
aws elb create-load-balancer-policy --load-balancer-name {{my-load-balancer}} --policy-name {{my-SSLNegotiation-policy}} --policy-type-name {{SSLNegotiationPolicyType}} --policy-attributes {{AttributeName=Reference-Security-Policy,AttributeValue=ELBSecurityPolicy-2015-03}}
```
**To create an SSL negotiation policy using a custom security policy**
This example creates an SSL negotiation policy for your HTTPS load balancer using a custom security policy by enabling the protocols and the ciphers.
Command:

```
aws elb create-load-balancer-policy --load-balancer-name {{my-load-balancer}} --policy-name {{my-SSLNegotiation-policy}} --policy-type-name {{SSLNegotiationPolicyType}} --policy-attributes {{AttributeName=Protocol-SSLv3,AttributeValue=true}} {{AttributeName=Protocol-TLSv1.1,AttributeValue=true}} {{AttributeName=DHE-RSA-AES256-SHA256,AttributeValue=true}} {{AttributeName=Server-Defined-Cipher-Order,AttributeValue=true}}
```
**To create a public key policy**
This example creates a public key policy.
Command:

```
aws elb create-load-balancer-policy --load-balancer-name {{my-load-balancer}} --policy-name {{my-PublicKey-policy}} --policy-type-name {{PublicKeyPolicyType}} --policy-attributes {{AttributeName=PublicKey,AttributeValue=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwAYUjnfyEyXr1pxjhFWBpMlggUcqoi3kl+dS74kj//c6x7ROtusUaeQCTgIUkayttRDWchuqo1pHC1u+n5xxXnBBe2ejbb2WRsKIQ5rXEeixsjFpFsojpSQKkzhVGI6mJVZBJDVKSHmswnwLBdofLhzvllpovBPTHe+o4haAWvDBALJU0pkSI1FecPHcs2hwxf14zHoXy1e2k36A64nXW43wtfx5qcVSIxtCEOjnYRg7RPvybaGfQ+v6Iaxb/+7J5kEvZhTFQId+bSiJImF1FSUT1W1xwzBZPUbcUkkXDj45vC2s3Z8E+Lk7a3uZhvsQHLZnrfuWjBWGWvZ/MhZYgEXAMPLE}}
```
**To create a backend server authentication policy**
This example creates a backend server authentication policy that enables authentication on your backend instance using a public key policy.
Command:

```
aws elb create-load-balancer-policy --load-balancer-name {{my-load-balancer}} --policy-name {{my-authentication-policy}} --policy-type-name {{BackendServerAuthenticationPolicyType}} --policy-attributes {{AttributeName=PublicKeyPolicyName,AttributeValue=my-PublicKey-policy}}
```
+  For API details, see [CreateLoadBalancerPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-policy.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a new proxy protocol policy for a specified load balancer.**

```
$attribute = New-Object Amazon.ElasticLoadBalancing.Model.PolicyAttribute -Property @{
         AttributeName="ProxyProtocol"
         AttributeValue="True"
    }
New-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer -PolicyName my-ProxyProtocol-policy -PolicyTypeName ProxyProtocolPolicyType -PolicyAttribute $attribute
```
+  For API details, see [CreateLoadBalancerPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a new proxy protocol policy for a specified load balancer.**

```
$attribute = New-Object Amazon.ElasticLoadBalancing.Model.PolicyAttribute -Property @{
         AttributeName="ProxyProtocol"
         AttributeValue="True"
    }
New-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer -PolicyName my-ProxyProtocol-policy -PolicyTypeName ProxyProtocolPolicyType -PolicyAttribute $attribute
```
+  For API details, see [CreateLoadBalancerPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

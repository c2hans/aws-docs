---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DescribeLoadBalancerPolicyTypes_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeLoadBalancerPolicyTypes` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DescribeLoadBalancerPolicyTypes_section"></a>

The following code examples show how to use `DescribeLoadBalancerPolicyTypes`.

------
#### [ CLI ]

**AWS CLI**
**To describe the load balancer policy types defined by Elastic Load Balancing**
This example describes the load balancer policy types that you can use to create policy configurations for your load balancer.
Command:

```
aws elb describe-load-balancer-policy-types
```
Output:

```
{
  "PolicyTypeDescriptions": [
      {
          "PolicyAttributeTypeDescriptions": [
              {
                  "Cardinality": "ONE",
                  "AttributeName": "ProxyProtocol",
                  "AttributeType": "Boolean"
              }
          ],
          "PolicyTypeName": "ProxyProtocolPolicyType",
          "Description": "Policy that controls whether to include the IP address and port of the originating request for TCP messages. This policy operates on TCP/SSL listeners only"
      },
      {
          "PolicyAttributeTypeDescriptions": [
              {
                  "Cardinality": "ONE",
                  "AttributeName": "PublicKey",
                  "AttributeType": "String"
              }
          ],
          "PolicyTypeName": "PublicKeyPolicyType",
          "Description": "Policy containing a list of public keys to accept when authenticating the back-end server(s). This policy cannot be applied directly to back-end servers or listeners but must be part of a BackendServerAuthenticationPolicyType."
      },
      {
          "PolicyAttributeTypeDescriptions": [
              {
                  "Cardinality": "ONE",
                  "AttributeName": "CookieName",
                  "AttributeType": "String"
              }
          ],
          "PolicyTypeName": "AppCookieStickinessPolicyType",
          "Description": "Stickiness policy with session lifetimes controlled by the lifetime of the application-generated cookie. This policy can be associated only with HTTP/HTTPS listeners."
      },
      {
          "PolicyAttributeTypeDescriptions": [
              {
                  "Cardinality": "ZERO_OR_ONE",
                  "AttributeName": "CookieExpirationPeriod",
                  "AttributeType": "Long"
              }
          ],
          "PolicyTypeName": "LBCookieStickinessPolicyType",
          "Description": "Stickiness policy with session lifetimes controlled by the browser (user-agent) or a specified expiration period. This policy can be associated only with HTTP/HTTPS listeners."
      },
      {
          "PolicyAttributeTypeDescriptions": [
              .
              .
              .
          ],
          "PolicyTypeName": "SSLNegotiationPolicyType",
          "Description": "Listener policy that defines the ciphers and protocols that will be accepted by the load balancer. This policy can be associated only with HTTPS/SSL listeners."
      },
      {
          "PolicyAttributeTypeDescriptions": [
              {
                  "Cardinality": "ONE_OR_MORE",
                  "AttributeName": "PublicKeyPolicyName",
                  "AttributeType": "PolicyName"
              }
          ],
          "PolicyTypeName": "BackendServerAuthenticationPolicyType",
          "Description": "Policy that controls authentication to back-end server(s) and contains one or more policies, such as an instance of a PublicKeyPolicyType. This policy can be associated only with back-end servers that are using HTTPS/SSL."
      }
  ]
}
```
+  For API details, see [DescribeLoadBalancerPolicyTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-policy-types.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets the policy types supported by Elastic Load Balancing.**

```
Get-ELBLoadBalancerPolicyType
```
**Output:**

```
Description                             PolicyAttributeTypeDescriptions         PolicyTypeName
-----------                             -------------------------------         --------------
Stickiness policy with session lifet... {CookieExpirationPeriod}                LBCookieStickinessPolicyType
Policy that controls authentication ... {PublicKeyPolicyName}                   BackendServerAuthenticationPolicyType
Listener policy that defines the cip... {Protocol-SSLv2, Protocol-TLSv1, Pro... SSLNegotiationPolicyType
Policy containing a list of public k... {PublicKey}                             PublicKeyPolicyType
Stickiness policy with session lifet... {CookieName}                            AppCookieStickinessPolicyType
Policy that controls whether to incl... {ProxyProtocol}                         ProxyProtocolPolicyType
```
**Example 2: This example describes the specified policy type.**

```
Get-ELBLoadBalancerPolicyType -PolicyTypeName ProxyProtocolPolicyType
```
**Output:**

```
Description                             PolicyAttributeTypeDescriptions         PolicyTypeName
-----------                             -------------------------------         --------------
Policy that controls whether to incl... {ProxyProtocol}                         ProxyProtocolPolicyType
```
**Example 3: This example displays the complete description of the specified policy type.**

```
(Get-ELBLoadBalancerPolicyType -PolicyTypeName).Description
```
**Output:**

```
Policy that controls whether to include the IP address and port of the originating request for TCP messages.
This policy operates on TCP/SSL listeners only
```
+  For API details, see [DescribeLoadBalancerPolicyTypes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets the policy types supported by Elastic Load Balancing.**

```
Get-ELBLoadBalancerPolicyType
```
**Output:**

```
Description                             PolicyAttributeTypeDescriptions         PolicyTypeName
-----------                             -------------------------------         --------------
Stickiness policy with session lifet... {CookieExpirationPeriod}                LBCookieStickinessPolicyType
Policy that controls authentication ... {PublicKeyPolicyName}                   BackendServerAuthenticationPolicyType
Listener policy that defines the cip... {Protocol-SSLv2, Protocol-TLSv1, Pro... SSLNegotiationPolicyType
Policy containing a list of public k... {PublicKey}                             PublicKeyPolicyType
Stickiness policy with session lifet... {CookieName}                            AppCookieStickinessPolicyType
Policy that controls whether to incl... {ProxyProtocol}                         ProxyProtocolPolicyType
```
**Example 2: This example describes the specified policy type.**

```
Get-ELBLoadBalancerPolicyType -PolicyTypeName ProxyProtocolPolicyType
```
**Output:**

```
Description                             PolicyAttributeTypeDescriptions         PolicyTypeName
-----------                             -------------------------------         --------------
Policy that controls whether to incl... {ProxyProtocol}                         ProxyProtocolPolicyType
```
**Example 3: This example displays the complete description of the specified policy type.**

```
(Get-ELBLoadBalancerPolicyType -PolicyTypeName).Description
```
**Output:**

```
Policy that controls whether to include the IP address and port of the originating request for TCP messages.
This policy operates on TCP/SSL listeners only
```
+  For API details, see [DescribeLoadBalancerPolicyTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing_example_elastic-load-balancing_DescribeLoadBalancerPolicies_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeLoadBalancerPolicies` with a CLI
<a name="elastic-load-balancing_example_elastic-load-balancing_DescribeLoadBalancerPolicies_section"></a>

The following code examples show how to use `DescribeLoadBalancerPolicies`.

------
#### [ CLI ]

**AWS CLI**
**To describe all policies associated with a load balancer**
This example describes all of the policies associated with the specified load balancer.
Command:

```
aws elb describe-load-balancer-policies --load-balancer-name {{my-load-balancer}}
```
Output:

```
{
  "PolicyDescriptions": [
    {
      "PolicyAttributeDescriptions": [
        {
          "AttributeName": "ProxyProtocol",
          "AttributeValue": "true"
        }
      ],
      "PolicyName": "my-ProxyProtocol-policy",
      "PolicyTypeName": "ProxyProtocolPolicyType"
    },
    {
        "PolicyAttributeDescriptions": [
            {
                "AttributeName": "CookieName",
                "AttributeValue": "my-app-cookie"
            }
        ],
        "PolicyName": "my-app-cookie-policy",
        "PolicyTypeName": "AppCookieStickinessPolicyType"
    },
    {
      "PolicyAttributeDescriptions": [
        {
          "AttributeName": "CookieExpirationPeriod",
          "AttributeValue": "60"
        }
      ],
      "PolicyName": "my-duration-cookie-policy",
      "PolicyTypeName": "LBCookieStickinessPolicyType"
    },
    .
    .
    .
  ]
}
```
**To describe a specific policy associated with a load balancer**
This example describes the specified policy associated with the specified load balancer.
Command:

```
aws elb describe-load-balancer-policies --load-balancer-name {{my-load-balancer}} --policy-name {{my-authentication-policy}}
```
Output:

```
{
  "PolicyDescriptions": [
      {
          "PolicyAttributeDescriptions": [
              {
                  "AttributeName": "PublicKeyPolicyName",
                  "AttributeValue": "my-PublicKey-policy"
              }
          ],
          "PolicyName": "my-authentication-policy",
          "PolicyTypeName": "BackendServerAuthenticationPolicyType"
      }
  ]
}
```
+  For API details, see [DescribeLoadBalancerPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-policies.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the policies associated with the specified load balancer.**

```
Get-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer
```
**Output:**

```
PolicyAttributeDescriptions             PolicyName                              PolicyTypeName
---------------------------             ----------                              --------------
{ProxyProtocol}                         my-ProxyProtocol-policy                 ProxyProtocolPolicyType
{CookieName}                            my-app-cookie-policy                    AppCookieStickinessPolicyType
```
**Example 2: This example describes the attributes of the specified policy.**

```
(Get-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer -PolicyName my-ProxyProtocol-policy).PolicyAttributeDescriptions
```
**Output:**

```
AttributeName    AttributeValue
-------------    --------------
ProxyProtocol    true
```
**Example 3: This example describes the predefined policies, including the sample policies. The names of the sample policies have the ELBSample- prefix.**

```
Get-ELBLoadBalancerPolicy
```
**Output:**

```
PolicyAttributeDescriptions             PolicyName                              PolicyTypeName
---------------------------             ----------                              --------------
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2015-05               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2015-03               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2015-02               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2014-10               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2014-01               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2011-08               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSample-ELBDefaultCipherPolicy        SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSample-OpenSSLDefaultCipherPolicy    SSLNegotiationPolicyType
```
+  For API details, see [DescribeLoadBalancerPolicies](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the policies associated with the specified load balancer.**

```
Get-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer
```
**Output:**

```
PolicyAttributeDescriptions             PolicyName                              PolicyTypeName
---------------------------             ----------                              --------------
{ProxyProtocol}                         my-ProxyProtocol-policy                 ProxyProtocolPolicyType
{CookieName}                            my-app-cookie-policy                    AppCookieStickinessPolicyType
```
**Example 2: This example describes the attributes of the specified policy.**

```
(Get-ELBLoadBalancerPolicy -LoadBalancerName my-load-balancer -PolicyName my-ProxyProtocol-policy).PolicyAttributeDescriptions
```
**Output:**

```
AttributeName    AttributeValue
-------------    --------------
ProxyProtocol    true
```
**Example 3: This example describes the predefined policies, including the sample policies. The names of the sample policies have the ELBSample- prefix.**

```
Get-ELBLoadBalancerPolicy
```
**Output:**

```
PolicyAttributeDescriptions             PolicyName                              PolicyTypeName
---------------------------             ----------                              --------------
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2015-05               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2015-03               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2015-02               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2014-10               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2014-01               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSecurityPolicy-2011-08               SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSample-ELBDefaultCipherPolicy        SSLNegotiationPolicyType
{Protocol-SSLv2, Protocol-TLSv1, Pro... ELBSample-OpenSSLDefaultCipherPolicy    SSLNegotiationPolicyType
```
+  For API details, see [DescribeLoadBalancerPolicies](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

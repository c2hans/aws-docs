---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancerPolicies.html
---

# DescribeLoadBalancerPolicies
<a name="API_DescribeLoadBalancerPolicies"></a>

Describes the specified policies.

If you specify a load balancer name, the action returns the descriptions of all policies created for the load balancer. If you specify a policy name associated with your load balancer, the action returns the description of that policy. If you don't specify a load balancer name, the action returns descriptions of the specified sample policies, or descriptions of all sample policies. The names of the sample policies have the `ELBSample-` prefix.

## Request Parameters
<a name="API_DescribeLoadBalancerPolicies_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: No

 **PolicyNames.member.N**
The names of the policies.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeLoadBalancerPolicies_ResponseElements"></a>

The following element is returned by the service.

 **PolicyDescriptions.member.N**
Information about the policies.
Type: Array of [PolicyDescription](API_PolicyDescription.md) objects

## Errors
<a name="API_DescribeLoadBalancerPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** PolicyNotFound **
One or more of the specified policies do not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeLoadBalancerPolicies_Examples"></a>

### Describe all policies
<a name="API_DescribeLoadBalancerPolicies_Example_1"></a>

This example describes all of the policies associated with the specified load balancer.

#### Sample Request
<a name="API_DescribeLoadBalancerPolicies_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeLoadBalancerPolicies
&LoadBalancerName=my-loadbalancer
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLoadBalancerPolicies_Example_1_Response"></a>

```
<DescribeLoadBalancerPoliciesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeLoadBalancerPoliciesResult>
    <PolicyDescriptions>
      <member>
        <PolicyName>my-duration-sticky-policy</PolicyName>
        <PolicyTypeName>LBCookieStickinessPolicyType</PolicyTypeName>
        <PolicyAttributeDescriptions>
          <member>
            <AttributeName>CookieExpirationPeriod</AttributeName>
            <AttributeValue>60</AttributeValue>
          </member>
        </PolicyAttributeDescriptions>
      </member>
      <member>
        <PolicyName>my-app-sticky-policy</PolicyName>
        <PolicyTypeName>AppCookieStickinessPolicyType</PolicyTypeName>
        <PolicyAttributeDescriptions>
          <member>
            <AttributeName>CookieName</AttributeName>
            <AttributeValue>my-app-cookie</AttributeValue>
          </member>
        </PolicyAttributeDescriptions>
      </member>
    </PolicyDescriptions>
  </DescribeLoadBalancerPoliciesResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeLoadBalancerPoliciesResponse>
```

### Describe a policy
<a name="API_DescribeLoadBalancerPolicies_Example_2"></a>

This example describes the specified policy associated with the specified load balancer.

#### Sample Request
<a name="API_DescribeLoadBalancerPolicies_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeLoadBalancerPolicies
&LoadBalancerName=my-loadbalancer
&PolicyNames.member.1=EnableProxyProtocol
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLoadBalancerPolicies_Example_2_Response"></a>

```
<DescribeLoadBalancerPoliciesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeLoadBalancerPoliciesResult>
   <PolicyDescriptions>
      <member>
        <PolicyName>EnableProxyProtocol</PolicyName>
        <PolicyTypeName>ProxyProtocolPolicyType</PolicyTypeName>
        <PolicyAttributeDescriptions>
          <member>
            <AttributeName>ProxyProtocol</AttributeName>
            <AttributeValue>true</AttributeValue>
          </member>
        </PolicyAttributeDescriptions>
      </member>
    </PolicyDescriptions>
  </DescribeLoadBalancerPoliciesResult>
  <ResponseMetadata>
    <RequestId>1549581b-12b7-11e3-895e-1334aEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeLoadBalancerPoliciesResponse>
```

## See Also
<a name="API_DescribeLoadBalancerPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicies)

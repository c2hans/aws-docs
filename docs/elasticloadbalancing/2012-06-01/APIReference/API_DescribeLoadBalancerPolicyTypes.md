---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancerPolicyTypes.html
---

# DescribeLoadBalancerPolicyTypes
<a name="API_DescribeLoadBalancerPolicyTypes"></a>

Describes the specified load balancer policy types or all load balancer policy types.

The description of each type indicates how it can be used. For example, some policies can be used only with layer 7 listeners, some policies can be used only with layer 4 listeners, and some policies can be used only with your EC2 instances.

You can use [CreateLoadBalancerPolicy](API_CreateLoadBalancerPolicy.md) to create a policy configuration for any of these policy types. Then, depending on the policy type, use either [SetLoadBalancerPoliciesOfListener](API_SetLoadBalancerPoliciesOfListener.md) or [SetLoadBalancerPoliciesForBackendServer](API_SetLoadBalancerPoliciesForBackendServer.md) to set the policy.

## Request Parameters
<a name="API_DescribeLoadBalancerPolicyTypes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **PolicyTypeNames.member.N**
The names of the policy types. If no names are specified, describes all policy types defined by Elastic Load Balancing.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeLoadBalancerPolicyTypes_ResponseElements"></a>

The following element is returned by the service.

 **PolicyTypeDescriptions.member.N**
Information about the policy types.
Type: Array of [PolicyTypeDescription](API_PolicyTypeDescription.md) objects

## Errors
<a name="API_DescribeLoadBalancerPolicyTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** PolicyTypeNotFound **
One or more of the specified policy types do not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeLoadBalancerPolicyTypes_Examples"></a>

### Describe all policy types
<a name="API_DescribeLoadBalancerPolicyTypes_Example_1"></a>

This example describes the load balancer policy types that you can use to create policy configurations.

#### Sample Request
<a name="API_DescribeLoadBalancerPolicyTypes_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeLoadBalancerPolicyTypes
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLoadBalancerPolicyTypes_Example_1_Response"></a>

```
<DescribeLoadBalancerPolicyTypesResponse  xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeLoadBalancerPolicyTypesResult>
    <PolicyTypeName>SSLNegotiationPolicyType</PolicyTypeName>
      <...>
    <PolicyTypeName>BackendServerAuthenticationPolicyType</PolicyTypeName>
      <...>
    <PolicyTypeName>PublicKeyPolicyType</PolicyTypeName>
      <...>
    <PolicyTypeName>AppCookieStickinessPolicyType</PolicyTypeName>
      <...>
    <PolicyTypeName>LBCookieStickinessPolicyType</PolicyTypeName>
      <...>
    <PolicyTypeName>ProxyProtocolPolicyType</PolicyTypeName>
      <...>
  </DescribeLoadBalancerPolicyTypesResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeLoadBalancerPolicyTypesResponse>
```

### Describe a policy type
<a name="API_DescribeLoadBalancerPolicyTypes_Example_2"></a>

This example describes the specified policy type.

#### Sample Request
<a name="API_DescribeLoadBalancerPolicyTypes_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeLoadBalancerPolicyTypes
&PolicyTypeNames.member.1=ProxyProtocolPolicyType
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLoadBalancerPolicyTypes_Example_2_Response"></a>

```
<DescribeLoadBalancerPolicyTypesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeLoadBalancerPolicyTypesResult>
    <PolicyTypeDescriptions>
      <member>
        <PolicyAttributeTypeDescriptions>
          <member>
            <AttributeName>ProxyProtocol</AttributeName>
            <AttributeType>Boolean</AttributeType>
            <Cardinality>ONE</Cardinality>
          </member>
        </PolicyAttributeTypeDescriptions>
        <PolicyTypeName>ProxyProtocolPolicyType</PolicyTypeName>
        <Description>Policy that controls whether to include the IP address and port of the originating request for TCP messages.
        This policy operates on TCP/SSL listeners only</Description>
      </member>
    </PolicyTypeDescriptions>
  </DescribeLoadBalancerPolicyTypesResult>
  <ResponseMetadata>
    <RequestId>1549581b-12b7-11e3-895e-1334aEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeLoadBalancerPolicyTypesResponse>
```

## See Also
<a name="API_DescribeLoadBalancerPolicyTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerPolicyTypes)

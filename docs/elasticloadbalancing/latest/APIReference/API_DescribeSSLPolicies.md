---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeSSLPolicies.html
---

# DescribeSSLPolicies
<a name="API_DescribeSSLPolicies"></a>

Describes the specified policies or all policies used for SSL negotiation.

For more information, see [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html) in the *Application Load Balancers Guide* and [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html) in the *Network Load Balancers Guide*.

## Request Parameters
<a name="API_DescribeSSLPolicies_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerType **
 The type of load balancer. The default lists the SSL policies for all load balancers.
Type: String
Valid Values: `application | network | gateway`
Required: No

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 **Names.member.N**
The names of the policies.
Type: Array of strings
Required: No

 ** PageSize **
The maximum number of results to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

## Response Elements
<a name="API_DescribeSSLPolicies_ResponseElements"></a>

The following elements are returned by the service.

 ** NextMarker **
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.
Type: String

 **SslPolicies.member.N**
Information about the security policies.
Type: Array of [SslPolicy](API_SslPolicy.md) objects

## Errors
<a name="API_DescribeSSLPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** SSLPolicyNotFound **
The specified SSL policy does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeSSLPolicies_Examples"></a>

### Describe the specified policy used for SSL negotiation
<a name="API_DescribeSSLPolicies_Example_1"></a>

This example describes the specified policy used for SSL negotiation.

#### Sample Request
<a name="API_DescribeSSLPolicies_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeSSLPolicies
&Names.member.1=ELBSecurityPolicy-2016-08
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeSSLPolicies_Example_1_Response"></a>

```
<DescribeSSLPoliciesResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeSSLPoliciesResult>
    <SslPolicies>
      <member>
        <Ciphers>
          <member>
            <Name>ECDHE-ECDSA-AES128-GCM-SHA256</Name>
            <Priority>1</Priority>
          </member>
          <member>
            <Name>ECDHE-RSA-AES128-GCM-SHA256</Name>
            <Priority>2</Priority>
          </member>
          <member>
            <Name>ECDHE-ECDSA-AES128-SHA256</Name>
            <Priority>3</Priority>
          </member>
          ...
          <member>
            <Name>AES256-SHA</Name>
            <Priority>19</Priority>
          </member>
        </Ciphers>
        <Name>ELBSecurityPolicy-2016-08</Name>
        <SslProtocols>
          <member>TLSv1</member>
          <member>TLSv1.1</member>
          <member>TLSv1.2</member>
        </SslProtocols>
      </member>
    </SslPolicies>
  </DescribeSSLPoliciesResult>
  <ResponseMetadata>
    <RequestId>a78c9aee-f2aa-11e5-8a24-ffe2bf8623ae</RequestId>
  </ResponseMetadata>
</DescribeSSLPoliciesResponse>
```

### Describe all policies used for SSL negotiation
<a name="API_DescribeSSLPolicies_Example_2"></a>

This example describes all the policies that you can use for SSL negotiation.

#### Sample Request
<a name="API_DescribeSSLPolicies_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeSSLPolicies
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_DescribeSSLPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeSSLPolicies)

---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancerAttributes.html
---

# DescribeLoadBalancerAttributes
<a name="API_DescribeLoadBalancerAttributes"></a>

Describes the attributes for the specified load balancer.

## Request Parameters
<a name="API_DescribeLoadBalancerAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeLoadBalancerAttributes_ResponseElements"></a>

The following element is returned by the service.

 ** LoadBalancerAttributes **
Information about the load balancer attributes.
Type: [LoadBalancerAttributes](API_LoadBalancerAttributes.md) object

## Errors
<a name="API_DescribeLoadBalancerAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerAttributeNotFound **
The specified load balancer attribute does not exist.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeLoadBalancerAttributes_Examples"></a>

### Describe load balancer attributes
<a name="API_DescribeLoadBalancerAttributes_Example_1"></a>

This example describes the attributes of the specified load balancer.

#### Sample Request
<a name="API_DescribeLoadBalancerAttributes_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeLoadBalancerAttributes
&LoadBalancerName=my-loadbalancer
&Version=2012-06-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLoadBalancerAttributes_Example_1_Response"></a>

```
<DescribeLoadBalancerAttributesResponse  xmlns="http://elasticloadbalancing.amazonaws.com/doc/2012-06-01/">
  <DescribeLoadBalancerAttributesResult>
    <LoadBalancerAttributes>
      <AccessLog>
        <Enabled>true</Enabled>
        <S3BucketName>my-loadbalancer-logs</S3BucketName>
        <S3BucketPrefix>testprefix</S3BucketPrefix>
        <EmitInterval>5</EmitInterval>
      </AccessLog>
      <ConnectionSettings>
        <IdleTimeout>30</IdleTimeout>
      </ConnectionSettings>
      <CrossZoneLoadBalancing>
        <Enabled>true</Enabled>
      </CrossZoneLoadBalancing>
      <ConnectionDraining>
        <Enabled>true</Enabled>
        <Timeout>60</Timeout>
      </ConnectionDraining>
    </LoadBalancerAttributes>
  </DescribeLoadBalancerAttributesResult>
  <ResponseMetadata>
    <RequestId>83c88b9d-12b7-11e3-8b82-87b12EXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeLoadBalancerAttributesResponse>
```

## See Also
<a name="API_DescribeLoadBalancerAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/DescribeLoadBalancerAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

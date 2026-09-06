---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTags.html
---

# DescribeTags
<a name="API_DescribeTags"></a>

Describes the tags for the specified Elastic Load Balancing resources. You can describe the tags for one or more Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, or rules.

## Request Parameters
<a name="API_DescribeTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ResourceArns.member.N**
The Amazon Resource Names (ARN) of the resources. You can specify up to 20 resources in a single call.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_DescribeTags_ResponseElements"></a>

The following element is returned by the service.

 **TagDescriptions.member.N**
Information about the tags.
Type: Array of [TagDescription](API_TagDescription.md) objects

## Errors
<a name="API_DescribeTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ListenerNotFound **
The specified listener does not exist.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** RuleNotFound **
The specified rule does not exist.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeTags_Examples"></a>

### Describe the tags assigned to a load balancer
<a name="API_DescribeTags_Example_1"></a>

This example describes the tags assigned to the specified load balancer.

#### Sample Request
<a name="API_DescribeTags_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeTags
&ResourceArns.member.1=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeTags_Example_1_Response"></a>

```
<DescribeTagsResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeTagsResult>
    <TagDescriptions>
      <member>
        <ResourceArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188</ResourceArn>
        <Tags>
          <member>
            <Value>lima</Value>
            <Key>project</Key>
          </member>
          <member>
            <Value>digital-media</Value>
            <Key>department</Key>
          </member>
        </Tags>
      </member>
    </TagDescriptions>
  </DescribeTagsResult>
  <ResponseMetadata>
    <RequestId>34f144db-f2d9-11e5-a53c-67205c0d10fd</RequestId>
  </ResponseMetadata>
</DescribeTagsResponse>
```

## See Also
<a name="API_DescribeTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeTags)

---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AddTags.html
---

# AddTags
<a name="API_AddTags"></a>

Adds the specified tags to the specified Elastic Load Balancing resource. You can tag your Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, trust stores, listeners, and rules.

Each tag consists of a key and an optional value. If a resource already has a tag with the same key, `AddTags` updates its value.

To list the current tags for your resources, use [DescribeTags](API_DescribeTags.md). To remove tags from your resources, use [RemoveTags](API_RemoveTags.md).

## Request Parameters
<a name="API_AddTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ResourceArns.member.N**
The Amazon Resource Name (ARN) of the resource.
Type: Array of strings
Required: Yes

 **Tags.member.N**
The tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Errors
<a name="API_AddTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateTagKeys **
A tag key was specified more than once.
HTTP Status Code: 400

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

 ** TooManyTags **
You've reached the limit on the number of tags for this resource.
HTTP Status Code: 400

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

## Examples
<a name="API_AddTags_Examples"></a>

### Add tags to a load balancer
<a name="API_AddTags_Example_1"></a>

This example adds the specified tags to the specified load balancer.

#### Sample Request
<a name="API_AddTags_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=AddTags
&ResourceArns.member.1=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Tags.member.1.Key=project
&Tags.member.1.Value=lima
&Tags.member.2.Key=department
&Tags.member.2.Value=digital-media
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_AddTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/AddTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/AddTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/AddTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/AddTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/AddTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/AddTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/AddTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/AddTags)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/AddTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/AddTags)

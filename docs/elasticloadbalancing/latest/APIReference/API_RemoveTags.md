---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RemoveTags.html
---

# RemoveTags
<a name="API_RemoveTags"></a>

Removes the specified tags from the specified Elastic Load Balancing resources. You can remove the tags for one or more Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, or rules.

To list the current tags for your resources, use [DescribeTags](API_DescribeTags.md).

## Request Parameters
<a name="API_RemoveTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ResourceArns.member.N**
The Amazon Resource Name (ARN) of the resource.
Type: Array of strings
Required: Yes

 **TagKeys.member.N**
The tag keys for the tags to remove.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Errors
<a name="API_RemoveTags_Errors"></a>

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

 ** TooManyTags **
You've reached the limit on the number of tags for this resource.
HTTP Status Code: 400

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

## Examples
<a name="API_RemoveTags_Examples"></a>

### Remove tags from a load balancer
<a name="API_RemoveTags_Example_1"></a>

This example removes the specified tags from the specified load balancer.

#### Sample Request
<a name="API_RemoveTags_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=RemoveTags
&ResourceArns.member.1=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&TagKeys.member.1=project
&TagKeys.member.2=department
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_RemoveTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/RemoveTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/RemoveTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/RemoveTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/RemoveTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/RemoveTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/RemoveTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/RemoveTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/RemoveTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/RemoveTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/RemoveTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

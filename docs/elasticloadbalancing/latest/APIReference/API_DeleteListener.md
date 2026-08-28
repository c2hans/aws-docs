---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DeleteListener.html
---

# DeleteListener
<a name="API_DeleteListener"></a>

Deletes the specified listener.

Alternatively, your listener is deleted when you delete the load balancer to which it is attached, using [DeleteLoadBalancer](API_DeleteLoadBalancer.md).

## Request Parameters
<a name="API_DeleteListener_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ListenerArn **
The Amazon Resource Name (ARN) of the listener.
Type: String
Required: Yes

## Errors
<a name="API_DeleteListener_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ListenerNotFound **
The specified listener does not exist.
HTTP Status Code: 400

 ** ResourceInUse **
A specified resource is in use.
HTTP Status Code: 400

## Examples
<a name="API_DeleteListener_Examples"></a>

### Delete a listener
<a name="API_DeleteListener_Example_1"></a>

This example deletes the specified listener.

#### Sample Request
<a name="API_DeleteListener_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DeleteListener
&ListenerArn=arn:aws:elasticloadbalancing:ua-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_DeleteListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DeleteListener)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DeleteListener)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DeleteListener)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DeleteListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DeleteListener)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DeleteListener)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DeleteListener)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DeleteListener)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DeleteListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DeleteListener)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

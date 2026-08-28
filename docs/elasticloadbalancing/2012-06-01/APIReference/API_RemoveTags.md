---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_RemoveTags.html
---

# RemoveTags
<a name="API_RemoveTags"></a>

Removes one or more tags from the specified load balancer.

## Request Parameters
<a name="API_RemoveTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **LoadBalancerNames.member.N**
The name of the load balancer. You can specify a maximum of one load balancer name.
Type: Array of strings
Required: Yes

 **Tags.member.N**
The list of tag keys to remove.
Type: Array of [TagKeyOnly](API_TagKeyOnly.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Errors
<a name="API_RemoveTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

## Examples
<a name="API_RemoveTags_Examples"></a>

### Remove load balancer tags
<a name="API_RemoveTags_Example_1"></a>

This example removes the specified tags from the specified load balancer.

#### Sample Request
<a name="API_RemoveTags_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=RemoveTags
&LoadBalancerName=my-loadbalancer
&Tags.member.1.Key=department
&Tags.member.2.Key=project
&Version=2012-06-01
&AUTHPARAMS
```

## See Also
<a name="API_RemoveTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/RemoveTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/RemoveTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/RemoveTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/RemoveTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/RemoveTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/RemoveTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/RemoveTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/RemoveTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/RemoveTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/RemoveTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AddTags.html
---

# AddTags
<a name="API_AddTags"></a>

Adds the specified tags to the specified load balancer. Each load balancer can have a maximum of 10 tags.

Each tag consists of a key and an optional value. If a tag with the same key is already associated with the load balancer, `AddTags` updates its value.

For more information, see [Tag your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html) in the *User Guide for Classic Load Balancers*.

## Request Parameters
<a name="API_AddTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **LoadBalancerNames.member.N**
The name of the load balancer. You can specify one load balancer only.
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

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** TooManyTags **
The quota for the number of tags that can be assigned to a load balancer has been reached.
HTTP Status Code: 400

## Examples
<a name="API_AddTags_Examples"></a>

### Add tags
<a name="API_AddTags_Example_1"></a>

This example adds tags to the specified load balancer.

#### Sample Request
<a name="API_AddTags_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=AddTags
&LoadBalancerNames.member.1=my-loadbalancer
&Tags.member.1.Key=project
&Tags.member.1.Value=lima
&Version=2012-06-01
&AUTHPARAMS
```

## See Also
<a name="API_AddTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancing-2012-06-01/AddTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancing-2012-06-01/AddTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/AddTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancing-2012-06-01/AddTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/AddTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancing-2012-06-01/AddTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancing-2012-06-01/AddTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancing-2012-06-01/AddTags)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancing-2012-06-01/AddTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/AddTags)

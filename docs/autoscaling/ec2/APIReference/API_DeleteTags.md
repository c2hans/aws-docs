---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteTags.html
---

# DeleteTags
<a name="API_DeleteTags"></a>

Deletes the specified tags.

## Request Parameters
<a name="API_DeleteTags_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Tags.member.N**
One or more tags.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Errors
<a name="API_DeleteTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ResourceInUse **
The operation can't be performed because the resource is in use.
 ** message **

HTTP Status Code: 400

## Examples
<a name="API_DeleteTags_Examples"></a>

### Example
<a name="API_DeleteTags_Example_1"></a>

This example illustrates one usage of DeleteTags.

#### Sample Request
<a name="API_DeleteTags_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DeleteTags
&Tags.member.1.ResourceId=my-asg
&Tags.member.1.ResourceType=auto-scaling-group
&Tags.member.1.Key=environment
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_DeleteTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DeleteTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DeleteTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DeleteTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DeleteTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DeleteTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DeleteTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DeleteTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DeleteTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DeleteTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DeleteTags)

---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachTrafficSources.html
---

# AttachTrafficSources
<a name="API_AttachTrafficSources"></a>

Attaches one or more traffic sources to the specified Auto Scaling group.

You can use any of the following as traffic sources for an Auto Scaling group:
+ Application Load Balancer
+ Classic Load Balancer
+ Gateway Load Balancer
+ Network Load Balancer
+ VPC Lattice

This operation is additive and does not detach existing traffic sources from the Auto Scaling group.

After the operation completes, use the [DescribeTrafficSources](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTrafficSources.html) API to return details about the state of the attachments between traffic sources and your Auto Scaling group. To detach a traffic source from the Auto Scaling group, call the [DetachTrafficSources](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachTrafficSources.html) API.

## Request Parameters
<a name="API_AttachTrafficSources_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** SkipZonalShiftValidation **
 If you enable zonal shift with cross-zone disabled load balancers, capacity could become imbalanced across Availability Zones. To skip the validation, specify `true`. For more information, see [Auto Scaling group zonal shift](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html) in the *Amazon EC2 Auto Scaling User Guide*.
Type: Boolean
Required: No

 **TrafficSources.member.N**
The unique identifiers of one or more traffic sources. You can specify up to 10 traffic sources.
Type: Array of [TrafficSourceIdentifier](API_TrafficSourceIdentifier.md) objects
Required: Yes

## Errors
<a name="API_AttachTrafficSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InstanceRefreshInProgress **
The request failed because an active instance refresh already exists for the specified Auto Scaling group.
HTTP Status Code: 400

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

 ** ServiceLinkedRoleFailure **
The service-linked role is not yet ready for use.
HTTP Status Code: 500

## Examples
<a name="API_AttachTrafficSources_Examples"></a>

### Example
<a name="API_AttachTrafficSources_Example_1"></a>

This example attaches two VPC Lattice target groups, as specified by their ARNs, to the Auto Scaling group named `my-asg`.

#### Sample Request
<a name="API_AttachTrafficSources_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=AttachTrafficSources
&AutoScalingGroupName=my-asg
&TrafficSources.member.1.Identifier=arn:aws:vpc-lattice:us-west-2:123456789012:targetgroup/tg-0e2f2665eEXAMPLE
&TrafficSources.member.2.Identifier=arn:aws:vpc-lattice:us-west-2:123456789012:targetgroup/tg-8360a9e72EXAMPLE
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_AttachTrafficSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/AttachTrafficSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/AttachTrafficSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/AttachTrafficSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/AttachTrafficSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/AttachTrafficSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/AttachTrafficSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/AttachTrafficSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/AttachTrafficSources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/AttachTrafficSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/AttachTrafficSources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

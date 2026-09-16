---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterInstanceEventNotificationAttributes.html
---

# RegisterInstanceEventNotificationAttributes
<a name="API_RegisterInstanceEventNotificationAttributes"></a>

Registers a set of tag keys to include in scheduled event notifications for your resources.

To remove tags, use [DeregisterInstanceEventNotificationAttributes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterInstanceEventNotificationAttributes.html).

## Request Parameters
<a name="API_RegisterInstanceEventNotificationAttributes_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceTagAttribute**
Information about the tag keys to register.
Type: [RegisterInstanceTagAttributeRequest](API_RegisterInstanceTagAttributeRequest.md) object
Required: No

## Response Elements
<a name="API_RegisterInstanceEventNotificationAttributes_ResponseElements"></a>

The following elements are returned by the service.

 **instanceTagAttribute**
The resulting set of tag keys.
Type: [InstanceTagNotificationAttribute](API_InstanceTagNotificationAttribute.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_RegisterInstanceEventNotificationAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_RegisterInstanceEventNotificationAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RegisterInstanceEventNotificationAttributes)

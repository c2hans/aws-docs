---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTrafficMirrorFilterNetworkServices.html
---

# ModifyTrafficMirrorFilterNetworkServices
<a name="API_ModifyTrafficMirrorFilterNetworkServices"></a>

Allows or restricts mirroring network services.

 By default, Amazon DNS network services are not eligible for Traffic Mirror. Use `AddNetworkServices` to add network services to a Traffic Mirror filter. When a network service is added to the Traffic Mirror filter, all traffic related to that network service will be mirrored. When you no longer want to mirror network services, use `RemoveNetworkServices` to remove the network services from the Traffic Mirror filter.

## Request Parameters
<a name="API_ModifyTrafficMirrorFilterNetworkServices_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddNetworkService.N**
The network service, for example Amazon DNS, that you want to mirror.
Type: Array of strings
Valid Values: `amazon-dns`
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **RemoveNetworkService.N**
The network service, for example Amazon DNS, that you no longer want to mirror.
Type: Array of strings
Valid Values: `amazon-dns`
Required: No

 **TrafficMirrorFilterId**
The ID of the Traffic Mirror filter.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyTrafficMirrorFilterNetworkServices_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **trafficMirrorFilter**
The Traffic Mirror filter that the network service is associated with.
Type: [TrafficMirrorFilter](API_TrafficMirrorFilter.md) object

## Errors
<a name="API_ModifyTrafficMirrorFilterNetworkServices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyTrafficMirrorFilterNetworkServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyTrafficMirrorFilterNetworkServices)

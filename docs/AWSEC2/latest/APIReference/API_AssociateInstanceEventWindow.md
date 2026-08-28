---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateInstanceEventWindow.html
---

# AssociateInstanceEventWindow
<a name="API_AssociateInstanceEventWindow"></a>

Associates one or more targets with an event window. Only one type of target (instance IDs, Dedicated Host IDs, or tags) can be specified with an event window.

For more information, see [Define event windows for scheduled events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_AssociateInstanceEventWindow_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationTarget**
One or more targets associated with the specified event window.
Type: [InstanceEventWindowAssociationRequest](API_InstanceEventWindowAssociationRequest.md) object
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceEventWindowId**
The ID of the event window.
Type: String
Required: Yes

## Response Elements
<a name="API_AssociateInstanceEventWindow_ResponseElements"></a>

The following elements are returned by the service.

 **instanceEventWindow**
Information about the event window.
Type: [InstanceEventWindow](API_InstanceEventWindow.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AssociateInstanceEventWindow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_AssociateInstanceEventWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateInstanceEventWindow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateInstanceEventWindow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateInstanceEventWindow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateInstanceEventWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateInstanceEventWindow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateInstanceEventWindow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateInstanceEventWindow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateInstanceEventWindow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateInstanceEventWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateInstanceEventWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyManagedResourceVisibility.html
---

# ModifyManagedResourceVisibility
<a name="API_ModifyManagedResourceVisibility"></a>

Modifies the managed resource visibility configuration for the account. Use this operation to control whether managed resources are hidden or visible by default. Visibility settings are account-wide and affect all IAM principals uniformly. Hidden resources remain fully operational and billable.

## Request Parameters
<a name="API_ModifyManagedResourceVisibility_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DefaultVisibility**
The default visibility setting for managed resources. Valid values: `hidden` \| `visible`.
Type: String
Valid Values: `hidden | visible`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_ModifyManagedResourceVisibility_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **visibility**
The updated managed resource visibility settings for the account.
Type: [ManagedResourceVisibilitySettings](API_ManagedResourceVisibilitySettings.md) object

## Errors
<a name="API_ModifyManagedResourceVisibility_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyManagedResourceVisibility_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyManagedResourceVisibility)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyManagedResourceVisibility)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyManagedResourceVisibility)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyManagedResourceVisibility)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyManagedResourceVisibility)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyManagedResourceVisibility)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyManagedResourceVisibility)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyManagedResourceVisibility)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyManagedResourceVisibility)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyManagedResourceVisibility)

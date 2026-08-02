---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableAllowedImagesSettings.html
---

# DisableAllowedImagesSettings
<a name="API_DisableAllowedImagesSettings"></a>

Disables Allowed AMIs for your account in the specified AWS Region. When set to `disabled`, the image criteria in your Allowed AMIs settings do not apply, and no restrictions are placed on AMI discoverability or usage. Users in your account can launch instances using any public AMI or AMI shared with your account.

**Note**
The Allowed AMIs feature does not restrict the AMIs owned by your account. Regardless of the criteria you set, the AMIs created by your account will always be discoverable and usable by users in your account.

For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) in *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_DisableAllowedImagesSettings_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DisableAllowedImagesSettings_ResponseElements"></a>

The following elements are returned by the service.

 **allowedImagesSettingsState**
Returns `disabled` if the request succeeds; otherwise, it returns an error.
Type: String
Valid Values: `disabled`

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DisableAllowedImagesSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DisableAllowedImagesSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableAllowedImagesSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableAllowedImagesSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableAllowedImagesSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableAllowedImagesSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableAllowedImagesSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableAllowedImagesSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableAllowedImagesSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableAllowedImagesSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableAllowedImagesSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableAllowedImagesSettings)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetAllowedImagesSettings.html
---

# GetAllowedImagesSettings
<a name="API_GetAllowedImagesSettings"></a>

Gets the current state of the Allowed AMIs setting and the list of Allowed AMIs criteria at the account level in the specified Region.

**Note**
The Allowed AMIs feature does not restrict the AMIs owned by your account. Regardless of the criteria you set, the AMIs created by your account will always be discoverable and usable by users in your account.

For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) in *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_GetAllowedImagesSettings_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_GetAllowedImagesSettings_ResponseElements"></a>

The following elements are returned by the service.

 **imageCriterionSet**
The list of criteria for images that are discoverable and usable in the account in the specified AWS Region.
Type: Array of [ImageCriterion](API_ImageCriterion.md) objects

 **managedBy**
The entity that manages the Allowed AMIs settings. Possible values include:
+  `account` - The Allowed AMIs settings is managed by the account.
+  `declarative-policy` - The Allowed AMIs settings is managed by a declarative policy and can't be modified by the account.
Type: String
Valid Values: `account | declarative-policy`

 **requestId**
The ID of the request.
Type: String

 **state**
The current state of the Allowed AMIs setting at the account level in the specified AWS Region.
Possible values:
+  `disabled`: All AMIs are allowed.
+  `audit-mode`: All AMIs are allowed, but the `ImageAllowed` field is set to `true` if the AMI would be allowed with the current list of criteria if allowed AMIs was enabled.
+  `enabled`: Only AMIs matching the image criteria are discoverable and available for use.
Type: String

## Errors
<a name="API_GetAllowedImagesSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetAllowedImagesSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetAllowedImagesSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetAllowedImagesSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetAllowedImagesSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetAllowedImagesSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetAllowedImagesSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetAllowedImagesSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetAllowedImagesSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetAllowedImagesSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetAllowedImagesSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetAllowedImagesSettings)

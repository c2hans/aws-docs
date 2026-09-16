---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataDefaults.html
---

# ModifyInstanceMetadataDefaults
<a name="API_ModifyInstanceMetadataDefaults"></a>

Modifies the default instance metadata service (IMDS) settings at the account level in the specified AWS  Region.

**Note**
To remove a parameter's account-level default setting, specify `no-preference`. If an account-level setting is cleared with `no-preference`, then the instance launch considers the other instance metadata settings. For more information, see [Order of precedence for instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#instance-metadata-options-order-of-precedence) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_ModifyInstanceMetadataDefaults_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **HttpEndpoint**
Enables or disables the IMDS endpoint on an instance. When disabled, the instance metadata can't be accessed.
Type: String
Valid Values: `disabled | enabled | no-preference`
Required: No

 **HttpPutResponseHopLimit**
The maximum number of hops that the metadata token can travel. To indicate no preference, specify `-1`.
Possible values: Integers from `1` to `64`, and `-1` to indicate no preference
Type: Integer
Required: No

 **HttpTokens**
Indicates whether IMDSv2 is required.
+  `optional` – IMDSv2 is optional, which means that you can use either IMDSv2 or IMDSv1.
+  `required` – IMDSv2 is required, which means that IMDSv1 is disabled, and you must use IMDSv2.
Type: String
Valid Values: `optional | required | no-preference`
Required: No

 **HttpTokensEnforced**
Specifies whether to enforce the requirement of IMDSv2 on an instance at the time of launch. When enforcement is enabled, the instance can't launch unless IMDSv2 (`HttpTokens`) is set to `required`. For more information, see [Enforce IMDSv2 at the account level](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#enforce-imdsv2-at-the-account-level) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `disabled | enabled | no-preference`
Required: No

 **InstanceMetadataTags**
Enables or disables access to an instance's tags from the instance metadata. For more information, see [View tags for your EC2 instances using instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `disabled | enabled | no-preference`
Required: No

## Response Elements
<a name="API_ModifyInstanceMetadataDefaults_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
If the request succeeds, the response returns `true`. If the request fails, no response is returned, and instead an error message is returned.
Type: Boolean

## Errors
<a name="API_ModifyInstanceMetadataDefaults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyInstanceMetadataDefaults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyInstanceMetadataDefaults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyInstanceMetadataDefaults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyInstanceMetadataDefaults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyInstanceMetadataDefaults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyInstanceMetadataDefaults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyInstanceMetadataDefaults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyInstanceMetadataDefaults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyInstanceMetadataDefaults)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyInstanceMetadataDefaults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyInstanceMetadataDefaults)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceMetadataDefaults.html
---

# GetInstanceMetadataDefaults
<a name="API_GetInstanceMetadataDefaults"></a>

Gets the default instance metadata service (IMDS) settings that are set at the account level in the specified AWS  Region.

For more information, see [Order of precedence for instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html#instance-metadata-options-order-of-precedence) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_GetInstanceMetadataDefaults_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_GetInstanceMetadataDefaults_ResponseElements"></a>

The following elements are returned by the service.

 **accountLevel**
The account-level default IMDS settings.
Type: [InstanceMetadataDefaultsResponse](API_InstanceMetadataDefaultsResponse.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetInstanceMetadataDefaults_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetInstanceMetadataDefaults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetInstanceMetadataDefaults)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetInstanceMetadataDefaults)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetInstanceMetadataDefaults)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetInstanceMetadataDefaults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetInstanceMetadataDefaults)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetInstanceMetadataDefaults)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetInstanceMetadataDefaults)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetInstanceMetadataDefaults)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetInstanceMetadataDefaults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetInstanceMetadataDefaults)

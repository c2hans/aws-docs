---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2ClientVpnEndpointClientConnectOptionsDetails.html
---

# AwsEc2ClientVpnEndpointClientConnectOptionsDetails
<a name="API_AwsEc2ClientVpnEndpointClientConnectOptionsDetails"></a>

 The options for managing connection authorization for new client connections.

## Contents
<a name="API_AwsEc2ClientVpnEndpointClientConnectOptionsDetails_Contents"></a>

 ** Enabled **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointClientConnectOptionsDetails-Enabled"></a>
 Indicates whether client connect options are enabled.
Type: Boolean
Required: No

 ** LambdaFunctionArn **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointClientConnectOptionsDetails-LambdaFunctionArn"></a>
 The Amazon Resource Name (ARN) of the Lambda function used for connection authorization.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsEc2ClientVpnEndpointClientConnectOptionsDetails-Status"></a>
 The status of any updates to the client connect options.
Type: [AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails](API_AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails.md) object
Required: No

## See Also
<a name="API_AwsEc2ClientVpnEndpointClientConnectOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2ClientVpnEndpointClientConnectOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2ClientVpnEndpointClientConnectOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2ClientVpnEndpointClientConnectOptionsDetails)

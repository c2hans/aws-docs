---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientConnectResponseOptions.html
---

# ClientConnectResponseOptions
<a name="API_ClientConnectResponseOptions"></a>

The options for managing connection authorization for new client connections.

## Contents
<a name="API_ClientConnectResponseOptions_Contents"></a>

 ** enabled **
Indicates whether client connect options are enabled.
Type: Boolean
Required: No

 ** lambdaFunctionArn **
The Amazon Resource Name (ARN) of the Lambda function used for connection authorization.
Type: String
Required: No

 ** status **
The status of any updates to the client connect options.
Type: [ClientVpnEndpointAttributeStatus](API_ClientVpnEndpointAttributeStatus.md) object
Required: No

## See Also
<a name="API_ClientConnectResponseOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientConnectResponseOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientConnectResponseOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientConnectResponseOptions)

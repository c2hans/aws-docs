---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualGateways.html
---

# DescribeVirtualGateways
<a name="API_DescribeVirtualGateways"></a>

**Note**
Deprecated. Use `DescribeVpnGateways` instead. See [DescribeVPNGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnGateways.html) in the *Amazon Elastic Compute Cloud API Reference*.

Lists the virtual private gateways owned by the AWS account.

You can create one or more Direct Connect private virtual interfaces linked to a virtual private gateway.

## Response Syntax
<a name="API_DescribeVirtualGateways_ResponseSyntax"></a>

```
{
   "virtualGateways": [
      {
         "virtualGatewayId": "string",
         "virtualGatewayState": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeVirtualGateways_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualGateways](#API_DescribeVirtualGateways_ResponseSyntax) **   <a name="DX-DescribeVirtualGateways-response-virtualGateways"></a>
The virtual private gateways.
Type: Array of [VirtualGateway](API_VirtualGateway.md) objects

## Errors
<a name="API_DescribeVirtualGateways_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeVirtualGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeVirtualGateways)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeVirtualGateways)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeVirtualGateways)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeVirtualGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeVirtualGateways)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeVirtualGateways)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeVirtualGateways)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeVirtualGateways)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeVirtualGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeVirtualGateways)

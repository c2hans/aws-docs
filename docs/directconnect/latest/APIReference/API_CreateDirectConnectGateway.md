---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGateway.html
---

# CreateDirectConnectGateway
<a name="API_CreateDirectConnectGateway"></a>

Creates a Direct Connect gateway, which is an intermediate object that enables you to connect a set of virtual interfaces and virtual private gateways. A Direct Connect gateway is global and visible in any AWS Region after it is created. The virtual interfaces and virtual private gateways that are connected through a Direct Connect gateway can be in different AWS Regions. This enables you to connect to a VPC in any Region, regardless of the Region in which the virtual interfaces are located, and pass traffic between them.

## Request Syntax
<a name="API_CreateDirectConnectGateway_RequestSyntax"></a>

```
{
   "amazonSideAsn": {{number}},
   "directConnectGatewayName": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDirectConnectGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [amazonSideAsn](#API_CreateDirectConnectGateway_RequestSyntax) **   <a name="DX-CreateDirectConnectGateway-request-amazonSideAsn"></a>
The autonomous system number (ASN) for Border Gateway Protocol (BGP) to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294. The default is 64512.
Type: Long
Required: No

 ** [directConnectGatewayName](#API_CreateDirectConnectGateway_RequestSyntax) **   <a name="DX-CreateDirectConnectGateway-request-directConnectGatewayName"></a>
The name of the Direct Connect gateway.
Type: String
Required: Yes

 ** [tags](#API_CreateDirectConnectGateway_RequestSyntax) **   <a name="DX-CreateDirectConnectGateway-request-tags"></a>
The key-value pair tags associated with the request.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_CreateDirectConnectGateway_ResponseSyntax"></a>

```
{
   "directConnectGateway": {
      "amazonSideAsn": number,
      "directConnectGatewayId": "string",
      "directConnectGatewayName": "string",
      "directConnectGatewayState": "string",
      "ownerAccount": "string",
      "stateChangeError": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ],
      "totalPrefixPoolAllocations": number
   }
}
```

## Response Elements
<a name="API_CreateDirectConnectGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGateway](#API_CreateDirectConnectGateway_ResponseSyntax) **   <a name="DX-CreateDirectConnectGateway-response-directConnectGateway"></a>
The Direct Connect gateway.
Type: [DirectConnectGateway](API_DirectConnectGateway.md) object

## Errors
<a name="API_CreateDirectConnectGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_CreateDirectConnectGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/CreateDirectConnectGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/CreateDirectConnectGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/CreateDirectConnectGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/CreateDirectConnectGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/CreateDirectConnectGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/CreateDirectConnectGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/CreateDirectConnectGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/CreateDirectConnectGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/CreateDirectConnectGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/CreateDirectConnectGateway)

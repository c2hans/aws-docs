---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGateway.html
---

# DeleteDirectConnectGateway
<a name="API_DeleteDirectConnectGateway"></a>

Deletes the specified Direct Connect gateway. You must first delete all virtual interfaces that are attached to the Direct Connect gateway and disassociate all virtual private gateways associated with the Direct Connect gateway.

## Request Syntax
<a name="API_DeleteDirectConnectGateway_RequestSyntax"></a>

```
{
   "directConnectGatewayId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDirectConnectGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [directConnectGatewayId](#API_DeleteDirectConnectGateway_RequestSyntax) **   <a name="DX-DeleteDirectConnectGateway-request-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteDirectConnectGateway_ResponseSyntax"></a>

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
<a name="API_DeleteDirectConnectGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGateway](#API_DeleteDirectConnectGateway_ResponseSyntax) **   <a name="DX-DeleteDirectConnectGateway-response-directConnectGateway"></a>
The Direct Connect gateway.
Type: [DirectConnectGateway](API_DirectConnectGateway.md) object

## Errors
<a name="API_DeleteDirectConnectGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDirectConnectGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DeleteDirectConnectGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DeleteDirectConnectGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DeleteDirectConnectGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DeleteDirectConnectGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DeleteDirectConnectGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DeleteDirectConnectGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DeleteDirectConnectGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DeleteDirectConnectGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DeleteDirectConnectGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DeleteDirectConnectGateway)

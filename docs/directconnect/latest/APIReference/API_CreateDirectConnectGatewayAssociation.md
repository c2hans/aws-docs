---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociation.html
---

# CreateDirectConnectGatewayAssociation
<a name="API_CreateDirectConnectGatewayAssociation"></a>

Creates an association between a Direct Connect gateway and a virtual private gateway. The virtual private gateway must be attached to a VPC and must not be associated with another Direct Connect gateway.

## Request Syntax
<a name="API_CreateDirectConnectGatewayAssociation_RequestSyntax"></a>

```
{
   "addAllowedPrefixesToDirectConnectGateway": [
      {
         "cidr": "{{string}}"
      }
   ],
   "directConnectGatewayId": "{{string}}",
   "gatewayId": "{{string}}",
   "virtualGatewayId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateDirectConnectGatewayAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [addAllowedPrefixesToDirectConnectGateway](#API_CreateDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociation-request-addAllowedPrefixesToDirectConnectGateway"></a>
The Amazon VPC prefixes to advertise to the Direct Connect gateway
This parameter is required when you create an association to a transit gateway.
For information about how to set the prefixes, see [Allowed Prefixes](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-vgw.html#allowed-prefixes) in the * Direct Connect User Guide*.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects
Required: No

 ** [directConnectGatewayId](#API_CreateDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociation-request-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: Yes

 ** [gatewayId](#API_CreateDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociation-request-gatewayId"></a>
The ID of the virtual private gateway or transit gateway.
Type: String
Required: No

 ** [virtualGatewayId](#API_CreateDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociation-request-virtualGatewayId"></a>
The ID of the virtual private gateway.
Type: String
Required: No

## Response Syntax
<a name="API_CreateDirectConnectGatewayAssociation_ResponseSyntax"></a>

```
{
   "directConnectGatewayAssociation": {
      "allowedPrefixesToDirectConnectGateway": [
         {
            "cidr": "string"
         }
      ],
      "associatedCoreNetwork": {
         "attachmentId": "string",
         "id": "string",
         "ownerAccount": "string"
      },
      "associatedGateway": {
         "id": "string",
         "ownerAccount": "string",
         "region": "string",
         "type": "string"
      },
      "associationId": "string",
      "associationState": "string",
      "directConnectGatewayId": "string",
      "directConnectGatewayOwnerAccount": "string",
      "stateChangeError": "string",
      "virtualGatewayId": "string",
      "virtualGatewayOwnerAccount": "string",
      "virtualGatewayRegion": "string"
   }
}
```

## Response Elements
<a name="API_CreateDirectConnectGatewayAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGatewayAssociation](#API_CreateDirectConnectGatewayAssociation_ResponseSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociation-response-directConnectGatewayAssociation"></a>
The association to be created.
Type: [DirectConnectGatewayAssociation](API_DirectConnectGatewayAssociation.md) object

## Errors
<a name="API_CreateDirectConnectGatewayAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_CreateDirectConnectGatewayAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/CreateDirectConnectGatewayAssociation)

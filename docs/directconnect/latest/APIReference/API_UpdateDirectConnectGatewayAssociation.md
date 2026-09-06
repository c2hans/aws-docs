---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateDirectConnectGatewayAssociation.html
---

# UpdateDirectConnectGatewayAssociation
<a name="API_UpdateDirectConnectGatewayAssociation"></a>

Updates the specified attributes of the Direct Connect gateway association.

Add or remove prefixes from the association.

## Request Syntax
<a name="API_UpdateDirectConnectGatewayAssociation_RequestSyntax"></a>

```
{
   "addAllowedPrefixesToDirectConnectGateway": [
      {
         "cidr": "{{string}}"
      }
   ],
   "associationId": "{{string}}",
   "removeAllowedPrefixesToDirectConnectGateway": [
      {
         "cidr": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateDirectConnectGatewayAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [addAllowedPrefixesToDirectConnectGateway](#API_UpdateDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-UpdateDirectConnectGatewayAssociation-request-addAllowedPrefixesToDirectConnectGateway"></a>
The Amazon VPC prefixes to advertise to the Direct Connect gateway.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects
Required: No

 ** [associationId](#API_UpdateDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-UpdateDirectConnectGatewayAssociation-request-associationId"></a>
The ID of the Direct Connect gateway association.
Type: String
Required: No

 ** [removeAllowedPrefixesToDirectConnectGateway](#API_UpdateDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-UpdateDirectConnectGatewayAssociation-request-removeAllowedPrefixesToDirectConnectGateway"></a>
The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects
Required: No

## Response Syntax
<a name="API_UpdateDirectConnectGatewayAssociation_ResponseSyntax"></a>

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
<a name="API_UpdateDirectConnectGatewayAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGatewayAssociation](#API_UpdateDirectConnectGatewayAssociation_ResponseSyntax) **   <a name="DX-UpdateDirectConnectGatewayAssociation-response-directConnectGatewayAssociation"></a>
Information about an association between a Direct Connect gateway and a virtual private gateway or transit gateway.
Type: [DirectConnectGatewayAssociation](API_DirectConnectGatewayAssociation.md) object

## Errors
<a name="API_UpdateDirectConnectGatewayAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_UpdateDirectConnectGatewayAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/UpdateDirectConnectGatewayAssociation)

---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_CreateDirectConnectGatewayAssociationProposal.html
---

# CreateDirectConnectGatewayAssociationProposal
<a name="API_CreateDirectConnectGatewayAssociationProposal"></a>

Creates a proposal to associate the specified virtual private gateway or transit gateway with the specified Direct Connect gateway.

You can associate a Direct Connect gateway and virtual private gateway or transit gateway that is owned by any AWS account.

## Request Syntax
<a name="API_CreateDirectConnectGatewayAssociationProposal_RequestSyntax"></a>

```
{
   "addAllowedPrefixesToDirectConnectGateway": [
      {
         "cidr": "{{string}}"
      }
   ],
   "directConnectGatewayId": "{{string}}",
   "directConnectGatewayOwnerAccount": "{{string}}",
   "gatewayId": "{{string}}",
   "removeAllowedPrefixesToDirectConnectGateway": [
      {
         "cidr": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDirectConnectGatewayAssociationProposal_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [addAllowedPrefixesToDirectConnectGateway](#API_CreateDirectConnectGatewayAssociationProposal_RequestSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociationProposal-request-addAllowedPrefixesToDirectConnectGateway"></a>
The Amazon VPC prefixes to advertise to the Direct Connect gateway.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects
Required: No

 ** [directConnectGatewayId](#API_CreateDirectConnectGatewayAssociationProposal_RequestSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociationProposal-request-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: Yes

 ** [directConnectGatewayOwnerAccount](#API_CreateDirectConnectGatewayAssociationProposal_RequestSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociationProposal-request-directConnectGatewayOwnerAccount"></a>
The ID of the AWS account that owns the Direct Connect gateway.
Type: String
Required: Yes

 ** [gatewayId](#API_CreateDirectConnectGatewayAssociationProposal_RequestSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociationProposal-request-gatewayId"></a>
The ID of the virtual private gateway or transit gateway.
Type: String
Required: Yes

 ** [removeAllowedPrefixesToDirectConnectGateway](#API_CreateDirectConnectGatewayAssociationProposal_RequestSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociationProposal-request-removeAllowedPrefixesToDirectConnectGateway"></a>
The Amazon VPC prefixes to no longer advertise to the Direct Connect gateway.
Type: Array of [RouteFilterPrefix](API_RouteFilterPrefix.md) objects
Required: No

## Response Syntax
<a name="API_CreateDirectConnectGatewayAssociationProposal_ResponseSyntax"></a>

```
{
   "directConnectGatewayAssociationProposal": {
      "associatedGateway": {
         "id": "string",
         "ownerAccount": "string",
         "region": "string",
         "type": "string"
      },
      "directConnectGatewayId": "string",
      "directConnectGatewayOwnerAccount": "string",
      "existingAllowedPrefixesToDirectConnectGateway": [
         {
            "cidr": "string"
         }
      ],
      "proposalId": "string",
      "proposalState": "string",
      "requestedAllowedPrefixesToDirectConnectGateway": [
         {
            "cidr": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_CreateDirectConnectGatewayAssociationProposal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGatewayAssociationProposal](#API_CreateDirectConnectGatewayAssociationProposal_ResponseSyntax) **   <a name="DX-CreateDirectConnectGatewayAssociationProposal-response-directConnectGatewayAssociationProposal"></a>
Information about the Direct Connect gateway proposal.
Type: [DirectConnectGatewayAssociationProposal](API_DirectConnectGatewayAssociationProposal.md) object

## Errors
<a name="API_CreateDirectConnectGatewayAssociationProposal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_CreateDirectConnectGatewayAssociationProposal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/CreateDirectConnectGatewayAssociationProposal)

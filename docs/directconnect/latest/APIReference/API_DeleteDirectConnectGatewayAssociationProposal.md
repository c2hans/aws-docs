---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociationProposal.html
---

# DeleteDirectConnectGatewayAssociationProposal
<a name="API_DeleteDirectConnectGatewayAssociationProposal"></a>

Deletes the association proposal request between the specified Direct Connect gateway and virtual private gateway or transit gateway.

## Request Syntax
<a name="API_DeleteDirectConnectGatewayAssociationProposal_RequestSyntax"></a>

```
{
   "proposalId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDirectConnectGatewayAssociationProposal_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [proposalId](#API_DeleteDirectConnectGatewayAssociationProposal_RequestSyntax) **   <a name="DX-DeleteDirectConnectGatewayAssociationProposal-request-proposalId"></a>
The ID of the proposal.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteDirectConnectGatewayAssociationProposal_ResponseSyntax"></a>

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
<a name="API_DeleteDirectConnectGatewayAssociationProposal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGatewayAssociationProposal](#API_DeleteDirectConnectGatewayAssociationProposal_ResponseSyntax) **   <a name="DX-DeleteDirectConnectGatewayAssociationProposal-response-directConnectGatewayAssociationProposal"></a>
The ID of the associated gateway.
Type: [DirectConnectGatewayAssociationProposal](API_DirectConnectGatewayAssociationProposal.md) object

## Errors
<a name="API_DeleteDirectConnectGatewayAssociationProposal_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDirectConnectGatewayAssociationProposal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociationProposal)

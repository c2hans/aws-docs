---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGatewayAssociation.html
---

# DeleteDirectConnectGatewayAssociation
<a name="API_DeleteDirectConnectGatewayAssociation"></a>

Deletes the association between the specified Direct Connect gateway and virtual private gateway.

We recommend that you specify the `associationID` to delete the association. Alternatively, if you own virtual gateway and a Direct Connect gateway association, you can specify the `virtualGatewayId` and `directConnectGatewayId` to delete an association.

## Request Syntax
<a name="API_DeleteDirectConnectGatewayAssociation_RequestSyntax"></a>

```
{
   "associationId": "{{string}}",
   "directConnectGatewayId": "{{string}}",
   "virtualGatewayId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDirectConnectGatewayAssociation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [associationId](#API_DeleteDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-DeleteDirectConnectGatewayAssociation-request-associationId"></a>
The ID of the Direct Connect gateway association.
Type: String
Required: No

 ** [directConnectGatewayId](#API_DeleteDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-DeleteDirectConnectGatewayAssociation-request-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** [virtualGatewayId](#API_DeleteDirectConnectGatewayAssociation_RequestSyntax) **   <a name="DX-DeleteDirectConnectGatewayAssociation-request-virtualGatewayId"></a>
The ID of the virtual private gateway.
Type: String
Required: No

## Response Syntax
<a name="API_DeleteDirectConnectGatewayAssociation_ResponseSyntax"></a>

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
<a name="API_DeleteDirectConnectGatewayAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGatewayAssociation](#API_DeleteDirectConnectGatewayAssociation_ResponseSyntax) **   <a name="DX-DeleteDirectConnectGatewayAssociation-response-directConnectGatewayAssociation"></a>
Information about the deleted association.
Type: [DirectConnectGatewayAssociation](API_DirectConnectGatewayAssociation.md) object

## Errors
<a name="API_DeleteDirectConnectGatewayAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDirectConnectGatewayAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DeleteDirectConnectGatewayAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

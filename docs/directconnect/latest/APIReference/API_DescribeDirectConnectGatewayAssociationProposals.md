---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociationProposals.html
---

# DescribeDirectConnectGatewayAssociationProposals
<a name="API_DescribeDirectConnectGatewayAssociationProposals"></a>

Describes one or more association proposals for connection between a virtual private gateway or transit gateway and a Direct Connect gateway.

## Request Syntax
<a name="API_DescribeDirectConnectGatewayAssociationProposals_RequestSyntax"></a>

```
{
   "associatedGatewayId": "{{string}}",
   "directConnectGatewayId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "proposalId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDirectConnectGatewayAssociationProposals_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [associatedGatewayId](#API_DescribeDirectConnectGatewayAssociationProposals_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociationProposals-request-associatedGatewayId"></a>
The ID of the associated gateway.
Type: String
Required: No

 ** [directConnectGatewayId](#API_DescribeDirectConnectGatewayAssociationProposals_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociationProposals-request-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** [maxResults](#API_DescribeDirectConnectGatewayAssociationProposals_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociationProposals-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeDirectConnectGatewayAssociationProposals_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociationProposals-request-nextToken"></a>
The token for the next page of results.
Type: String
Required: No

 ** [proposalId](#API_DescribeDirectConnectGatewayAssociationProposals_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociationProposals-request-proposalId"></a>
The ID of the proposal.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeDirectConnectGatewayAssociationProposals_ResponseSyntax"></a>

```
{
   "directConnectGatewayAssociationProposals": [
      {
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDirectConnectGatewayAssociationProposals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGatewayAssociationProposals](#API_DescribeDirectConnectGatewayAssociationProposals_ResponseSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociationProposals-response-directConnectGatewayAssociationProposals"></a>
Describes the Direct Connect gateway association proposals.
Type: Array of [DirectConnectGatewayAssociationProposal](API_DirectConnectGatewayAssociationProposal.md) objects

 ** [nextToken](#API_DescribeDirectConnectGatewayAssociationProposals_ResponseSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociationProposals-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

## Errors
<a name="API_DescribeDirectConnectGatewayAssociationProposals_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDirectConnectGatewayAssociationProposals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociationProposals)

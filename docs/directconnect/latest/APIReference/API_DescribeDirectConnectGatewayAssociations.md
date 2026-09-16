---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAssociations.html
---

# DescribeDirectConnectGatewayAssociations
<a name="API_DescribeDirectConnectGatewayAssociations"></a>

Lists the associations between your Direct Connect gateways and virtual private gateways and transit gateways. You must specify one of the following:
+ A Direct Connect gateway

  The response contains all virtual private gateways and transit gateways associated with the Direct Connect gateway.
+ A virtual private gateway

  The response contains the Direct Connect gateway.
+ A transit gateway

  The response contains the Direct Connect gateway.
+ A Direct Connect gateway and a virtual private gateway

  The response contains the association between the Direct Connect gateway and virtual private gateway.
+ A Direct Connect gateway and a transit gateway

  The response contains the association between the Direct Connect gateway and transit gateway.
+ A Direct Connect gateway and a virtual private gateway

  The response contains the association between the Direct Connect gateway and virtual private gateway.
+ A Direct Connect gateway association to a Cloud WAN core network

  The response contains the Cloud WAN core network ID that the Direct Connect gateway is associated to.

## Request Syntax
<a name="API_DescribeDirectConnectGatewayAssociations_RequestSyntax"></a>

```
{
   "associatedGatewayId": "{{string}}",
   "associationId": "{{string}}",
   "directConnectGatewayId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "virtualGatewayId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDirectConnectGatewayAssociations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [associatedGatewayId](#API_DescribeDirectConnectGatewayAssociations_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociations-request-associatedGatewayId"></a>
The ID of the associated gateway.
Type: String
Required: No

 ** [associationId](#API_DescribeDirectConnectGatewayAssociations_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociations-request-associationId"></a>
The ID of the Direct Connect gateway association.
Type: String
Required: No

 ** [directConnectGatewayId](#API_DescribeDirectConnectGatewayAssociations_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociations-request-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** [maxResults](#API_DescribeDirectConnectGatewayAssociations_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociations-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeDirectConnectGatewayAssociations_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociations-request-nextToken"></a>
The token provided in the previous call to retrieve the next page.
Type: String
Required: No

 ** [virtualGatewayId](#API_DescribeDirectConnectGatewayAssociations_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociations-request-virtualGatewayId"></a>
The ID of the virtual private gateway or transit gateway.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeDirectConnectGatewayAssociations_ResponseSyntax"></a>

```
{
   "directConnectGatewayAssociations": [
      {
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDirectConnectGatewayAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGatewayAssociations](#API_DescribeDirectConnectGatewayAssociations_ResponseSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociations-response-directConnectGatewayAssociations"></a>
Information about the associations.
Type: Array of [DirectConnectGatewayAssociation](API_DirectConnectGatewayAssociation.md) objects

 ** [nextToken](#API_DescribeDirectConnectGatewayAssociations_ResponseSyntax) **   <a name="DX-DescribeDirectConnectGatewayAssociations-response-nextToken"></a>
The token to retrieve the next page.
Type: String

## Errors
<a name="API_DescribeDirectConnectGatewayAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDirectConnectGatewayAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeDirectConnectGatewayAssociations)

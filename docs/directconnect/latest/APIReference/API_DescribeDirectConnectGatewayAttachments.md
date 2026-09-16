---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGatewayAttachments.html
---

# DescribeDirectConnectGatewayAttachments
<a name="API_DescribeDirectConnectGatewayAttachments"></a>

Lists the attachments between your Direct Connect gateways and virtual interfaces. You must specify a Direct Connect gateway, a virtual interface, or both. If you specify a Direct Connect gateway, the response contains all virtual interfaces attached to the Direct Connect gateway. If you specify a virtual interface, the response contains all Direct Connect gateways attached to the virtual interface. If you specify both, the response contains the attachment between the Direct Connect gateway and the virtual interface.

## Request Syntax
<a name="API_DescribeDirectConnectGatewayAttachments_RequestSyntax"></a>

```
{
   "directConnectGatewayId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDirectConnectGatewayAttachments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [directConnectGatewayId](#API_DescribeDirectConnectGatewayAttachments_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAttachments-request-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** [maxResults](#API_DescribeDirectConnectGatewayAttachments_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAttachments-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeDirectConnectGatewayAttachments_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAttachments-request-nextToken"></a>
The token provided in the previous call to retrieve the next page.
Type: String
Required: No

 ** [virtualInterfaceId](#API_DescribeDirectConnectGatewayAttachments_RequestSyntax) **   <a name="DX-DescribeDirectConnectGatewayAttachments-request-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeDirectConnectGatewayAttachments_ResponseSyntax"></a>

```
{
   "directConnectGatewayAttachments": [
      {
         "attachmentState": "string",
         "attachmentType": "string",
         "directConnectGatewayId": "string",
         "stateChangeError": "string",
         "virtualInterfaceId": "string",
         "virtualInterfaceOwnerAccount": "string",
         "virtualInterfaceRegion": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDirectConnectGatewayAttachments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGatewayAttachments](#API_DescribeDirectConnectGatewayAttachments_ResponseSyntax) **   <a name="DX-DescribeDirectConnectGatewayAttachments-response-directConnectGatewayAttachments"></a>
The attachments.
Type: Array of [DirectConnectGatewayAttachment](API_DirectConnectGatewayAttachment.md) objects

 ** [nextToken](#API_DescribeDirectConnectGatewayAttachments_ResponseSyntax) **   <a name="DX-DescribeDirectConnectGatewayAttachments-response-nextToken"></a>
The token to retrieve the next page.
Type: String

## Errors
<a name="API_DescribeDirectConnectGatewayAttachments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDirectConnectGatewayAttachments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeDirectConnectGatewayAttachments)

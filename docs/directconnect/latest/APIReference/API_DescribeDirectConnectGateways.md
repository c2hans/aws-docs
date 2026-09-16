---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeDirectConnectGateways.html
---

# DescribeDirectConnectGateways
<a name="API_DescribeDirectConnectGateways"></a>

Lists all your Direct Connect gateways or only the specified Direct Connect gateway. Deleted Direct Connect gateways are not returned.

## Request Syntax
<a name="API_DescribeDirectConnectGateways_RequestSyntax"></a>

```
{
   "directConnectGatewayId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDirectConnectGateways_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [directConnectGatewayId](#API_DescribeDirectConnectGateways_RequestSyntax) **   <a name="DX-DescribeDirectConnectGateways-request-directConnectGatewayId"></a>
The ID of the Direct Connect gateway.
Type: String
Required: No

 ** [maxResults](#API_DescribeDirectConnectGateways_RequestSyntax) **   <a name="DX-DescribeDirectConnectGateways-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_DescribeDirectConnectGateways_RequestSyntax) **   <a name="DX-DescribeDirectConnectGateways-request-nextToken"></a>
The token provided in the previous call to retrieve the next page.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeDirectConnectGateways_ResponseSyntax"></a>

```
{
   "directConnectGateways": [
      {
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDirectConnectGateways_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [directConnectGateways](#API_DescribeDirectConnectGateways_ResponseSyntax) **   <a name="DX-DescribeDirectConnectGateways-response-directConnectGateways"></a>
The Direct Connect gateways.
Type: Array of [DirectConnectGateway](API_DirectConnectGateway.md) objects

 ** [nextToken](#API_DescribeDirectConnectGateways_ResponseSyntax) **   <a name="DX-DescribeDirectConnectGateways-response-nextToken"></a>
The token to retrieve the next page.
Type: String

## Errors
<a name="API_DescribeDirectConnectGateways_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DescribeDirectConnectGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DescribeDirectConnectGateways)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DescribeDirectConnectGateways)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DescribeDirectConnectGateways)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DescribeDirectConnectGateways)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DescribeDirectConnectGateways)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DescribeDirectConnectGateways)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DescribeDirectConnectGateways)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DescribeDirectConnectGateways)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DescribeDirectConnectGateways)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DescribeDirectConnectGateways)

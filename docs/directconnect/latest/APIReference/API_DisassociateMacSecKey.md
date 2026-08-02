---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DisassociateMacSecKey.html
---

# DisassociateMacSecKey
<a name="API_DisassociateMacSecKey"></a>

Removes the association between a MAC Security (MACsec) security key and a Direct Connect connection.

## Request Syntax
<a name="API_DisassociateMacSecKey_RequestSyntax"></a>

```
{
   "connectionId": "{{string}}",
   "secretARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateMacSecKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [connectionId](#API_DisassociateMacSecKey_RequestSyntax) **   <a name="DX-DisassociateMacSecKey-request-connectionId"></a>
The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).
You can use [DescribeConnections](API_DescribeConnections.md), [DescribeInterconnects](API_DescribeInterconnects.md), or [DescribeLags](API_DescribeLags.md) to retrieve connection ID.
Type: String
Required: Yes

 ** [secretARN](#API_DisassociateMacSecKey_RequestSyntax) **   <a name="DX-DisassociateMacSecKey-request-secretARN"></a>
The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key.
You can use [DescribeConnections](API_DescribeConnections.md) to retrieve the ARN of the MAC Security (MACsec) secret key.
Type: String
Required: Yes

## Response Syntax
<a name="API_DisassociateMacSecKey_ResponseSyntax"></a>

```
{
   "connectionId": "string",
   "macSecKeys": [
      {
         "ckn": "string",
         "secretARN": "string",
         "startOn": "string",
         "state": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DisassociateMacSecKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectionId](#API_DisassociateMacSecKey_ResponseSyntax) **   <a name="DX-DisassociateMacSecKey-response-connectionId"></a>
The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).
Type: String

 ** [macSecKeys](#API_DisassociateMacSecKey_ResponseSyntax) **   <a name="DX-DisassociateMacSecKey-response-macSecKeys"></a>
The MAC Security (MACsec) security keys no longer associated with the connection.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

## Errors
<a name="API_DisassociateMacSecKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateMacSecKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/DisassociateMacSecKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/DisassociateMacSecKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/DisassociateMacSecKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/DisassociateMacSecKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/DisassociateMacSecKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/DisassociateMacSecKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/DisassociateMacSecKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/DisassociateMacSecKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/DisassociateMacSecKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/DisassociateMacSecKey)

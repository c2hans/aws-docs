---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateMacSecKey.html
---

# AssociateMacSecKey
<a name="API_AssociateMacSecKey"></a>

Associates a MAC Security (MACsec) Connection Key Name (CKN)/ Connectivity Association Key (CAK) pair with a Direct Connect connection.

You must supply either the `secretARN,` or the CKN/CAK (`ckn` and `cak`) pair in the request.

For information about MAC Security (MACsec) key considerations, see [MACsec pre-shared CKN/CAK key considerations ](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-mac-sec-getting-started.html#mac-sec-key-consideration) in the * Direct Connect User Guide*.

## Request Syntax
<a name="API_AssociateMacSecKey_RequestSyntax"></a>

```
{
   "cak": "{{string}}",
   "ckn": "{{string}}",
   "connectionId": "{{string}}",
   "secretARN": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateMacSecKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [cak](#API_AssociateMacSecKey_RequestSyntax) **   <a name="DX-AssociateMacSecKey-request-cak"></a>
The MAC Security (MACsec) CAK to associate with the connection.
You can create the CKN/CAK pair using an industry standard tool.
 The valid values are 64 hexadecimal characters (0-9, A-E).
If you use this request parameter, you must use the `ckn` request parameter and not use the `secretARN` request parameter.
Type: String
Required: No

 ** [ckn](#API_AssociateMacSecKey_RequestSyntax) **   <a name="DX-AssociateMacSecKey-request-ckn"></a>
The MAC Security (MACsec) CKN to associate with the connection.
You can create the CKN/CAK pair using an industry standard tool.
 The valid values are 64 hexadecimal characters (0-9, A-E).
If you use this request parameter, you must use the `cak` request parameter and not use the `secretARN` request parameter.
Type: String
Required: No

 ** [connectionId](#API_AssociateMacSecKey_RequestSyntax) **   <a name="DX-AssociateMacSecKey-request-connectionId"></a>
The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).
You can use [DescribeConnections](API_DescribeConnections.md), [DescribeInterconnects](API_DescribeInterconnects.md), or [DescribeLags](API_DescribeLags.md) to retrieve connection ID.
Type: String
Required: Yes

 ** [secretARN](#API_AssociateMacSecKey_RequestSyntax) **   <a name="DX-AssociateMacSecKey-request-secretARN"></a>
The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key to associate with the connection.
You can use [DescribeConnections](API_DescribeConnections.md) or [DescribeLags](API_DescribeLags.md) to retrieve the MAC Security (MACsec) secret key.
If you use this request parameter, you do not use the `ckn` and `cak` request parameters.
Type: String
Required: No

## Response Syntax
<a name="API_AssociateMacSecKey_ResponseSyntax"></a>

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
<a name="API_AssociateMacSecKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [connectionId](#API_AssociateMacSecKey_ResponseSyntax) **   <a name="DX-AssociateMacSecKey-response-connectionId"></a>
The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).
Type: String

 ** [macSecKeys](#API_AssociateMacSecKey_ResponseSyntax) **   <a name="DX-AssociateMacSecKey-response-macSecKeys"></a>
The MAC Security (MACsec) security keys associated with the connection.
Type: Array of [MacSecKey](API_MacSecKey.md) objects

## Errors
<a name="API_AssociateMacSecKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_AssociateMacSecKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/AssociateMacSecKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/AssociateMacSecKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AssociateMacSecKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/AssociateMacSecKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AssociateMacSecKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/AssociateMacSecKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/AssociateMacSecKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/AssociateMacSecKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/AssociateMacSecKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AssociateMacSecKey)

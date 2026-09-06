---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StopBgpFailoverTest.html
---

# StopBgpFailoverTest
<a name="API_StopBgpFailoverTest"></a>

Stops the virtual interface failover test.

## Request Syntax
<a name="API_StopBgpFailoverTest_RequestSyntax"></a>

```
{
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopBgpFailoverTest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [virtualInterfaceId](#API_StopBgpFailoverTest_RequestSyntax) **   <a name="DX-StopBgpFailoverTest-request-virtualInterfaceId"></a>
The ID of the virtual interface you no longer want to test.
Type: String
Required: Yes

## Response Syntax
<a name="API_StopBgpFailoverTest_ResponseSyntax"></a>

```
{
   "virtualInterfaceTest": {
      "bgpPeers": [ "string" ],
      "endTime": number,
      "ownerAccount": "string",
      "startTime": number,
      "status": "string",
      "testDurationInMinutes": number,
      "testId": "string",
      "virtualInterfaceId": "string"
   }
}
```

## Response Elements
<a name="API_StopBgpFailoverTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualInterfaceTest](#API_StopBgpFailoverTest_ResponseSyntax) **   <a name="DX-StopBgpFailoverTest-response-virtualInterfaceTest"></a>
Information about the virtual interface failover test.
Type: [VirtualInterfaceTestHistory](API_VirtualInterfaceTestHistory.md) object

## Errors
<a name="API_StopBgpFailoverTest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_StopBgpFailoverTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/StopBgpFailoverTest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/StopBgpFailoverTest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/StopBgpFailoverTest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/StopBgpFailoverTest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/StopBgpFailoverTest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/StopBgpFailoverTest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/StopBgpFailoverTest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/StopBgpFailoverTest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/StopBgpFailoverTest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/StopBgpFailoverTest)

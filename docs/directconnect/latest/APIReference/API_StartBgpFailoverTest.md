---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StartBgpFailoverTest.html
---

# StartBgpFailoverTest
<a name="API_StartBgpFailoverTest"></a>

Starts the virtual interface failover test that verifies your configuration meets your resiliency requirements by placing the BGP peering session in the DOWN state. You can then send traffic to verify that there are no outages.

You can run the test on public, private, transit, and hosted virtual interfaces.

You can use [ListVirtualInterfaceTestHistory](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceTestHistory.html) to view the virtual interface test history.

If you need to stop the test before the test interval completes, use [StopBgpFailoverTest](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_StopBgpFailoverTest.html).

## Request Syntax
<a name="API_StartBgpFailoverTest_RequestSyntax"></a>

```
{
   "bgpPeers": [ "{{string}}" ],
   "testDurationInMinutes": {{number}},
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_StartBgpFailoverTest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bgpPeers](#API_StartBgpFailoverTest_RequestSyntax) **   <a name="DX-StartBgpFailoverTest-request-bgpPeers"></a>
The BGP peers to place in the DOWN state.
Type: Array of strings
Required: No

 ** [testDurationInMinutes](#API_StartBgpFailoverTest_RequestSyntax) **   <a name="DX-StartBgpFailoverTest-request-testDurationInMinutes"></a>
The time in minutes that the virtual interface failover test will last.
Maximum value: 4,320 minutes (72 hours).
Default: 180 minutes (3 hours).
Type: Integer
Required: No

 ** [virtualInterfaceId](#API_StartBgpFailoverTest_RequestSyntax) **   <a name="DX-StartBgpFailoverTest-request-virtualInterfaceId"></a>
The ID of the virtual interface you want to test.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartBgpFailoverTest_ResponseSyntax"></a>

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
<a name="API_StartBgpFailoverTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [virtualInterfaceTest](#API_StartBgpFailoverTest_ResponseSyntax) **   <a name="DX-StartBgpFailoverTest-response-virtualInterfaceTest"></a>
Information about the virtual interface failover test.
Type: [VirtualInterfaceTestHistory](API_VirtualInterfaceTestHistory.md) object

## Errors
<a name="API_StartBgpFailoverTest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_StartBgpFailoverTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/StartBgpFailoverTest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/StartBgpFailoverTest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/StartBgpFailoverTest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/StartBgpFailoverTest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/StartBgpFailoverTest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/StartBgpFailoverTest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/StartBgpFailoverTest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/StartBgpFailoverTest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/StartBgpFailoverTest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/StartBgpFailoverTest)

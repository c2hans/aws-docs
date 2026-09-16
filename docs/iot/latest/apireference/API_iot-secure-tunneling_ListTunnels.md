---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iot-secure-tunneling_ListTunnels.html
---

# ListTunnels
<a name="API_iot-secure-tunneling_ListTunnels"></a>

List all tunnels for an AWS account. Tunnels are listed by creation time in descending order, newer tunnels will be listed before older tunnels.

Requires permission to access the [ListTunnels](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iot-secure-tunneling_ListTunnels_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "thingName": "{{string}}"
}
```

## Request Parameters
<a name="API_iot-secure-tunneling_ListTunnels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_iot-secure-tunneling_ListTunnels_RequestSyntax) **   <a name="iot-iot-secure-tunneling_ListTunnels-request-maxResults"></a>
The maximum number of results to return at once.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_iot-secure-tunneling_ListTunnels_RequestSyntax) **   <a name="iot-iot-secure-tunneling_ListTunnels-request-nextToken"></a>
To retrieve the next set of results, the nextToken value from a previous response; otherwise null to receive the first set of results.
Type: String
Pattern: `[a-zA-Z0-9_=-]{1,4096}`
Required: No

 ** [thingName](#API_iot-secure-tunneling_ListTunnels_RequestSyntax) **   <a name="iot-iot-secure-tunneling_ListTunnels-request-thingName"></a>
The name of the IoT thing associated with the destination device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

## Response Syntax
<a name="API_iot-secure-tunneling_ListTunnels_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tunnelSummaries": [
      {
         "createdAt": number,
         "description": "string",
         "lastUpdatedAt": number,
         "status": "string",
         "tunnelArn": "string",
         "tunnelId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_iot-secure-tunneling_ListTunnels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_iot-secure-tunneling_ListTunnels_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_ListTunnels-response-nextToken"></a>
The token to use to get the next set of results, or null if there are no additional results.
Type: String
Pattern: `[a-zA-Z0-9_=-]{1,4096}`

 ** [tunnelSummaries](#API_iot-secure-tunneling_ListTunnels_ResponseSyntax) **   <a name="iot-iot-secure-tunneling_ListTunnels-response-tunnelSummaries"></a>
A short description of the tunnels in an AWS account.
Type: Array of [TunnelSummary](API_iot-secure-tunneling_TunnelSummary.md) objects

## See Also
<a name="API_iot-secure-tunneling_ListTunnels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsecuretunneling-2018-10-05/ListTunnels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsecuretunneling-2018-10-05/ListTunnels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsecuretunneling-2018-10-05/ListTunnels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsecuretunneling-2018-10-05/ListTunnels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsecuretunneling-2018-10-05/ListTunnels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsecuretunneling-2018-10-05/ListTunnels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsecuretunneling-2018-10-05/ListTunnels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsecuretunneling-2018-10-05/ListTunnels)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsecuretunneling-2018-10-05/ListTunnels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsecuretunneling-2018-10-05/ListTunnels)

---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_GetConnectivityInfo.html
---

# GetConnectivityInfo
<a name="API_GetConnectivityInfo"></a>

Retrieves connectivity information for a Greengrass core device.

Connectivity information includes endpoints and ports where client devices can connect to an MQTT broker on the core device. When a client device calls the [AWS IoT Greengrass discovery API](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-discover-api.html), AWS IoT Greengrass returns connectivity information for all of the core devices where the client device can connect. For more information, see [Connect client devices to core devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/connect-client-devices.html) in the * AWS IoT Greengrass Version 2 Developer Guide*.

## Request Syntax
<a name="API_GetConnectivityInfo_RequestSyntax"></a>

```
GET /greengrass/things/{{thingName}}/connectivityInfo HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConnectivityInfo_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingName](#API_GetConnectivityInfo_RequestSyntax) **   <a name="greengrassv2-GetConnectivityInfo-request-uri-thingName"></a>
The name of the core device. This is also the name of the AWS IoT thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_GetConnectivityInfo_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConnectivityInfo_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectivityInfo": [
      {
         "HostAddress": "string",
         "Id": "string",
         "Metadata": "string",
         "PortNumber": number
      }
   ],
   "Message": "string"
}
```

## Response Elements
<a name="API_GetConnectivityInfo_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectivityInfo](#API_GetConnectivityInfo_ResponseSyntax) **   <a name="greengrassv2-GetConnectivityInfo-response-ConnectivityInfo"></a>
The connectivity information for the core device.
Type: Array of [ConnectivityInfo](API_ConnectivityInfo.md) objects

 ** [Message](#API_GetConnectivityInfo_ResponseSyntax) **   <a name="greengrassv2-GetConnectivityInfo-response-Message"></a>
A message about the connectivity information request.
Type: String

## Errors
<a name="API_GetConnectivityInfo_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 AWS IoT Greengrass can't process your request right now. Try again later.
 ** retryAfterSeconds **
The amount of time to wait before you retry the request.
HTTP Status Code: 500

 ** ValidationException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.
 ** fields **
The list of fields that failed to validate.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_GetConnectivityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/greengrassv2-2020-11-30/GetConnectivityInfo)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/greengrassv2-2020-11-30/GetConnectivityInfo)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/GetConnectivityInfo)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/greengrassv2-2020-11-30/GetConnectivityInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/GetConnectivityInfo)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/greengrassv2-2020-11-30/GetConnectivityInfo)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/greengrassv2-2020-11-30/GetConnectivityInfo)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/greengrassv2-2020-11-30/GetConnectivityInfo)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/GetConnectivityInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/GetConnectivityInfo)

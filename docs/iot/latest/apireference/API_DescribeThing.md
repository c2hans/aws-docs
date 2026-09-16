---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeThing.html
---

# DescribeThing
<a name="API_DescribeThing"></a>

Gets information about the specified thing.

Requires permission to access the [DescribeThing](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeThing_RequestSyntax"></a>

```
GET /things/{{thingName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeThing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingName](#API_DescribeThing_RequestSyntax) **   <a name="iot-DescribeThing-request-uri-thingName"></a>
The name of the thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DescribeThing_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeThing_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributes": {
      "string" : "string"
   },
   "billingGroupName": "string",
   "defaultClientId": "string",
   "thingArn": "string",
   "thingId": "string",
   "thingName": "string",
   "thingTypeName": "string",
   "version": number
}
```

## Response Elements
<a name="API_DescribeThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributes](#API_DescribeThing_ResponseSyntax) **   <a name="iot-DescribeThing-response-attributes"></a>
The thing attributes.
Type: String to string map
Key Length Constraints: Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_.,@/:#-]+`
Value Length Constraints: Maximum length of 800.
Value Pattern: `[a-zA-Z0-9_.,@/:#=\[\]-]*`

 ** [billingGroupName](#API_DescribeThing_ResponseSyntax) **   <a name="iot-DescribeThing-response-billingGroupName"></a>
The name of the billing group the thing belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [defaultClientId](#API_DescribeThing_ResponseSyntax) **   <a name="iot-DescribeThing-response-defaultClientId"></a>
The default MQTT client ID. For a typical device, the thing name is also used as the default MQTT client ID. Although we don’t require a mapping between a thing's registry name and its use of MQTT client IDs, certificates, or shadow state, we recommend that you choose a thing name and use it as the MQTT client ID for the registry and the Device Shadow service.
This lets you better organize your AWS IoT fleet without removing the flexibility of the underlying device certificate model or shadows.
Type: String

 ** [thingArn](#API_DescribeThing_ResponseSyntax) **   <a name="iot-DescribeThing-response-thingArn"></a>
The ARN of the thing to describe.
Type: String

 ** [thingId](#API_DescribeThing_ResponseSyntax) **   <a name="iot-DescribeThing-response-thingId"></a>
The ID of the thing to describe.
Type: String

 ** [thingName](#API_DescribeThing_ResponseSyntax) **   <a name="iot-DescribeThing-response-thingName"></a>
The name of the thing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [thingTypeName](#API_DescribeThing_ResponseSyntax) **   <a name="iot-DescribeThing-response-thingTypeName"></a>
The thing type name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [version](#API_DescribeThing_ResponseSyntax) **   <a name="iot-DescribeThing-response-version"></a>
The current version of the thing record in the registry.
To avoid unintentional changes to the information in the registry, you can pass the version information in the `expectedVersion` parameter of the `UpdateThing` and `DeleteThing` calls.
Type: Long

## Errors
<a name="API_DescribeThing_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DescribeThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeThing)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeThing)

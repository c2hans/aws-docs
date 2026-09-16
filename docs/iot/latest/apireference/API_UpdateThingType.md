---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingType.html
---

# UpdateThingType
<a name="API_UpdateThingType"></a>

Updates a thing type.

## Request Syntax
<a name="API_UpdateThingType_RequestSyntax"></a>

```
PATCH /thing-types/{{thingTypeName}} HTTP/1.1
Content-type: application/json

{
   "thingTypeProperties": {
      "mqtt5Configuration": {
         "propagatingAttributes": [
            {
               "connectionAttribute": "{{string}}",
               "thingAttribute": "{{string}}",
               "userPropertyKey": "{{string}}"
            }
         ]
      },
      "searchableAttributes": [ "{{string}}" ],
      "thingTypeDescription": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateThingType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingTypeName](#API_UpdateThingType_RequestSyntax) **   <a name="iot-UpdateThingType-request-uri-thingTypeName"></a>
The name of a thing type.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_UpdateThingType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [thingTypeProperties](#API_UpdateThingType_RequestSyntax) **   <a name="iot-UpdateThingType-request-thingTypeProperties"></a>
The ThingTypeProperties contains information about the thing type including: a thing type description, and a list of searchable thing attribute names.
Type: [ThingTypeProperties](API_ThingTypeProperties.md) object
Required: No

## Response Syntax
<a name="API_UpdateThingType_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateThingType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateThingType_Errors"></a>

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
<a name="API_UpdateThingType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateThingType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateThingType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateThingType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateThingType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateThingType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateThingType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateThingType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateThingType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateThingType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateThingType)

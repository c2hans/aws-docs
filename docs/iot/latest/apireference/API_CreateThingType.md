---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateThingType.html
---

# CreateThingType
<a name="API_CreateThingType"></a>

Creates a new thing type. If this call is made multiple times using the same thing type name and configuration, the call will succeed. If this call is made with the same thing type name but different configuration a `ResourceAlreadyExistsException` is thrown.

Requires permission to access the [CreateThingType](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateThingType_RequestSyntax"></a>

```
POST /thing-types/{{thingTypeName}} HTTP/1.1
Content-type: application/json

{
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
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
<a name="API_CreateThingType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingTypeName](#API_CreateThingType_RequestSyntax) **   <a name="iot-CreateThingType-request-uri-thingTypeName"></a>
The name of the thing type.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_CreateThingType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_CreateThingType_RequestSyntax) **   <a name="iot-CreateThingType-request-tags"></a>
Metadata which can be used to manage the thing type.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [thingTypeProperties](#API_CreateThingType_RequestSyntax) **   <a name="iot-CreateThingType-request-thingTypeProperties"></a>
The ThingTypeProperties for the thing type to create. It contains information about the new thing type including a description, and a list of searchable thing attribute names.
Type: [ThingTypeProperties](API_ThingTypeProperties.md) object
Required: No

## Response Syntax
<a name="API_CreateThingType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "thingTypeArn": "string",
   "thingTypeId": "string",
   "thingTypeName": "string"
}
```

## Response Elements
<a name="API_CreateThingType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [thingTypeArn](#API_CreateThingType_ResponseSyntax) **   <a name="iot-CreateThingType-response-thingTypeArn"></a>
The Amazon Resource Name (ARN) of the thing type.
Type: String

 ** [thingTypeId](#API_CreateThingType_ResponseSyntax) **   <a name="iot-CreateThingType-response-thingTypeId"></a>
The thing type ID.
Type: String

 ** [thingTypeName](#API_CreateThingType_ResponseSyntax) **   <a name="iot-CreateThingType-response-thingTypeName"></a>
The name of the thing type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Errors
<a name="API_CreateThingType_Errors"></a>

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

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

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
<a name="API_CreateThingType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateThingType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateThingType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateThingType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateThingType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateThingType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateThingType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateThingType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateThingType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateThingType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateThingType)

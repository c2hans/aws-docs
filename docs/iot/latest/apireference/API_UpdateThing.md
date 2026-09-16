---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThing.html
---

# UpdateThing
<a name="API_UpdateThing"></a>

Updates the data for a thing.

Requires permission to access the [UpdateThing](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateThing_RequestSyntax"></a>

```
PATCH /things/{{thingName}} HTTP/1.1
Content-type: application/json

{
   "attributePayload": {
      "attributes": {
         "{{string}}" : "{{string}}"
      },
      "merge": {{boolean}}
   },
   "expectedVersion": {{number}},
   "removeThingType": {{boolean}},
   "thingTypeName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateThing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingName](#API_UpdateThing_RequestSyntax) **   <a name="iot-UpdateThing-request-uri-thingName"></a>
The name of the thing to update.
You can't change a thing's name. To change a thing's name, you must create a new thing, give it the new name, and then delete the old thing.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_UpdateThing_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributePayload](#API_UpdateThing_RequestSyntax) **   <a name="iot-UpdateThing-request-attributePayload"></a>
A list of thing attributes, a JSON string containing name-value pairs. For example:
 `{\"attributes\":{\"name1\":\"value2\"}}`
This data is used to add new attributes or update existing attributes.
Type: [AttributePayload](API_AttributePayload.md) object
Required: No

 ** [expectedVersion](#API_UpdateThing_RequestSyntax) **   <a name="iot-UpdateThing-request-expectedVersion"></a>
The expected version of the thing record in the registry. If the version of the record in the registry does not match the expected version specified in the request, the `UpdateThing` request is rejected with a `VersionConflictException`.
Type: Long
Required: No

 ** [removeThingType](#API_UpdateThing_RequestSyntax) **   <a name="iot-UpdateThing-request-removeThingType"></a>
Remove a thing type association. If **true**, the association is removed.
Type: Boolean
Required: No

 ** [thingTypeName](#API_UpdateThing_RequestSyntax) **   <a name="iot-UpdateThing-request-thingTypeName"></a>
The name of the thing type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

## Response Syntax
<a name="API_UpdateThing_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateThing_Errors"></a>

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

 ** VersionConflictException **
An exception thrown when the version of an entity specified with the `expectedVersion` parameter does not match the latest version in the system.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_UpdateThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateThing)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateThing)

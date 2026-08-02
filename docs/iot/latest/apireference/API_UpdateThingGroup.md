---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingGroup.html
---

# UpdateThingGroup
<a name="API_UpdateThingGroup"></a>

Update a thing group.

Requires permission to access the [UpdateThingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateThingGroup_RequestSyntax"></a>

```
PATCH /thing-groups/{{thingGroupName}} HTTP/1.1
Content-type: application/json

{
   "expectedVersion": {{number}},
   "thingGroupProperties": {
      "attributePayload": {
         "attributes": {
            "{{string}}" : "{{string}}"
         },
         "merge": {{boolean}}
      },
      "thingGroupDescription": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateThingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingGroupName](#API_UpdateThingGroup_RequestSyntax) **   <a name="iot-UpdateThingGroup-request-uri-thingGroupName"></a>
The thing group to update.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_UpdateThingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [expectedVersion](#API_UpdateThingGroup_RequestSyntax) **   <a name="iot-UpdateThingGroup-request-expectedVersion"></a>
The expected version of the thing group. If this does not match the version of the thing group being updated, the update will fail.
Type: Long
Required: No

 ** [thingGroupProperties](#API_UpdateThingGroup_RequestSyntax) **   <a name="iot-UpdateThingGroup-request-thingGroupProperties"></a>
The thing group properties.
Type: [ThingGroupProperties](API_ThingGroupProperties.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateThingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "version": number
}
```

## Response Elements
<a name="API_UpdateThingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [version](#API_UpdateThingGroup_ResponseSyntax) **   <a name="iot-UpdateThingGroup-response-version"></a>
The version of the updated thing group.
Type: Long

## Errors
<a name="API_UpdateThingGroup_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** VersionConflictException **
An exception thrown when the version of an entity specified with the `expectedVersion` parameter does not match the latest version in the system.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_UpdateThingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateThingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateThingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateThingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateThingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateThingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateThingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateThingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateThingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateThingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateThingGroup)

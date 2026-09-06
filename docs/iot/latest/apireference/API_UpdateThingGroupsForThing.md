---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingGroupsForThing.html
---

# UpdateThingGroupsForThing
<a name="API_UpdateThingGroupsForThing"></a>

Updates the groups to which the thing belongs.

Requires permission to access the [UpdateThingGroupsForThing](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateThingGroupsForThing_RequestSyntax"></a>

```
PUT /thing-groups/updateThingGroupsForThing HTTP/1.1
Content-type: application/json

{
   "overrideDynamicGroups": {{boolean}},
   "thingGroupsToAdd": [ "{{string}}" ],
   "thingGroupsToRemove": [ "{{string}}" ],
   "thingName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateThingGroupsForThing_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateThingGroupsForThing_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [overrideDynamicGroups](#API_UpdateThingGroupsForThing_RequestSyntax) **   <a name="iot-UpdateThingGroupsForThing-request-overrideDynamicGroups"></a>
Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.
Type: Boolean
Required: No

 ** [thingGroupsToAdd](#API_UpdateThingGroupsForThing_RequestSyntax) **   <a name="iot-UpdateThingGroupsForThing-request-thingGroupsToAdd"></a>
The groups to which the thing will be added.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [thingGroupsToRemove](#API_UpdateThingGroupsForThing_RequestSyntax) **   <a name="iot-UpdateThingGroupsForThing-request-thingGroupsToRemove"></a>
The groups from which the thing will be removed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [thingName](#API_UpdateThingGroupsForThing_RequestSyntax) **   <a name="iot-UpdateThingGroupsForThing-request-thingName"></a>
The thing whose group memberships will be updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

## Response Syntax
<a name="API_UpdateThingGroupsForThing_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateThingGroupsForThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateThingGroupsForThing_Errors"></a>

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

## See Also
<a name="API_UpdateThingGroupsForThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateThingGroupsForThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateThingGroupsForThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateThingGroupsForThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateThingGroupsForThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateThingGroupsForThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateThingGroupsForThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateThingGroupsForThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateThingGroupsForThing)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateThingGroupsForThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateThingGroupsForThing)

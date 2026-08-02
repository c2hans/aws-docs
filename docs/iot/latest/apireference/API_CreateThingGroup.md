---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateThingGroup.html
---

# CreateThingGroup
<a name="API_CreateThingGroup"></a>

Create a thing group.

**Note**
This is a control plane operation. See [Authorization](https://docs.aws.amazon.com/iot/latest/developerguide/iot-authorization.html) for information about authorizing control plane actions.
If the `ThingGroup` that you create has the exact same attributes as an existing `ThingGroup`, you will get a 200 success response.

Requires permission to access the [CreateThingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateThingGroup_RequestSyntax"></a>

```
POST /thing-groups/{{thingGroupName}} HTTP/1.1
Content-type: application/json

{
   "parentGroupName": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
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
<a name="API_CreateThingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingGroupName](#API_CreateThingGroup_RequestSyntax) **   <a name="iot-CreateThingGroup-request-uri-thingGroupName"></a>
The thing group name to create.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_CreateThingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [parentGroupName](#API_CreateThingGroup_RequestSyntax) **   <a name="iot-CreateThingGroup-request-parentGroupName"></a>
The name of the parent thing group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [tags](#API_CreateThingGroup_RequestSyntax) **   <a name="iot-CreateThingGroup-request-tags"></a>
Metadata which can be used to manage the thing group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [thingGroupProperties](#API_CreateThingGroup_RequestSyntax) **   <a name="iot-CreateThingGroup-request-thingGroupProperties"></a>
The thing group properties.
Type: [ThingGroupProperties](API_ThingGroupProperties.md) object
Required: No

## Response Syntax
<a name="API_CreateThingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "thingGroupArn": "string",
   "thingGroupId": "string",
   "thingGroupName": "string"
}
```

## Response Elements
<a name="API_CreateThingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [thingGroupArn](#API_CreateThingGroup_ResponseSyntax) **   <a name="iot-CreateThingGroup-response-thingGroupArn"></a>
The thing group ARN.
Type: String

 ** [thingGroupId](#API_CreateThingGroup_ResponseSyntax) **   <a name="iot-CreateThingGroup-response-thingGroupId"></a>
The thing group ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`

 ** [thingGroupName](#API_CreateThingGroup_ResponseSyntax) **   <a name="iot-CreateThingGroup-response-thingGroupName"></a>
The thing group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Errors
<a name="API_CreateThingGroup_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateThingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateThingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateThingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateThingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateThingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateThingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateThingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateThingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateThingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateThingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateThingGroup)

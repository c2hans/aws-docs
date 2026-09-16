---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDynamicThingGroup.html
---

# CreateDynamicThingGroup
<a name="API_CreateDynamicThingGroup"></a>

Creates a dynamic thing group.

Requires permission to access the [CreateDynamicThingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateDynamicThingGroup_RequestSyntax"></a>

```
POST /dynamic-thing-groups/{{thingGroupName}} HTTP/1.1
Content-type: application/json

{
   "indexName": "{{string}}",
   "queryString": "{{string}}",
   "queryVersion": "{{string}}",
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
<a name="API_CreateDynamicThingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingGroupName](#API_CreateDynamicThingGroup_RequestSyntax) **   <a name="iot-CreateDynamicThingGroup-request-uri-thingGroupName"></a>
The dynamic thing group name to create.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_CreateDynamicThingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [indexName](#API_CreateDynamicThingGroup_RequestSyntax) **   <a name="iot-CreateDynamicThingGroup-request-indexName"></a>
The dynamic thing group index name.
Currently one index is supported: `AWS_Things`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [queryString](#API_CreateDynamicThingGroup_RequestSyntax) **   <a name="iot-CreateDynamicThingGroup-request-queryString"></a>
The dynamic thing group search query string.
See [Query Syntax](https://docs.aws.amazon.com/iot/latest/developerguide/query-syntax.html) for information about query string syntax.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [queryVersion](#API_CreateDynamicThingGroup_RequestSyntax) **   <a name="iot-CreateDynamicThingGroup-request-queryVersion"></a>
The dynamic thing group query version.
Currently one query version is supported: "2017-09-30". If not specified, the query version defaults to this value.
Type: String
Required: No

 ** [tags](#API_CreateDynamicThingGroup_RequestSyntax) **   <a name="iot-CreateDynamicThingGroup-request-tags"></a>
Metadata which can be used to manage the dynamic thing group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [thingGroupProperties](#API_CreateDynamicThingGroup_RequestSyntax) **   <a name="iot-CreateDynamicThingGroup-request-thingGroupProperties"></a>
The dynamic thing group properties.
Type: [ThingGroupProperties](API_ThingGroupProperties.md) object
Required: No

## Response Syntax
<a name="API_CreateDynamicThingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "indexName": "string",
   "queryString": "string",
   "queryVersion": "string",
   "thingGroupArn": "string",
   "thingGroupId": "string",
   "thingGroupName": "string"
}
```

## Response Elements
<a name="API_CreateDynamicThingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [indexName](#API_CreateDynamicThingGroup_ResponseSyntax) **   <a name="iot-CreateDynamicThingGroup-response-indexName"></a>
The dynamic thing group index name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [queryString](#API_CreateDynamicThingGroup_ResponseSyntax) **   <a name="iot-CreateDynamicThingGroup-response-queryString"></a>
The dynamic thing group search query string.
Type: String
Length Constraints: Minimum length of 1.

 ** [queryVersion](#API_CreateDynamicThingGroup_ResponseSyntax) **   <a name="iot-CreateDynamicThingGroup-response-queryVersion"></a>
The dynamic thing group query version.
Type: String

 ** [thingGroupArn](#API_CreateDynamicThingGroup_ResponseSyntax) **   <a name="iot-CreateDynamicThingGroup-response-thingGroupArn"></a>
The dynamic thing group ARN.
Type: String

 ** [thingGroupId](#API_CreateDynamicThingGroup_ResponseSyntax) **   <a name="iot-CreateDynamicThingGroup-response-thingGroupId"></a>
The dynamic thing group ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`

 ** [thingGroupName](#API_CreateDynamicThingGroup_ResponseSyntax) **   <a name="iot-CreateDynamicThingGroup-response-thingGroupName"></a>
The dynamic thing group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Errors
<a name="API_CreateDynamicThingGroup_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidQueryException **
The query is invalid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

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
<a name="API_CreateDynamicThingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateDynamicThingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateDynamicThingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateDynamicThingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateDynamicThingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateDynamicThingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateDynamicThingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateDynamicThingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateDynamicThingGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateDynamicThingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateDynamicThingGroup)

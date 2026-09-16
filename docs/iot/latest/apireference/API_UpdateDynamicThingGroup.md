---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDynamicThingGroup.html
---

# UpdateDynamicThingGroup
<a name="API_UpdateDynamicThingGroup"></a>

Updates a dynamic thing group.

Requires permission to access the [UpdateDynamicThingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateDynamicThingGroup_RequestSyntax"></a>

```
PATCH /dynamic-thing-groups/{{thingGroupName}} HTTP/1.1
Content-type: application/json

{
   "expectedVersion": {{number}},
   "indexName": "{{string}}",
   "queryString": "{{string}}",
   "queryVersion": "{{string}}",
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
<a name="API_UpdateDynamicThingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [thingGroupName](#API_UpdateDynamicThingGroup_RequestSyntax) **   <a name="iot-UpdateDynamicThingGroup-request-uri-thingGroupName"></a>
The name of the dynamic thing group to update.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_UpdateDynamicThingGroup_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [expectedVersion](#API_UpdateDynamicThingGroup_RequestSyntax) **   <a name="iot-UpdateDynamicThingGroup-request-expectedVersion"></a>
The expected version of the dynamic thing group to update.
Type: Long
Required: No

 ** [indexName](#API_UpdateDynamicThingGroup_RequestSyntax) **   <a name="iot-UpdateDynamicThingGroup-request-indexName"></a>
The dynamic thing group index to update.
Currently one index is supported: `AWS_Things`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [queryString](#API_UpdateDynamicThingGroup_RequestSyntax) **   <a name="iot-UpdateDynamicThingGroup-request-queryString"></a>
The dynamic thing group search query string to update.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [queryVersion](#API_UpdateDynamicThingGroup_RequestSyntax) **   <a name="iot-UpdateDynamicThingGroup-request-queryVersion"></a>
The dynamic thing group query version to update.
Currently one query version is supported: "2017-09-30". If not specified, the query version defaults to this value.
Type: String
Required: No

 ** [thingGroupProperties](#API_UpdateDynamicThingGroup_RequestSyntax) **   <a name="iot-UpdateDynamicThingGroup-request-thingGroupProperties"></a>
The dynamic thing group properties to update.
Type: [ThingGroupProperties](API_ThingGroupProperties.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateDynamicThingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "version": number
}
```

## Response Elements
<a name="API_UpdateDynamicThingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [version](#API_UpdateDynamicThingGroup_ResponseSyntax) **   <a name="iot-UpdateDynamicThingGroup-response-version"></a>
The dynamic thing group version.
Type: Long

## Errors
<a name="API_UpdateDynamicThingGroup_Errors"></a>

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
<a name="API_UpdateDynamicThingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateDynamicThingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateDynamicThingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateDynamicThingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateDynamicThingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateDynamicThingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateDynamicThingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateDynamicThingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateDynamicThingGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateDynamicThingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateDynamicThingGroup)

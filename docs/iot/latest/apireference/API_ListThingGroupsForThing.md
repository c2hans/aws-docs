---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingGroupsForThing.html
---

# ListThingGroupsForThing
<a name="API_ListThingGroupsForThing"></a>

List the thing groups to which the specified thing belongs.

Requires permission to access the [ListThingGroupsForThing](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListThingGroupsForThing_RequestSyntax"></a>

```
GET /things/{{thingName}}/thing-groups?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListThingGroupsForThing_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListThingGroupsForThing_RequestSyntax) **   <a name="iot-ListThingGroupsForThing-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListThingGroupsForThing_RequestSyntax) **   <a name="iot-ListThingGroupsForThing-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

 ** [thingName](#API_ListThingGroupsForThing_RequestSyntax) **   <a name="iot-ListThingGroupsForThing-request-uri-thingName"></a>
The thing name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_ListThingGroupsForThing_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListThingGroupsForThing_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "thingGroups": [
      {
         "groupArn": "string",
         "groupName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListThingGroupsForThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListThingGroupsForThing_ResponseSyntax) **   <a name="iot-ListThingGroupsForThing-response-nextToken"></a>
The token to use to get the next set of results, or **null** if there are no additional results.
Type: String

 ** [thingGroups](#API_ListThingGroupsForThing_ResponseSyntax) **   <a name="iot-ListThingGroupsForThing-response-thingGroups"></a>
The thing groups.
Type: Array of [GroupNameAndArn](API_GroupNameAndArn.md) objects

## Errors
<a name="API_ListThingGroupsForThing_Errors"></a>

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
<a name="API_ListThingGroupsForThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListThingGroupsForThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListThingGroupsForThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListThingGroupsForThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListThingGroupsForThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListThingGroupsForThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListThingGroupsForThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListThingGroupsForThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListThingGroupsForThing)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListThingGroupsForThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListThingGroupsForThing)

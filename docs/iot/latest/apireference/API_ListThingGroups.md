---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingGroups.html
---

# ListThingGroups
<a name="API_ListThingGroups"></a>

List the thing groups in your account.

Requires permission to access the [ListThingGroups](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListThingGroups_RequestSyntax"></a>

```
GET /thing-groups?maxResults={{maxResults}}&namePrefixFilter={{namePrefixFilter}}&nextToken={{nextToken}}&parentGroup={{parentGroup}}&recursive={{recursive}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListThingGroups_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListThingGroups_RequestSyntax) **   <a name="iot-ListThingGroups-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [namePrefixFilter](#API_ListThingGroups_RequestSyntax) **   <a name="iot-ListThingGroups-request-uri-namePrefixFilter"></a>
A filter that limits the results to those with the specified name prefix.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [nextToken](#API_ListThingGroups_RequestSyntax) **   <a name="iot-ListThingGroups-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

 ** [parentGroup](#API_ListThingGroups_RequestSyntax) **   <a name="iot-ListThingGroups-request-uri-parentGroup"></a>
A filter that limits the results to those with the specified parent group.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [recursive](#API_ListThingGroups_RequestSyntax) **   <a name="iot-ListThingGroups-request-uri-recursive"></a>
If true, return child groups as well.

## Request Body
<a name="API_ListThingGroups_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListThingGroups_ResponseSyntax"></a>

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
<a name="API_ListThingGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListThingGroups_ResponseSyntax) **   <a name="iot-ListThingGroups-response-nextToken"></a>
The token to use to get the next set of results. Will not be returned if operation has returned all results.
Type: String

 ** [thingGroups](#API_ListThingGroups_ResponseSyntax) **   <a name="iot-ListThingGroups-response-thingGroups"></a>
The thing groups.
Type: Array of [GroupNameAndArn](API_GroupNameAndArn.md) objects

## Errors
<a name="API_ListThingGroups_Errors"></a>

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
<a name="API_ListThingGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListThingGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListThingGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListThingGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListThingGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListThingGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListThingGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListThingGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListThingGroups)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListThingGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListThingGroups)

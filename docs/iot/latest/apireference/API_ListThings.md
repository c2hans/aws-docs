---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListThings.html
---

# ListThings
<a name="API_ListThings"></a>

Lists your things. Use the **attributeName** and **attributeValue** parameters to filter your things. For example, calling `ListThings` with attributeName=Color and attributeValue=Red retrieves all things in the registry that contain an attribute **Color** with the value **Red**. For more information, see [List Things](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html#list-things) from the * AWS IoT Core Developer Guide*.

Requires permission to access the [ListThings](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

**Note**
You will not be charged for calling this API if an `Access denied` error is returned. You will also not be charged if no attributes or pagination token was provided in request and no pagination token and no results were returned.

## Request Syntax
<a name="API_ListThings_RequestSyntax"></a>

```
GET /things?attributeName={{attributeName}}&attributeValue={{attributeValue}}&maxResults={{maxResults}}&nextToken={{nextToken}}&thingTypeName={{thingTypeName}}&usePrefixAttributeValue={{usePrefixAttributeValue}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListThings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attributeName](#API_ListThings_RequestSyntax) **   <a name="iot-ListThings-request-uri-attributeName"></a>
The attribute name used to search for things.
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_.,@/:#-]+`

 ** [attributeValue](#API_ListThings_RequestSyntax) **   <a name="iot-ListThings-request-uri-attributeValue"></a>
The attribute value used to search for things.
Length Constraints: Maximum length of 800.
Pattern: `[a-zA-Z0-9_.,@/:#=\[\]-]*`

 ** [maxResults](#API_ListThings_RequestSyntax) **   <a name="iot-ListThings-request-uri-maxResults"></a>
The maximum number of results to return in this operation.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListThings_RequestSyntax) **   <a name="iot-ListThings-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

 ** [thingTypeName](#API_ListThings_RequestSyntax) **   <a name="iot-ListThings-request-uri-thingTypeName"></a>
The name of the thing type used to search for things.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [usePrefixAttributeValue](#API_ListThings_RequestSyntax) **   <a name="iot-ListThings-request-uri-usePrefixAttributeValue"></a>
When `true`, the action returns the thing resources with attribute values that start with the `attributeValue` provided.
When `false`, or not present, the action returns only the thing resources with attribute values that match the entire `attributeValue` provided.

## Request Body
<a name="API_ListThings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListThings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "things": [
      {
         "attributes": {
            "string" : "string"
         },
         "thingArn": "string",
         "thingName": "string",
         "thingTypeName": "string",
         "version": number
      }
   ]
}
```

## Response Elements
<a name="API_ListThings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListThings_ResponseSyntax) **   <a name="iot-ListThings-response-nextToken"></a>
The token to use to get the next set of results. Will not be returned if operation has returned all results.
Type: String

 ** [things](#API_ListThings_ResponseSyntax) **   <a name="iot-ListThings-response-things"></a>
The things.
Type: Array of [ThingAttribute](API_ThingAttribute.md) objects

## Errors
<a name="API_ListThings_Errors"></a>

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
<a name="API_ListThings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListThings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListThings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListThings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListThings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListThings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListThings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListThings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListThings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListThings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListThings)

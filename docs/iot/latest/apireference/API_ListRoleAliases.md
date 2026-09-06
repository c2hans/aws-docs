---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListRoleAliases.html
---

# ListRoleAliases
<a name="API_ListRoleAliases"></a>

Lists the role aliases registered in your account.

Requires permission to access the [ListRoleAliases](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListRoleAliases_RequestSyntax"></a>

```
GET /role-aliases?isAscendingOrder={{ascendingOrder}}&marker={{marker}}&pageSize={{pageSize}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRoleAliases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ascendingOrder](#API_ListRoleAliases_RequestSyntax) **   <a name="iot-ListRoleAliases-request-uri-ascendingOrder"></a>
Return the list of role aliases in ascending alphabetical order.

 ** [marker](#API_ListRoleAliases_RequestSyntax) **   <a name="iot-ListRoleAliases-request-uri-marker"></a>
A marker used to get the next set of results.
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [pageSize](#API_ListRoleAliases_RequestSyntax) **   <a name="iot-ListRoleAliases-request-uri-pageSize"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

## Request Body
<a name="API_ListRoleAliases_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRoleAliases_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextMarker": "string",
   "roleAliases": [ "string" ]
}
```

## Response Elements
<a name="API_ListRoleAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextMarker](#API_ListRoleAliases_ResponseSyntax) **   <a name="iot-ListRoleAliases-response-nextMarker"></a>
A marker used to get the next set of results.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [roleAliases](#API_ListRoleAliases_ResponseSyntax) **   <a name="iot-ListRoleAliases-response-roleAliases"></a>
The role aliases.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w=,@-]+`

## Errors
<a name="API_ListRoleAliases_Errors"></a>

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
<a name="API_ListRoleAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListRoleAliases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListRoleAliases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListRoleAliases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListRoleAliases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListRoleAliases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListRoleAliases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListRoleAliases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListRoleAliases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListRoleAliases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListRoleAliases)

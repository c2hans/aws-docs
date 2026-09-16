---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListPlugins.html
---

# ListPlugins
<a name="API_ListPlugins"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Lists configured Amazon Q Business plugins.

## Request Syntax
<a name="API_ListPlugins_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/plugins?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPlugins_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListPlugins_RequestSyntax) **   <a name="qbusiness-ListPlugins-request-uri-applicationId"></a>
The identifier of the application the plugin is attached to.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [maxResults](#API_ListPlugins_RequestSyntax) **   <a name="qbusiness-ListPlugins-request-uri-maxResults"></a>
The maximum number of documents to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListPlugins_RequestSyntax) **   <a name="qbusiness-ListPlugins-request-uri-nextToken"></a>
If the `maxResults` response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of plugins.
Length Constraints: Minimum length of 1. Maximum length of 800.

## Request Body
<a name="API_ListPlugins_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPlugins_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "plugins": [
      {
         "buildStatus": "string",
         "createdAt": number,
         "displayName": "string",
         "pluginId": "string",
         "serverUrl": "string",
         "state": "string",
         "type": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListPlugins_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPlugins_ResponseSyntax) **   <a name="qbusiness-ListPlugins-response-nextToken"></a>
If the `maxResults` response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of plugins.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [plugins](#API_ListPlugins_ResponseSyntax) **   <a name="qbusiness-ListPlugins-response-plugins"></a>
Information about a configured plugin.
Type: Array of [Plugin](API_Plugin.md) objects

## Errors
<a name="API_ListPlugins_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_ListPlugins_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/ListPlugins)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/ListPlugins)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ListPlugins)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/ListPlugins)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ListPlugins)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/ListPlugins)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/ListPlugins)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/ListPlugins)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/ListPlugins)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ListPlugins)

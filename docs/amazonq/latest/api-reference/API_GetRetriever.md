---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetRetriever.html
---

# GetRetriever
<a name="API_GetRetriever"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Gets information about an existing retriever used by an Amazon Q Business application.

## Request Syntax
<a name="API_GetRetriever_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/retrievers/{{retrieverId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRetriever_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetRetriever_RequestSyntax) **   <a name="qbusiness-GetRetriever-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application using the retriever.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [retrieverId](#API_GetRetriever_RequestSyntax) **   <a name="qbusiness-GetRetriever-request-uri-retrieverId"></a>
The identifier of the retriever.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_GetRetriever_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRetriever_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "configuration": { ... },
   "createdAt": number,
   "displayName": "string",
   "retrieverArn": "string",
   "retrieverId": "string",
   "roleArn": "string",
   "status": "string",
   "type": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetRetriever_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-applicationId"></a>
The identifier of the Amazon Q Business application using the retriever.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [configuration](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-configuration"></a>
Provides information on how the retriever used for your Amazon Q Business application is configured.
Type: [RetrieverConfiguration](API_RetrieverConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-createdAt"></a>
The Unix timestamp when the retriever was created.
Type: Timestamp

 ** [displayName](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-displayName"></a>
The name of the retriever.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

 ** [retrieverArn](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-retrieverArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the retriever.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [retrieverId](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-retrieverId"></a>
The identifier of the retriever.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [roleArn](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-roleArn"></a>
The Amazon Resource Name (ARN) of the role with the permission to access the retriever and required resources.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [status](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-status"></a>
The status of the retriever.
Type: String
Valid Values: `CREATING | ACTIVE | FAILED`

 ** [type](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-type"></a>
The type of the retriever.
Type: String
Valid Values: `NATIVE_INDEX | KENDRA_INDEX`

 ** [updatedAt](#API_GetRetriever_ResponseSyntax) **   <a name="qbusiness-GetRetriever-response-updatedAt"></a>
The Unix timestamp when the retriever was last updated.
Type: Timestamp

## Errors
<a name="API_GetRetriever_Errors"></a>

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
<a name="API_GetRetriever_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/GetRetriever)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/GetRetriever)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GetRetriever)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/GetRetriever)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GetRetriever)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/GetRetriever)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/GetRetriever)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/GetRetriever)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/GetRetriever)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GetRetriever)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateRetriever.html
---

# CreateRetriever
<a name="API_CreateRetriever"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Adds a retriever to your Amazon Q Business application.

## Request Syntax
<a name="API_CreateRetriever_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/retrievers HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "configuration": { ... },
   "displayName": "{{string}}",
   "roleArn": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRetriever_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CreateRetriever_RequestSyntax) **   <a name="qbusiness-CreateRetriever-request-uri-applicationId"></a>
The identifier of your Amazon Q Business application.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_CreateRetriever_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateRetriever_RequestSyntax) **   <a name="qbusiness-CreateRetriever-request-clientToken"></a>
A token that you provide to identify the request to create your Amazon Q Business application retriever.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [configuration](#API_CreateRetriever_RequestSyntax) **   <a name="qbusiness-CreateRetriever-request-configuration"></a>
Provides information on how the retriever used for your Amazon Q Business application is configured.
Type: [RetrieverConfiguration](API_RetrieverConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [displayName](#API_CreateRetriever_RequestSyntax) **   <a name="qbusiness-CreateRetriever-request-displayName"></a>
The name of your retriever.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [roleArn](#API_CreateRetriever_RequestSyntax) **   <a name="qbusiness-CreateRetriever-request-roleArn"></a>
The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** [tags](#API_CreateRetriever_RequestSyntax) **   <a name="qbusiness-CreateRetriever-request-tags"></a>
A list of key-value pairs that identify or categorize the retriever. You can also use tags to help control access to the retriever. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [type](#API_CreateRetriever_RequestSyntax) **   <a name="qbusiness-CreateRetriever-request-type"></a>
The type of retriever you are using.
Type: String
Valid Values: `NATIVE_INDEX | KENDRA_INDEX`
Required: Yes

## Response Syntax
<a name="API_CreateRetriever_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "retrieverArn": "string",
   "retrieverId": "string"
}
```

## Response Elements
<a name="API_CreateRetriever_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [retrieverArn](#API_CreateRetriever_ResponseSyntax) **   <a name="qbusiness-CreateRetriever-response-retrieverArn"></a>
The Amazon Resource Name (ARN) of an IAM role associated with a retriever.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [retrieverId](#API_CreateRetriever_ResponseSyntax) **   <a name="qbusiness-CreateRetriever-response-retrieverId"></a>
The identifier of the retriever you are using.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

## Errors
<a name="API_CreateRetriever_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
You have exceeded the set limits for your Amazon Q Business service.
 ** message **
The message describing a `ServiceQuotaExceededException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 402

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
<a name="API_CreateRetriever_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CreateRetriever)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CreateRetriever)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CreateRetriever)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CreateRetriever)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CreateRetriever)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CreateRetriever)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CreateRetriever)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CreateRetriever)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CreateRetriever)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CreateRetriever)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

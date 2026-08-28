---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListWebExperiences.html
---

# ListWebExperiences
<a name="API_ListWebExperiences"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Lists one or more Amazon Q Business Web Experiences.

## Request Syntax
<a name="API_ListWebExperiences_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/experiences?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListWebExperiences_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListWebExperiences_RequestSyntax) **   <a name="qbusiness-ListWebExperiences-request-uri-applicationId"></a>
The identifier of the Amazon Q Business application linked to the listed web experiences.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [maxResults](#API_ListWebExperiences_RequestSyntax) **   <a name="qbusiness-ListWebExperiences-request-uri-maxResults"></a>
The maximum number of Amazon Q Business Web Experiences to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListWebExperiences_RequestSyntax) **   <a name="qbusiness-ListWebExperiences-request-uri-nextToken"></a>
If the `maxResults` response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business conversations.
Length Constraints: Minimum length of 1. Maximum length of 800.

## Request Body
<a name="API_ListWebExperiences_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListWebExperiences_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "webExperiences": [
      {
         "createdAt": number,
         "defaultEndpoint": "string",
         "status": "string",
         "updatedAt": number,
         "webExperienceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWebExperiences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWebExperiences_ResponseSyntax) **   <a name="qbusiness-ListWebExperiences-response-nextToken"></a>
If the response is truncated, Amazon Q Business returns this token, which you can use in a later request to list the next set of messages.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

 ** [webExperiences](#API_ListWebExperiences_ResponseSyntax) **   <a name="qbusiness-ListWebExperiences-response-webExperiences"></a>
An array of summary information for one or more Amazon Q Business experiences.
Type: Array of [WebExperience](API_WebExperience.md) objects

## Errors
<a name="API_ListWebExperiences_Errors"></a>

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
<a name="API_ListWebExperiences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/ListWebExperiences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/ListWebExperiences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ListWebExperiences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/ListWebExperiences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ListWebExperiences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/ListWebExperiences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/ListWebExperiences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/ListWebExperiences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/ListWebExperiences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ListWebExperiences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

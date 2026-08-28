---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetSpace.html
---

# GetSpace
<a name="API_GetSpace"></a>

Returns information about an space.

## Request Syntax
<a name="API_GetSpace_RequestSyntax"></a>

```
GET /v1/spaces/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSpace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_GetSpace_RequestSyntax) **   <a name="codecatalyst-GetSpace-request-uri-name"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_GetSpace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSpace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "displayName": "string",
   "name": "string",
   "regionName": "string"
}
```

## Response Elements
<a name="API_GetSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_GetSpace_ResponseSyntax) **   <a name="codecatalyst-GetSpace-response-description"></a>
The description of the space.
Type: String

 ** [displayName](#API_GetSpace_ResponseSyntax) **   <a name="codecatalyst-GetSpace-response-displayName"></a>
The friendly name of the space displayed to users.
Type: String

 ** [name](#API_GetSpace_ResponseSyntax) **   <a name="codecatalyst-GetSpace-response-name"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [regionName](#API_GetSpace_ResponseSyntax) **   <a name="codecatalyst-GetSpace-response-regionName"></a>
The AWS Region where the space exists.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 16.
Pattern: `(us(?:-gov)?|af|ap|ca|cn|eu|sa)-(central|(?:north|south)?(?:east|west)?)-(\d+)`

## Errors
<a name="API_GetSpace_Errors"></a>

 ** AccessDeniedException **
The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.
HTTP Status Code: 403

 ** ConflictException **
The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.
HTTP Status Code: 400

## See Also
<a name="API_GetSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/GetSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/GetSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/GetSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/GetSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/GetSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/GetSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/GetSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/GetSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/GetSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/GetSpace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

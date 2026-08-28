---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteProject.html
---

# DeleteProject
<a name="API_DeleteProject"></a>

Deletes a project in Amazon DataZone.

## Request Syntax
<a name="API_DeleteProject_RequestSyntax"></a>

```
DELETE /v2/domains/{{domainIdentifier}}/projects/{{identifier}}?skipDeletionCheck={{skipDeletionCheck}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DeleteProject_RequestSyntax) **   <a name="datazone-DeleteProject-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the project is deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_DeleteProject_RequestSyntax) **   <a name="datazone-DeleteProject-request-uri-identifier"></a>
The identifier of the project that is to be deleted.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [skipDeletionCheck](#API_DeleteProject_RequestSyntax) **   <a name="datazone-DeleteProject-request-uri-skipDeletionCheck"></a>
Specifies the optional flag to delete all child entities within the project.

## Request Body
<a name="API_DeleteProject_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteProject_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteProject)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteProject)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteProject)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteProject)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteProject)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteProject)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteProject)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CheckDocumentAccess.html
---

# CheckDocumentAccess
<a name="API_CheckDocumentAccess"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Verifies if a user has access permissions for a specified document and returns the actual ACL attached to the document. Resolves user access on the document via user aliases and groups when verifying user access.

## Request Syntax
<a name="API_CheckDocumentAccess_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/index/{{indexId}}/users/{{userId}}/documents/{{documentId}}/check-document-access?dataSourceId={{dataSourceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CheckDocumentAccess_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CheckDocumentAccess_RequestSyntax) **   <a name="qbusiness-CheckDocumentAccess-request-uri-applicationId"></a>
The unique identifier of the application. This is required to identify the specific Amazon Q Business application context for the document access check.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [dataSourceId](#API_CheckDocumentAccess_RequestSyntax) **   <a name="qbusiness-CheckDocumentAccess-request-uri-dataSourceId"></a>
The unique identifier of the data source. Identifies the specific data source from which the document originates. Should not be used when a document is uploaded directly with BatchPutDocument, as no dataSourceId is available or necessary.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [documentId](#API_CheckDocumentAccess_RequestSyntax) **   <a name="qbusiness-CheckDocumentAccess-request-uri-documentId"></a>
The unique identifier of the document. Specifies which document's access permissions are being checked.
Length Constraints: Minimum length of 1. Maximum length of 1825.
Pattern: `\P{C}*`
Required: Yes

 ** [indexId](#API_CheckDocumentAccess_RequestSyntax) **   <a name="qbusiness-CheckDocumentAccess-request-uri-indexId"></a>
The unique identifier of the index. Used to locate the correct index within the application where the document is stored.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [userId](#API_CheckDocumentAccess_RequestSyntax) **   <a name="qbusiness-CheckDocumentAccess-request-uri-userId"></a>
The unique identifier of the user. Used to check the access permissions for this specific user against the document's ACL.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Request Body
<a name="API_CheckDocumentAccess_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CheckDocumentAccess_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "documentAcl": {
      "allowlist": {
         "conditions": [
            {
               "groups": [
                  {
                     "name": "string",
                     "type": "string"
                  }
               ],
               "memberRelation": "string",
               "users": [
                  {
                     "id": "string",
                     "type": "string"
                  }
               ]
            }
         ],
         "memberRelation": "string"
      },
      "denyList": {
         "conditions": [
            {
               "groups": [
                  {
                     "name": "string",
                     "type": "string"
                  }
               ],
               "memberRelation": "string",
               "users": [
                  {
                     "id": "string",
                     "type": "string"
                  }
               ]
            }
         ],
         "memberRelation": "string"
      }
   },
   "hasAccess": boolean,
   "userAliases": [
      {
         "id": "string",
         "type": "string"
      }
   ],
   "userGroups": [
      {
         "name": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CheckDocumentAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [documentAcl](#API_CheckDocumentAccess_ResponseSyntax) **   <a name="qbusiness-CheckDocumentAccess-response-documentAcl"></a>
The Access Control List (ACL) associated with the document. Includes allowlist and denylist conditions that determine user access.
Type: [DocumentAcl](API_DocumentAcl.md) object

 ** [hasAccess](#API_CheckDocumentAccess_ResponseSyntax) **   <a name="qbusiness-CheckDocumentAccess-response-hasAccess"></a>
A boolean value indicating whether the specified user has access to the document, either direct access or transitive access via groups and aliases attached to the document.
Type: Boolean

 ** [userAliases](#API_CheckDocumentAccess_ResponseSyntax) **   <a name="qbusiness-CheckDocumentAccess-response-userAliases"></a>
An array of aliases associated with the user. This includes both global and local aliases, each with a name and type.
Type: Array of [AssociatedUser](API_AssociatedUser.md) objects

 ** [userGroups](#API_CheckDocumentAccess_ResponseSyntax) **   <a name="qbusiness-CheckDocumentAccess-response-userGroups"></a>
An array of groups the user is part of for the specified data source. Each group has a name and type.
Type: Array of [AssociatedGroup](API_AssociatedGroup.md) objects

## Errors
<a name="API_CheckDocumentAccess_Errors"></a>

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
<a name="API_CheckDocumentAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CheckDocumentAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CheckDocumentAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CheckDocumentAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CheckDocumentAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CheckDocumentAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CheckDocumentAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CheckDocumentAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CheckDocumentAccess)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CheckDocumentAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CheckDocumentAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

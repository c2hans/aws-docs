---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredAudienceModelAssociation.html
---

# CreateConfiguredAudienceModelAssociation
<a name="API_CreateConfiguredAudienceModelAssociation"></a>

Provides the details necessary to create a configured audience model association.

## Request Syntax
<a name="API_CreateConfiguredAudienceModelAssociation_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/configuredaudiencemodelassociations HTTP/1.1
Content-type: application/json

{
   "configuredAudienceModelArn": "{{string}}",
   "configuredAudienceModelAssociationName": "{{string}}",
   "description": "{{string}}",
   "manageResourcePolicies": {{boolean}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateConfiguredAudienceModelAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_CreateConfiguredAudienceModelAssociation_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModelAssociation-request-uri-membershipIdentifier"></a>
A unique identifier for one of your memberships for a collaboration. The configured audience model is associated to the collaboration that this membership belongs to. Accepts a membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateConfiguredAudienceModelAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuredAudienceModelArn](#API_CreateConfiguredAudienceModelAssociation_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModelAssociation-request-configuredAudienceModelArn"></a>
A unique identifier for the configured audience model that you want to associate.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-audience-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [configuredAudienceModelAssociationName](#API_CreateConfiguredAudienceModelAssociation_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModelAssociation-request-configuredAudienceModelAssociationName"></a>
The name of the configured audience model association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [description](#API_CreateConfiguredAudienceModelAssociation_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModelAssociation-request-description"></a>
A description of the configured audience model association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [manageResourcePolicies](#API_CreateConfiguredAudienceModelAssociation_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModelAssociation-request-manageResourcePolicies"></a>
When `TRUE`, indicates that the resource policy for the configured audience model resource being associated is configured for AWS Clean Rooms to manage permissions related to the given collaboration. When `FALSE`, indicates that the configured audience model resource owner will manage permissions related to the given collaboration.
Setting this to `TRUE` requires you to have permissions to create, update, and delete the resource policy for the `cleanrooms-ml` resource when you call the [DeleteConfiguredAudienceModelAssociation](API_DeleteConfiguredAudienceModelAssociation.md) resource. In addition, if you are the collaboration creator and specify `TRUE`, you must have the same permissions when you call the [DeleteMember](API_DeleteMember.md) and [DeleteCollaboration](API_DeleteCollaboration.md) APIs.
Type: Boolean
Required: Yes

 ** [tags](#API_CreateConfiguredAudienceModelAssociation_RequestSyntax) **   <a name="API-CreateConfiguredAudienceModelAssociation-request-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateConfiguredAudienceModelAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredAudienceModelAssociation": {
      "arn": "string",
      "collaborationArn": "string",
      "collaborationId": "string",
      "configuredAudienceModelArn": "string",
      "createTime": number,
      "description": "string",
      "id": "string",
      "manageResourcePolicies": boolean,
      "membershipArn": "string",
      "membershipId": "string",
      "name": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_CreateConfiguredAudienceModelAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredAudienceModelAssociation](#API_CreateConfiguredAudienceModelAssociation_ResponseSyntax) **   <a name="API-CreateConfiguredAudienceModelAssociation-response-configuredAudienceModelAssociation"></a>
Information about the configured audience model association.
Type: [ConfiguredAudienceModelAssociation](API_ConfiguredAudienceModelAssociation.md) object

## Errors
<a name="API_CreateConfiguredAudienceModelAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** reason **
A reason code for the exception.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request denied because service quota has been exceeded.
 ** quotaName **
The name of the quota.
 ** quotaValue **
The value of the quota.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateConfiguredAudienceModelAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreateConfiguredAudienceModelAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

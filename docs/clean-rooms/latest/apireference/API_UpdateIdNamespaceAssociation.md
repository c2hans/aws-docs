---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateIdNamespaceAssociation.html
---

# UpdateIdNamespaceAssociation
<a name="API_UpdateIdNamespaceAssociation"></a>

Provides the details that are necessary to update an ID namespace association.

## Request Syntax
<a name="API_UpdateIdNamespaceAssociation_RequestSyntax"></a>

```
PATCH /memberships/{{membershipIdentifier}}/idnamespaceassociations/{{idNamespaceAssociationIdentifier}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "idMappingConfig": {
      "allowUseAsDimensionColumn": {{boolean}}
   },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIdNamespaceAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [idNamespaceAssociationIdentifier](#API_UpdateIdNamespaceAssociation_RequestSyntax) **   <a name="API-UpdateIdNamespaceAssociation-request-uri-idNamespaceAssociationIdentifier"></a>
The unique identifier of the ID namespace association that you want to update.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_UpdateIdNamespaceAssociation_RequestSyntax) **   <a name="API-UpdateIdNamespaceAssociation-request-uri-membershipIdentifier"></a>
The unique identifier of the membership that contains the ID namespace association that you want to update.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateIdNamespaceAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateIdNamespaceAssociation_RequestSyntax) **   <a name="API-UpdateIdNamespaceAssociation-request-description"></a>
A new description for the ID namespace association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [idMappingConfig](#API_UpdateIdNamespaceAssociation_RequestSyntax) **   <a name="API-UpdateIdNamespaceAssociation-request-idMappingConfig"></a>
The configuration settings for the ID mapping table.
Type: [IdMappingConfig](API_IdMappingConfig.md) object
Required: No

 ** [name](#API_UpdateIdNamespaceAssociation_RequestSyntax) **   <a name="API-UpdateIdNamespaceAssociation-request-name"></a>
A new name for the ID namespace association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: No

## Response Syntax
<a name="API_UpdateIdNamespaceAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "idNamespaceAssociation": {
      "arn": "string",
      "collaborationArn": "string",
      "collaborationId": "string",
      "createTime": number,
      "description": "string",
      "id": "string",
      "idMappingConfig": {
         "allowUseAsDimensionColumn": boolean
      },
      "inputReferenceConfig": {
         "inputReferenceArn": "string",
         "manageResourcePolicies": boolean
      },
      "inputReferenceProperties": {
         "idMappingWorkflowsSupported": [ JSON value ],
         "idNamespaceType": "string"
      },
      "membershipArn": "string",
      "membershipId": "string",
      "name": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_UpdateIdNamespaceAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [idNamespaceAssociation](#API_UpdateIdNamespaceAssociation_ResponseSyntax) **   <a name="API-UpdateIdNamespaceAssociation-response-idNamespaceAssociation"></a>
The updated ID namespace association.
Type: [IdNamespaceAssociation](API_IdNamespaceAssociation.md) object

## Errors
<a name="API_UpdateIdNamespaceAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

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
<a name="API_UpdateIdNamespaceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateIdNamespaceAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

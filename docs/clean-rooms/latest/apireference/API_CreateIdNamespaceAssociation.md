---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateIdNamespaceAssociation.html
---

# CreateIdNamespaceAssociation
<a name="API_CreateIdNamespaceAssociation"></a>

Creates an ID namespace association.

## Request Syntax
<a name="API_CreateIdNamespaceAssociation_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/idnamespaceassociations HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "idMappingConfig": {
      "allowUseAsDimensionColumn": {{boolean}}
   },
   "inputReferenceConfig": {
      "inputReferenceArn": "{{string}}",
      "manageResourcePolicies": {{boolean}}
   },
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateIdNamespaceAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_CreateIdNamespaceAssociation_RequestSyntax) **   <a name="API-CreateIdNamespaceAssociation-request-uri-membershipIdentifier"></a>
The unique identifier of the membership that contains the ID namespace association.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateIdNamespaceAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateIdNamespaceAssociation_RequestSyntax) **   <a name="API-CreateIdNamespaceAssociation-request-description"></a>
The description of the ID namespace association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [idMappingConfig](#API_CreateIdNamespaceAssociation_RequestSyntax) **   <a name="API-CreateIdNamespaceAssociation-request-idMappingConfig"></a>
The configuration settings for the ID mapping table.
Type: [IdMappingConfig](API_IdMappingConfig.md) object
Required: No

 ** [inputReferenceConfig](#API_CreateIdNamespaceAssociation_RequestSyntax) **   <a name="API-CreateIdNamespaceAssociation-request-inputReferenceConfig"></a>
The input reference configuration needed to create the ID namespace association.
Type: [IdNamespaceAssociationInputReferenceConfig](API_IdNamespaceAssociationInputReferenceConfig.md) object
Required: Yes

 ** [name](#API_CreateIdNamespaceAssociation_RequestSyntax) **   <a name="API-CreateIdNamespaceAssociation-request-name"></a>
The name for the ID namespace association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** [tags](#API_CreateIdNamespaceAssociation_RequestSyntax) **   <a name="API-CreateIdNamespaceAssociation-request-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateIdNamespaceAssociation_ResponseSyntax"></a>

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
<a name="API_CreateIdNamespaceAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [idNamespaceAssociation](#API_CreateIdNamespaceAssociation_ResponseSyntax) **   <a name="API-CreateIdNamespaceAssociation-response-idNamespaceAssociation"></a>
The ID namespace association that was created.
Type: [IdNamespaceAssociation](API_IdNamespaceAssociation.md) object

## Errors
<a name="API_CreateIdNamespaceAssociation_Errors"></a>

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
<a name="API_CreateIdNamespaceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreateIdNamespaceAssociation)

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_GetCollaborationConfiguredAudienceModelAssociation.html
---

# GetCollaborationConfiguredAudienceModelAssociation
<a name="API_GetCollaborationConfiguredAudienceModelAssociation"></a>

Retrieves a configured audience model association within a collaboration.

## Request Syntax
<a name="API_GetCollaborationConfiguredAudienceModelAssociation_RequestSyntax"></a>

```
GET /collaborations/{{collaborationIdentifier}}/configuredaudiencemodelassociations/{{configuredAudienceModelAssociationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCollaborationConfiguredAudienceModelAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationIdentifier](#API_GetCollaborationConfiguredAudienceModelAssociation_RequestSyntax) **   <a name="API-GetCollaborationConfiguredAudienceModelAssociation-request-uri-collaborationIdentifier"></a>
A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [configuredAudienceModelAssociationIdentifier](#API_GetCollaborationConfiguredAudienceModelAssociation_RequestSyntax) **   <a name="API-GetCollaborationConfiguredAudienceModelAssociation-request-uri-configuredAudienceModelAssociationIdentifier"></a>
A unique identifier for the configured audience model association that you want to retrieve.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetCollaborationConfiguredAudienceModelAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCollaborationConfiguredAudienceModelAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaborationConfiguredAudienceModelAssociation": {
      "arn": "string",
      "collaborationArn": "string",
      "collaborationId": "string",
      "configuredAudienceModelArn": "string",
      "createTime": number,
      "creatorAccountId": "string",
      "description": "string",
      "id": "string",
      "name": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_GetCollaborationConfiguredAudienceModelAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationConfiguredAudienceModelAssociation](#API_GetCollaborationConfiguredAudienceModelAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredAudienceModelAssociation-response-collaborationConfiguredAudienceModelAssociation"></a>
The metadata of the configured audience model association.
Type: [CollaborationConfiguredAudienceModelAssociation](API_CollaborationConfiguredAudienceModelAssociation.md) object

## Errors
<a name="API_GetCollaborationConfiguredAudienceModelAssociation_Errors"></a>

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
<a name="API_GetCollaborationConfiguredAudienceModelAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/GetCollaborationConfiguredAudienceModelAssociation)

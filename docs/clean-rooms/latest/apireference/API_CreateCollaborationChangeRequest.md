---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateCollaborationChangeRequest.html
---

# CreateCollaborationChangeRequest
<a name="API_CreateCollaborationChangeRequest"></a>

Creates a new change request to modify an existing collaboration. This enables post-creation modifications to collaborations through a structured API-driven approach.

## Request Syntax
<a name="API_CreateCollaborationChangeRequest_RequestSyntax"></a>

```
POST /collaborations/{{collaborationIdentifier}}/changeRequests HTTP/1.1
Content-type: application/json

{
   "changes": [
      {
         "specification": { ... },
         "specificationType": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateCollaborationChangeRequest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationIdentifier](#API_CreateCollaborationChangeRequest_RequestSyntax) **   <a name="API-CreateCollaborationChangeRequest-request-uri-collaborationIdentifier"></a>
The identifier of the collaboration that the change request is made against.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_CreateCollaborationChangeRequest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [changes](#API_CreateCollaborationChangeRequest_RequestSyntax) **   <a name="API-CreateCollaborationChangeRequest-request-changes"></a>
The list of changes to apply to the collaboration. Each change specifies the type of modification and the details of what should be changed.
Type: Array of [ChangeInput](API_ChangeInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## Response Syntax
<a name="API_CreateCollaborationChangeRequest_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaborationChangeRequest": {
      "approvals": {
         "string" : {
            "status": "string"
         }
      },
      "changes": [
         {
            "specification": { ... },
            "specificationType": "string",
            "types": [ "string" ]
         }
      ],
      "collaborationId": "string",
      "createTime": number,
      "id": "string",
      "isAutoApproved": boolean,
      "status": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_CreateCollaborationChangeRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationChangeRequest](#API_CreateCollaborationChangeRequest_ResponseSyntax) **   <a name="API-CreateCollaborationChangeRequest-response-collaborationChangeRequest"></a>
Represents a request to modify a collaboration. Change requests enable structured modifications to collaborations after they have been created.
Type: [CollaborationChangeRequest](API_CollaborationChangeRequest.md) object

## Errors
<a name="API_CreateCollaborationChangeRequest_Errors"></a>

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
<a name="API_CreateCollaborationChangeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CreateCollaborationChangeRequest)

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateCollaborationChangeRequest.html
---

# UpdateCollaborationChangeRequest
<a name="API_UpdateCollaborationChangeRequest"></a>

Updates an existing collaboration change request. This operation allows approval actions for pending change requests in collaborations (APPROVE, DENY, CANCEL, COMMIT).

For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.

## Request Syntax
<a name="API_UpdateCollaborationChangeRequest_RequestSyntax"></a>

```
PATCH /collaborations/{{collaborationIdentifier}}/changeRequests/{{changeRequestIdentifier}} HTTP/1.1
Content-type: application/json

{
   "action": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCollaborationChangeRequest_RequestParameters"></a>

The request uses the following URI parameters.

 ** [changeRequestIdentifier](#API_UpdateCollaborationChangeRequest_RequestSyntax) **   <a name="API-UpdateCollaborationChangeRequest-request-uri-changeRequestIdentifier"></a>
The unique identifier of the specific change request to be updated within the collaboration.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [collaborationIdentifier](#API_UpdateCollaborationChangeRequest_RequestSyntax) **   <a name="API-UpdateCollaborationChangeRequest-request-uri-collaborationIdentifier"></a>
The unique identifier of the collaboration that contains the change request to be updated.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateCollaborationChangeRequest_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [action](#API_UpdateCollaborationChangeRequest_RequestSyntax) **   <a name="API-UpdateCollaborationChangeRequest-request-action"></a>
The action to perform on the change request. Valid values include APPROVE (approve the change), DENY (reject the change), CANCEL (cancel the request), and COMMIT (commit after the request is approved).
For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.
Type: String
Valid Values: `APPROVE | DENY | CANCEL | COMMIT`
Required: Yes

## Response Syntax
<a name="API_UpdateCollaborationChangeRequest_ResponseSyntax"></a>

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
<a name="API_UpdateCollaborationChangeRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationChangeRequest](#API_UpdateCollaborationChangeRequest_ResponseSyntax) **   <a name="API-UpdateCollaborationChangeRequest-response-collaborationChangeRequest"></a>
Represents a request to modify a collaboration. Change requests enable structured modifications to collaborations after they have been created.
Type: [CollaborationChangeRequest](API_CollaborationChangeRequest.md) object

## Errors
<a name="API_UpdateCollaborationChangeRequest_Errors"></a>

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
<a name="API_UpdateCollaborationChangeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateCollaborationChangeRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

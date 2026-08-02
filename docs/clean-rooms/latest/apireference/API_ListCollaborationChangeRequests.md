---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ListCollaborationChangeRequests.html
---

# ListCollaborationChangeRequests
<a name="API_ListCollaborationChangeRequests"></a>

Lists all change requests for a collaboration with pagination support. Returns change requests sorted by creation time.

## Request Syntax
<a name="API_ListCollaborationChangeRequests_RequestSyntax"></a>

```
GET /collaborations/{{collaborationIdentifier}}/changeRequests?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCollaborationChangeRequests_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationIdentifier](#API_ListCollaborationChangeRequests_RequestSyntax) **   <a name="API-ListCollaborationChangeRequests-request-uri-collaborationIdentifier"></a>
The identifier of the collaboration that the change request is made against.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [maxResults](#API_ListCollaborationChangeRequests_RequestSyntax) **   <a name="API-ListCollaborationChangeRequests-request-uri-maxResults"></a>
The maximum number of results that are returned for an API request call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCollaborationChangeRequests_RequestSyntax) **   <a name="API-ListCollaborationChangeRequests-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [status](#API_ListCollaborationChangeRequests_RequestSyntax) **   <a name="API-ListCollaborationChangeRequests-request-uri-status"></a>
A filter to only return change requests with the specified status.
Valid Values: `PENDING | APPROVED | CANCELLED | DENIED | COMMITTED`

## Request Body
<a name="API_ListCollaborationChangeRequests_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCollaborationChangeRequests_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaborationChangeRequestSummaries": [
      {
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCollaborationChangeRequests_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationChangeRequestSummaries](#API_ListCollaborationChangeRequests_ResponseSyntax) **   <a name="API-ListCollaborationChangeRequests-response-collaborationChangeRequestSummaries"></a>
The list of collaboration change request summaries.
Type: Array of [CollaborationChangeRequestSummary](API_CollaborationChangeRequestSummary.md) objects

 ** [nextToken](#API_ListCollaborationChangeRequests_ResponseSyntax) **   <a name="API-ListCollaborationChangeRequests-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

## Errors
<a name="API_ListCollaborationChangeRequests_Errors"></a>

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
<a name="API_ListCollaborationChangeRequests_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/ListCollaborationChangeRequests)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/ListCollaborationChangeRequests)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ListCollaborationChangeRequests)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/ListCollaborationChangeRequests)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ListCollaborationChangeRequests)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/ListCollaborationChangeRequests)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/ListCollaborationChangeRequests)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/ListCollaborationChangeRequests)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/ListCollaborationChangeRequests)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ListCollaborationChangeRequests)

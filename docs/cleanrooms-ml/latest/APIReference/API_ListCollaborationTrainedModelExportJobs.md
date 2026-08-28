---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListCollaborationTrainedModelExportJobs.html
---

# ListCollaborationTrainedModelExportJobs
<a name="API_ListCollaborationTrainedModelExportJobs"></a>

Returns a list of the export jobs for a trained model in a collaboration.

## Request Syntax
<a name="API_ListCollaborationTrainedModelExportJobs_RequestSyntax"></a>

```
GET /collaborations/{{collaborationIdentifier}}/trained-models/{{trainedModelArn}}/export-jobs?maxResults={{maxResults}}&nextToken={{nextToken}}&trainedModelVersionIdentifier={{trainedModelVersionIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCollaborationTrainedModelExportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationIdentifier](#API_ListCollaborationTrainedModelExportJobs_RequestSyntax) **   <a name="API-ListCollaborationTrainedModelExportJobs-request-uri-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the trained model export jobs that you are interested in.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [maxResults](#API_ListCollaborationTrainedModelExportJobs_RequestSyntax) **   <a name="API-ListCollaborationTrainedModelExportJobs-request-uri-maxResults"></a>
The maximum size of the results that is returned per call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCollaborationTrainedModelExportJobs_RequestSyntax) **   <a name="API-ListCollaborationTrainedModelExportJobs-request-uri-nextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10240.

 ** [trainedModelArn](#API_ListCollaborationTrainedModelExportJobs_RequestSyntax) **   <a name="API-ListCollaborationTrainedModelExportJobs-request-uri-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model that was used to create the export jobs that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [trainedModelVersionIdentifier](#API_ListCollaborationTrainedModelExportJobs_RequestSyntax) **   <a name="API-ListCollaborationTrainedModelExportJobs-request-uri-trainedModelVersionIdentifier"></a>
The version identifier of the trained model to filter export jobs by. When specified, only export jobs for this specific version of the trained model are returned.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Request Body
<a name="API_ListCollaborationTrainedModelExportJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCollaborationTrainedModelExportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaborationTrainedModelExportJobs": [
      {
         "collaborationIdentifier": "string",
         "createTime": "string",
         "creatorAccountId": "string",
         "description": "string",
         "membershipIdentifier": "string",
         "name": "string",
         "outputConfiguration": {
            "members": [
               {
                  "accountId": "string"
               }
            ]
         },
         "status": "string",
         "statusDetails": {
            "message": "string",
            "statusCode": "string"
         },
         "trainedModelArn": "string",
         "trainedModelVersionIdentifier": "string",
         "updateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCollaborationTrainedModelExportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationTrainedModelExportJobs](#API_ListCollaborationTrainedModelExportJobs_ResponseSyntax) **   <a name="API-ListCollaborationTrainedModelExportJobs-response-collaborationTrainedModelExportJobs"></a>
The exports jobs that exist for the requested trained model in the requested collaboration.
Type: Array of [CollaborationTrainedModelExportJobSummary](API_CollaborationTrainedModelExportJobSummary.md) objects

 ** [nextToken](#API_ListCollaborationTrainedModelExportJobs_ResponseSyntax) **   <a name="API-ListCollaborationTrainedModelExportJobs-response-nextToken"></a>
The token value used to access the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Errors
<a name="API_ListCollaborationTrainedModelExportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_ListCollaborationTrainedModelExportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ListCollaborationTrainedModelExportJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

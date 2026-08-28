---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PopulateIdMappingTable.html
---

# PopulateIdMappingTable
<a name="API_PopulateIdMappingTable"></a>

Defines the information that's necessary to populate an ID mapping table.

## Request Syntax
<a name="API_PopulateIdMappingTable_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/idmappingtables/{{idMappingTableIdentifier}}/populate HTTP/1.1
Content-type: application/json

{
   "jobType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PopulateIdMappingTable_RequestParameters"></a>

The request uses the following URI parameters.

 ** [idMappingTableIdentifier](#API_PopulateIdMappingTable_RequestSyntax) **   <a name="API-PopulateIdMappingTable-request-uri-idMappingTableIdentifier"></a>
The unique identifier of the ID mapping table that you want to populate.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_PopulateIdMappingTable_RequestSyntax) **   <a name="API-PopulateIdMappingTable-request-uri-membershipIdentifier"></a>
The unique identifier of the membership that contains the ID mapping table that you want to populate.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_PopulateIdMappingTable_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [jobType](#API_PopulateIdMappingTable_RequestSyntax) **   <a name="API-PopulateIdMappingTable-request-jobType"></a>
The job type of the rule-based ID mapping job. Valid values include:
 `INCREMENTAL`: Processes only new or changed data since the last job run. This is the default job type if the ID mapping workflow was created in AWS Entity Resolution with `incrementalRunConfig` specified.
 `BATCH`: Processes all data from the input source, regardless of previous job runs. This is the default job type if the ID mapping workflow was created in AWS Entity Resolution but `incrementalRunConfig` wasn't specified.
 `DELETE_ONLY`: Processes only deletion requests from `BatchDeleteUniqueId`, which is set in AWS Entity Resolution.
For more information about `incrementalRunConfig` and `BatchDeleteUniqueId`, see the [AWS Entity Resolution API Reference](https://docs.aws.amazon.com/entityresolution/latest/apireference/Welcome.html).
Type: String
Valid Values: `BATCH | INCREMENTAL | DELETE_ONLY`
Required: No

## Response Syntax
<a name="API_PopulateIdMappingTable_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "idMappingJobId": "string"
}
```

## Response Elements
<a name="API_PopulateIdMappingTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [idMappingJobId](#API_PopulateIdMappingTable_ResponseSyntax) **   <a name="API-PopulateIdMappingTable-response-idMappingJobId"></a>
The unique identifier of the mapping job that will populate the ID mapping table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

## Errors
<a name="API_PopulateIdMappingTable_Errors"></a>

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
<a name="API_PopulateIdMappingTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/PopulateIdMappingTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/PopulateIdMappingTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PopulateIdMappingTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/PopulateIdMappingTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PopulateIdMappingTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/PopulateIdMappingTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/PopulateIdMappingTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/PopulateIdMappingTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/PopulateIdMappingTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PopulateIdMappingTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

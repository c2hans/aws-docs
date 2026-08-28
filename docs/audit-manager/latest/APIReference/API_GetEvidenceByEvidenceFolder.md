---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceByEvidenceFolder.html
---

# GetEvidenceByEvidenceFolder
<a name="API_GetEvidenceByEvidenceFolder"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

 Gets all evidence from a specified evidence folder in AWS Audit Manager.

## Request Syntax
<a name="API_GetEvidenceByEvidenceFolder_RequestSyntax"></a>

```
GET /assessments/{{assessmentId}}/controlSets/{{controlSetId}}/evidenceFolders/{{evidenceFolderId}}/evidence?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEvidenceByEvidenceFolder_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentId](#API_GetEvidenceByEvidenceFolder_RequestSyntax) **   <a name="auditmanager-GetEvidenceByEvidenceFolder-request-uri-assessmentId"></a>
 The identifier for the assessment.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [controlSetId](#API_GetEvidenceByEvidenceFolder_RequestSyntax) **   <a name="auditmanager-GetEvidenceByEvidenceFolder-request-uri-controlSetId"></a>
 The identifier for the control set.
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[\w\W\s\S]*$`
Required: Yes

 ** [evidenceFolderId](#API_GetEvidenceByEvidenceFolder_RequestSyntax) **   <a name="auditmanager-GetEvidenceByEvidenceFolder-request-uri-evidenceFolderId"></a>
 The unique identifier for the folder that the evidence is stored in.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [maxResults](#API_GetEvidenceByEvidenceFolder_RequestSyntax) **   <a name="auditmanager-GetEvidenceByEvidenceFolder-request-uri-maxResults"></a>
 Represents the maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_GetEvidenceByEvidenceFolder_RequestSyntax) **   <a name="auditmanager-GetEvidenceByEvidenceFolder-request-uri-nextToken"></a>
 The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Request Body
<a name="API_GetEvidenceByEvidenceFolder_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEvidenceByEvidenceFolder_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "evidence": [
      {
         "assessmentReportSelection": "string",
         "attributes": {
            "string" : "string"
         },
         "awsAccountId": "string",
         "awsOrganization": "string",
         "complianceCheck": "string",
         "dataSource": "string",
         "eventName": "string",
         "eventSource": "string",
         "evidenceAwsAccountId": "string",
         "evidenceByType": "string",
         "evidenceFolderId": "string",
         "iamId": "string",
         "id": "string",
         "resourcesIncluded": [
            {
               "arn": "string",
               "complianceCheck": "string",
               "value": "string"
            }
         ],
         "time": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetEvidenceByEvidenceFolder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [evidence](#API_GetEvidenceByEvidenceFolder_ResponseSyntax) **   <a name="auditmanager-GetEvidenceByEvidenceFolder-response-evidence"></a>
 The list of evidence that the `GetEvidenceByEvidenceFolder` API returned.
Type: Array of [Evidence](API_Evidence.md) objects

 ** [nextToken](#API_GetEvidenceByEvidenceFolder_ResponseSyntax) **   <a name="auditmanager-GetEvidenceByEvidenceFolder-response-nextToken"></a>
 The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Errors
<a name="API_GetEvidenceByEvidenceFolder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource that's specified in the request can't be found.
 ** resourceId **
 The unique identifier for the resource.
 ** resourceType **
 The type of resource that's affected by the error.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
 ** fields **
 The fields that caused the error, if applicable.
 ** reason **
 The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_GetEvidenceByEvidenceFolder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

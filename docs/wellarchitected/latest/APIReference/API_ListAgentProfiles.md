---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ListAgentProfiles.html
---

# ListAgentProfiles
<a name="API_ListAgentProfiles"></a>

**Note**
 AWS Well-Architected Agent is in preview release and is subject to change.

**Important**
Organizational profiles are not available during the preview release.

Lists optimization profiles in your account. Profiles define the scope and configuration for generating optimization recommendations.

## Request Syntax
<a name="API_ListAgentProfiles_RequestSyntax"></a>

```
GET /api/v1/agent-profiles?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAgentProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAgentProfiles_RequestSyntax) **   <a name="wellarchitected-ListAgentProfiles-request-uri-maxResults"></a>
The maximum number of profiles to return in a single call. Default is 100.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAgentProfiles_RequestSyntax) **   <a name="wellarchitected-ListAgentProfiles-request-uri-nextToken"></a>
A pagination token returned from a previous call to continue retrieving results.
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

## Request Body
<a name="API_ListAgentProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAgentProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "aggregationConfiguration": [
            {
               "accessRoleArn": "string",
               "accountId": "string",
               "regions": [ "string" ]
            }
         ],
         "arn": "string",
         "businessOverview": "string",
         "createdAt": "string",
         "createdBy": "string",
         "deletionProtection": boolean,
         "description": "string",
         "displayName": "string",
         "eligibleForArchitectureGeneration": boolean,
         "eligibleForScheduledGeneration": boolean,
         "executionRoleArn": "string",
         "fieldErrors": {
            "string" : "string"
         },
         "lastModifiedAt": "string",
         "lastModifiedBy": "string",
         "name": "string",
         "organizationalAggregationConfiguration": {
            "accounts": [
               {
                  "accountId": "string",
                  "regions": [ "string" ]
               }
            ],
            "organizationalUnits": [
               {
                  "organizationalUnitId": "string",
                  "regions": [ "string" ]
               }
            ]
         },
         "pillars": [ "string" ],
         "profileType": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAgentProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAgentProfiles_ResponseSyntax) **   <a name="wellarchitected-ListAgentProfiles-response-items"></a>
A list of profile summaries.
Type: Array of [AgentProfileSummary](API_AgentProfileSummary.md) objects

 ** [nextToken](#API_ListAgentProfiles_ResponseSyntax) **   <a name="wellarchitected-ListAgentProfiles-response-nextToken"></a>
A pagination token to retrieve the next set of results, if available.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[A-Za-z0-9+\/=_-]+`

## Errors
<a name="API_ListAgentProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListAgentProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/ListAgentProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/ListAgentProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ListAgentProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/ListAgentProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ListAgentProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/ListAgentProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/ListAgentProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/ListAgentProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/ListAgentProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ListAgentProfiles)

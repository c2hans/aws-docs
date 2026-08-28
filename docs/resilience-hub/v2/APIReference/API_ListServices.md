---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListServices.html
---

# ListServices
<a name="API_ListServices"></a>

Lists services.

## Request Syntax
<a name="API_ListServices_RequestSyntax"></a>

```
GET /v2/list-services?accountId={{accountId}}&assessmentStatus={{assessmentStatus}}&maxResults={{maxResults}}&nextToken={{nextToken}}&ouId={{ouId}}&policyArn={{policyArn}}&systemArn={{systemArn}}&userJourneyId={{userJourneyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListServices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_ListServices_RequestSyntax) **   <a name="ngresiliencehub-ListServices-request-uri-accountId"></a>
Filter services by AWS account ID.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [assessmentStatus](#API_ListServices_RequestSyntax) **   <a name="ngresiliencehub-ListServices-request-uri-assessmentStatus"></a>
Filter services by assessment status.
Valid Values: `NOT_STARTED | PENDING | IN_PROGRESS | FAILED | SUCCESS`

 ** [maxResults](#API_ListServices_RequestSyntax) **   <a name="ngresiliencehub-ListServices-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListServices_RequestSyntax) **   <a name="ngresiliencehub-ListServices-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [ouId](#API_ListServices_RequestSyntax) **   <a name="ngresiliencehub-ListServices-request-uri-ouId"></a>
Filter services by organizational unit (OU) identifier.
Length Constraints: Minimum length of 16. Maximum length of 68.
Pattern: `ou-[a-z0-9]{4,32}-[a-z0-9]{8,32}`

 ** [policyArn](#API_ListServices_RequestSyntax) **   <a name="ngresiliencehub-ListServices-request-uri-policyArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [systemArn](#API_ListServices_RequestSyntax) **   <a name="ngresiliencehub-ListServices-request-uri-systemArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [userJourneyId](#API_ListServices_RequestSyntax) **   <a name="ngresiliencehub-ListServices-request-uri-userJourneyId"></a>
Filter services by user journey identifier.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`

## Request Body
<a name="API_ListServices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListServices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "serviceSummaries": [
      {
         "accountId": "string",
         "achievability": {
            "availabilitySlo": "string",
            "dataRecoveryTimeBetweenBackups": "string",
            "multiAzRtoRpo": "string",
            "multiRegionRtoRpo": "string"
         },
         "assessmentStatus": "string",
         "associatedSystems": [
            {
               "systemArn": "string",
               "systemName": "string",
               "userJourneyIds": [ "string" ]
            }
         ],
         "createdAt": number,
         "dependencyDiscovery": {
            "eligibleResourceCount": number,
            "message": "string",
            "status": "string",
            "updatedAt": number
         },
         "name": "string",
         "openFindingsCount": number,
         "organizationId": "string",
         "ouId": "string",
         "policyArn": "string",
         "regions": [ "string" ],
         "resolvedFindingsCount": number,
         "serviceArn": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListServices_ResponseSyntax) **   <a name="ngresiliencehub-ListServices-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceSummaries](#API_ListServices_ResponseSyntax) **   <a name="ngresiliencehub-ListServices-response-serviceSummaries"></a>
The list of service summaries.
Type: Array of [ServiceSummary](API_ServiceSummary.md) objects

## Errors
<a name="API_ListServices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

 ** InternalServerException **
Internal service error.
HTTP Status Code: 500

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListServices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListServices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

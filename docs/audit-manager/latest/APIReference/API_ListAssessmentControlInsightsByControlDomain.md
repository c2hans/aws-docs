---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentControlInsightsByControlDomain.html
---

# ListAssessmentControlInsightsByControlDomain
<a name="API_ListAssessmentControlInsightsByControlDomain"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

Lists the latest analytics data for controls within a specific control domain and a specific active assessment.

**Note**
Control insights are listed only if the control belongs to the control domain and assessment that was specified. Moreover, the control must have collected evidence on the `lastUpdated` date of `controlInsightsByAssessment`. If neither of these conditions are met, no data is listed for that control.

## Request Syntax
<a name="API_ListAssessmentControlInsightsByControlDomain_RequestSyntax"></a>

```
GET /insights/controls-by-assessment?assessmentId={{assessmentId}}&controlDomainId={{controlDomainId}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssessmentControlInsightsByControlDomain_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentId](#API_ListAssessmentControlInsightsByControlDomain_RequestSyntax) **   <a name="auditmanager-ListAssessmentControlInsightsByControlDomain-request-uri-assessmentId"></a>
The unique identifier for the active assessment.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [controlDomainId](#API_ListAssessmentControlInsightsByControlDomain_RequestSyntax) **   <a name="auditmanager-ListAssessmentControlInsightsByControlDomain-request-uri-controlDomainId"></a>
The unique identifier for the control domain.
Audit Manager supports the control domains that are provided by AWS Control Catalog. For information about how to find a list of available control domains, see [https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html) in the AWS Control Catalog API Reference.
Length Constraints: Minimum length of 13. Maximum length of 2048.
Pattern: `^arn:.*:controlcatalog:.*:.*:domain/.*|UNCATEGORIZED|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [maxResults](#API_ListAssessmentControlInsightsByControlDomain_RequestSyntax) **   <a name="auditmanager-ListAssessmentControlInsightsByControlDomain-request-uri-maxResults"></a>
Represents the maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListAssessmentControlInsightsByControlDomain_RequestSyntax) **   <a name="auditmanager-ListAssessmentControlInsightsByControlDomain-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Request Body
<a name="API_ListAssessmentControlInsightsByControlDomain_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssessmentControlInsightsByControlDomain_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "controlInsightsByAssessment": [
      {
         "controlSetName": "string",
         "evidenceInsights": {
            "compliantEvidenceCount": number,
            "inconclusiveEvidenceCount": number,
            "noncompliantEvidenceCount": number
         },
         "id": "string",
         "lastUpdated": number,
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssessmentControlInsightsByControlDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [controlInsightsByAssessment](#API_ListAssessmentControlInsightsByControlDomain_ResponseSyntax) **   <a name="auditmanager-ListAssessmentControlInsightsByControlDomain-response-controlInsightsByAssessment"></a>
The assessment control analytics data that the `ListAssessmentControlInsightsByControlDomain` API returned.
Type: Array of [ControlInsightsMetadataByAssessmentItem](API_ControlInsightsMetadataByAssessmentItem.md) objects

 ** [nextToken](#API_ListAssessmentControlInsightsByControlDomain_ResponseSyntax) **   <a name="auditmanager-ListAssessmentControlInsightsByControlDomain-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Errors
<a name="API_ListAssessmentControlInsightsByControlDomain_Errors"></a>

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
<a name="API_ListAssessmentControlInsightsByControlDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ListAssessmentControlInsightsByControlDomain)

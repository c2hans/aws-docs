---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControlDomainInsights.html
---

# ListControlDomainInsights
<a name="API_ListControlDomainInsights"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

Lists the latest analytics data for control domains across all of your active assessments.

Audit Manager supports the control domains that are provided by AWS Control Catalog. For information about how to find a list of available control domains, see [`ListDomains`](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains.html) in the AWS Control Catalog API Reference.

**Note**
A control domain is listed only if at least one of the controls within that domain collected evidence on the `lastUpdated` date of `controlDomainInsights`. If this condition isn’t met, no data is listed for that control domain.

## Request Syntax
<a name="API_ListControlDomainInsights_RequestSyntax"></a>

```
GET /insights/control-domains?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListControlDomainInsights_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListControlDomainInsights_RequestSyntax) **   <a name="auditmanager-ListControlDomainInsights-request-uri-maxResults"></a>
Represents the maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListControlDomainInsights_RequestSyntax) **   <a name="auditmanager-ListControlDomainInsights-request-uri-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Request Body
<a name="API_ListControlDomainInsights_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListControlDomainInsights_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "controlDomainInsights": [
      {
         "controlsCountByNoncompliantEvidence": number,
         "evidenceInsights": {
            "compliantEvidenceCount": number,
            "inconclusiveEvidenceCount": number,
            "noncompliantEvidenceCount": number
         },
         "id": "string",
         "lastUpdated": number,
         "name": "string",
         "totalControlsCount": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListControlDomainInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [controlDomainInsights](#API_ListControlDomainInsights_ResponseSyntax) **   <a name="auditmanager-ListControlDomainInsights-response-controlDomainInsights"></a>
The control domain analytics data that the `ListControlDomainInsights` API returned.
Type: Array of [ControlDomainInsights](API_ControlDomainInsights.md) objects

 ** [nextToken](#API_ListControlDomainInsights_ResponseSyntax) **   <a name="auditmanager-ListControlDomainInsights-response-nextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[A-Za-z0-9+\/=]*$`

## Errors
<a name="API_ListControlDomainInsights_Errors"></a>

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
<a name="API_ListControlDomainInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/ListControlDomainInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/ListControlDomainInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ListControlDomainInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/ListControlDomainInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ListControlDomainInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/ListControlDomainInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/ListControlDomainInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/ListControlDomainInsights)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/ListControlDomainInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ListControlDomainInsights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

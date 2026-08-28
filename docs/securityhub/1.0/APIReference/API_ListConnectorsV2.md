---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListConnectorsV2.html
---

# ListConnectorsV2
<a name="API_ListConnectorsV2"></a>

Grants permission to retrieve a list of connectorsV2 and their metadata for the calling account.

## Request Syntax
<a name="API_ListConnectorsV2_RequestSyntax"></a>

```
GET /connectorsv2?ConnectorStatus={{ConnectorStatus}}&EnablementStatus={{EnablementStatus}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&ProviderName={{ProviderName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConnectorsV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectorStatus](#API_ListConnectorsV2_RequestSyntax) **   <a name="securityhub-ListConnectorsV2-request-uri-ConnectorStatus"></a>
The status for the connectorV2.
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | PENDING_AUTHORIZATION | PENDING_CONFIGURATION | UNKNOWN`

 ** [EnablementStatus](#API_ListConnectorsV2_RequestSyntax) **   <a name="securityhub-ListConnectorsV2-request-uri-EnablementStatus"></a>
The enablement status to filter connectors by.
Valid Values: `ENABLED | PENDING_ENABLEMENT | FAILED_TO_ENABLE | PENDING_UPDATE | FAILED_TO_UPDATE | PENDING_DELETION | FAILED_TO_DELETE`

 ** [MaxResults](#API_ListConnectorsV2_RequestSyntax) **   <a name="securityhub-ListConnectorsV2-request-uri-MaxResults"></a>
The maximum number of results to be returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListConnectorsV2_RequestSyntax) **   <a name="securityhub-ListConnectorsV2-request-uri-NextToken"></a>
The pagination token per the AWS Pagination standard

 ** [ProviderName](#API_ListConnectorsV2_RequestSyntax) **   <a name="securityhub-ListConnectorsV2-request-uri-ProviderName"></a>
The name of the third-party provider.
Valid Values: `JIRA_CLOUD | SERVICENOW | AZURE`

## Request Body
<a name="API_ListConnectorsV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConnectorsV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Connectors": [
      {
         "ConnectorArn": "string",
         "ConnectorId": "string",
         "CreatedAt": "string",
         "Description": "string",
         "EnablementStatus": "string",
         "EnablementStatusReason": "string",
         "Name": "string",
         "ProviderSummary": {
            "ConnectorStatus": "string",
            "ProviderConfiguration": { ... },
            "ProviderName": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectorsV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connectors](#API_ListConnectorsV2_ResponseSyntax) **   <a name="securityhub-ListConnectorsV2-response-Connectors"></a>
An array of connectorV2 summaries.
Type: Array of [ConnectorSummary](API_ConnectorSummary.md) objects

 ** [NextToken](#API_ListConnectorsV2_ResponseSyntax) **   <a name="securityhub-ListConnectorsV2-response-NextToken"></a>
The pagination token to use to request the next page of results. Otherwise, this parameter is null.
Type: String

## Errors
<a name="API_ListConnectorsV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_ListConnectorsV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListConnectorsV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListConnectorsV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListConnectorsV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListConnectorsV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListConnectorsV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListConnectorsV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListConnectorsV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListConnectorsV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListConnectorsV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListConnectorsV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

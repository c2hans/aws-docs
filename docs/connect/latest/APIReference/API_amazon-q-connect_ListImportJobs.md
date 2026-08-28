---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ListImportJobs.html
---

# ListImportJobs
<a name="API_amazon-q-connect_ListImportJobs"></a>

Lists information about import jobs.

## Request Syntax
<a name="API_amazon-q-connect_ListImportJobs_RequestSyntax"></a>

```
GET /knowledgeBases/{{knowledgeBaseId}}/importJobs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_ListImportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_ListImportJobs_RequestSyntax) **   <a name="connect-amazon-q-connect_ListImportJobs-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [maxResults](#API_amazon-q-connect_ListImportJobs_RequestSyntax) **   <a name="connect-amazon-q-connect_ListImportJobs-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_amazon-q-connect_ListImportJobs_RequestSyntax) **   <a name="connect-amazon-q-connect_ListImportJobs-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Request Body
<a name="API_amazon-q-connect_ListImportJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_ListImportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "importJobSummaries": [
      {
         "createdTime": number,
         "externalSourceConfiguration": {
            "configuration": { ... },
            "source": "string"
         },
         "importJobId": "string",
         "importJobType": "string",
         "knowledgeBaseArn": "string",
         "knowledgeBaseId": "string",
         "lastModifiedTime": number,
         "metadata": {
            "string" : "string"
         },
         "status": "string",
         "uploadId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_ListImportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [importJobSummaries](#API_amazon-q-connect_ListImportJobs_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListImportJobs-response-importJobSummaries"></a>
Summary information about the import jobs.
Type: Array of [ImportJobSummary](API_amazon-q-connect_ImportJobSummary.md) objects

 ** [nextToken](#API_amazon-q-connect_ListImportJobs_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListImportJobs-response-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

## Errors
<a name="API_amazon-q-connect_ListImportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_ListImportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/ListImportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/ListImportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ListImportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/ListImportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ListImportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/ListImportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/ListImportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/ListImportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/ListImportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ListImportJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

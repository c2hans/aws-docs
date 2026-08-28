---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListExecutions.html
---

# ListExecutions
<a name="API_ListExecutions"></a>

Retrieves a paginated list of summaries of all executions.

## Request Syntax
<a name="API_ListExecutions_RequestSyntax"></a>

```
GET /executions?actionType={{actionType}}&maxResults={{maxResults}}&nextToken={{nextToken}}&resolveToResourceId={{resolveToResourceId}}&resolveToResourceType={{resolveToResourceType}}&targetResourceId={{targetResourceId}}&targetResourceType={{targetResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListExecutions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionType](#API_ListExecutions_RequestSyntax) **   <a name="iotsitewise-ListExecutions-request-uri-actionType"></a>
The type of action exectued.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`

 ** [maxResults](#API_ListExecutions_RequestSyntax) **   <a name="iotsitewise-ListExecutions-request-uri-maxResults"></a>
The maximum number of results returned for each paginated request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListExecutions_RequestSyntax) **   <a name="iotsitewise-ListExecutions-request-uri-nextToken"></a>
The token used for the next set of paginated results.
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

 ** [resolveToResourceId](#API_ListExecutions_RequestSyntax) **   <a name="iotsitewise-ListExecutions-request-uri-resolveToResourceId"></a>
The ID of the resolved resource.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`

 ** [resolveToResourceType](#API_ListExecutions_RequestSyntax) **   <a name="iotsitewise-ListExecutions-request-uri-resolveToResourceType"></a>
The type of the resolved resource.
Valid Values: `ASSET`

 ** [targetResourceId](#API_ListExecutions_RequestSyntax) **   <a name="iotsitewise-ListExecutions-request-uri-targetResourceId"></a>
The ID of the target resource.
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** [targetResourceType](#API_ListExecutions_RequestSyntax) **   <a name="iotsitewise-ListExecutions-request-uri-targetResourceType"></a>
The type of the target resource.
Valid Values: `ASSET | COMPUTATION_MODEL`
Required: Yes

## Request Body
<a name="API_ListExecutions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListExecutions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "executionSummaries": [
      {
         "actionType": "string",
         "executionEndTime": number,
         "executionEntityVersion": "string",
         "executionId": "string",
         "executionStartTime": number,
         "executionStatus": {
            "state": "string"
         },
         "resolveTo": {
            "assetId": "string"
         },
         "targetResource": {
            "assetId": "string",
            "computationModelId": "string"
         },
         "targetResourceVersion": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [executionSummaries](#API_ListExecutions_ResponseSyntax) **   <a name="iotsitewise-ListExecutions-response-executionSummaries"></a>
Contains the list of execution summaries of the computation models.
Type: Array of [ExecutionSummary](API_ExecutionSummary.md) objects

 ** [nextToken](#API_ListExecutions_ResponseSyntax) **   <a name="iotsitewise-ListExecutions-response-nextToken"></a>
The token for the next set of results, or null if there are no additional results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_ListExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_ListExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

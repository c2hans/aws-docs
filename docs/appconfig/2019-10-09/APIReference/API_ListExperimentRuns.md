---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExperimentRuns.html
---

# ListExperimentRuns
<a name="API_ListExperimentRuns"></a>

Lists the experiment runs for a specified experiment definition. You can filter by status.

## Request Syntax
<a name="API_ListExperimentRuns_RequestSyntax"></a>

```
GET /applications/{{ApplicationIdentifier}}/experimentdefinitions/{{ExperimentDefinitionIdentifier}}/experimentruns?max_results={{MaxResults}}&next_token={{NextToken}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListExperimentRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_ListExperimentRuns_RequestSyntax) **   <a name="appconfig-ListExperimentRuns-request-uri-ApplicationIdentifier"></a>
The application ID or name.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [ExperimentDefinitionIdentifier](#API_ListExperimentRuns_RequestSyntax) **   <a name="appconfig-ListExperimentRuns-request-uri-ExperimentDefinitionIdentifier"></a>
The experiment definition ID or name.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [MaxResults](#API_ListExperimentRuns_RequestSyntax) **   <a name="appconfig-ListExperimentRuns-request-uri-MaxResults"></a>
The maximum number of items to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_ListExperimentRuns_RequestSyntax) **   <a name="appconfig-ListExperimentRuns-request-uri-NextToken"></a>
A token to start the list from a previously truncated response.
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Status](#API_ListExperimentRuns_RequestSyntax) **   <a name="appconfig-ListExperimentRuns-request-uri-Status"></a>
A filter for the experiment run status.
Valid Values: `RUNNING | DONE`

## Request Body
<a name="API_ListExperimentRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListExperimentRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Description": "string",
         "EndedAt": "string",
         "ExperimentDefinitionId": "string",
         "Run": number,
         "StartedAt": "string",
         "Status": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListExperimentRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListExperimentRuns_ResponseSyntax) **   <a name="appconfig-ListExperimentRuns-response-Items"></a>
The list of experiment runs.
Type: Array of [ExperimentRunSummary](API_ExperimentRunSummary.md) objects

 ** [NextToken](#API_ListExperimentRuns_ResponseSyntax) **   <a name="appconfig-ListExperimentRuns-response-NextToken"></a>
A token to use for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListExperimentRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_ListExperimentRuns_Examples"></a>

### Example
<a name="API_ListExperimentRuns_Example_1"></a>

This example illustrates one usage of ListExperimentRuns.

#### Sample Request
<a name="API_ListExperimentRuns_Example_1_Request"></a>

```
GET /applications/abc1234/experimentdefinitions/bsxyd7k/experimentruns HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
User-Agent: aws-cli
X-Amz-Date: 20210916T175455Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210916/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_ListExperimentRuns_Example_1_Response"></a>

```
{
	"Items": [
		{
			"EndedAt": "2026-06-16T17:57:36.083Z",
			"ExperimentDefinitionId": "bsxyd7k",
			"Run": 1,
			"StartedAt": "2026-06-16T17:57:10.046Z",
			"Status": "DONE",
			"UpdatedAt": "2026-06-16T17:57:36.083Z"
		}
	]
}
```

## See Also
<a name="API_ListExperimentRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/ListExperimentRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/ListExperimentRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ListExperimentRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/ListExperimentRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ListExperimentRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/ListExperimentRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/ListExperimentRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/ListExperimentRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/ListExperimentRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ListExperimentRuns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

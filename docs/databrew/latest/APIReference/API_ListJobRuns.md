---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ListJobRuns.html
---

# ListJobRuns
<a name="API_ListJobRuns"></a>

Lists all of the previous runs of a particular DataBrew job.

## Request Syntax
<a name="API_ListJobRuns_RequestSyntax"></a>

```
GET /jobs/{{name}}/jobRuns?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobRuns_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListJobRuns_RequestSyntax) **   <a name="databrew-ListJobRuns-request-uri-MaxResults"></a>
The maximum number of results to return in this request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [name](#API_ListJobRuns_RequestSyntax) **   <a name="databrew-ListJobRuns-request-uri-Name"></a>
The name of the job.
Length Constraints: Minimum length of 1. Maximum length of 240.
Required: Yes

 ** [NextToken](#API_ListJobRuns_RequestSyntax) **   <a name="databrew-ListJobRuns-request-uri-NextToken"></a>
The token returned by a previous call to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Request Body
<a name="API_ListJobRuns_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobRuns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "JobRuns": [
      {
         "Attempt": number,
         "CompletedOn": number,
         "DatabaseOutputs": [
            {
               "DatabaseOptions": {
                  "TableName": "string",
                  "TempDirectory": {
                     "Bucket": "string",
                     "BucketOwner": "string",
                     "Key": "string"
                  }
               },
               "DatabaseOutputMode": "string",
               "GlueConnectionName": "string"
            }
         ],
         "DataCatalogOutputs": [
            {
               "CatalogId": "string",
               "DatabaseName": "string",
               "DatabaseOptions": {
                  "TableName": "string",
                  "TempDirectory": {
                     "Bucket": "string",
                     "BucketOwner": "string",
                     "Key": "string"
                  }
               },
               "Overwrite": boolean,
               "S3Options": {
                  "Location": {
                     "Bucket": "string",
                     "BucketOwner": "string",
                     "Key": "string"
                  }
               },
               "TableName": "string"
            }
         ],
         "DatasetName": "string",
         "ErrorMessage": "string",
         "ExecutionTime": number,
         "JobName": "string",
         "JobSample": {
            "Mode": "string",
            "Size": number
         },
         "LogGroupName": "string",
         "LogSubscription": "string",
         "Outputs": [
            {
               "CompressionFormat": "string",
               "Format": "string",
               "FormatOptions": {
                  "Csv": {
                     "Delimiter": "string"
                  }
               },
               "Location": {
                  "Bucket": "string",
                  "BucketOwner": "string",
                  "Key": "string"
               },
               "MaxOutputFiles": number,
               "Overwrite": boolean,
               "PartitionColumns": [ "string" ]
            }
         ],
         "RecipeReference": {
            "Name": "string",
            "RecipeVersion": "string"
         },
         "RunId": "string",
         "StartedBy": "string",
         "StartedOn": number,
         "State": "string",
         "ValidationConfigurations": [
            {
               "RulesetArn": "string",
               "ValidationMode": "string"
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListJobRuns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobRuns](#API_ListJobRuns_ResponseSyntax) **   <a name="databrew-ListJobRuns-response-JobRuns"></a>
A list of job runs that have occurred for the specified job.
Type: Array of [JobRun](API_JobRun.md) objects

 ** [NextToken](#API_ListJobRuns_ResponseSyntax) **   <a name="databrew-ListJobRuns-response-NextToken"></a>
A token that you can use in a subsequent call to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListJobRuns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListJobRuns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/ListJobRuns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/ListJobRuns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ListJobRuns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/ListJobRuns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ListJobRuns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/ListJobRuns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/ListJobRuns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/ListJobRuns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/ListJobRuns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ListJobRuns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

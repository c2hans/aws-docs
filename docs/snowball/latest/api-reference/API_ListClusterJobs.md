---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListClusterJobs.html
---

# ListClusterJobs
<a name="API_ListClusterJobs"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Returns an array of `JobListEntry` objects of the specified length. Each `JobListEntry` object is for a job in the specified cluster and contains a job's state, a job's ID, and other information.

## Request Syntax
<a name="API_ListClusterJobs_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListClusterJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ListClusterJobs_RequestSyntax) **   <a name="Snowball-ListClusterJobs-request-ClusterId"></a>
The 39-character ID for the cluster that you want to list, for example `CID123e4567-e89b-12d3-a456-426655440000`.
Type: String
Length Constraints: Fixed length of 39.
Pattern: `CID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [MaxResults](#API_ListClusterJobs_RequestSyntax) **   <a name="Snowball-ListClusterJobs-request-MaxResults"></a>
The number of `JobListEntry` objects to return.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListClusterJobs_RequestSyntax) **   <a name="Snowball-ListClusterJobs-request-NextToken"></a>
HTTP requests are stateless. To identify what object comes "next" in the list of `JobListEntry` objects, you have the option of specifying `NextToken` as the starting point for your returned list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListClusterJobs_ResponseSyntax"></a>

```
{
   "JobListEntries": [
      {
         "CreationDate": number,
         "Description": "string",
         "IsMaster": boolean,
         "JobId": "string",
         "JobState": "string",
         "JobType": "string",
         "SnowballType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListClusterJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobListEntries](#API_ListClusterJobs_ResponseSyntax) **   <a name="Snowball-ListClusterJobs-response-JobListEntries"></a>
Each `JobListEntry` object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of export jobs.
Type: Array of [JobListEntry](API_JobListEntry.md) objects

 ** [NextToken](#API_ListClusterJobs_ResponseSyntax) **   <a name="Snowball-ListClusterJobs-response-NextToken"></a>
HTTP requests are stateless. If you use the automatically generated `NextToken` value in your next `ListClusterJobsResult` call, your list of returned jobs will start from this point in the array.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_ListClusterJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The `NextToken` string was altered unexpectedly, and the operation has stopped. Run the operation without changing the `NextToken` string, and try again.
HTTP Status Code: 400

 ** InvalidResourceException **
The specified resource can't be found. Check the information you provided in your last request, and try again.
 ** ResourceType **
The provided resource value is invalid.
HTTP Status Code: 400

## See Also
<a name="API_ListClusterJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/ListClusterJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/ListClusterJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ListClusterJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/ListClusterJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ListClusterJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/ListClusterJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/ListClusterJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/ListClusterJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/ListClusterJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ListClusterJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

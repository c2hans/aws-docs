---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListJobs.html
---

# ListJobs
<a name="API_ListJobs"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Returns an array of `JobListEntry` objects of the specified length. Each `JobListEntry` object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of export jobs. Calling this API action in one of the US regions will return jobs from the list of all jobs associated with this account in all US regions.

## Request Syntax
<a name="API_ListJobs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListJobs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListJobs_RequestSyntax) **   <a name="Snowball-ListJobs-request-MaxResults"></a>
The number of `JobListEntry` objects to return.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListJobs_RequestSyntax) **   <a name="Snowball-ListJobs-request-NextToken"></a>
HTTP requests are stateless. To identify what object comes "next" in the list of `JobListEntry` objects, you have the option of specifying `NextToken` as the starting point for your returned list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListJobs_ResponseSyntax"></a>

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
<a name="API_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobListEntries](#API_ListJobs_ResponseSyntax) **   <a name="Snowball-ListJobs-response-JobListEntries"></a>
Each `JobListEntry` object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of export jobs.
Type: Array of [JobListEntry](API_JobListEntry.md) objects

 ** [NextToken](#API_ListJobs_ResponseSyntax) **   <a name="Snowball-ListJobs-response-NextToken"></a>
HTTP requests are stateless. If you use this automatically generated `NextToken` value in your next `ListJobs` call, your returned `JobListEntry` objects will start from this point in the array.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_ListJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNextTokenException **
The `NextToken` string was altered unexpectedly, and the operation has stopped. Run the operation without changing the `NextToken` string, and try again.
HTTP Status Code: 400

## See Also
<a name="API_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/ListJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/ListJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/ListJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/ListJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/ListJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/ListJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/ListJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/ListJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/ListJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/ListJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Snowball. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snowball` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

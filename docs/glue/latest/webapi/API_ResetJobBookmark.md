---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ResetJobBookmark.html
---

# ResetJobBookmark
<a name="API_ResetJobBookmark"></a>

Resets a bookmark entry.

For more information about enabling and using job bookmarks, see:
+  [Tracking processed data using job bookmarks](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html)
+  [Job parameters used by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html)
+  [Job structure](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html#aws-glue-api-jobs-job-Job)

## Request Syntax
<a name="API_ResetJobBookmark_RequestSyntax"></a>

```
{
   "JobName": "{{string}}",
   "RunId": "{{string}}"
}
```

## Request Parameters
<a name="API_ResetJobBookmark_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobName](#API_ResetJobBookmark_RequestSyntax) **   <a name="Glue-ResetJobBookmark-request-JobName"></a>
The name of the job in question.
Type: String
Required: Yes

 ** [RunId](#API_ResetJobBookmark_RequestSyntax) **   <a name="Glue-ResetJobBookmark-request-RunId"></a>
The unique run identifier associated with this job run.
Type: String
Required: No

## Response Syntax
<a name="API_ResetJobBookmark_ResponseSyntax"></a>

```
{
   "JobBookmarkEntry": {
      "Attempt": number,
      "JobBookmark": "string",
      "JobName": "string",
      "PreviousRunId": "string",
      "Run": number,
      "RunId": "string",
      "Version": number
   }
}
```

## Response Elements
<a name="API_ResetJobBookmark_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobBookmarkEntry](#API_ResetJobBookmark_ResponseSyntax) **   <a name="Glue-ResetJobBookmark-response-JobBookmarkEntry"></a>
The reset bookmark entry.
Type: [JobBookmarkEntry](API_JobBookmarkEntry.md) object

## Errors
<a name="API_ResetJobBookmark_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_ResetJobBookmark_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/ResetJobBookmark)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/ResetJobBookmark)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ResetJobBookmark)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/ResetJobBookmark)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ResetJobBookmark)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/ResetJobBookmark)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/ResetJobBookmark)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/ResetJobBookmark)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/ResetJobBookmark)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ResetJobBookmark)

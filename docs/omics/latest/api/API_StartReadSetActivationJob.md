---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_StartReadSetActivationJob.html
---

# StartReadSetActivationJob
<a name="API_StartReadSetActivationJob"></a>

Activates an archived read set and returns its metadata in a JSON formatted output. AWS HealthOmics automatically archives unused read sets after 30 days. To monitor the status of your read set activation job, use the `GetReadSetActivationJob` operation.

To learn more, see [Activating read sets](https://docs.aws.amazon.com/omics/latest/dev/activating-read-sets.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_StartReadSetActivationJob_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/activationjob HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "sources": [
      {
         "readSetId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_StartReadSetActivationJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sequenceStoreId](#API_StartReadSetActivationJob_RequestSyntax) **   <a name="omics-StartReadSetActivationJob-request-uri-sequenceStoreId"></a>
The read set's sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_StartReadSetActivationJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartReadSetActivationJob_RequestSyntax) **   <a name="omics-StartReadSetActivationJob-request-clientToken"></a>
To ensure that jobs don't run multiple times, specify a unique token for each job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [sources](#API_StartReadSetActivationJob_RequestSyntax) **   <a name="omics-StartReadSetActivationJob-request-sources"></a>
The job's source files.
Type: Array of [StartReadSetActivationJobSourceItem](API_StartReadSetActivationJobSourceItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_StartReadSetActivationJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "id": "string",
   "sequenceStoreId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_StartReadSetActivationJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_StartReadSetActivationJob_ResponseSyntax) **   <a name="omics-StartReadSetActivationJob-response-creationTime"></a>
When the job was created.
Type: Timestamp

 ** [id](#API_StartReadSetActivationJob_ResponseSyntax) **   <a name="omics-StartReadSetActivationJob-response-id"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [sequenceStoreId](#API_StartReadSetActivationJob_ResponseSyntax) **   <a name="omics-StartReadSetActivationJob-response-sequenceStoreId"></a>
The read set's sequence store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [status](#API_StartReadSetActivationJob_ResponseSyntax) **   <a name="omics-StartReadSetActivationJob-response-status"></a>
The job's status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | CANCELLING | CANCELLED | FAILED | COMPLETED | COMPLETED_WITH_FAILURES`

## Errors
<a name="API_StartReadSetActivationJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartReadSetActivationJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/StartReadSetActivationJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/StartReadSetActivationJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/StartReadSetActivationJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/StartReadSetActivationJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/StartReadSetActivationJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/StartReadSetActivationJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/StartReadSetActivationJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/StartReadSetActivationJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/StartReadSetActivationJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/StartReadSetActivationJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

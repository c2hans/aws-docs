---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoverySnapshots.html
---

# DescribeRecoverySnapshots
<a name="API_DescribeRecoverySnapshots"></a>

Lists all Recovery Snapshots for a single Source Server.

## Request Syntax
<a name="API_DescribeRecoverySnapshots_RequestSyntax"></a>

```
POST /DescribeRecoverySnapshots HTTP/1.1
Content-type: application/json

{
   "filters": {
      "fromDateTime": "{{string}}",
      "toDateTime": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "order": "{{string}}",
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeRecoverySnapshots_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeRecoverySnapshots_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_DescribeRecoverySnapshots_RequestSyntax) **   <a name="drs-DescribeRecoverySnapshots-request-filters"></a>
A set of filters by which to return Recovery Snapshots.
Type: [DescribeRecoverySnapshotsRequestFilters](API_DescribeRecoverySnapshotsRequestFilters.md) object
Required: No

 ** [maxResults](#API_DescribeRecoverySnapshots_RequestSyntax) **   <a name="drs-DescribeRecoverySnapshots-request-maxResults"></a>
Maximum number of Recovery Snapshots to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [nextToken](#API_DescribeRecoverySnapshots_RequestSyntax) **   <a name="drs-DescribeRecoverySnapshots-request-nextToken"></a>
The token of the next Recovery Snapshot to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [order](#API_DescribeRecoverySnapshots_RequestSyntax) **   <a name="drs-DescribeRecoverySnapshots-request-order"></a>
The sorted ordering by which to return Recovery Snapshots.
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** [sourceServerID](#API_DescribeRecoverySnapshots_RequestSyntax) **   <a name="drs-DescribeRecoverySnapshots-request-sourceServerID"></a>
Filter Recovery Snapshots by Source Server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_DescribeRecoverySnapshots_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "ebsSnapshots": [ "string" ],
         "expectedTimestamp": "string",
         "snapshotID": "string",
         "sourceServerID": "string",
         "timestamp": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeRecoverySnapshots_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_DescribeRecoverySnapshots_ResponseSyntax) **   <a name="drs-DescribeRecoverySnapshots-response-items"></a>
An array of Recovery Snapshots.
Type: Array of [RecoverySnapshot](API_RecoverySnapshot.md) objects

 ** [nextToken](#API_DescribeRecoverySnapshots_ResponseSyntax) **   <a name="drs-DescribeRecoverySnapshots-response-nextToken"></a>
The token of the next Recovery Snapshot to retrieve.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_DescribeRecoverySnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRecoverySnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DescribeRecoverySnapshots)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DescribeRecoverySnapshots)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeRecoverySnapshots)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DescribeRecoverySnapshots)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeRecoverySnapshots)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DescribeRecoverySnapshots)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DescribeRecoverySnapshots)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DescribeRecoverySnapshots)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DescribeRecoverySnapshots)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeRecoverySnapshots)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

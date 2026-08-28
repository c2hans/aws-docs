---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListRecoveryPoints.html
---

# ListRecoveryPoints
<a name="API_ListRecoveryPoints"></a>

Returns an array of recovery points.

## Request Syntax
<a name="API_ListRecoveryPoints_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "maxResults": {{number}},
   "namespaceArn": "{{string}}",
   "namespaceName": "{{string}}",
   "nextToken": "{{string}}",
   "startTime": {{number}}
}
```

## Request Parameters
<a name="API_ListRecoveryPoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_ListRecoveryPoints_RequestSyntax) **   <a name="redshiftserverless-ListRecoveryPoints-request-endTime"></a>
The time when creation of the recovery point finished.
Type: Timestamp
Required: No

 ** [maxResults](#API_ListRecoveryPoints_RequestSyntax) **   <a name="redshiftserverless-ListRecoveryPoints-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to display the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [namespaceArn](#API_ListRecoveryPoints_RequestSyntax) **   <a name="redshiftserverless-ListRecoveryPoints-request-namespaceArn"></a>
The Amazon Resource Name (ARN) of the namespace from which to list recovery points.
Type: String
Required: No

 ** [namespaceName](#API_ListRecoveryPoints_RequestSyntax) **   <a name="redshiftserverless-ListRecoveryPoints-request-namespaceName"></a>
The name of the namespace to list recovery points for.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

 ** [nextToken](#API_ListRecoveryPoints_RequestSyntax) **   <a name="redshiftserverless-ListRecoveryPoints-request-nextToken"></a>
If your initial `ListRecoveryPoints` operation returns a `nextToken`, you can include the returned `nextToken` in following `ListRecoveryPoints` operations, which returns results in the next page.
Type: String
Required: No

 ** [startTime](#API_ListRecoveryPoints_RequestSyntax) **   <a name="redshiftserverless-ListRecoveryPoints-request-startTime"></a>
The time when the recovery point's creation was initiated.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_ListRecoveryPoints_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "recoveryPoints": [
      {
         "namespaceArn": "string",
         "namespaceName": "string",
         "recoveryPointCreateTime": "string",
         "recoveryPointId": "string",
         "totalSizeInMegaBytes": number,
         "workgroupName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRecoveryPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRecoveryPoints_ResponseSyntax) **   <a name="redshiftserverless-ListRecoveryPoints-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

 ** [recoveryPoints](#API_ListRecoveryPoints_ResponseSyntax) **   <a name="redshiftserverless-ListRecoveryPoints-response-recoveryPoints"></a>
The returned recovery point objects.
Type: Array of [RecoveryPoint](API_RecoveryPoint.md) objects

## Errors
<a name="API_ListRecoveryPoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListRecoveryPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListRecoveryPoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListRecoveryPoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListRecoveryPoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListRecoveryPoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListRecoveryPoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListRecoveryPoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListRecoveryPoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListRecoveryPoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListRecoveryPoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListRecoveryPoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

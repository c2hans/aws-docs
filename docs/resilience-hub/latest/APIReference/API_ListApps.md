---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListApps.html
---

# ListApps
<a name="API_ListApps"></a>

Lists your AWS Resilience Hub applications.

**Note**
You can filter applications using only one filter at a time or without using any filter. If you try to filter applications using multiple filters, you will get the following error:
 `An error occurred (ValidationException) when calling the ListApps operation: Only one filter is supported for this operation.`

## Request Syntax
<a name="API_ListApps_RequestSyntax"></a>

```
GET /list-apps?appArn={{appArn}}&awsApplicationArn={{awsApplicationArn}}&fromLastAssessmentTime={{fromLastAssessmentTime}}&maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&reverseOrder={{reverseOrder}}&toLastAssessmentTime={{toLastAssessmentTime}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApps_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appArn](#API_ListApps_RequestSyntax) **   <a name="resiliencehub-ListApps-request-uri-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [awsApplicationArn](#API_ListApps_RequestSyntax) **   <a name="resiliencehub-ListApps-request-uri-awsApplicationArn"></a>
Amazon Resource Name (ARN) of AWS Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [fromLastAssessmentTime](#API_ListApps_RequestSyntax) **   <a name="resiliencehub-ListApps-request-uri-fromLastAssessmentTime"></a>
Lower limit of the range that is used to filter applications based on their last assessment times.

 ** [maxResults](#API_ListApps_RequestSyntax) **   <a name="resiliencehub-ListApps-request-uri-maxResults"></a>
Maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [name](#API_ListApps_RequestSyntax) **   <a name="resiliencehub-ListApps-request-uri-name"></a>
The name for the one of the listed applications.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`

 ** [nextToken](#API_ListApps_RequestSyntax) **   <a name="resiliencehub-ListApps-request-uri-nextToken"></a>
Null, or the token from a previous call to get the next set of results.
Pattern: `\S{1,2000}`

 ** [reverseOrder](#API_ListApps_RequestSyntax) **   <a name="resiliencehub-ListApps-request-uri-reverseOrder"></a>
The application list is sorted based on the values of `lastAppComplianceEvaluationTime` field. By default, application list is sorted in ascending order. To sort the application list in descending order, set this field to `True`.

 ** [toLastAssessmentTime](#API_ListApps_RequestSyntax) **   <a name="resiliencehub-ListApps-request-uri-toLastAssessmentTime"></a>
Upper limit of the range that is used to filter the applications based on their last assessment times.

## Request Body
<a name="API_ListApps_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApps_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appSummaries": [
      {
         "appArn": "string",
         "assessmentSchedule": "string",
         "awsApplicationArn": "string",
         "complianceStatus": "string",
         "creationTime": number,
         "description": "string",
         "driftStatus": "string",
         "lastAppComplianceEvaluationTime": number,
         "name": "string",
         "resiliencyScore": number,
         "rpoInSecs": number,
         "rtoInSecs": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApps_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appSummaries](#API_ListApps_ResponseSyntax) **   <a name="resiliencehub-ListApps-response-appSummaries"></a>
Summaries for the AWS Resilience Hub application.
Type: Array of [AppSummary](API_AppSummary.md) objects

 ** [nextToken](#API_ListApps_ResponseSyntax) **   <a name="resiliencehub-ListApps-response-nextToken"></a>
Token for the next set of results, or null if there are no more results.
Type: String
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListApps_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Resilience Hub service.
HTTP Status Code: 500

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListApps_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/ListApps)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/ListApps)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ListApps)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/ListApps)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ListApps)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/ListApps)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/ListApps)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/ListApps)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/ListApps)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ListApps)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

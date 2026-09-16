---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListAppAssessments.html
---

# ListAppAssessments
<a name="API_ListAppAssessments"></a>

Lists the assessments for an AWS Resilience Hub application. You can use request parameters to refine the results for the response object.

## Request Syntax
<a name="API_ListAppAssessments_RequestSyntax"></a>

```
GET /list-app-assessments?appArn={{appArn}}&assessmentName={{assessmentName}}&assessmentStatus={{assessmentStatus}}&complianceStatus={{complianceStatus}}&invoker={{invoker}}&maxResults={{maxResults}}&nextToken={{nextToken}}&reverseOrder={{reverseOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAppAssessments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appArn](#API_ListAppAssessments_RequestSyntax) **   <a name="resiliencehub-ListAppAssessments-request-uri-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [assessmentName](#API_ListAppAssessments_RequestSyntax) **   <a name="resiliencehub-ListAppAssessments-request-uri-assessmentName"></a>
The name for the assessment.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`

 ** [assessmentStatus](#API_ListAppAssessments_RequestSyntax) **   <a name="resiliencehub-ListAppAssessments-request-uri-assessmentStatus"></a>
The current status of the assessment for the resiliency policy.
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `Pending | InProgress | Failed | Success`

 ** [complianceStatus](#API_ListAppAssessments_RequestSyntax) **   <a name="resiliencehub-ListAppAssessments-request-uri-complianceStatus"></a>
The current status of compliance for the resiliency policy.
Valid Values: `PolicyBreached | PolicyMet | NotApplicable | MissingPolicy`

 ** [invoker](#API_ListAppAssessments_RequestSyntax) **   <a name="resiliencehub-ListAppAssessments-request-uri-invoker"></a>
Specifies the entity that invoked a specific assessment, either a `User` or the `System`.
Valid Values: `User | System`

 ** [maxResults](#API_ListAppAssessments_RequestSyntax) **   <a name="resiliencehub-ListAppAssessments-request-uri-maxResults"></a>
Maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAppAssessments_RequestSyntax) **   <a name="resiliencehub-ListAppAssessments-request-uri-nextToken"></a>
Null, or the token from a previous call to get the next set of results.
Pattern: `\S{1,2000}`

 ** [reverseOrder](#API_ListAppAssessments_RequestSyntax) **   <a name="resiliencehub-ListAppAssessments-request-uri-reverseOrder"></a>
The default is to sort by ascending **startTime**. To sort by descending **startTime**, set reverseOrder to `true`.

## Request Body
<a name="API_ListAppAssessments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAppAssessments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assessmentSummaries": [
      {
         "appArn": "string",
         "appVersion": "string",
         "assessmentArn": "string",
         "assessmentName": "string",
         "assessmentStatus": "string",
         "complianceStatus": "string",
         "cost": {
            "amount": number,
            "currency": "string",
            "frequency": "string"
         },
         "driftStatus": "string",
         "endTime": number,
         "invoker": "string",
         "message": "string",
         "resiliencyScore": number,
         "startTime": number,
         "versionName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAppAssessments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentSummaries](#API_ListAppAssessments_ResponseSyntax) **   <a name="resiliencehub-ListAppAssessments-response-assessmentSummaries"></a>
The summaries for the specified assessments, returned as an object. This object includes application versions, associated Amazon Resource Numbers (ARNs), cost, messages, resiliency scores, and more.
Type: Array of [AppAssessmentSummary](API_AppAssessmentSummary.md) objects

 ** [nextToken](#API_ListAppAssessments_ResponseSyntax) **   <a name="resiliencehub-ListAppAssessments-response-nextToken"></a>
Token for the next set of results, or null if there are no more results.
Type: String
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListAppAssessments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Resilience Hub service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This exception occurs when the specified resource could not be found.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 404

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListAppAssessments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/ListAppAssessments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/ListAppAssessments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ListAppAssessments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/ListAppAssessments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ListAppAssessments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/ListAppAssessments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/ListAppAssessments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/ListAppAssessments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/ListAppAssessments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ListAppAssessments)

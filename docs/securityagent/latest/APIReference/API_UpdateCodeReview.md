---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_UpdateCodeReview.html
---

# UpdateCodeReview
<a name="API_UpdateCodeReview"></a>

Updates an existing code review configuration.

## Request Syntax
<a name="API_UpdateCodeReview_RequestSyntax"></a>

```
POST /UpdateCodeReview HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "assets": {
      "actors": [
         {
            "authentication": {
               "providerType": "{{string}}",
               "value": "{{string}}"
            },
            "description": "{{string}}",
            "enableEmailMfa": {{boolean}},
            "identifier": "{{string}}",
            "mfaForwardingAddress": "{{string}}",
            "uris": [ "{{string}}" ]
         }
      ],
      "documents": [
         {
            "artifactId": "{{string}}",
            "integratedDocument": {
               "integrationId": "{{string}}",
               "resourceId": "{{string}}"
            },
            "s3Location": "{{string}}"
         }
      ],
      "endpoints": [
         {
            "uri": "{{string}}"
         }
      ],
      "integratedRepositories": [
         {
            "branch": "{{string}}",
            "integrationId": "{{string}}",
            "providerResourceId": "{{string}}"
         }
      ],
      "sourceCode": [
         {
            "s3Location": "{{string}}"
         }
      ]
   },
   "codeRemediationStrategy": "{{string}}",
   "codeReviewId": "{{string}}",
   "logConfig": {
      "logGroup": "{{string}}",
      "logStream": "{{string}}"
   },
   "maxTaskHours": {{number}},
   "serviceRole": "{{string}}",
   "title": "{{string}}",
   "validationMode": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCodeReview_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateCodeReview_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_UpdateCodeReview_RequestSyntax) **   <a name="securityagent-UpdateCodeReview-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the code review.
Type: String
Required: Yes

 ** [assets](#API_UpdateCodeReview_RequestSyntax) **   <a name="securityagent-UpdateCodeReview-request-assets"></a>
The updated assets for the code review.
Type: [Assets](API_Assets.md) object
Required: No

 ** [codeRemediationStrategy](#API_UpdateCodeReview_RequestSyntax) **   <a name="securityagent-UpdateCodeReview-request-codeRemediationStrategy"></a>
The updated code remediation strategy for the code review.
Type: String
Valid Values: `AUTOMATIC | DISABLED`
Required: No

 ** [codeReviewId](#API_UpdateCodeReview_RequestSyntax) **   <a name="securityagent-UpdateCodeReview-request-codeReviewId"></a>
The unique identifier of the code review to update.
Type: String
Required: Yes

 ** [logConfig](#API_UpdateCodeReview_RequestSyntax) **   <a name="securityagent-UpdateCodeReview-request-logConfig"></a>
The updated CloudWatch Logs configuration for the code review.
Type: [CloudWatchLog](API_CloudWatchLog.md) object
Required: No

 ** [maxTaskHours](#API_UpdateCodeReview_RequestSyntax) **   <a name="securityagent-UpdateCodeReview-request-maxTaskHours"></a>
The updated maximum number of billable task hours allowed for jobs started from this code review.
Type: Double
Required: No

 ** [serviceRole](#API_UpdateCodeReview_RequestSyntax) **   <a name="securityagent-UpdateCodeReview-request-serviceRole"></a>
The updated IAM service role for the code review.
Type: String
Required: No

 ** [title](#API_UpdateCodeReview_RequestSyntax) **   <a name="securityagent-UpdateCodeReview-request-title"></a>
The updated title of the code review.
Type: String
Required: No

 ** [validationMode](#API_UpdateCodeReview_RequestSyntax) **   <a name="securityagent-UpdateCodeReview-request-validationMode"></a>
The updated validation mode for the code review. Valid values are SIMULATED and DISABLED.
Type: String
Valid Values: `DISABLED | SIMULATED`
Required: No

## Response Syntax
<a name="API_UpdateCodeReview_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaceId": "string",
   "assets": {
      "actors": [
         {
            "authentication": {
               "providerType": "string",
               "value": "string"
            },
            "description": "string",
            "enableEmailMfa": boolean,
            "identifier": "string",
            "mfaForwardingAddress": "string",
            "uris": [ "string" ]
         }
      ],
      "documents": [
         {
            "artifactId": "string",
            "integratedDocument": {
               "integrationId": "string",
               "resourceId": "string"
            },
            "s3Location": "string"
         }
      ],
      "endpoints": [
         {
            "uri": "string"
         }
      ],
      "integratedRepositories": [
         {
            "branch": "string",
            "integrationId": "string",
            "providerResourceId": "string"
         }
      ],
      "sourceCode": [
         {
            "s3Location": "string"
         }
      ]
   },
   "codeRemediationStrategy": "string",
   "codeReviewId": "string",
   "createdAt": "string",
   "logConfig": {
      "logGroup": "string",
      "logStream": "string"
   },
   "maxTaskHours": number,
   "serviceRole": "string",
   "title": "string",
   "updatedAt": "string",
   "validationMode": "string"
}
```

## Response Elements
<a name="API_UpdateCodeReview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceId](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-agentSpaceId"></a>
The unique identifier of the agent space that contains the code review.
Type: String

 ** [assets](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-assets"></a>
The assets included in the code review.
Type: [Assets](API_Assets.md) object

 ** [codeRemediationStrategy](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-codeRemediationStrategy"></a>
The code remediation strategy for the code review.
Type: String
Valid Values: `AUTOMATIC | DISABLED`

 ** [codeReviewId](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-codeReviewId"></a>
The unique identifier of the code review.
Type: String

 ** [createdAt](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-createdAt"></a>
The date and time the code review was created, in UTC format.
Type: Timestamp

 ** [logConfig](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-logConfig"></a>
The CloudWatch Logs configuration for the code review.
Type: [CloudWatchLog](API_CloudWatchLog.md) object

 ** [maxTaskHours](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-maxTaskHours"></a>
The maximum number of billable task hours configured for jobs started from this code review. Null if no budget cap is set.
Type: Double

 ** [serviceRole](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-serviceRole"></a>
The IAM service role used for the code review.
Type: String

 ** [title](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-title"></a>
The title of the code review.
Type: String

 ** [updatedAt](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-updatedAt"></a>
The date and time the code review was last updated, in UTC format.
Type: Timestamp

 ** [validationMode](#API_UpdateCodeReview_ResponseSyntax) **   <a name="securityagent-UpdateCodeReview-response-validationMode"></a>
The validation mode for the code review.
Type: String
Valid Values: `DISABLED | SIMULATED`

## Errors
<a name="API_UpdateCodeReview_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_UpdateCodeReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/UpdateCodeReview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/UpdateCodeReview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/UpdateCodeReview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/UpdateCodeReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/UpdateCodeReview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/UpdateCodeReview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/UpdateCodeReview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/UpdateCodeReview)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/UpdateCodeReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/UpdateCodeReview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

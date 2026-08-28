---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DeleteRecommendationTemplate.html
---

# DeleteRecommendationTemplate
<a name="API_DeleteRecommendationTemplate"></a>

Deletes a recommendation template. This is a destructive action that can't be undone.

## Request Syntax
<a name="API_DeleteRecommendationTemplate_RequestSyntax"></a>

```
POST /delete-recommendation-template HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "recommendationTemplateArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteRecommendationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteRecommendationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_DeleteRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-DeleteRecommendationTemplate-request-clientToken"></a>
Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [recommendationTemplateArn](#API_DeleteRecommendationTemplate_RequestSyntax) **   <a name="resiliencehub-DeleteRecommendationTemplate-request-recommendationTemplateArn"></a>
The Amazon Resource Name (ARN) for a recommendation template.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_DeleteRecommendationTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "recommendationTemplateArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteRecommendationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recommendationTemplateArn](#API_DeleteRecommendationTemplate_ResponseSyntax) **   <a name="resiliencehub-DeleteRecommendationTemplate-response-recommendationTemplateArn"></a>
The Amazon Resource Name (ARN) for a recommendation template.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [status](#API_DeleteRecommendationTemplate_ResponseSyntax) **   <a name="resiliencehub-DeleteRecommendationTemplate-response-status"></a>
Status of the action.
Type: String
Valid Values: `Pending | InProgress | Failed | Success`

## Errors
<a name="API_DeleteRecommendationTemplate_Errors"></a>

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
<a name="API_DeleteRecommendationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/DeleteRecommendationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/DeleteRecommendationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/DeleteRecommendationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/DeleteRecommendationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/DeleteRecommendationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/DeleteRecommendationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/DeleteRecommendationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/DeleteRecommendationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/DeleteRecommendationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/DeleteRecommendationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

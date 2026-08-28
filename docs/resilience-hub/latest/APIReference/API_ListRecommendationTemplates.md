---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListRecommendationTemplates.html
---

# ListRecommendationTemplates
<a name="API_ListRecommendationTemplates"></a>

Lists the recommendation templates for the AWS Resilience Hub applications.

## Request Syntax
<a name="API_ListRecommendationTemplates_RequestSyntax"></a>

```
GET /list-recommendation-templates?assessmentArn={{assessmentArn}}&maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&recommendationTemplateArn={{recommendationTemplateArn}}&reverseOrder={{reverseOrder}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRecommendationTemplates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentArn](#API_ListRecommendationTemplates_RequestSyntax) **   <a name="resiliencehub-ListRecommendationTemplates-request-uri-assessmentArn"></a>
Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app-assessment/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [maxResults](#API_ListRecommendationTemplates_RequestSyntax) **   <a name="resiliencehub-ListRecommendationTemplates-request-uri-maxResults"></a>
Maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [name](#API_ListRecommendationTemplates_RequestSyntax) **   <a name="resiliencehub-ListRecommendationTemplates-request-uri-name"></a>
The name for one of the listed recommendation templates.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`

 ** [nextToken](#API_ListRecommendationTemplates_RequestSyntax) **   <a name="resiliencehub-ListRecommendationTemplates-request-uri-nextToken"></a>
Null, or the token from a previous call to get the next set of results.
Pattern: `\S{1,2000}`

 ** [recommendationTemplateArn](#API_ListRecommendationTemplates_RequestSyntax) **   <a name="resiliencehub-ListRecommendationTemplates-request-uri-recommendationTemplateArn"></a>
The Amazon Resource Name (ARN) for a recommendation template.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [reverseOrder](#API_ListRecommendationTemplates_RequestSyntax) **   <a name="resiliencehub-ListRecommendationTemplates-request-uri-reverseOrder"></a>
The default is to sort by ascending **startTime**. To sort by descending **startTime**, set reverseOrder to `true`.

 ** [status](#API_ListRecommendationTemplates_RequestSyntax) **   <a name="resiliencehub-ListRecommendationTemplates-request-uri-status"></a>
Status of the action.
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `Pending | InProgress | Failed | Success`

## Request Body
<a name="API_ListRecommendationTemplates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRecommendationTemplates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "recommendationTemplates": [
      {
         "appArn": "string",
         "assessmentArn": "string",
         "endTime": number,
         "format": "string",
         "message": "string",
         "name": "string",
         "needsReplacements": boolean,
         "recommendationIds": [ "string" ],
         "recommendationTemplateArn": "string",
         "recommendationTypes": [ "string" ],
         "startTime": number,
         "status": "string",
         "tags": {
            "string" : "string"
         },
         "templatesLocation": {
            "bucket": "string",
            "prefix": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendationTemplates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRecommendationTemplates_ResponseSyntax) **   <a name="resiliencehub-ListRecommendationTemplates-response-nextToken"></a>
Token for the next set of results, or null if there are no more results.
Type: String
Pattern: `\S{1,2000}`

 ** [recommendationTemplates](#API_ListRecommendationTemplates_ResponseSyntax) **   <a name="resiliencehub-ListRecommendationTemplates-response-recommendationTemplates"></a>
The recommendation templates for the AWS Resilience Hub applications.
Type: Array of [RecommendationTemplate](API_RecommendationTemplate.md) objects

## Errors
<a name="API_ListRecommendationTemplates_Errors"></a>

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
<a name="API_ListRecommendationTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/ListRecommendationTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/ListRecommendationTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ListRecommendationTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/ListRecommendationTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ListRecommendationTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/ListRecommendationTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/ListRecommendationTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/ListRecommendationTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/ListRecommendationTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ListRecommendationTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

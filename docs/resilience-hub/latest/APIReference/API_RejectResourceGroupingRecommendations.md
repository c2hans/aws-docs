---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_RejectResourceGroupingRecommendations.html
---

# RejectResourceGroupingRecommendations
<a name="API_RejectResourceGroupingRecommendations"></a>

Rejects resource grouping recommendations.

## Request Syntax
<a name="API_RejectResourceGroupingRecommendations_RequestSyntax"></a>

```
POST /reject-resource-grouping-recommendations HTTP/1.1
Content-type: application/json

{
   "appArn": "{{string}}",
   "entries": [
      {
         "groupingRecommendationId": "{{string}}",
         "rejectionReason": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_RejectResourceGroupingRecommendations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RejectResourceGroupingRecommendations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appArn](#API_RejectResourceGroupingRecommendations_RequestSyntax) **   <a name="resiliencehub-RejectResourceGroupingRecommendations-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [entries](#API_RejectResourceGroupingRecommendations_RequestSyntax) **   <a name="resiliencehub-RejectResourceGroupingRecommendations-request-entries"></a>
List of resource grouping recommendations you have selected to exclude from your application.
Type: Array of [RejectGroupingRecommendationEntry](API_RejectGroupingRecommendationEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: Yes

## Response Syntax
<a name="API_RejectResourceGroupingRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "failedEntries": [
      {
         "errorMessage": "string",
         "groupingRecommendationId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_RejectResourceGroupingRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_RejectResourceGroupingRecommendations_ResponseSyntax) **   <a name="resiliencehub-RejectResourceGroupingRecommendations-response-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [failedEntries](#API_RejectResourceGroupingRecommendations_ResponseSyntax) **   <a name="resiliencehub-RejectResourceGroupingRecommendations-response-failedEntries"></a>
List of resource grouping recommendations that failed to get excluded in your application.
Type: Array of [FailedGroupingRecommendationEntry](API_FailedGroupingRecommendationEntry.md) objects

## Errors
<a name="API_RejectResourceGroupingRecommendations_Errors"></a>

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
<a name="API_RejectResourceGroupingRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/RejectResourceGroupingRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

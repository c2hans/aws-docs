---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ListResiliencyPolicies.html
---

# ListResiliencyPolicies
<a name="API_ListResiliencyPolicies"></a>

Lists the resiliency policies for the AWS Resilience Hub applications.

## Request Syntax
<a name="API_ListResiliencyPolicies_RequestSyntax"></a>

```
GET /list-resiliency-policies?maxResults={{maxResults}}&nextToken={{nextToken}}&policyName={{policyName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListResiliencyPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListResiliencyPolicies_RequestSyntax) **   <a name="resiliencehub-ListResiliencyPolicies-request-uri-maxResults"></a>
Maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListResiliencyPolicies_RequestSyntax) **   <a name="resiliencehub-ListResiliencyPolicies-request-uri-nextToken"></a>
Null, or the token from a previous call to get the next set of results.
Pattern: `\S{1,2000}`

 ** [policyName](#API_ListResiliencyPolicies_RequestSyntax) **   <a name="resiliencehub-ListResiliencyPolicies-request-uri-policyName"></a>
Name of the resiliency policy.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`

## Request Body
<a name="API_ListResiliencyPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListResiliencyPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "resiliencyPolicies": [
      {
         "creationTime": number,
         "dataLocationConstraint": "string",
         "estimatedCostTier": "string",
         "policy": {
            "string" : {
               "rpoInSecs": number,
               "rtoInSecs": number
            }
         },
         "policyArn": "string",
         "policyDescription": "string",
         "policyName": "string",
         "tags": {
            "string" : "string"
         },
         "tier": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListResiliencyPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListResiliencyPolicies_ResponseSyntax) **   <a name="resiliencehub-ListResiliencyPolicies-response-nextToken"></a>
Token for the next set of results, or null if there are no more results.
Type: String
Pattern: `\S{1,2000}`

 ** [resiliencyPolicies](#API_ListResiliencyPolicies_ResponseSyntax) **   <a name="resiliencehub-ListResiliencyPolicies-response-resiliencyPolicies"></a>
The resiliency policies for the AWS Resilience Hub applications.
Type: Array of [ResiliencyPolicy](API_ResiliencyPolicy.md) objects

## Errors
<a name="API_ListResiliencyPolicies_Errors"></a>

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
<a name="API_ListResiliencyPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/ListResiliencyPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/ListResiliencyPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ListResiliencyPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/ListResiliencyPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ListResiliencyPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/ListResiliencyPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/ListResiliencyPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/ListResiliencyPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/ListResiliencyPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ListResiliencyPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

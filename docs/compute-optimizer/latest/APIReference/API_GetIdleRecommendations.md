---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetIdleRecommendations.html
---

# GetIdleRecommendations
<a name="API_GetIdleRecommendations"></a>

Returns idle resource recommendations. AWS Compute Optimizer generates recommendations for idle resources that meet a specific set of requirements. For more information, see [Resource requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the * AWS Compute Optimizer User Guide*

## Request Syntax
<a name="API_GetIdleRecommendations_RequestSyntax"></a>

```
{
   "accountIds": [ "{{string}}" ],
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "orderBy": {
      "dimension": "{{string}}",
      "order": "{{string}}"
   },
   "resourceArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetIdleRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetIdleRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetIdleRecommendations-request-accountIds"></a>
Return the idle resource recommendations to the specified AWS account IDs.
If your account is the management account or the delegated administrator of an organization, use this parameter to return the idle resource recommendations to specific member accounts.
You can only specify one account ID per request.
Type: Array of strings
Required: No

 ** [filters](#API_GetIdleRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetIdleRecommendations-request-filters"></a>
An array of objects to specify a filter that returns a more specific list of idle resource recommendations.
Type: Array of [IdleRecommendationFilter](API_IdleRecommendationFilter.md) objects
Required: No

 ** [maxResults](#API_GetIdleRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetIdleRecommendations-request-maxResults"></a>
The maximum number of idle resource recommendations to return with a single request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [nextToken](#API_GetIdleRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetIdleRecommendations-request-nextToken"></a>
The token to advance to the next page of idle resource recommendations.
Type: String
Required: No

 ** [orderBy](#API_GetIdleRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetIdleRecommendations-request-orderBy"></a>
The order to sort the idle resource recommendations.
Type: [OrderBy](API_OrderBy.md) object
Required: No

 ** [resourceArns](#API_GetIdleRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetIdleRecommendations-request-resourceArns"></a>
The ARN that identifies the idle resource.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_GetIdleRecommendations_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "code": "string",
         "identifier": "string",
         "message": "string",
         "resourceType": "string"
      }
   ],
   "idleRecommendations": [
      {
         "accountId": "string",
         "finding": "string",
         "findingDescription": "string",
         "lastRefreshTimestamp": number,
         "lookBackPeriodInDays": number,
         "resourceArn": "string",
         "resourceId": "string",
         "resourceType": "string",
         "savingsOpportunity": {
            "estimatedMonthlySavings": {
               "currency": "string",
               "value": number
            },
            "savingsOpportunityPercentage": number
         },
         "savingsOpportunityAfterDiscounts": {
            "estimatedMonthlySavings": {
               "currency": "string",
               "value": number
            },
            "savingsOpportunityPercentage": number
         },
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "utilizationMetrics": [
            {
               "dimensions": [
                  {
                     "key": "string",
                     "values": [ "string" ]
                  }
               ],
               "name": "string",
               "statistic": "string",
               "value": number
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetIdleRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_GetIdleRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetIdleRecommendations-response-errors"></a>
An array of objects that describe errors of the request.
Type: Array of [IdleRecommendationError](API_IdleRecommendationError.md) objects

 ** [idleRecommendations](#API_GetIdleRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetIdleRecommendations-response-idleRecommendations"></a>
An array of objects that describe the idle resource recommendations.
Type: Array of [IdleRecommendation](API_IdleRecommendation.md) objects

 ** [nextToken](#API_GetIdleRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetIdleRecommendations-response-nextToken"></a>
The token to advance to the next page of idle resource recommendations.
Type: String

## Errors
<a name="API_GetIdleRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal error has occurred. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterValueException **
The value supplied for the input parameter is out of range or not valid.
HTTP Status Code: 400

 ** MissingAuthenticationToken **
The request must contain either a valid (registered) AWS access key ID or X.509 certificate.
HTTP Status Code: 400

 ** OptInRequiredException **
The account is not opted in to AWS Compute Optimizer.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed due to a temporary failure of the server.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_GetIdleRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetIdleRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetIdleRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetIdleRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetIdleRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetIdleRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetIdleRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetIdleRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetIdleRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetIdleRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetIdleRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

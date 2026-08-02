---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRecommendationPreferences.html
---

# GetRecommendationPreferences
<a name="API_GetRecommendationPreferences"></a>

Returns existing recommendation preferences, such as enhanced infrastructure metrics.

Use the `scope` parameter to specify which preferences to return. You can specify to return preferences for an organization, a specific account ID, or a specific EC2 instance or Auto Scaling group Amazon Resource Name (ARN).

For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_GetRecommendationPreferences_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceType": "{{string}}",
   "scope": {
      "name": "{{string}}",
      "value": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_GetRecommendationPreferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_GetRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-GetRecommendationPreferences-request-maxResults"></a>
The maximum number of recommendation preferences to return with a single request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-GetRecommendationPreferences-request-nextToken"></a>
The token to advance to the next page of recommendation preferences.
Type: String
Required: No

 ** [resourceType](#API_GetRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-GetRecommendationPreferences-request-resourceType"></a>
The target resource type of the recommendation preference for which to return preferences.
The `Ec2Instance` option encompasses standalone instances and instances that are part of Auto Scaling groups. The `AutoScalingGroup` option encompasses only instances that are part of an Auto Scaling group.
Type: String
Valid Values: `Ec2Instance | AutoScalingGroup | EbsVolume | EcsService | RdsDBInstance | AuroraDBClusterStorage`
Required: Yes

 ** [scope](#API_GetRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-GetRecommendationPreferences-request-scope"></a>
An object that describes the scope of the recommendation preference to return.
You can return recommendation preferences that are created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.
Type: [Scope](API_Scope.md) object
Required: No

## Response Syntax
<a name="API_GetRecommendationPreferences_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "recommendationPreferencesDetails": [
      {
         "enhancedInfrastructureMetrics": "string",
         "externalMetricsPreference": {
            "source": "string"
         },
         "inferredWorkloadTypes": "string",
         "lookBackPeriod": "string",
         "preferredResources": [
            {
               "effectiveIncludeList": [ "string" ],
               "excludeList": [ "string" ],
               "includeList": [ "string" ],
               "name": "string"
            }
         ],
         "resourceType": "string",
         "savingsEstimationMode": "string",
         "scope": {
            "name": "string",
            "value": "string"
         },
         "utilizationPreferences": [
            {
               "metricName": "string",
               "metricParameters": {
                  "headroom": "string",
                  "threshold": "string"
               }
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetRecommendationPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_GetRecommendationPreferences_ResponseSyntax) **   <a name="computeoptimizer-GetRecommendationPreferences-response-nextToken"></a>
The token to use to advance to the next page of recommendation preferences.
This value is null when there are no more pages of recommendation preferences to return.
Type: String

 ** [recommendationPreferencesDetails](#API_GetRecommendationPreferences_ResponseSyntax) **   <a name="computeoptimizer-GetRecommendationPreferences-response-recommendationPreferencesDetails"></a>
An array of objects that describe recommendation preferences.
Type: Array of [RecommendationPreferencesDetail](API_RecommendationPreferencesDetail.md) objects

## Errors
<a name="API_GetRecommendationPreferences_Errors"></a>

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
<a name="API_GetRecommendationPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetRecommendationPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetRecommendationPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetRecommendationPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetRecommendationPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetRecommendationPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetRecommendationPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetRecommendationPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetRecommendationPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetRecommendationPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetRecommendationPreferences)

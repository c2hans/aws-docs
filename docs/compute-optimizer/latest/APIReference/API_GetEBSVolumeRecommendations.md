---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEBSVolumeRecommendations.html
---

# GetEBSVolumeRecommendations
<a name="API_GetEBSVolumeRecommendations"></a>

Returns Amazon Elastic Block Store (Amazon EBS) volume recommendations.

 AWS Compute Optimizer generates recommendations for Amazon EBS volumes that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_GetEBSVolumeRecommendations_RequestSyntax"></a>

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
   "volumeArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetEBSVolumeRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetEBSVolumeRecommendations-request-accountIds"></a>
The ID of the AWS account for which to return volume recommendations.
If your account is the management account of an organization, use this parameter to specify the member account for which you want to return volume recommendations.
Only one account ID can be specified per request.
Type: Array of strings
Required: No

 ** [filters](#API_GetEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetEBSVolumeRecommendations-request-filters"></a>
An array of objects to specify a filter that returns a more specific list of volume recommendations.
Type: Array of [EBSFilter](API_EBSFilter.md) objects
Required: No

 ** [maxResults](#API_GetEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetEBSVolumeRecommendations-request-maxResults"></a>
The maximum number of volume recommendations to return with a single request.
To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetEBSVolumeRecommendations-request-nextToken"></a>
The token to advance to the next page of volume recommendations.
Type: String
Required: No

 ** [volumeArns](#API_GetEBSVolumeRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetEBSVolumeRecommendations-request-volumeArns"></a>
The Amazon Resource Name (ARN) of the volumes for which to return recommendations.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_GetEBSVolumeRecommendations_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "code": "string",
         "identifier": "string",
         "message": "string"
      }
   ],
   "nextToken": "string",
   "volumeRecommendations": [
      {
         "accountId": "string",
         "currentConfiguration": {
            "rootVolume": boolean,
            "volumeBaselineIOPS": number,
            "volumeBaselineThroughput": number,
            "volumeBurstIOPS": number,
            "volumeBurstThroughput": number,
            "volumeSize": number,
            "volumeType": "string"
         },
         "currentPerformanceRisk": "string",
         "effectiveRecommendationPreferences": {
            "lookBackPeriod": "string",
            "savingsEstimationMode": {
               "source": "string"
            }
         },
         "finding": "string",
         "lastRefreshTimestamp": number,
         "lookBackPeriodInDays": number,
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "utilizationMetrics": [
            {
               "name": "string",
               "statistic": "string",
               "value": number
            }
         ],
         "volumeArn": "string",
         "volumeRecommendationOptions": [
            {
               "configuration": {
                  "rootVolume": boolean,
                  "volumeBaselineIOPS": number,
                  "volumeBaselineThroughput": number,
                  "volumeBurstIOPS": number,
                  "volumeBurstThroughput": number,
                  "volumeSize": number,
                  "volumeType": "string"
               },
               "performanceRisk": number,
               "rank": number,
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
               }
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetEBSVolumeRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_GetEBSVolumeRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetEBSVolumeRecommendations-response-errors"></a>
An array of objects that describe errors of the request.
For example, an error is returned if you request recommendations for an unsupported volume.
Type: Array of [GetRecommendationError](API_GetRecommendationError.md) objects

 ** [nextToken](#API_GetEBSVolumeRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetEBSVolumeRecommendations-response-nextToken"></a>
The token to use to advance to the next page of volume recommendations.
This value is null when there are no more pages of volume recommendations to return.
Type: String

 ** [volumeRecommendations](#API_GetEBSVolumeRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetEBSVolumeRecommendations-response-volumeRecommendations"></a>
An array of objects that describe volume recommendations.
Type: Array of [VolumeRecommendation](API_VolumeRecommendation.md) objects

## Errors
<a name="API_GetEBSVolumeRecommendations_Errors"></a>

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
<a name="API_GetEBSVolumeRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetEBSVolumeRecommendations)

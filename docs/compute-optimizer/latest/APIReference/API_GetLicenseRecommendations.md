---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetLicenseRecommendations.html
---

# GetLicenseRecommendations
<a name="API_GetLicenseRecommendations"></a>

Returns license recommendations for Amazon EC2 instances that run on a specific license.

 AWS Compute Optimizer generates recommendations for licenses that meet a specific set of requirements. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_GetLicenseRecommendations_RequestSyntax"></a>

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
   "resourceArns": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetLicenseRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_GetLicenseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLicenseRecommendations-request-accountIds"></a>
The ID of the AWS account for which to return license recommendations.
If your account is the management account of an organization, use this parameter to specify the member account for which you want to return license recommendations.
Only one account ID can be specified per request.
Type: Array of strings
Required: No

 ** [filters](#API_GetLicenseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLicenseRecommendations-request-filters"></a>
 An array of objects to specify a filter that returns a more specific list of license recommendations.
Type: Array of [LicenseRecommendationFilter](API_LicenseRecommendationFilter.md) objects
Required: No

 ** [maxResults](#API_GetLicenseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLicenseRecommendations-request-maxResults"></a>
 The maximum number of license recommendations to return with a single request.
 To retrieve the remaining results, make another request with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_GetLicenseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLicenseRecommendations-request-nextToken"></a>
 The token to advance to the next page of license recommendations.
Type: String
Required: No

 ** [resourceArns](#API_GetLicenseRecommendations_RequestSyntax) **   <a name="computeoptimizer-GetLicenseRecommendations-request-resourceArns"></a>
 The ARN that identifies the Amazon EC2 instance.
 The following is the format of the ARN:
 `arn:aws:ec2:region:aws_account_id:instance/instance-id`
Type: Array of strings
Required: No

## Response Syntax
<a name="API_GetLicenseRecommendations_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "code": "string",
         "identifier": "string",
         "message": "string"
      }
   ],
   "licenseRecommendations": [
      {
         "accountId": "string",
         "currentLicenseConfiguration": {
            "instanceType": "string",
            "licenseEdition": "string",
            "licenseModel": "string",
            "licenseName": "string",
            "licenseVersion": "string",
            "metricsSource": [
               {
                  "provider": "string",
                  "providerArn": "string"
               }
            ],
            "numberOfCores": number,
            "operatingSystem": "string"
         },
         "finding": "string",
         "findingReasonCodes": [ "string" ],
         "lastRefreshTimestamp": number,
         "licenseRecommendationOptions": [
            {
               "licenseEdition": "string",
               "licenseModel": "string",
               "operatingSystem": "string",
               "rank": number,
               "savingsOpportunity": {
                  "estimatedMonthlySavings": {
                     "currency": "string",
                     "value": number
                  },
                  "savingsOpportunityPercentage": number
               }
            }
         ],
         "lookbackPeriodInDays": number,
         "resourceArn": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_GetLicenseRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_GetLicenseRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetLicenseRecommendations-response-errors"></a>
 An array of objects that describe errors of the request.
Type: Array of [GetRecommendationError](API_GetRecommendationError.md) objects

 ** [licenseRecommendations](#API_GetLicenseRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetLicenseRecommendations-response-licenseRecommendations"></a>
 An array of objects that describe license recommendations.
Type: Array of [LicenseRecommendation](API_LicenseRecommendation.md) objects

 ** [nextToken](#API_GetLicenseRecommendations_ResponseSyntax) **   <a name="computeoptimizer-GetLicenseRecommendations-response-nextToken"></a>
 The token to use to advance to the next page of license recommendations.
Type: String

## Errors
<a name="API_GetLicenseRecommendations_Errors"></a>

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
<a name="API_GetLicenseRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/GetLicenseRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/GetLicenseRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/GetLicenseRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/GetLicenseRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/GetLicenseRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/GetLicenseRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/GetLicenseRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/GetLicenseRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/GetLicenseRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/GetLicenseRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

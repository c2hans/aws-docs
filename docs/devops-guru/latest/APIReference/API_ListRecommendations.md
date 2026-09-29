---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListRecommendations.html
---

# ListRecommendations
<a name="API_ListRecommendations"></a>

**Note**
End of support notice: On September 30, 2027, AWS will end support for Amazon DevOps Guru. After September 30, 2027, you will no longer be able to access the Amazon DevOps Guru console or Amazon DevOps Guru resources. For more information, see [Amazon DevOps Guru end of support](https://docs.aws.amazon.com/devops-guru/latest/userguide/devops-guru-end-of-support.html).

 Returns a list of a specified insight's recommendations. Each recommendation includes a list of related metrics and a list of related events.

## Request Syntax
<a name="API_ListRecommendations_RequestSyntax"></a>

```
POST /recommendations HTTP/1.1
Content-type: application/json

{
   "AccountId": "{{string}}",
   "InsightId": "{{string}}",
   "Locale": "{{string}}",
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListRecommendations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListRecommendations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountId](#API_ListRecommendations_RequestSyntax) **   <a name="DevOpsGuru-ListRecommendations-request-AccountId"></a>
The ID of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [InsightId](#API_ListRecommendations_RequestSyntax) **   <a name="DevOpsGuru-ListRecommendations-request-InsightId"></a>
 The ID of the requested insight.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[\w-]*$`
Required: Yes

 ** [Locale](#API_ListRecommendations_RequestSyntax) **   <a name="DevOpsGuru-ListRecommendations-request-Locale"></a>
A locale that specifies the language to use for recommendations.
Type: String
Valid Values: `DE_DE | EN_US | EN_GB | ES_ES | FR_FR | IT_IT | JA_JP | KO_KR | PT_BR | ZH_CN | ZH_TW`
Required: No

 ** [NextToken](#API_ListRecommendations_RequestSyntax) **   <a name="DevOpsGuru-ListRecommendations-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

## Response Syntax
<a name="API_ListRecommendations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Recommendations": [
      {
         "Category": "string",
         "Description": "string",
         "Link": "string",
         "Name": "string",
         "Reason": "string",
         "RelatedAnomalies": [
            {
               "AnomalyId": "string",
               "Resources": [
                  {
                     "Name": "string",
                     "Type": "string"
                  }
               ],
               "SourceDetails": [
                  {
                     "CloudWatchMetrics": [
                        {
                           "MetricName": "string",
                           "Namespace": "string"
                        }
                     ]
                  }
               ]
            }
         ],
         "RelatedEvents": [
            {
               "Name": "string",
               "Resources": [
                  {
                     "Name": "string",
                     "Type": "string"
                  }
               ]
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_ListRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRecommendations_ResponseSyntax) **   <a name="DevOpsGuru-ListRecommendations-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [Recommendations](#API_ListRecommendations_ResponseSyntax) **   <a name="DevOpsGuru-ListRecommendations-response-Recommendations"></a>
 An array of the requested recommendations.
Type: Array of [Recommendation](API_Recommendation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_ListRecommendations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource could not be found
 ** ResourceId **
 The ID of the AWS resource that could not be found.
 ** ResourceType **
 The type of the AWS resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_ListRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/ListRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/ListRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ListRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/ListRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ListRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/ListRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/ListRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/ListRecommendations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/ListRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ListRecommendations)

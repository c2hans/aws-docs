---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_ListAccountActivities.html
---

# ListAccountActivities
<a name="API_freetier_ListAccountActivities"></a>

 Returns a list of activities that are available. This operation supports pagination and filtering by status.

## Request Syntax
<a name="API_freetier_ListAccountActivities_RequestSyntax"></a>

```
{
   "filterActivityStatuses": [ "{{string}}" ],
   "languageCode": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_freetier_ListAccountActivities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filterActivityStatuses](#API_freetier_ListAccountActivities_RequestSyntax) **   <a name="awscostmanagement-freetier_ListAccountActivities-request-filterActivityStatuses"></a>
 The activity status filter. This field can be used to filter the response by activities status.
Type: Array of strings
Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | EXPIRING`
Required: No

 ** [languageCode](#API_freetier_ListAccountActivities_RequestSyntax) **   <a name="awscostmanagement-freetier_ListAccountActivities-request-languageCode"></a>
 The language code used to return translated titles.
Type: String
Valid Values: `en-US | en-GB | id-ID | de-DE | es-ES | fr-FR | ja-JP | it-IT | pt-PT | ko-KR | zh-CN | zh-TW | tr-TR`
Required: No

 ** [maxResults](#API_freetier_ListAccountActivities_RequestSyntax) **   <a name="awscostmanagement-freetier_ListAccountActivities-request-maxResults"></a>
 The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_freetier_ListAccountActivities_RequestSyntax) **   <a name="awscostmanagement-freetier_ListAccountActivities-request-nextToken"></a>
 A token from a previous paginated response. If this is specified, the response includes records beginning from this token (inclusive), up to the number specified by `maxResults`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_freetier_ListAccountActivities_ResponseSyntax"></a>

```
{
   "activities": [
      {
         "activityId": "string",
         "reward": { ... },
         "status": "string",
         "title": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_freetier_ListAccountActivities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activities](#API_freetier_ListAccountActivities_ResponseSyntax) **   <a name="awscostmanagement-freetier_ListAccountActivities-response-activities"></a>
 A brief information about the activities.
Type: Array of [ActivitySummary](API_freetier_ActivitySummary.md) objects

 ** [nextToken](#API_freetier_ListAccountActivities_ResponseSyntax) **   <a name="awscostmanagement-freetier_ListAccountActivities-response-nextToken"></a>
 The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_freetier_ListAccountActivities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_freetier_ListAccountActivities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/freetier-2023-09-07/ListAccountActivities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/freetier-2023-09-07/ListAccountActivities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/freetier-2023-09-07/ListAccountActivities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/freetier-2023-09-07/ListAccountActivities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/freetier-2023-09-07/ListAccountActivities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/freetier-2023-09-07/ListAccountActivities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/freetier-2023-09-07/ListAccountActivities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/freetier-2023-09-07/ListAccountActivities)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/freetier-2023-09-07/ListAccountActivities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/freetier-2023-09-07/ListAccountActivities)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_ListCampaigns.html
---

# ListCampaigns
<a name="API_connect-outbound-campaigns_ListCampaigns"></a>

Lists outbound campaigns.

## Request Syntax
<a name="API_connect-outbound-campaigns_ListCampaigns_RequestSyntax"></a>

```
POST /campaigns-summary HTTP/1.1
Content-type: application/json

{
   "filters": {
      "instanceIdFilter": {
         "operator": "{{string}}",
         "value": "{{string}}"
      }
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_ListCampaigns_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-outbound-campaigns_ListCampaigns_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_connect-outbound-campaigns_ListCampaigns_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_ListCampaigns-request-filters"></a>
Filters the list of campaigns.
Type: [CampaignFilters](API_connect-outbound-campaigns_CampaignFilters.md) object
Required: No

 ** [maxResults](#API_connect-outbound-campaigns_ListCampaigns_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_ListCampaigns-request-maxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_connect-outbound-campaigns_ListCampaigns_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_ListCampaigns-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## Response Syntax
<a name="API_connect-outbound-campaigns_ListCampaigns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "campaignSummaryList": [
      {
         "arn": "string",
         "connectInstanceId": "string",
         "id": "string",
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_connect-outbound-campaigns_ListCampaigns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [campaignSummaryList](#API_connect-outbound-campaigns_ListCampaigns_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_ListCampaigns-response-campaignSummaryList"></a>
Summary information about the outbound campaigns.
Type: Array of [CampaignSummary](API_connect-outbound-campaigns_CampaignSummary.md) objects

 ** [nextToken](#API_connect-outbound-campaigns_ListCampaigns_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_ListCampaigns-response-nextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Errors
<a name="API_connect-outbound-campaigns_ListCampaigns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the outbound campaigns.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWSservice.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns_ListCampaigns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/ListCampaigns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/ListCampaigns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/ListCampaigns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/ListCampaigns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/ListCampaigns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/ListCampaigns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/ListCampaigns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/ListCampaigns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/ListCampaigns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/ListCampaigns)

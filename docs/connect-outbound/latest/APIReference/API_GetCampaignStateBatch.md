---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_GetCampaignStateBatch.html
---

# GetCampaignStateBatch
<a name="API_connect-outbound-campaigns_GetCampaignStateBatch"></a>

Returns the state of listed of outbound campaigns.

## Request Syntax
<a name="API_connect-outbound-campaigns_GetCampaignStateBatch_RequestSyntax"></a>

```
POST /campaigns-state HTTP/1.1
Content-type: application/json

{
   "campaignIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_GetCampaignStateBatch_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_connect-outbound-campaigns_GetCampaignStateBatch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [campaignIds](#API_connect-outbound-campaigns_GetCampaignStateBatch_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_GetCampaignStateBatch-request-campaignIds"></a>
The identifiers of the campaigns.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_connect-outbound-campaigns_GetCampaignStateBatch_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedRequests": [
      {
         "campaignId": "string",
         "failureCode": "string"
      }
   ],
   "successfulRequests": [
      {
         "campaignId": "string",
         "state": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-outbound-campaigns_GetCampaignStateBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedRequests](#API_connect-outbound-campaigns_GetCampaignStateBatch_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_GetCampaignStateBatch-response-failedRequests"></a>
Failed requests.
Type: Array of [FailedCampaignStateResponse](API_connect-outbound-campaigns_FailedCampaignStateResponse.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [successfulRequests](#API_connect-outbound-campaigns_GetCampaignStateBatch_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_GetCampaignStateBatch-response-successfulRequests"></a>
Successful requests.
Type: Array of [SuccessfulCampaignStateResponse](API_connect-outbound-campaigns_SuccessfulCampaignStateResponse.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_connect-outbound-campaigns_GetCampaignStateBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the outbound campaigns.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWSservice.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns_GetCampaignStateBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/GetCampaignStateBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/GetCampaignStateBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/GetCampaignStateBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/GetCampaignStateBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/GetCampaignStateBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/GetCampaignStateBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/GetCampaignStateBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/GetCampaignStateBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/GetCampaignStateBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/GetCampaignStateBatch)

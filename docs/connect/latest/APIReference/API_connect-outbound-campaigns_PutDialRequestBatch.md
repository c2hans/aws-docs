---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_PutDialRequestBatch.html
---

# PutDialRequestBatch
<a name="API_connect-outbound-campaigns_PutDialRequestBatch"></a>

Takes in a list of [DialRequests](https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DialRequest.html) to be dialed as part of an outbound campaign. For more information about using PutDialRequestBatch, see [Best practices for using PutDialRequestBatch for outbound campaign calling](https://docs.aws.amazon.com/connect/latest/devguide/api-outbound-campaign-calls.html).

## Request Syntax
<a name="API_connect-outbound-campaigns_PutDialRequestBatch_RequestSyntax"></a>

```
PUT /campaigns/{{id}}/dial-requests HTTP/1.1
Content-type: application/json

{
   "dialRequests": [
      {
         "attributes": {
            "{{string}}" : "{{string}}"
         },
         "clientToken": "{{string}}",
         "expirationTime": "{{string}}",
         "phoneNumber": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_PutDialRequestBatch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_connect-outbound-campaigns_PutDialRequestBatch_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_PutDialRequestBatch-request-uri-id"></a>
The identifier of the campaign.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns_PutDialRequestBatch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dialRequests](#API_connect-outbound-campaigns_PutDialRequestBatch_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_PutDialRequestBatch-request-dialRequests"></a>
Dial requests.
Type: Array of [DialRequest](API_connect-outbound-campaigns_DialRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_connect-outbound-campaigns_PutDialRequestBatch_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "failedRequests": [
      {
         "clientToken": "string",
         "failureCode": "string",
         "id": "string"
      }
   ],
   "successfulRequests": [
      {
         "clientToken": "string",
         "id": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-outbound-campaigns_PutDialRequestBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [failedRequests](#API_connect-outbound-campaigns_PutDialRequestBatch_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_PutDialRequestBatch-response-failedRequests"></a>
Failed dial requests.
Type: Array of [FailedRequest](API_connect-outbound-campaigns_FailedRequest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

 ** [successfulRequests](#API_connect-outbound-campaigns_PutDialRequestBatch_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_PutDialRequestBatch-response-successfulRequests"></a>
Successful dial requests.
Type: Array of [SuccessfulRequest](API_connect-outbound-campaigns_SuccessfulRequest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_connect-outbound-campaigns_PutDialRequestBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
This exception occurs when there is an internal failure in the outbound campaigns.
HTTP Status Code: 500

 ** InvalidCampaignStateException **
An attempt was made to modify a campaign that is in a state that is not valid. Check your campaign to ensure that it is in a valid state before retrying the operation.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWSservice.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns_PutDialRequestBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/PutDialRequestBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/PutDialRequestBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/PutDialRequestBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/PutDialRequestBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/PutDialRequestBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/PutDialRequestBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/PutDialRequestBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/PutDialRequestBatch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/PutDialRequestBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/PutDialRequestBatch)

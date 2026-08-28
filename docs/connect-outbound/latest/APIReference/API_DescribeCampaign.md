---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DescribeCampaign.html
---

# DescribeCampaign
<a name="API_connect-outbound-campaigns_DescribeCampaign"></a>

Describes an outbound campaign.

## Request Syntax
<a name="API_connect-outbound-campaigns_DescribeCampaign_RequestSyntax"></a>

```
GET /campaigns/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-outbound-campaigns_DescribeCampaign_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_connect-outbound-campaigns_DescribeCampaign_RequestSyntax) **   <a name="connect-connect-outbound-campaigns_DescribeCampaign-request-uri-id"></a>
The identifier of the campaign.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[-:/a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_connect-outbound-campaigns_DescribeCampaign_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-outbound-campaigns_DescribeCampaign_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "campaign": {
      "arn": "string",
      "connectInstanceId": "string",
      "dialerConfig": { ... },
      "id": "string",
      "name": "string",
      "outboundCallConfig": {
         "answerMachineDetectionConfig": {
            "awaitAnswerMachinePrompt": boolean,
            "enableAnswerMachineDetection": boolean
         },
         "connectContactFlowId": "string",
         "connectQueueId": "string",
         "connectSourcePhoneNumber": "string"
      },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_connect-outbound-campaigns_DescribeCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [campaign](#API_connect-outbound-campaigns_DescribeCampaign_ResponseSyntax) **   <a name="connect-connect-outbound-campaigns_DescribeCampaign-response-campaign"></a>
The campaign.
Type: [Campaign](API_connect-outbound-campaigns_Campaign.md) object

## Errors
<a name="API_connect-outbound-campaigns_DescribeCampaign_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the outbound campaigns.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWSservice.
HTTP Status Code: 400

## See Also
<a name="API_connect-outbound-campaigns_DescribeCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcampaigns-2021-01-30/DescribeCampaign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcampaigns-2021-01-30/DescribeCampaign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/DescribeCampaign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcampaigns-2021-01-30/DescribeCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/DescribeCampaign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcampaigns-2021-01-30/DescribeCampaign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcampaigns-2021-01-30/DescribeCampaign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcampaigns-2021-01-30/DescribeCampaign)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcampaigns-2021-01-30/DescribeCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/DescribeCampaign)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

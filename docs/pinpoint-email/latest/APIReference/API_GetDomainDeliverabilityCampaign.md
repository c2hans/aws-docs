---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDomainDeliverabilityCampaign.html
---

# GetDomainDeliverabilityCampaign
<a name="API_GetDomainDeliverabilityCampaign"></a>

Retrieve all the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for (`PutDeliverabilityDashboardOption` operation).

## Request Syntax
<a name="API_GetDomainDeliverabilityCampaign_RequestSyntax"></a>

```
GET /v1/email/deliverability-dashboard/campaigns/{{CampaignId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomainDeliverabilityCampaign_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CampaignId](#API_GetDomainDeliverabilityCampaign_RequestSyntax) **   <a name="pinpoint-GetDomainDeliverabilityCampaign-request-uri-CampaignId"></a>
The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns this identifier to a campaign. This value is not the same as the campaign identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon Pinpoint API or the Amazon Pinpoint console.
Required: Yes

## Request Body
<a name="API_GetDomainDeliverabilityCampaign_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomainDeliverabilityCampaign_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainDeliverabilityCampaign": {
      "CampaignId": "string",
      "DeleteRate": number,
      "Esps": [ "string" ],
      "FirstSeenDateTime": number,
      "FromAddress": "string",
      "ImageUrl": "string",
      "InboxCount": number,
      "LastSeenDateTime": number,
      "ProjectedVolume": number,
      "ReadDeleteRate": number,
      "ReadRate": number,
      "SendingIps": [ "string" ],
      "SpamCount": number,
      "Subject": "string"
   }
}
```

## Response Elements
<a name="API_GetDomainDeliverabilityCampaign_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainDeliverabilityCampaign](#API_GetDomainDeliverabilityCampaign_ResponseSyntax) **   <a name="pinpoint-GetDomainDeliverabilityCampaign-response-DomainDeliverabilityCampaign"></a>
An object that contains the deliverability data for the campaign.
Type: [DomainDeliverabilityCampaign](API_DomainDeliverabilityCampaign.md) object

## Errors
<a name="API_GetDomainDeliverabilityCampaign_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** NotFoundException **
The resource you attempted to access doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
Too many requests have been made to the operation.
HTTP Status Code: 429

## See Also
<a name="API_GetDomainDeliverabilityCampaign_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/GetDomainDeliverabilityCampaign)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

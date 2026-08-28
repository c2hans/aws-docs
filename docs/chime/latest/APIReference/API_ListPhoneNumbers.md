---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_ListPhoneNumbers.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# ListPhoneNumbers
<a name="API_ListPhoneNumbers"></a>

Lists the phone numbers for the specified Amazon Chime account, Amazon Chime user, Amazon Chime Voice Connector, or Amazon Chime Voice Connector group.

## Request Syntax
<a name="API_ListPhoneNumbers_RequestSyntax"></a>

```
GET /phone-numbers?filter-name={{FilterName}}&filter-value={{FilterValue}}&max-results={{MaxResults}}&next-token={{NextToken}}&product-type={{ProductType}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPhoneNumbers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FilterName](#API_ListPhoneNumbers_RequestSyntax) **   <a name="chime-ListPhoneNumbers-request-uri-FilterName"></a>
The filter to use to limit the number of results.
Valid Values: `AccountId | UserId | VoiceConnectorId | VoiceConnectorGroupId | SipRuleId`

 ** [FilterValue](#API_ListPhoneNumbers_RequestSyntax) **   <a name="chime-ListPhoneNumbers-request-uri-FilterValue"></a>
The value to use for the filter.

 ** [MaxResults](#API_ListPhoneNumbers_RequestSyntax) **   <a name="chime-ListPhoneNumbers-request-uri-MaxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 99.

 ** [NextToken](#API_ListPhoneNumbers_RequestSyntax) **   <a name="chime-ListPhoneNumbers-request-uri-NextToken"></a>
The token to use to retrieve the next page of results.

 ** [ProductType](#API_ListPhoneNumbers_RequestSyntax) **   <a name="chime-ListPhoneNumbers-request-uri-ProductType"></a>
The phone number product type.
Valid Values: `BusinessCalling | VoiceConnector | SipMediaApplicationDialIn`

 ** [Status](#API_ListPhoneNumbers_RequestSyntax) **   <a name="chime-ListPhoneNumbers-request-uri-Status"></a>
The phone number status.
Valid Values: `AcquireInProgress | AcquireFailed | Unassigned | Assigned | ReleaseInProgress | DeleteInProgress | ReleaseFailed | DeleteFailed`

## Request Body
<a name="API_ListPhoneNumbers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPhoneNumbers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "PhoneNumbers": [
      {
         "Associations": [
            {
               "AssociatedTimestamp": "string",
               "Name": "string",
               "Value": "string"
            }
         ],
         "CallingName": "string",
         "CallingNameStatus": "string",
         "Capabilities": {
            "InboundCall": boolean,
            "InboundMMS": boolean,
            "InboundSMS": boolean,
            "OutboundCall": boolean,
            "OutboundMMS": boolean,
            "OutboundSMS": boolean
         },
         "Country": "string",
         "CreatedTimestamp": "string",
         "DeletionTimestamp": "string",
         "E164PhoneNumber": "string",
         "PhoneNumberId": "string",
         "ProductType": "string",
         "Status": "string",
         "Type": "string",
         "UpdatedTimestamp": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPhoneNumbers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPhoneNumbers_ResponseSyntax) **   <a name="chime-ListPhoneNumbers-response-NextToken"></a>
The token to use to retrieve the next page of results.
Type: String

 ** [PhoneNumbers](#API_ListPhoneNumbers_ResponseSyntax) **   <a name="chime-ListPhoneNumbers-response-PhoneNumbers"></a>
The phone number details.
Type: Array of [PhoneNumber](API_PhoneNumber.md) objects

## Errors
<a name="API_ListPhoneNumbers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## Examples
<a name="API_ListPhoneNumbers_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListPhoneNumbers_Example_1"></a>

This example lists the phone numbers for the account.

#### Sample Request
<a name="API_ListPhoneNumbers_Example_1_Request"></a>

```
GET /phone-numbers HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20191028T184455Z Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_ListPhoneNumbers_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: c859a1d1-84ce-4cfc-a3ad-4dcde29d9265 Content-Type: application/json Content-Length: 1620 Date: Mon, 28 Oct 2019 18:44:55 GMT Connection: keep-alive {"NextToken":null,"PhoneNumbers":[{"Associations":[{"AssociatedTimestamp":"2019-10-28T18:40:37.453Z","Name":"VoiceConnectorId","Value":"abcdef1ghij2klmno3pqr4"}],"CallingName":null,"CallingNameStatus":"UpdateInProgress","Capabilities":{"InboundCall":true,"InboundMMS":true,"InboundSMS":true,"OutboundCall":true,"OutboundMMS":true,"OutboundSMS":true},"CreatedTimestamp":"2019-08-12T22:10:20.521Z","DeletionTimestamp":null,"E164PhoneNumber":"+12065550100","PhoneNumberId":"%2B12065550100","ProductType":"Voice Connector","Status":"Assigned","Type":"Local","UpdatedTimestamp":"2019-10-28T18:42:07.964Z"},{"Associations":[{"AssociatedTimestamp":"2019-10-28T18:40:37.511Z","Name":"VoiceConnectorId","Value":"abcdef1ghij2klmno3pqr4"}],"CallingName":null,"CallingNameStatus":"UpdateInProgress","Capabilities":{"InboundCall":true,"InboundMMS":true,"InboundSMS":true,"OutboundCall":true,"OutboundMMS":true,"OutboundSMS":true},"CreatedTimestamp":"2019-08-12T22:10:20.521Z","DeletionTimestamp":null,"E164PhoneNumber":"+12065550101","PhoneNumberId":"%2B12065550101","ProductType":"Voice Connector","Status":"Assigned","Type":"Local","UpdatedTimestamp":"2019-10-28T18:42:07.960Z"},{"Associations":[],"CallingName":null,"CallingNameStatus":"Unassigned","Capabilities":{"InboundCall":true,"InboundMMS":true,"InboundSMS":true,"OutboundCall":true,"OutboundMMS":true,"OutboundSMS":true},"CreatedTimestamp":"2019-08-09T21:35:21.445Z","DeletionTimestamp":null,"E164PhoneNumber":"+12065550102","PhoneNumberId":"%2B12065550102","ProductType":"Voice Connector","Status":"Unassigned","Type":"Local","UpdatedTimestamp":"2019-10-28T18:31:55.339Z"}]}
```

## See Also
<a name="API_ListPhoneNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/ListPhoneNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/ListPhoneNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/ListPhoneNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/ListPhoneNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/ListPhoneNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/ListPhoneNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/ListPhoneNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/ListPhoneNumbers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/ListPhoneNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/ListPhoneNumbers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

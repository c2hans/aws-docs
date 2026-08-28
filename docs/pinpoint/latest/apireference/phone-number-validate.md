---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference/phone-number-validate.html
---

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Phone Number Validate
<a name="phone-number-validate"></a>

You can use the Phone Number Validate resource to convert a phone number to E.164 format and to get more information about a phone number.

This resource accepts a POST request that includes a phone number in the request body. It responds with information about the phone number. This information includes whether the phone number is valid and the type of phone line that's associated with the number, such as mobile or landline. It also provides other helpful information about the number, such as the carrier that the number is registered with and the location where the number was originally registered.

## URI
<a name="phone-number-validate-url"></a>

`/v1/phone/number/validate`

## HTTP methods
<a name="phone-number-validate-http-methods"></a>

### POST
<a name="phone-number-validatepost"></a>

**Operation ID:** `PhoneNumberValidate`

Retrieves information about a phone number.

**Header parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| accept | String | False | Indicates which content types, expressed as MIME types, the client understands. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | NumberValidateResponse | The request succeeded. |
| 400 | MessageBody | The request contains a syntax error (BadRequestException). |
| 403 | MessageBody | The request was denied because access to the specified resource is forbidden (ForbiddenException). |
| 404 | MessageBody | The request failed because the specified resource was not found (NotFoundException). |
| 405 | MessageBody | The request failed because the method is not allowed for the specified resource (MethodNotAllowedException). |
| 413 | MessageBody | The request failed because the payload for the body of the request is too large (RequestEntityTooLargeException). |
| 429 | MessageBody | The request failed because too many requests were sent during a certain amount of time (TooManyRequestsException). |
| 500 | MessageBody | The request failed due to an unknown internal server error, exception, or failure (InternalServerErrorException). |

### OPTIONS
<a name="phone-number-validateoptions"></a>

Retrieves information about the communication requirements and options that are available for the Phone Number Validate resource.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | The request succeeded. |

## Schemas
<a name="phone-number-validate-schemas"></a>

### Request bodies
<a name="phone-number-validate-request-examples"></a>

#### POST schema
<a name="phone-number-validate-request-body-post-example"></a>

```
{
  "PhoneNumber": "string",
  "IsoCountryCode": "string"
}
```

### Response bodies
<a name="phone-number-validate-response-examples"></a>

#### NumberValidateResponse schema
<a name="phone-number-validate-response-body-numbervalidateresponse-example"></a>

```
{
  "CountryCodeIso2": "string",
  "CountryCodeNumeric": "string",
  "Country": "string",
  "City": "string",
  "ZipCode": "string",
  "County": "string",
  "Timezone": "string",
  "CleansedPhoneNumberNational": "string",
  "CleansedPhoneNumberE164": "string",
  "Carrier": "string",
  "PhoneTypeCode": integer,
  "PhoneType": "string",
  "OriginalPhoneNumber": "string",
  "OriginalCountryCodeIso2": "string"
}
```

#### MessageBody schema
<a name="phone-number-validate-response-body-messagebody-example"></a>

```
{
  "RequestID": "string",
  "Message": "string"
}
```

## Properties
<a name="phone-number-validate-properties"></a>

### MessageBody
<a name="phone-number-validate-model-messagebody"></a>

Provides information about an API request or response.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Message | string | False | The message that's returned from the API. |
| RequestID | string | False | The unique identifier for the request or response. |

### NumberValidateRequest
<a name="phone-number-validate-model-numbervalidaterequest"></a>

Specifies a phone number to validate and retrieve information about.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| IsoCountryCode | string | False | The two-character code, in ISO 3166-1 alpha-2 format, for the country or region where the phone number was originally registered. |
| PhoneNumber | string | False | The phone number to retrieve information about. The phone number that you provide should include a valid numeric country code. Otherwise, the operation might result in an error. |

### NumberValidateResponse
<a name="phone-number-validate-model-numbervalidateresponse"></a>

Provides information about a phone number.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Carrier | string | False | The carrier or service provider that the phone number is currently registered with. In some countries and regions, this value may be the carrier or service provider that the phone number was originally registered with. |
| City | string | False | The name of the city where the phone number was originally registered. |
| CleansedPhoneNumberE164 | string | False | The cleansed phone number, in E.164 format, for the location where the phone number was originally registered. |
| CleansedPhoneNumberNational | string | False | The cleansed phone number, in the format for the location where the phone number was originally registered. |
| Country | string | False | The name of the country or region where the phone number was originally registered. |
| CountryCodeIso2 | string | False | The two-character code, in ISO 3166-1 alpha-2 format, for the country or region where the phone number was originally registered. |
| CountryCodeNumeric | string | False | The numeric code for the country or region where the phone number was originally registered. |
| County | string | False | The name of the county where the phone number was originally registered. |
| OriginalCountryCodeIso2 | string | False | The two-character code, in ISO 3166-1 alpha-2 format, that was sent in the request body. |
| OriginalPhoneNumber | string | False | The phone number that was sent in the request body. |
| PhoneType | string | False | The description of the phone type. Valid values are: `MOBILE, LANDLINE, VOIP, INVALID, PREPAID,` and `OTHER`. |
| PhoneTypeCode | integer | False | The phone type, represented by an integer. Valid values are: `0` (mobile), `1` (landline), `2` (VoIP), `3` (invalid), `4` (other), and `5` (prepaid). |
| Timezone | string | False | The time zone for the location where the phone number was originally registered. |
| ZipCode | string | False | The postal or ZIP code for the location where the phone number was originally registered. |

## See also
<a name="phone-number-validate-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### PhoneNumberValidate
<a name="PhoneNumberValidate-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/pinpoint-2016-12-01/PhoneNumberValidate)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/pinpoint-2016-12-01/PhoneNumberValidate)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/pinpoint-2016-12-01/PhoneNumberValidate)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/pinpoint-2016-12-01/PhoneNumberValidate)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/pinpoint-2016-12-01/PhoneNumberValidate)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/pinpoint-2016-12-01/PhoneNumberValidate)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/pinpoint-2016-12-01/PhoneNumberValidate)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/pinpoint-2016-12-01/PhoneNumberValidate)
+ [AWS SDK for Python](/goto/boto3/pinpoint-2016-12-01/PhoneNumberValidate)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/pinpoint-2016-12-01/PhoneNumberValidate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_ListSupportedPhoneNumberCountries.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# ListSupportedPhoneNumberCountries
<a name="API_ListSupportedPhoneNumberCountries"></a>

Lists supported phone number countries.

## Request Syntax
<a name="API_ListSupportedPhoneNumberCountries_RequestSyntax"></a>

```
GET /phone-number-countries?product-type={{ProductType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSupportedPhoneNumberCountries_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ProductType](#API_ListSupportedPhoneNumberCountries_RequestSyntax) **   <a name="chime-ListSupportedPhoneNumberCountries-request-uri-ProductType"></a>
The phone number product type.
Valid Values: `BusinessCalling | VoiceConnector | SipMediaApplicationDialIn`
Required: Yes

## Request Body
<a name="API_ListSupportedPhoneNumberCountries_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSupportedPhoneNumberCountries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "PhoneNumberCountries": [
      {
         "CountryCode": "string",
         "SupportedPhoneNumberTypes": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_ListSupportedPhoneNumberCountries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PhoneNumberCountries](#API_ListSupportedPhoneNumberCountries_ResponseSyntax) **   <a name="chime-ListSupportedPhoneNumberCountries-response-PhoneNumberCountries"></a>
The supported phone number countries.
Type: Array of [PhoneNumberCountry](API_PhoneNumberCountry.md) objects

## Errors
<a name="API_ListSupportedPhoneNumberCountries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation.
HTTP Status Code: 403

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

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

## See Also
<a name="API_ListSupportedPhoneNumberCountries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/ListSupportedPhoneNumberCountries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/ListSupportedPhoneNumberCountries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/ListSupportedPhoneNumberCountries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/ListSupportedPhoneNumberCountries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/ListSupportedPhoneNumberCountries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/ListSupportedPhoneNumberCountries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/ListSupportedPhoneNumberCountries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/ListSupportedPhoneNumberCountries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/ListSupportedPhoneNumberCountries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/ListSupportedPhoneNumberCountries)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_SearchAvailablePhoneNumbers.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# SearchAvailablePhoneNumbers
<a name="API_SearchAvailablePhoneNumbers"></a>

Searches for phone numbers that can be ordered. For US numbers, provide at least one of the following search filters: `AreaCode`, `City`, `State`, or `TollFreePrefix`. If you provide `City`, you must also provide `State`. Numbers outside the US only support the `PhoneNumberType` filter, which you must use.

## Request Syntax
<a name="API_SearchAvailablePhoneNumbers_RequestSyntax"></a>

```
GET /search?type=phone-numbers&area-code={{AreaCode}}&city={{City}}&country={{Country}}&max-results={{MaxResults}}&next-token={{NextToken}}&phone-number-type={{PhoneNumberType}}&state={{State}}&toll-free-prefix={{TollFreePrefix}} HTTP/1.1
```

## URI Request Parameters
<a name="API_SearchAvailablePhoneNumbers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AreaCode](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-request-uri-AreaCode"></a>
The area code used to filter results. Only applies to the US.

 ** [City](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-request-uri-City"></a>
The city used to filter results. Only applies to the US.

 ** [Country](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-request-uri-Country"></a>
The country used to filter results. Defaults to the US Format: ISO 3166-1 alpha-2.
Pattern: `[A-Z]{2}`

 ** [MaxResults](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-request-uri-MaxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-request-uri-NextToken"></a>
The token used to retrieve the next page of results.

 ** [PhoneNumberType](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-request-uri-PhoneNumberType"></a>
The phone number type used to filter results. Required for non-US numbers.
Valid Values: `Local | TollFree`

 ** [State](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-request-uri-State"></a>
The state used to filter results. Required only if you provide `City`. Only applies to the US.

 ** [TollFreePrefix](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-request-uri-TollFreePrefix"></a>
The toll-free prefix that you use to filter results. Only applies to the US.
Length Constraints: Fixed length of 3.
Pattern: `^8(00|33|44|55|66|77|88)$`

## Request Body
<a name="API_SearchAvailablePhoneNumbers_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_SearchAvailablePhoneNumbers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "E164PhoneNumbers": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchAvailablePhoneNumbers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [E164PhoneNumbers](#API_SearchAvailablePhoneNumbers_ResponseSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-response-E164PhoneNumbers"></a>
List of phone numbers, in E.164 format.
Type: Array of strings
Pattern: `^\+?[1-9]\d{1,14}$`

 ** [NextToken](#API_SearchAvailablePhoneNumbers_ResponseSyntax) **   <a name="chime-SearchAvailablePhoneNumbers-response-NextToken"></a>
The token used to retrieve the next page of search results.
Type: String

## Errors
<a name="API_SearchAvailablePhoneNumbers_Errors"></a>

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

## Examples
<a name="API_SearchAvailablePhoneNumbers_Examples"></a>

In the following examples, the Authorization header contents (`AUTHPARAMS`) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_SearchAvailablePhoneNumbers_Example_1"></a>

 This example searches for phone numbers with an area code of `206`.

#### Sample Request
<a name="API_SearchAvailablePhoneNumbers_Example_1_Request"></a>

```
GET /search?type=phone-numbers&area-code=206 HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20190918T180157Z Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_SearchAvailablePhoneNumbers_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: 98bb7b5b-0f5b-48c3-a959-ab0d7fd42b97 Content-Type: application/json Content-Length: 1522 Date: Wed, 18 Sep 2019 18:01:57 GMT Connection: keep-alive {"E164PhoneNumbers":["+12065550100","+12065550101","+12065550102"], "NextToken": null}
```

### Example
<a name="API_SearchAvailablePhoneNumbers_Example_2"></a>

 This example searches local phone numbers in the United Kingdom.

#### Sample Request
<a name="API_SearchAvailablePhoneNumbers_Example_2_Request"></a>

```
GET /search?type=phone-numbers&country=GB&phone-number-type=Local HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.170 Python/3.6.0 Windows/10 botocore/1.12.160 X-Amz-Date: 20210224T201356Z Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_SearchAvailablePhoneNumbers_Example_2_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: 86b1ec89-b95b-47de-bd67-92c6d778bbd5 Content-Type: application/json Content-Length: 1522 Date: Wed, 24 Feb 2021 20:13:56 GMT Connection: keep-alive {"E164PhoneNumbers":["+442012345677","+442012345678","+442012345679"], "NextToken": null}
```

## See Also
<a name="API_SearchAvailablePhoneNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/SearchAvailablePhoneNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/SearchAvailablePhoneNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/SearchAvailablePhoneNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/SearchAvailablePhoneNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/SearchAvailablePhoneNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/SearchAvailablePhoneNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/SearchAvailablePhoneNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/SearchAvailablePhoneNumbers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/SearchAvailablePhoneNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/SearchAvailablePhoneNumbers)

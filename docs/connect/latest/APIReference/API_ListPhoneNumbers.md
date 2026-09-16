---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbers.html
---

# ListPhoneNumbers
<a name="API_ListPhoneNumbers"></a>

Provides information about the phone numbers for the specified Connect Customer instance.

For more information about phone numbers, see [Set Up Phone Numbers for Your Contact Center](https://docs.aws.amazon.com/connect/latest/adminguide/contact-center-phone-number.html) in the *Connect Customer Administrator Guide*.

**Important**
We recommend using [ListPhoneNumbersV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html) to return phone number types. ListPhoneNumbers doesn't support number types `UIFN`, `SHARED`, `THIRD_PARTY_TF`, and `THIRD_PARTY_DID`. While it returns numbers of those types, it incorrectly lists them as `TOLL_FREE` or `DID`.
The phone number `Arn` value that is returned from each of the items in the [PhoneNumberSummaryList](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbers.html#connect-ListPhoneNumbers-response-PhoneNumberSummaryList) cannot be used to tag phone number resources. It will fail with a `ResourceNotFoundException`. Instead, use the [ListPhoneNumbersV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html) API. It returns the new phone number ARN that can be used to tag phone number resources.

## Request Syntax
<a name="API_ListPhoneNumbers_RequestSyntax"></a>

```
GET /phone-numbers-summary/{{InstanceId}}?maxResults={{MaxResults}}&nextToken={{NextToken}}&phoneNumberCountryCodes={{PhoneNumberCountryCodes}}&phoneNumberTypes={{PhoneNumberTypes}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPhoneNumbers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListPhoneNumbers_RequestSyntax) **   <a name="connect-ListPhoneNumbers-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListPhoneNumbers_RequestSyntax) **   <a name="connect-ListPhoneNumbers-request-uri-MaxResults"></a>
The maximum number of results to return per page. The default MaxResult size is 100.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListPhoneNumbers_RequestSyntax) **   <a name="connect-ListPhoneNumbers-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

 ** [PhoneNumberCountryCodes](#API_ListPhoneNumbers_RequestSyntax) **   <a name="connect-ListPhoneNumbers-request-uri-PhoneNumberCountryCodes"></a>
The ISO country code.
Array Members: Maximum number of 10 items.
Valid Values: `AF | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BA | BW | BR | IO | VG | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CK | CR | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | TL | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | PF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GU | GT | GG | GN | GW | GY | HT | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | CI | JM | JP | JE | JO | KZ | KE | KI | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | KP | MP | NO | OM | PK | PW | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | CG | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | KR | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TG | TK | TO | TT | TN | TR | TM | TC | TV | VI | UG | UA | AE | GB | US | UY | UZ | VU | VA | VE | VN | WF | EH | YE | ZM | ZW`

 ** [PhoneNumberTypes](#API_ListPhoneNumbers_RequestSyntax) **   <a name="connect-ListPhoneNumbers-request-uri-PhoneNumberTypes"></a>
The type of phone number.
We recommend using [ListPhoneNumbersV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html) to return phone number types. While ListPhoneNumbers returns number types `UIFN`, `SHARED`, `THIRD_PARTY_TF`, and `THIRD_PARTY_DID`, it incorrectly lists them as `TOLL_FREE` or `DID`.
Array Members: Maximum number of 6 items.
Valid Values: `TOLL_FREE | DID | UIFN | SHARED | THIRD_PARTY_TF | THIRD_PARTY_DID | SHORT_CODE`

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
   "PhoneNumberSummaryList": [
      {
         "Arn": "string",
         "Id": "string",
         "PhoneNumber": "string",
         "PhoneNumberCountryCode": "string",
         "PhoneNumberType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPhoneNumbers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPhoneNumbers_ResponseSyntax) **   <a name="connect-ListPhoneNumbers-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [PhoneNumberSummaryList](#API_ListPhoneNumbers_ResponseSyntax) **   <a name="connect-ListPhoneNumbers-response-PhoneNumberSummaryList"></a>
Information about the phone numbers.
Type: Array of [PhoneNumberSummary](API_PhoneNumberSummary.md) objects

## Errors
<a name="API_ListPhoneNumbers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListPhoneNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListPhoneNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListPhoneNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListPhoneNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListPhoneNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListPhoneNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListPhoneNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListPhoneNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListPhoneNumbers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListPhoneNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListPhoneNumbers)

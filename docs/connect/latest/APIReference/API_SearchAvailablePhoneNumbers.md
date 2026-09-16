---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchAvailablePhoneNumbers.html
---

# SearchAvailablePhoneNumbers
<a name="API_SearchAvailablePhoneNumbers"></a>

Searches for available phone numbers that you can claim to your Connect Customer instance or traffic distribution group. If the provided `TargetArn` is a traffic distribution group, you can call this API in both AWS Regions associated with the traffic distribution group.

## Request Syntax
<a name="API_SearchAvailablePhoneNumbers_RequestSyntax"></a>

```
POST /phone-number/search-available HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PhoneNumberCountryCode": "{{string}}",
   "PhoneNumberPrefix": "{{string}}",
   "PhoneNumberType": "{{string}}",
   "TargetArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchAvailablePhoneNumbers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchAvailablePhoneNumbers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="connect-SearchAvailablePhoneNumbers-request-InstanceId"></a>
The identifier of the Connect Customer instance that phone numbers are claimed to. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance. You must enter `InstanceId` or `TargetArn`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [MaxResults](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="connect-SearchAvailablePhoneNumbers-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [NextToken](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="connect-SearchAvailablePhoneNumbers-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: No

 ** [PhoneNumberCountryCode](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="connect-SearchAvailablePhoneNumbers-request-PhoneNumberCountryCode"></a>
The ISO country code.
Type: String
Valid Values: `AF | AL | DZ | AS | AD | AO | AI | AQ | AG | AR | AM | AW | AU | AT | AZ | BS | BH | BD | BB | BY | BE | BZ | BJ | BM | BT | BO | BA | BW | BR | IO | VG | BN | BG | BF | BI | KH | CM | CA | CV | KY | CF | TD | CL | CN | CX | CC | CO | KM | CK | CR | HR | CU | CW | CY | CZ | CD | DK | DJ | DM | DO | TL | EC | EG | SV | GQ | ER | EE | ET | FK | FO | FJ | FI | FR | PF | GA | GM | GE | DE | GH | GI | GR | GL | GD | GU | GT | GG | GN | GW | GY | HT | HN | HK | HU | IS | IN | ID | IR | IQ | IE | IM | IL | IT | CI | JM | JP | JE | JO | KZ | KE | KI | KW | KG | LA | LV | LB | LS | LR | LY | LI | LT | LU | MO | MK | MG | MW | MY | MV | ML | MT | MH | MR | MU | YT | MX | FM | MD | MC | MN | ME | MS | MA | MZ | MM | NA | NR | NP | NL | AN | NC | NZ | NI | NE | NG | NU | KP | MP | NO | OM | PK | PW | PA | PG | PY | PE | PH | PN | PL | PT | PR | QA | CG | RE | RO | RU | RW | BL | SH | KN | LC | MF | PM | VC | WS | SM | ST | SA | SN | RS | SC | SL | SG | SX | SK | SI | SB | SO | ZA | KR | ES | LK | SD | SR | SJ | SZ | SE | CH | SY | TW | TJ | TZ | TH | TG | TK | TO | TT | TN | TR | TM | TC | TV | VI | UG | UA | AE | GB | US | UY | UZ | VU | VA | VE | VN | WF | EH | YE | ZM | ZW`
Required: Yes

 ** [PhoneNumberPrefix](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="connect-SearchAvailablePhoneNumbers-request-PhoneNumberPrefix"></a>
The prefix of the phone number. If provided, it must contain `+` as part of the country code.
Type: String
Pattern: `\\+?[0-9]{1,11}`
Required: No

 ** [PhoneNumberType](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="connect-SearchAvailablePhoneNumbers-request-PhoneNumberType"></a>
The type of phone number.
Type: String
Valid Values: `TOLL_FREE | DID | UIFN | SHARED | THIRD_PARTY_TF | THIRD_PARTY_DID | SHORT_CODE`
Required: Yes

 ** [TargetArn](#API_SearchAvailablePhoneNumbers_RequestSyntax) **   <a name="connect-SearchAvailablePhoneNumbers-request-TargetArn"></a>
The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through. You must enter `InstanceId` or `TargetArn`.
Type: String
Required: No

## Response Syntax
<a name="API_SearchAvailablePhoneNumbers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AvailableNumbersList": [
      {
         "PhoneNumber": "string",
         "PhoneNumberCountryCode": "string",
         "PhoneNumberType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_SearchAvailablePhoneNumbers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailableNumbersList](#API_SearchAvailablePhoneNumbers_ResponseSyntax) **   <a name="connect-SearchAvailablePhoneNumbers-response-AvailableNumbersList"></a>
A list of available phone numbers that you can claim to your Connect Customer instance or traffic distribution group.
Type: Array of [AvailableNumberSummary](API_AvailableNumberSummary.md) objects

 ** [NextToken](#API_SearchAvailablePhoneNumbers_ResponseSyntax) **   <a name="connect-SearchAvailablePhoneNumbers-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.

## Errors
<a name="API_SearchAvailablePhoneNumbers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_SearchAvailablePhoneNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchAvailablePhoneNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchAvailablePhoneNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchAvailablePhoneNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchAvailablePhoneNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchAvailablePhoneNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchAvailablePhoneNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchAvailablePhoneNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchAvailablePhoneNumbers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchAvailablePhoneNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchAvailablePhoneNumbers)

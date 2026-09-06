---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetProfile.html
---

# GetProfile
<a name="API_GetProfile"></a>

Returns information about the profile of the Amazon Lightsail account that makes the request. The response includes the profile type and, for accounts enrolled in the Lightsail partner program, the partner membership details.

## Response Syntax
<a name="API_GetProfile_ResponseSyntax"></a>

```
{
   "partner": {
      "enrolledAt": number,
      "status": "string",
      "tierName": "string"
   },
   "profileType": "string"
}
```

## Response Elements
<a name="API_GetProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [partner](#API_GetProfile_ResponseSyntax) **   <a name="Lightsail-GetProfile-response-partner"></a>
An object that describes the partner membership of the account, such as the tier of the membership, its status, and when the account was enrolled.
This parameter is returned only for accounts that have a `profileType` of `LightsailPartner`.
Type: [PartnerInfo](API_PartnerInfo.md) object

 ** [profileType](#API_GetProfile_ResponseSyntax) **   <a name="Lightsail-GetProfile-response-profileType"></a>
The type of the profile.
The following profile types are possible:
+  `Lightsailor` – The account is not enrolled in the Lightsail partner program.
+  `LightsailPartner` – The account is enrolled in the Lightsail partner program.
Type: String
Valid Values: `Lightsailor | LightsailPartner`

## Errors
<a name="API_GetProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** AccountSetupInProgressException **
Lightsail throws this exception when an account is still in the setup in progress state.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetProfile)

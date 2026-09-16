---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_CheckIfPhoneNumberIsOptedOut.html
---

# CheckIfPhoneNumberIsOptedOut
<a name="API_CheckIfPhoneNumberIsOptedOut"></a>

Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS messages from your AWS account. You cannot send SMS messages to a number that is opted out.

To resume sending messages, you can opt in the number by using the `OptInPhoneNumber` action.

## Request Parameters
<a name="API_CheckIfPhoneNumberIsOptedOut_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** phoneNumber **
The phone number for which you want to check the opt out status.
Type: String
Required: Yes

## Response Elements
<a name="API_CheckIfPhoneNumberIsOptedOut_ResponseElements"></a>

The following element is returned by the service.

 ** isOptedOut **
Indicates whether the phone number is opted out:
+  `true` – The phone number is opted out, meaning you cannot publish SMS messages to it.
+  `false` – The phone number is opted in, meaning you can publish SMS messages to it.
Type: Boolean

## Errors
<a name="API_CheckIfPhoneNumberIsOptedOut_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** Throttled **
Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.
 ** message **
Throttled request.
HTTP Status Code: 429

## See Also
<a name="API_CheckIfPhoneNumberIsOptedOut_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut)

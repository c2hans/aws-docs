---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_CreateSMSSandboxPhoneNumber.html
---

# CreateSMSSandboxPhoneNumber
<a name="API_CreateSMSSandboxPhoneNumber"></a>

Adds a destination phone number to an AWS account in the SMS sandbox and sends a one-time password (OTP) to that phone number.

When you start using Amazon SNS to send SMS messages, your AWS account is in the *SMS sandbox*. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your AWS account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see [SMS sandbox](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) in the *Amazon SNS Developer Guide*.

## Request Parameters
<a name="API_CreateSMSSandboxPhoneNumber_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LanguageCode **
The language to use for sending the OTP. The default value is `en-US`.
Type: String
Valid Values: `en-US | en-GB | es-419 | es-ES | de-DE | fr-CA | fr-FR | it-IT | ja-JP | pt-BR | kr-KR | zh-CN | zh-TW`
Required: No

 ** PhoneNumber **
The destination phone number to verify. On verification, Amazon SNS adds this phone number to the list of verified phone numbers that you can send SMS messages to.
Type: String
Length Constraints: Maximum length of 20.
Pattern: `^(\+[0-9]{8,}|[0-9]{0,9})$`
Required: Yes

## Errors
<a name="API_CreateSMSSandboxPhoneNumber_Errors"></a>

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

 ** OptedOut **
Indicates that the specified phone number opted out of receiving SMS messages from your AWS account. You can't send SMS messages to phone numbers that opt out.
HTTP Status Code: 400

 ** Throttled **
Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.
 ** message **
Throttled request.
HTTP Status Code: 429

 ** UserError **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

## Examples
<a name="API_CreateSMSSandboxPhoneNumber_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_CreateSMSSandboxPhoneNumber_Example_1"></a>

This example illustrates one usage of CreateSMSSandboxPhoneNumber.

#### Sample Request
<a name="API_CreateSMSSandboxPhoneNumber_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=CreateSMSSandboxPhoneNumber
&PhoneNumber=%2B12065550100
&LanguageCode=en-US
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateSMSSandboxPhoneNumber_Example_1_Response"></a>

```
<CreateSMSSandboxPhoneNumberResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <CreateSMSSandboxPhoneNumberResult>
    </CreateSMSSandboxPhoneNumberResult>
    <ResponseMetadata>
        <RequestId>0d30fe4d-b737-5759-a82a-a6b75f920cdb</RequestId>
    </ResponseMetadata>
</CreateSMSSandboxPhoneNumberResponse>
```

## See Also
<a name="API_CreateSMSSandboxPhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/CreateSMSSandboxPhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/CreateSMSSandboxPhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/CreateSMSSandboxPhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/CreateSMSSandboxPhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/CreateSMSSandboxPhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/CreateSMSSandboxPhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/CreateSMSSandboxPhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/CreateSMSSandboxPhoneNumber)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/CreateSMSSandboxPhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/CreateSMSSandboxPhoneNumber)

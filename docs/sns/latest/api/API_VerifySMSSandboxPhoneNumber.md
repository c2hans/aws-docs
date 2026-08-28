---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_VerifySMSSandboxPhoneNumber.html
---

# VerifySMSSandboxPhoneNumber
<a name="API_VerifySMSSandboxPhoneNumber"></a>

Verifies a destination phone number with a one-time password (OTP) for the calling AWS account.

When you start using Amazon SNS to send SMS messages, your AWS account is in the *SMS sandbox*. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your AWS account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see [SMS sandbox](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) in the *Amazon SNS Developer Guide*.

## Request Parameters
<a name="API_VerifySMSSandboxPhoneNumber_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** OneTimePassword **
The OTP sent to the destination number from the `CreateSMSSandBoxPhoneNumber` call.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 8.
Pattern: `^[0-9]+$`
Required: Yes

 ** PhoneNumber **
The destination phone number to verify.
Type: String
Length Constraints: Maximum length of 20.
Pattern: `^(\+[0-9]{8,}|[0-9]{0,9})$`
Required: Yes

## Errors
<a name="API_VerifySMSSandboxPhoneNumber_Errors"></a>

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

 ** ResourceNotFound **
Can’t perform the action on the specified resource. Make sure that the resource exists.
HTTP Status Code: 404

 ** Throttled **
Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.
 ** message **
Throttled request.
HTTP Status Code: 429

 ** Verification **
Indicates that the one-time password (OTP) used for verification is invalid.
 ** Status **
The status of the verification error.
HTTP Status Code: 400

## Examples
<a name="API_VerifySMSSandboxPhoneNumber_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_VerifySMSSandboxPhoneNumber_Example_1"></a>

This example illustrates one usage of VerifySMSSandboxPhoneNumber.

#### Sample Request
<a name="API_VerifySMSSandboxPhoneNumber_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=VerifySMSSandboxPhoneNumber
&PhoneNumber=%2B12065550100
&OneTimePassword=7973610
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_VerifySMSSandboxPhoneNumber_Example_1_Response"></a>

```
<VerifySMSSandboxPhoneNumberResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <VerifySMSSandboxPhoneNumberResult>
    </VerifySMSSandboxPhoneNumberResult>
    <ResponseMetadata>
        <RequestId>65e432d1-b1bf-5d5f-a962-6a2b5b4c5c94</RequestId>
    </ResponseMetadata>
</VerifySMSSandboxPhoneNumberResponse>
```

## See Also
<a name="API_VerifySMSSandboxPhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/VerifySMSSandboxPhoneNumber)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/VerifySMSSandboxPhoneNumber)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/VerifySMSSandboxPhoneNumber)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/VerifySMSSandboxPhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/VerifySMSSandboxPhoneNumber)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/VerifySMSSandboxPhoneNumber)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/VerifySMSSandboxPhoneNumber)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/VerifySMSSandboxPhoneNumber)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/VerifySMSSandboxPhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/VerifySMSSandboxPhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

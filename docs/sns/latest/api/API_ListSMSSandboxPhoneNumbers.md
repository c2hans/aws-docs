---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ListSMSSandboxPhoneNumbers.html
---

# ListSMSSandboxPhoneNumbers
<a name="API_ListSMSSandboxPhoneNumbers"></a>

Lists the calling AWS account's current verified and pending destination phone numbers in the SMS sandbox.

When you start using Amazon SNS to send SMS messages, your AWS account is in the *SMS sandbox*. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your AWS account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see [SMS sandbox](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) in the *Amazon SNS Developer Guide*.

## Request Parameters
<a name="API_ListSMSSandboxPhoneNumbers_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** MaxResults **
The maximum number of phone numbers to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** NextToken **
Token that the previous `ListSMSSandboxPhoneNumbersInput` request returns.
Type: String
Required: No

## Response Elements
<a name="API_ListSMSSandboxPhoneNumbers_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
A `NextToken` string is returned when you call the `ListSMSSandboxPhoneNumbersInput` operation if additional pages of records are available.
Type: String

 **PhoneNumbers.member.N**
A list of the calling account's pending and verified phone numbers.
Type: Array of [SMSSandboxPhoneNumber](API_SMSSandboxPhoneNumber.md) objects

## Errors
<a name="API_ListSMSSandboxPhoneNumbers_Errors"></a>

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

## Examples
<a name="API_ListSMSSandboxPhoneNumbers_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_ListSMSSandboxPhoneNumbers_Example_1"></a>

This example illustrates one usage of ListSMSSandboxPhoneNumbers.

#### Sample Request
<a name="API_ListSMSSandboxPhoneNumbers_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=ListSMSSandboxPhoneNumbers
&NextToken=eyJBd3NBY2NvdW50SWQiOnsicyI6IjU3MjQ1OTY4NzAxNCJ9LCJEZXN0aW5hdGlvblBob25lTnVtYmVyIjp7InMiOiIrMTc3ODI1NTM4NSJ9fQ%3D%3D
&MaxResults=2
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListSMSSandboxPhoneNumbers_Example_1_Response"></a>

```
<ListSMSSandboxPhoneNumbersResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ListSMSSandboxPhoneNumbersResult>
           <NextToken>eyJBd3NBY2NvdW50SWQiOnsicyI6IjU3MjQ1OTY4NzAxNCJ9LCJEZXN0aW5hdGlvblBob25lTnVtYmVyIjp7InMiOiIrMTc3ODk4NjU0MjkifX0=</NextToken>
        <PhoneNumbers>
            <member>
                <PhoneNumber>+12065550111</PhoneNumber>
                <Status>Pending</Status>
            </member>
            <member>
                <PhoneNumber>+12065550122</PhoneNumber>
                <Status>Verified</Status>
            </member>
        </PhoneNumbers>
    </ListSMSSandboxPhoneNumbersResult>
    <ResponseMetadata>
        <RequestId>6b6ae37e-3200-54b6-8882-bb84f47c2141</RequestId>
    </ResponseMetadata>
</ListSMSSandboxPhoneNumbersResponse>
```

## See Also
<a name="API_ListSMSSandboxPhoneNumbers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ListSMSSandboxPhoneNumbers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ListSMSSandboxPhoneNumbers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ListSMSSandboxPhoneNumbers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ListSMSSandboxPhoneNumbers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ListSMSSandboxPhoneNumbers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ListSMSSandboxPhoneNumbers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ListSMSSandboxPhoneNumbers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ListSMSSandboxPhoneNumbers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ListSMSSandboxPhoneNumbers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ListSMSSandboxPhoneNumbers)

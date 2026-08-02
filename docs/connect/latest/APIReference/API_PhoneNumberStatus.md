---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PhoneNumberStatus.html
---

# PhoneNumberStatus
<a name="API_PhoneNumberStatus"></a>

The status of the phone number.
+  `CLAIMED` means the previous [ClaimPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html) or [UpdatePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html) operation succeeded.
+  `IN_PROGRESS` means a [ClaimPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html), [UpdatePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html), or [UpdatePhoneNumberMetadata](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumberMetadata.html) operation is still in progress and has not yet completed. You can call [DescribePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html) at a later time to verify if the previous operation has completed.
+  `FAILED` indicates that the previous [ClaimPhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimPhoneNumber.html) or [UpdatePhoneNumber](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html) operation has failed. It will include a message indicating the failure reason. A common reason for a failure may be that the `TargetArn` value you are claiming or updating a phone number to has reached its limit of total claimed numbers. If you received a `FAILED` status from a `ClaimPhoneNumber` API call, you have one day to retry claiming the phone number before the number is released back to the inventory for other customers to claim.

## Contents
<a name="API_PhoneNumberStatus_Contents"></a>

 ** Message **   <a name="connect-Type-PhoneNumberStatus-Message"></a>
The status message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^[\W\S_]*`
Required: No

 ** Status **   <a name="connect-Type-PhoneNumberStatus-Status"></a>
The status.
Type: String
Valid Values: `CLAIMED | IN_PROGRESS | FAILED`
Required: No

## See Also
<a name="API_PhoneNumberStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PhoneNumberStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PhoneNumberStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PhoneNumberStatus)

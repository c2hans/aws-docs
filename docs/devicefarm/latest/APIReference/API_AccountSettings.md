---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_AccountSettings.html
---

# AccountSettings
<a name="API_AccountSettings"></a>

A container for account-level settings in AWS Device Farm.

## Contents
<a name="API_AccountSettings_Contents"></a>

 ** awsAccountNumber **   <a name="devicefarm-Type-AccountSettings-awsAccountNumber"></a>
The AWS account number specified in the `AccountSettings` container.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 16.
Required: No

 ** defaultJobTimeoutMinutes **   <a name="devicefarm-Type-AccountSettings-defaultJobTimeoutMinutes"></a>
The default number of minutes (at the account level) a test run executes before it times out. The default value is 150 minutes.
Type: Integer
Required: No

 ** maxJobTimeoutMinutes **   <a name="devicefarm-Type-AccountSettings-maxJobTimeoutMinutes"></a>
The maximum number of minutes a test run executes before it times out.
Type: Integer
Required: No

 ** maxSlots **   <a name="devicefarm-Type-AccountSettings-maxSlots"></a>
The maximum number of device slots that the AWS account can purchase. Each maximum is expressed as an `offering-id:number` pair, where the `offering-id` represents one of the IDs returned by the `ListOfferings` command.
Type: String to integer map
Required: No

 ** skipAppResign **   <a name="devicefarm-Type-AccountSettings-skipAppResign"></a>
When set to `true`, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.
For more information about how Device Farm re-signs your apps, see [Do you modify my app?](http://aws.amazon.com/device-farm/faqs/) in the *AWS Device Farm FAQs*.
Type: Boolean
Required: No

 ** trialMinutes **   <a name="devicefarm-Type-AccountSettings-trialMinutes"></a>
Information about an AWS account's usage of free trial device minutes.
Type: [TrialMinutes](API_TrialMinutes.md) object
Required: No

 ** unmeteredDevices **   <a name="devicefarm-Type-AccountSettings-unmeteredDevices"></a>
Returns the unmetered devices you have purchased or want to purchase.
Type: String to integer map
Valid Keys: `ANDROID | IOS`
Required: No

 ** unmeteredRemoteAccessDevices **   <a name="devicefarm-Type-AccountSettings-unmeteredRemoteAccessDevices"></a>
Returns the unmetered remote access devices you have purchased or want to purchase.
Type: String to integer map
Valid Keys: `ANDROID | IOS`
Required: No

## See Also
<a name="API_AccountSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/AccountSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/AccountSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/AccountSettings)

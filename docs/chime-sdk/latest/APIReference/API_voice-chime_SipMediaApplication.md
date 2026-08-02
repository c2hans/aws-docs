---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_SipMediaApplication.html
---

# SipMediaApplication
<a name="API_voice-chime_SipMediaApplication"></a>

The details of the SIP media application, including name and endpoints. An AWS account can have multiple SIP media applications.

## Contents
<a name="API_voice-chime_SipMediaApplication_Contents"></a>

 ** AwsRegion **   <a name="chimesdk-Type-voice-chime_SipMediaApplication-AwsRegion"></a>
The AWS Region in which the SIP media application is created.
Type: String
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_SipMediaApplication-CreatedTimestamp"></a>
The SIP media application creation timestamp, in ISO 8601 format.
Type: Timestamp
Required: No

 ** Endpoints **   <a name="chimesdk-Type-voice-chime_SipMediaApplication-Endpoints"></a>
List of endpoints for a SIP media application. Currently, only one endpoint per SIP media application is permitted.
Type: Array of [SipMediaApplicationEndpoint](API_voice-chime_SipMediaApplicationEndpoint.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_SipMediaApplication-Name"></a>
The SIP media application's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: No

 ** SipMediaApplicationArn **   <a name="chimesdk-Type-voice-chime_SipMediaApplication-SipMediaApplicationArn"></a>
The ARN of the SIP media application.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SipMediaApplicationId **   <a name="chimesdk-Type-voice-chime_SipMediaApplication-SipMediaApplicationId"></a>
A SIP media application's ID.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_SipMediaApplication-UpdatedTimestamp"></a>
The time at which the SIP media application was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_voice-chime_SipMediaApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/SipMediaApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/SipMediaApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/SipMediaApplication)

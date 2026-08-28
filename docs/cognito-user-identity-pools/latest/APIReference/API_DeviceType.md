---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DeviceType.html
---

# DeviceType
<a name="API_DeviceType"></a>

Information about a user's device that they've registered for device SRP authentication in your application. For more information, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html).

This data type is a response parameter of [AdminGetDevice](API_AdminGetDevice.md), [AdminListDevices](API_AdminListDevices.md), and [GetDevice](API_GetDevice.md).

## Contents
<a name="API_DeviceType_Contents"></a>

 ** DeviceAttributes **   <a name="CognitoUserPools-Type-DeviceType-DeviceAttributes"></a>
Metadata about a user's device, like name and last-access source IP.
Type: Array of [AttributeType](API_AttributeType.md) objects
Required: No

 ** DeviceCreateDate **   <a name="CognitoUserPools-Type-DeviceType-DeviceCreateDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** DeviceKey **   <a name="CognitoUserPools-Type-DeviceType-DeviceKey"></a>
The device key, for example `us-west-2_EXAMPLE-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-f-]+`
Required: No

 ** DeviceLastAuthenticatedDate **   <a name="CognitoUserPools-Type-DeviceType-DeviceLastAuthenticatedDate"></a>
The date when the user last signed in with the device.
Type: Timestamp
Required: No

 ** DeviceLastModifiedDate **   <a name="CognitoUserPools-Type-DeviceType-DeviceLastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

## See Also
<a name="API_DeviceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DeviceType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DeviceType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DeviceType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

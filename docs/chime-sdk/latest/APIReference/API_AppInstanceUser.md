---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceUser.html
---

# AppInstanceUser
<a name="API_AppInstanceUser"></a>

The details of an `AppInstanceUser`.

## Contents
<a name="API_AppInstanceUser_Contents"></a>

 ** AppInstanceUserArn **   <a name="chimesdk-Type-AppInstanceUser-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-AppInstanceUser-CreatedTimestamp"></a>
The time at which the `AppInstanceUser` was created.
Type: Timestamp
Required: No

 ** ExpirationSettings **   <a name="chimesdk-Type-AppInstanceUser-ExpirationSettings"></a>
The interval after which an `AppInstanceUser` is automatically deleted.
Type: [ExpirationSettings](API_ExpirationSettings.md) object
Required: No

 ** LastUpdatedTimestamp **   <a name="chimesdk-Type-AppInstanceUser-LastUpdatedTimestamp"></a>
The time at which the `AppInstanceUser` was last updated.
Type: Timestamp
Required: No

 ** Metadata **   <a name="chimesdk-Type-AppInstanceUser-Metadata"></a>
The metadata of the `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Name **   <a name="chimesdk-Type-AppInstanceUser-Name"></a>
The name of the `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AppInstanceUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/AppInstanceUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/AppInstanceUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/AppInstanceUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstance.html
---

# AppInstance
<a name="API_AppInstance"></a>

The details of an `AppInstance`, an instance of an Amazon Chime SDK messaging application.

## Contents
<a name="API_AppInstance_Contents"></a>

 ** AppInstanceArn **   <a name="chimesdk-Type-AppInstance-AppInstanceArn"></a>
The ARN of the messaging instance.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-AppInstance-CreatedTimestamp"></a>
The time at which an `AppInstance` was created. In epoch milliseconds.
Type: Timestamp
Required: No

 ** LastUpdatedTimestamp **   <a name="chimesdk-Type-AppInstance-LastUpdatedTimestamp"></a>
The time an `AppInstance` was last updated. In epoch milliseconds.
Type: Timestamp
Required: No

 ** Metadata **   <a name="chimesdk-Type-AppInstance-Metadata"></a>
The metadata of an `AppInstance`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Name **   <a name="chimesdk-Type-AppInstance-Name"></a>
The name of an `AppInstance`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: No

## See Also
<a name="API_AppInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/AppInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/AppInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/AppInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

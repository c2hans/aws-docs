---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceBot.html
---

# AppInstanceBot
<a name="API_AppInstanceBot"></a>

An Amazon Lex V2 chat bot created under an `AppInstance`.

## Contents
<a name="API_AppInstanceBot_Contents"></a>

 ** AppInstanceBotArn **   <a name="chimesdk-Type-AppInstanceBot-AppInstanceBotArn"></a>
The ARN of the AppInstanceBot.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** Configuration **   <a name="chimesdk-Type-AppInstanceBot-Configuration"></a>
The data processing instructions for an AppInstanceBot.
Type: [Configuration](API_Configuration.md) object
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-AppInstanceBot-CreatedTimestamp"></a>
The time at which the `AppInstanceBot` was created.
Type: Timestamp
Required: No

 ** LastUpdatedTimestamp **   <a name="chimesdk-Type-AppInstanceBot-LastUpdatedTimestamp"></a>
The time at which the `AppInstanceBot` was last updated.
Type: Timestamp
Required: No

 ** Metadata **   <a name="chimesdk-Type-AppInstanceBot-Metadata"></a>
The metadata for an AppInstanceBot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Name **   <a name="chimesdk-Type-AppInstanceBot-Name"></a>
The name of the AppInstanceBot.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u0085\u00A0-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]*`
Required: No

## See Also
<a name="API_AppInstanceBot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/AppInstanceBot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/AppInstanceBot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/AppInstanceBot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

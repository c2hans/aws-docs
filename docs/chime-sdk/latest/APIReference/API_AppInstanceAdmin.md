---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceAdmin.html
---

# AppInstanceAdmin
<a name="API_AppInstanceAdmin"></a>

The name and ARN of the admin for the `AppInstance`.

## Contents
<a name="API_AppInstanceAdmin_Contents"></a>

 ** Admin **   <a name="chimesdk-Type-AppInstanceAdmin-Admin"></a>
The `AppInstanceAdmin` data.
Type: [Identity](API_Identity.md) object
Required: No

 ** AppInstanceArn **   <a name="chimesdk-Type-AppInstanceAdmin-AppInstanceArn"></a>
The ARN of the `AppInstance` for which the user is an administrator.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-AppInstanceAdmin-CreatedTimestamp"></a>
The time at which an administrator was created.
Type: Timestamp
Required: No

## See Also
<a name="API_AppInstanceAdmin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/AppInstanceAdmin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/AppInstanceAdmin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/AppInstanceAdmin)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

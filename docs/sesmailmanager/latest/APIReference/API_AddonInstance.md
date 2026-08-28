---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_AddonInstance.html
---

# AddonInstance
<a name="API_AddonInstance"></a>

An Add On instance represents a specific configuration of an Add On.

## Contents
<a name="API_AddonInstance_Contents"></a>

 ** AddonInstanceArn **   <a name="sesmailmanager-Type-AddonInstance-AddonInstanceArn"></a>
The Amazon Resource Name (ARN) of the Add On instance.
Type: String
Required: No

 ** AddonInstanceId **   <a name="sesmailmanager-Type-AddonInstance-AddonInstanceId"></a>
The unique ID of the Add On instance.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `ai-[a-zA-Z0-9]{1,64}`
Required: No

 ** AddonName **   <a name="sesmailmanager-Type-AddonInstance-AddonName"></a>
The name of the Add On for the instance.
Type: String
Required: No

 ** AddonSubscriptionId **   <a name="sesmailmanager-Type-AddonInstance-AddonSubscriptionId"></a>
The subscription ID for the instance.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `as-[a-zA-Z0-9]{1,64}`
Required: No

 ** CreatedTimestamp **   <a name="sesmailmanager-Type-AddonInstance-CreatedTimestamp"></a>
The timestamp of when the Add On instance was created.
Type: Timestamp
Required: No

## See Also
<a name="API_AddonInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/AddonInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/AddonInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/AddonInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_AddonSubscription.html
---

# AddonSubscription
<a name="API_AddonSubscription"></a>

A subscription for an Add On representing the acceptance of its terms of use and additional pricing.

## Contents
<a name="API_AddonSubscription_Contents"></a>

 ** AddonName **   <a name="sesmailmanager-Type-AddonSubscription-AddonName"></a>
The name of the Add On.
Type: String
Required: No

 ** AddonSubscriptionArn **   <a name="sesmailmanager-Type-AddonSubscription-AddonSubscriptionArn"></a>
The Amazon Resource Name (ARN) of the Add On subscription.
Type: String
Required: No

 ** AddonSubscriptionId **   <a name="sesmailmanager-Type-AddonSubscription-AddonSubscriptionId"></a>
The unique ID of the Add On subscription.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 67.
Pattern: `as-[a-zA-Z0-9]{1,64}`
Required: No

 ** CreatedTimestamp **   <a name="sesmailmanager-Type-AddonSubscription-CreatedTimestamp"></a>
The timestamp of when the Add On subscription was created.
Type: Timestamp
Required: No

## See Also
<a name="API_AddonSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/AddonSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/AddonSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/AddonSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

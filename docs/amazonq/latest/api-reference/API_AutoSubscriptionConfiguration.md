---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AutoSubscriptionConfiguration.html
---

# AutoSubscriptionConfiguration
<a name="API_AutoSubscriptionConfiguration"></a>

Subscription configuration information for an Amazon Q Business application using IAM identity federation for user management.

## Contents
<a name="API_AutoSubscriptionConfiguration_Contents"></a>

 ** autoSubscribe **   <a name="qbusiness-Type-AutoSubscriptionConfiguration-autoSubscribe"></a>
Describes whether automatic subscriptions are enabled for an Amazon Q Business application using IAM identity federation for user management.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** defaultSubscriptionType **   <a name="qbusiness-Type-AutoSubscriptionConfiguration-defaultSubscriptionType"></a>
Describes the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management. If the value for `autoSubscribe` is set to `ENABLED` you must select a value for this field.
Type: String
Valid Values: `Q_LITE | Q_BUSINESS`
Required: No

## See Also
<a name="API_AutoSubscriptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AutoSubscriptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AutoSubscriptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AutoSubscriptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

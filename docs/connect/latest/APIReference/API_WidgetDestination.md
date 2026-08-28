---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_WidgetDestination.html
---

# WidgetDestination
<a name="API_WidgetDestination"></a>

The destination for an outbound web notification, specifying the communication widget that delivers the notification and the customer profile of the recipient.

## Contents
<a name="API_WidgetDestination_Contents"></a>

 ** ProfileId **   <a name="connect-Type-WidgetDestination-ProfileId"></a>
The identifier of the customer profile associated with the browser session that should receive the notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** WidgetId **   <a name="connect-Type-WidgetDestination-WidgetId"></a>
The identifier of the communication widget that delivers the notification to the customer's browser.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

## See Also
<a name="API_WidgetDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/WidgetDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/WidgetDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/WidgetDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

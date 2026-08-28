---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_IspPlacement.html
---

# IspPlacement
<a name="API_IspPlacement"></a>

An object that describes how email sent during the predictive inbox placement test was handled by a certain email provider.

## Contents
<a name="API_IspPlacement_Contents"></a>

 ** IspName **   <a name="pinpoint-Type-IspPlacement-IspName"></a>
The name of the email provider that the inbox placement data applies to.
Type: String
Required: No

 ** PlacementStatistics **   <a name="pinpoint-Type-IspPlacement-PlacementStatistics"></a>
An object that contains inbox placement metrics for a specific email provider.
Type: [PlacementStatistics](API_PlacementStatistics.md) object
Required: No

## See Also
<a name="API_IspPlacement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/IspPlacement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/IspPlacement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/IspPlacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

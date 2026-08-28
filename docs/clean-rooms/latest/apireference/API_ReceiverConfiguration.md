---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ReceiverConfiguration.html
---

# ReceiverConfiguration
<a name="API_ReceiverConfiguration"></a>

 The receiver configuration for a protected query.

## Contents
<a name="API_ReceiverConfiguration_Contents"></a>

 ** analysisType **   <a name="API-Type-ReceiverConfiguration-analysisType"></a>
 The type of analysis for the protected query. The results of the query can be analyzed directly (`DIRECT_ANALYSIS`) or used as input into additional analyses (`ADDITIONAL_ANALYSIS`), such as a query that is a seed for a lookalike ML model.
Type: String
Valid Values: `DIRECT_ANALYSIS | ADDITIONAL_ANALYSIS`
Required: Yes

 ** configurationDetails **   <a name="API-Type-ReceiverConfiguration-configurationDetails"></a>
 The configuration details of the receiver configuration.
Type: [ConfigurationDetails](API_ConfigurationDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ReceiverConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ReceiverConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ReceiverConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ReceiverConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

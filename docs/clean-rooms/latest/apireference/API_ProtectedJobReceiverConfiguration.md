---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedJobReceiverConfiguration.html
---

# ProtectedJobReceiverConfiguration
<a name="API_ProtectedJobReceiverConfiguration"></a>

The protected job receiver configuration.

## Contents
<a name="API_ProtectedJobReceiverConfiguration_Contents"></a>

 ** analysisType **   <a name="API-Type-ProtectedJobReceiverConfiguration-analysisType"></a>
 The analysis type for the protected job receiver configuration.
Type: String
Valid Values: `DIRECT_ANALYSIS`
Required: Yes

 ** configurationDetails **   <a name="API-Type-ProtectedJobReceiverConfiguration-configurationDetails"></a>
 The configuration details for the protected job receiver.
Type: [ProtectedJobConfigurationDetails](API_ProtectedJobConfigurationDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ProtectedJobReceiverConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedJobReceiverConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedJobReceiverConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedJobReceiverConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

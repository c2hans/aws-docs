---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_LinkConfiguration.html
---

# LinkConfiguration
<a name="API_LinkConfiguration"></a>

Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.

## Contents
<a name="API_LinkConfiguration_Contents"></a>

 ** LogGroupConfiguration **   <a name="OAM-Type-LinkConfiguration-LogGroupConfiguration"></a>
Use this structure to filter which log groups are to send log events from the source account to the monitoring account.
Type: [LogGroupConfiguration](API_LogGroupConfiguration.md) object
Required: No

 ** MetricConfiguration **   <a name="OAM-Type-LinkConfiguration-MetricConfiguration"></a>
Use this structure to filter which metric namespaces are to be shared from the source account to the monitoring account.
Type: [MetricConfiguration](API_MetricConfiguration.md) object
Required: No

## See Also
<a name="API_LinkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/LinkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/LinkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/LinkConfiguration)

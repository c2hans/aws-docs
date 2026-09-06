---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationCodeConfigurationUpdate.html
---

# ApplicationCodeConfigurationUpdate
<a name="API_ApplicationCodeConfigurationUpdate"></a>

Describes code configuration updates for an application. This is supported for a Managed Service for Apache Flink application or a SQL-based Kinesis Data Analytics application.

## Contents
<a name="API_ApplicationCodeConfigurationUpdate_Contents"></a>

 ** CodeContentTypeUpdate **   <a name="APIReference-Type-ApplicationCodeConfigurationUpdate-CodeContentTypeUpdate"></a>
Describes updates to the code content type.
Type: String
Valid Values: `PLAINTEXT | ZIPFILE`
Required: No

 ** CodeContentUpdate **   <a name="APIReference-Type-ApplicationCodeConfigurationUpdate-CodeContentUpdate"></a>
Describes updates to the code content of an application.
Type: [CodeContentUpdate](API_CodeContentUpdate.md) object
Required: No

## See Also
<a name="API_ApplicationCodeConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationCodeConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationCodeConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationCodeConfigurationUpdate)

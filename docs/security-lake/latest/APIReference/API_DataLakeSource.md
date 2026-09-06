---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeSource.html
---

# DataLakeSource
<a name="API_DataLakeSource"></a>

Amazon Security Lake collects logs and events from supported AWS services and custom sources. For the list of supported AWS services, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html).

## Contents
<a name="API_DataLakeSource_Contents"></a>

 ** account **   <a name="securitylake-Type-DataLakeSource-account"></a>
The ID of the Security Lake account for which logs are collected.
Type: String
Required: No

 ** eventClasses **   <a name="securitylake-Type-DataLakeSource-eventClasses"></a>
The Open Cybersecurity Schema Framework (OCSF) event classes describes the type of data that the custom source will send to Security Lake. For the list of supported event classes, see [Supported OCSF Event classes](https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html#ocsf-eventclass.html) in the Amazon Security Lake User Guide.
Type: Array of strings
Pattern: `[A-Z\_0-9]*`
Required: No

 ** sourceName **   <a name="securitylake-Type-DataLakeSource-sourceName"></a>
The supported AWS services from which logs and events are collected. Amazon Security Lake supports log and event collection for natively supported AWS services.
Type: String
Required: No

 ** sourceStatuses **   <a name="securitylake-Type-DataLakeSource-sourceStatuses"></a>
The log status for the Security Lake account.
Type: Array of [DataLakeSourceStatus](API_DataLakeSourceStatus.md) objects
Required: No

## See Also
<a name="API_DataLakeSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DataLakeSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DataLakeSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DataLakeSource)

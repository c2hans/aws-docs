---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ServiceQuotaExceededExceptionReason.html
---

# ServiceQuotaExceededExceptionReason
<a name="API_ServiceQuotaExceededExceptionReason"></a>

The reason for the exception.

## Contents
<a name="API_ServiceQuotaExceededExceptionReason_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AttachedFileServiceQuotaExceededExceptionReason **   <a name="connect-Type-ServiceQuotaExceededExceptionReason-AttachedFileServiceQuotaExceededExceptionReason"></a>
Total file size of all files or total number of files exceeds the service quota
Type: String
Valid Values: `TOTAL_FILE_SIZE_EXCEEDED | TOTAL_FILE_COUNT_EXCEEDED`
Required: No

## See Also
<a name="API_ServiceQuotaExceededExceptionReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ServiceQuotaExceededExceptionReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ServiceQuotaExceededExceptionReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ServiceQuotaExceededExceptionReason)

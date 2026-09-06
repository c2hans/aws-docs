---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_LogGroupSummary.html
---

# LogGroupSummary
<a name="API_LogGroupSummary"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

A subset of the attributes that describe a log group. In CloudWatch a log group is a group of log streams that share the same retention, monitoring, and access control settings.

## Contents
<a name="API_LogGroupSummary_Contents"></a>

 ** logGroupName **   <a name="m2-Type-LogGroupSummary-logGroupName"></a>
The name of the log group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** logType **   <a name="m2-Type-LogGroupSummary-logType"></a>
The type of log.
Type: String
Pattern: `\S{1,20}`
Required: Yes

## See Also
<a name="API_LogGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/LogGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/LogGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/LogGroupSummary)

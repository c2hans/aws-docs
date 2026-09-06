---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_ApplicationVersionSummary.html
---

# ApplicationVersionSummary
<a name="API_ApplicationVersionSummary"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Defines an application version summary.

## Contents
<a name="API_ApplicationVersionSummary_Contents"></a>

 ** applicationVersion **   <a name="m2-Type-ApplicationVersionSummary-applicationVersion"></a>
The application version.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** creationTime **   <a name="m2-Type-ApplicationVersionSummary-creationTime"></a>
The timestamp when the application version was created.
Type: Timestamp
Required: Yes

 ** status **   <a name="m2-Type-ApplicationVersionSummary-status"></a>
The status of the application.
Type: String
Valid Values: `Creating | Available | Failed`
Required: Yes

 ** statusReason **   <a name="m2-Type-ApplicationVersionSummary-statusReason"></a>
The reason for the reported status.
Type: String
Required: No

## See Also
<a name="API_ApplicationVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/ApplicationVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/ApplicationVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/ApplicationVersionSummary)

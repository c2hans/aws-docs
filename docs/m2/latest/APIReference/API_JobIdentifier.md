---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_JobIdentifier.html
---

# JobIdentifier
<a name="API_JobIdentifier"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Identifies a specific batch job.

## Contents
<a name="API_JobIdentifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fileName **   <a name="m2-Type-JobIdentifier-fileName"></a>
The name of the file that contains the batch job definition.
Type: String
Required: No

 ** scriptName **   <a name="m2-Type-JobIdentifier-scriptName"></a>
The name of the script that contains the batch job definition.
Type: String
Required: No

## See Also
<a name="API_JobIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/JobIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/JobIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/JobIdentifier)

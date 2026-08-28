---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_AlternateKey.html
---

# AlternateKey
<a name="API_AlternateKey"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Defines an alternate key. This value is optional. A legacy data set might not have any alternate key defined but if those alternate keys definitions exist, provide them, as some applications will make use of them.

## Contents
<a name="API_AlternateKey_Contents"></a>

 ** length **   <a name="m2-Type-AlternateKey-length"></a>
A strictly positive integer value representing the length of the alternate key.
Type: Integer
Required: Yes

 ** offset **   <a name="m2-Type-AlternateKey-offset"></a>
A positive integer value representing the offset to mark the start of the alternate key part in the record byte array.
Type: Integer
Required: Yes

 ** allowDuplicates **   <a name="m2-Type-AlternateKey-allowDuplicates"></a>
Indicates whether the alternate key values are supposed to be unique for the given data set.
Type: Boolean
Required: No

 ** name **   <a name="m2-Type-AlternateKey-name"></a>
The name of the alternate key.
Type: String
Required: No

## See Also
<a name="API_AlternateKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/AlternateKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/AlternateKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/AlternateKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

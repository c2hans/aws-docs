---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_GdgAttributes.html
---

# GdgAttributes
<a name="API_GdgAttributes"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

The required attributes for a generation data group data set. A generation data set is one of a collection of successive, historically related, catalogued data sets that together are known as a generation data group (GDG). Use this structure when you want to import a GDG. For more information on GDG, see [Generation data sets](https://www.ibm.com/docs/en/zos/2.3.0?topic=guide-generation-data-sets).

## Contents
<a name="API_GdgAttributes_Contents"></a>

 ** limit **   <a name="m2-Type-GdgAttributes-limit"></a>
The maximum number of generation data sets, up to 255, in a GDG.
Type: Integer
Required: No

 ** rollDisposition **   <a name="m2-Type-GdgAttributes-rollDisposition"></a>
The disposition of the data set in the catalog.
Type: String
Required: No

## See Also
<a name="API_GdgAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/GdgAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/GdgAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/GdgAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

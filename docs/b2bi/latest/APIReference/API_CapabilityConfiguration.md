---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CapabilityConfiguration.html
---

# CapabilityConfiguration
<a name="API_CapabilityConfiguration"></a>

A capability object. Currently, only EDI (electronic data interchange) capabilities are supported. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

## Contents
<a name="API_CapabilityConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** edi **   <a name="b2bi-Type-CapabilityConfiguration-edi"></a>
An EDI (electronic data interchange) configuration object.
Type: [EdiConfiguration](API_EdiConfiguration.md) object
Required: No

## See Also
<a name="API_CapabilityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/CapabilityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/CapabilityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/CapabilityConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

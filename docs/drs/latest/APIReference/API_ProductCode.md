---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ProductCode.html
---

# ProductCode
<a name="API_ProductCode"></a>

Properties of a product code associated with a volume.

## Contents
<a name="API_ProductCode_Contents"></a>

 ** productCodeId **   <a name="drs-Type-ProductCode-productCodeId"></a>
Id of a product code associated with a volume.
Type: String
Length Constraints: Fixed length of 25.
Pattern: `([A-Za-z0-9])+`
Required: No

 ** productCodeMode **   <a name="drs-Type-ProductCode-productCodeMode"></a>
Mode of a product code associated with a volume.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ProductCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ProductCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ProductCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ProductCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ProductCodeListItem.html
---

# ProductCodeListItem
<a name="API_ProductCodeListItem"></a>

Information about a single product code.

## Contents
<a name="API_ProductCodeListItem_Contents"></a>

 ** productCodeId **   <a name="imagebuilder-Type-ProductCodeListItem-productCodeId"></a>
For AWS Marketplace components, this contains the product code ID that can be stamped onto an EC2 AMI to ensure that components are billed correctly. If this property is empty, it might mean that the component is not published.
Type: String
Pattern: `^[A-Za-z0-9]{1,25}$`
Required: Yes

 ** productCodeType **   <a name="imagebuilder-Type-ProductCodeListItem-productCodeType"></a>
The owner of the product code that's billed. If this property is empty, it might mean that the component is not published.
Type: String
Valid Values: `marketplace`
Required: Yes

## See Also
<a name="API_ProductCodeListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ProductCodeListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ProductCodeListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ProductCodeListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

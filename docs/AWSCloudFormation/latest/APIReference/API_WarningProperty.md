---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_WarningProperty.html
---

# WarningProperty
<a name="API_WarningProperty"></a>

A specific property that is impacted by a warning.

## Contents
<a name="API_WarningProperty_Contents"></a>

 ** Description **
The description of the property from the resource provider schema.
Type: String
Required: No

 ** PropertyPath **
The path of the property. For example, if this is for the `S3Bucket` member of the `Code` property, the property path would be `Code/S3Bucket`.
Type: String
Required: No

 ** Required **
If `true`, the specified property is required.
Type: Boolean
Required: No

## See Also
<a name="API_WarningProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/WarningProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/WarningProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/WarningProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

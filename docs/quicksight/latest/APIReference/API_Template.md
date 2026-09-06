---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Template.html
---

# Template
<a name="API_Template"></a>

A template object. A *template* is an entity in Quick Sight that encapsulates the metadata required to create an analysis and that you can use to create a dashboard. A template adds a layer of abstraction by using placeholders to replace the dataset associated with an analysis. You can use templates to create dashboards by replacing dataset placeholders with datasets that follow the same schema that was used to create the source analysis and template.

You can share templates across AWS accounts by allowing users in other AWS accounts to create a template or a dashboard from an existing template.

## Contents
<a name="API_Template_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-Template-Arn"></a>
The Amazon Resource Name (ARN) of the template.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-Template-CreatedTime"></a>
Time when this was created.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-Template-LastUpdatedTime"></a>
Time when this was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-Template-Name"></a>
The display name of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** TemplateId **   <a name="QS-Type-Template-TemplateId"></a>
The ID for the template. This is unique per AWS Region for each AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** Version **   <a name="QS-Type-Template-Version"></a>
A structure describing the versions of the template.
Type: [TemplateVersion](API_TemplateVersion.md) object
Required: No

## See Also
<a name="API_Template_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Template)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Template)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Template)

---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BorderSettings.html
---

# BorderSettings
<a name="API_BorderSettings"></a>

Border settings configuration for visual elements, including visibility, width, and color properties.

## Contents
<a name="API_BorderSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BorderColor **   <a name="QS-Type-BorderSettings-BorderColor"></a>
Color of the border.
Type: String
Pattern: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
Required: No

 ** BorderVisibility **   <a name="QS-Type-BorderSettings-BorderVisibility"></a>
Visibility setting for the border.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** BorderWidth **   <a name="QS-Type-BorderSettings-BorderWidth"></a>
Width of the border. Valid range is from 1px to 8px.
Type: String
Required: No

## See Also
<a name="API_BorderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BorderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BorderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BorderSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

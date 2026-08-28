---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabelsSettings.html
---

# DetectLabelsSettings
<a name="API_DetectLabelsSettings"></a>

Settings for the DetectLabels request. Settings can include filters for both GENERAL\_LABELS and IMAGE\_PROPERTIES. GENERAL\_LABELS filters can be inclusive or exclusive and applied to individual labels or label categories. IMAGE\_PROPERTIES filters allow specification of a maximum number of dominant colors.

## Contents
<a name="API_DetectLabelsSettings_Contents"></a>

 ** GeneralLabels **   <a name="rekognition-Type-DetectLabelsSettings-GeneralLabels"></a>
Contains the specified filters for GENERAL\_LABELS.
Type: [GeneralLabelsSettings](API_GeneralLabelsSettings.md) object
Required: No

 ** ImageProperties **   <a name="rekognition-Type-DetectLabelsSettings-ImageProperties"></a>
Contains the chosen number of maximum dominant colors in an image.
Type: [DetectLabelsImagePropertiesSettings](API_DetectLabelsImagePropertiesSettings.md) object
Required: No

## See Also
<a name="API_DetectLabelsSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DetectLabelsSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DetectLabelsSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DetectLabelsSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

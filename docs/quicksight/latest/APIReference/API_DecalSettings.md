---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DecalSettings.html
---

# DecalSettings
<a name="API_DecalSettings"></a>

Decal settings for accessibility features that define visual patterns and styling for data elements.

## Contents
<a name="API_DecalSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DecalColor **   <a name="QS-Type-DecalSettings-DecalColor"></a>
Color configuration for the decal pattern.
Type: String
Pattern: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
Required: No

 ** DecalPatternType **   <a name="QS-Type-DecalSettings-DecalPatternType"></a>
Type of pattern used for the decal, such as solid, diagonal, or circular patterns in various sizes.
+  `SOLID`: Solid fill pattern.
+  `DIAGONAL_SMALL`: Small diagonal stripes pattern.
+  `DIAGONAL_MEDIUM`: Medium diagonal stripes pattern.
+  `DIAGONAL_LARGE`: Large diagonal stripes pattern.
+  `DIAGONAL_OPPOSITE_SMALL`: Small cross-diagonal stripes pattern.
+  `DIAGONAL_OPPOSITE_MEDIUM`: Medium cross-diagonal stripes pattern.
+  `DIAGONAL_OPPOSITE_LARGE`: Large cross-diagonal stripes pattern.
+  `CIRCLE_SMALL`: Small circle pattern.
+  `CIRCLE_MEDIUM`: Medium circle pattern.
+  `CIRCLE_LARGE`: Large circle pattern.
+  `DIAMOND_SMALL`: Small diamonds pattern.
+  `DIAMOND_MEDIUM`: Medium diamonds pattern.
+  `DIAMOND_LARGE`: Large diamonds pattern.
+  `DIAMOND_GRID_SMALL`: Small diamond grid pattern.
+  `DIAMOND_GRID_MEDIUM`: Medium diamond grid pattern.
+  `DIAMOND_GRID_LARGE`: Large diamond grid pattern.
+  `CHECKERBOARD_SMALL`: Small checkerboard pattern.
+  `CHECKERBOARD_MEDIUM`: Medium checkerboard pattern.
+  `CHECKERBOARD_LARGE`: Large checkerboard pattern.
+  `TRIANGLE_SMALL`: Small triangles pattern.
+  `TRIANGLE_MEDIUM`: Medium triangles pattern.
+  `TRIANGLE_LARGE`: Large triangles pattern.
Type: String
Valid Values: `SOLID | DIAGONAL_MEDIUM | CIRCLE_MEDIUM | DIAMOND_GRID_MEDIUM | CHECKERBOARD_MEDIUM | TRIANGLE_MEDIUM | DIAGONAL_OPPOSITE_MEDIUM | DIAMOND_MEDIUM | DIAGONAL_LARGE | CIRCLE_LARGE | DIAMOND_GRID_LARGE | CHECKERBOARD_LARGE | TRIANGLE_LARGE | DIAGONAL_OPPOSITE_LARGE | DIAMOND_LARGE | DIAGONAL_SMALL | CIRCLE_SMALL | DIAMOND_GRID_SMALL | CHECKERBOARD_SMALL | TRIANGLE_SMALL | DIAGONAL_OPPOSITE_SMALL | DIAMOND_SMALL`
Required: No

 ** DecalStyleType **   <a name="QS-Type-DecalSettings-DecalStyleType"></a>
Style type for the decal, which can be either manual or automatic. This field is only applicable for line series.
+  `Manual`: Apply manual line and marker configuration for line series.
+  `Auto`: Apply automatic line and marker configuration for line series.
Type: String
Valid Values: `Manual | Auto`
Required: No

 ** DecalVisibility **   <a name="QS-Type-DecalSettings-DecalVisibility"></a>
Visibility setting for the decal pattern.
Type: String
Valid Values: `HIDDEN | VISIBLE`
Required: No

 ** ElementValue **   <a name="QS-Type-DecalSettings-ElementValue"></a>
Field value of the field that you are setting the decal pattern to. Applicable only for field level settings.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_DecalSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DecalSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DecalSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DecalSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

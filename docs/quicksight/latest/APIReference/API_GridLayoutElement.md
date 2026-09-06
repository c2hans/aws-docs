---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GridLayoutElement.html
---

# GridLayoutElement
<a name="API_GridLayoutElement"></a>

An element within a grid layout.

## Contents
<a name="API_GridLayoutElement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ColumnSpan **   <a name="QS-Type-GridLayoutElement-ColumnSpan"></a>
The width of a grid element expressed as a number of grid columns.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 36.
Required: Yes

 ** ElementId **   <a name="QS-Type-GridLayoutElement-ElementId"></a>
A unique identifier for an element within a grid layout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** ElementType **   <a name="QS-Type-GridLayoutElement-ElementType"></a>
The type of element.
Type: String
Valid Values: `VISUAL | FILTER_CONTROL | PARAMETER_CONTROL | TEXT_BOX | IMAGE`
Required: Yes

 ** RowSpan **   <a name="QS-Type-GridLayoutElement-RowSpan"></a>
The height of a grid element expressed as a number of grid rows.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 21.
Required: Yes

 ** BackgroundStyle **   <a name="QS-Type-GridLayoutElement-BackgroundStyle"></a>
The background style configuration of a grid layout element.
Type: [GridLayoutElementBackgroundStyle](API_GridLayoutElementBackgroundStyle.md) object
Required: No

 ** BorderRadius **   <a name="QS-Type-GridLayoutElement-BorderRadius"></a>
The border radius of a grid layout element.
Type: String
Length Constraints: Maximum length of 50.
Required: No

 ** BorderStyle **   <a name="QS-Type-GridLayoutElement-BorderStyle"></a>
The border style configuration of a grid layout element.
Type: [GridLayoutElementBorderStyle](API_GridLayoutElementBorderStyle.md) object
Required: No

 ** ColumnIndex **   <a name="QS-Type-GridLayoutElement-ColumnIndex"></a>
The column index for the upper left corner of an element.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 35.
Required: No

 ** LoadingAnimation **   <a name="QS-Type-GridLayoutElement-LoadingAnimation"></a>
The configuration of loading animation in free-form layout.
Type: [LoadingAnimation](API_LoadingAnimation.md) object
Required: No

 ** Padding **   <a name="QS-Type-GridLayoutElement-Padding"></a>
The padding of a grid layout element.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** RowIndex **   <a name="QS-Type-GridLayoutElement-RowIndex"></a>
The row index for the upper left corner of an element.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 9009.
Required: No

 ** SelectedBorderStyle **   <a name="QS-Type-GridLayoutElement-SelectedBorderStyle"></a>
The border style configuration of a grid layout element. This border style is used when the element is selected.
Type: [GridLayoutElementBorderStyle](API_GridLayoutElementBorderStyle.md) object
Required: No

## See Also
<a name="API_GridLayoutElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GridLayoutElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GridLayoutElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GridLayoutElement)

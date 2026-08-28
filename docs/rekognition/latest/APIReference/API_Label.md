---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Label.html
---

# Label
<a name="API_Label"></a>

Structure containing details about the detected label, including the name, detected instances, parent labels, and level of confidence.

## Contents
<a name="API_Label_Contents"></a>

 ** Aliases **   <a name="rekognition-Type-Label-Aliases"></a>
A list of potential aliases for a given label.
Type: Array of [LabelAlias](API_LabelAlias.md) objects
Required: No

 ** Categories **   <a name="rekognition-Type-Label-Categories"></a>
A list of the categories associated with a given label.
Type: Array of [LabelCategory](API_LabelCategory.md) objects
Required: No

 ** Confidence **   <a name="rekognition-Type-Label-Confidence"></a>
Level of confidence.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Instances **   <a name="rekognition-Type-Label-Instances"></a>
If `Label` represents an object, `Instances` contains the bounding boxes for each instance of the detected object. Bounding boxes are returned for common object labels such as people, cars, furniture, apparel or pets.
Type: Array of [Instance](API_Instance.md) objects
Required: No

 ** Name **   <a name="rekognition-Type-Label-Name"></a>
The name (label) of the object or scene.
Type: String
Required: No

 ** Parents **   <a name="rekognition-Type-Label-Parents"></a>
The parent labels for a label. The response includes all ancestor labels.
Type: Array of [Parent](API_Parent.md) objects
Required: No

## See Also
<a name="API_Label_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Label)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/Label)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/Label)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_HumanLoopDataAttributes.html
---

# HumanLoopDataAttributes
<a name="API_HumanLoopDataAttributes"></a>

Allows you to set attributes of the image. Currently, you can declare an image as free of personally identifiable information.

## Contents
<a name="API_HumanLoopDataAttributes_Contents"></a>

 ** ContentClassifiers **   <a name="rekognition-Type-HumanLoopDataAttributes-ContentClassifiers"></a>
Sets whether the input image is free of personally identifiable information.
Type: Array of strings
Array Members: Maximum number of 256 items.
Valid Values: `FreeOfPersonallyIdentifiableInformation | FreeOfAdultContent`
Required: No

## See Also
<a name="API_HumanLoopDataAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/HumanLoopDataAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/HumanLoopDataAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/HumanLoopDataAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

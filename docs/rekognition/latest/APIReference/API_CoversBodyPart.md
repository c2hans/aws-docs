---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CoversBodyPart.html
---

# CoversBodyPart
<a name="API_CoversBodyPart"></a>

Information about an item of Personal Protective Equipment covering a corresponding body part. For more information, see [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md).

## Contents
<a name="API_CoversBodyPart_Contents"></a>

 ** Confidence **   <a name="rekognition-Type-CoversBodyPart-Confidence"></a>
The confidence that Amazon Rekognition has in the value of `Value`.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Value **   <a name="rekognition-Type-CoversBodyPart-Value"></a>
True if the PPE covers the corresponding body part, otherwise false.
Type: Boolean
Required: No

## See Also
<a name="API_CoversBodyPart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CoversBodyPart)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CoversBodyPart)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CoversBodyPart)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

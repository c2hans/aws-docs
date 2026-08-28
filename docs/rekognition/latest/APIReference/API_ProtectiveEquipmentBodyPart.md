---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ProtectiveEquipmentBodyPart.html
---

# ProtectiveEquipmentBodyPart
<a name="API_ProtectiveEquipmentBodyPart"></a>

Information about a body part detected by [DetectProtectiveEquipment](API_DetectProtectiveEquipment.md) that contains PPE. An array of `ProtectiveEquipmentBodyPart` objects is returned for each person detected by `DetectProtectiveEquipment`.

## Contents
<a name="API_ProtectiveEquipmentBodyPart_Contents"></a>

 ** Confidence **   <a name="rekognition-Type-ProtectiveEquipmentBodyPart-Confidence"></a>
The confidence that Amazon Rekognition has in the detection accuracy of the detected body part.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** EquipmentDetections **   <a name="rekognition-Type-ProtectiveEquipmentBodyPart-EquipmentDetections"></a>
An array of Personal Protective Equipment items detected around a body part.
Type: Array of [EquipmentDetection](API_EquipmentDetection.md) objects
Required: No

 ** Name **   <a name="rekognition-Type-ProtectiveEquipmentBodyPart-Name"></a>
The detected body part.
Type: String
Valid Values: `FACE | HEAD | LEFT_HAND | RIGHT_HAND`
Required: No

## See Also
<a name="API_ProtectiveEquipmentBodyPart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProtectiveEquipmentBodyPart)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProtectiveEquipmentBodyPart)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProtectiveEquipmentBodyPart)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

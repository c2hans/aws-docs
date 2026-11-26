---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_EncounterContext.html
---

# EncounterContext

Context information about the clinical encounter

## Contents
<a name="API_EncounterContext_Contents"></a>

 ** medicalCodingContext **   <a name="connecthealth-Type-EncounterContext-medicalCodingContext"></a>
Structured patient and encounter context for medical code generation.
Type: [MedicalCodingContext](API_MedicalCodingContext.md) object
Required: No

 ** unstructuredContext **   <a name="connecthealth-Type-EncounterContext-unstructuredContext"></a>
Unstructured context information in markdown format. The service uses this field for two purposes:
+ Clinical documentation: You can include background not spoken aloud during the visit, such as the reason for the visit, active problems, current medications, and allergies. After the session, the service uses this context together with the transcript to generate the clinical documentation.
+ Real-time periodontal charting: You can include a periodontal exam setup block, described below, to specify which teeth are missing and the charting order. The block can share this field with other context.
Real-time extraction is in preview release for Amazon Connect Health and is subject to change. To request access to this feature, contact your AWS account team.
If the session includes a periodontal exam, you can include a periodontal exam setup block in this field. The block tells the service which teeth are missing and the order in which the clinician charts the mouth. With that information, the service charts dictated values that don't name a tooth at the correct position. The block is optional. Without it, the service assumes that all 32 teeth are present and charts them in the `quadrant_by_quadrant` order.
The block starts with a line that contains only `[PERIO_EXAM_SETUP v1]` and ends with a line that contains only `[/PERIO_EXAM_SETUP]`. These two lines must appear exactly as shown. Keys and values are not case sensitive, and every key is optional.
Each line between the two marker lines contains one of the following keys, followed by a colon and a value:
+  `numbering`: The tooth numbering system, for example `numbering: universal`. The only valid value is `universal`, which is the default.
+  `route`: The order in which the clinician charts the mouth, for example `route: quadrant_by_quadrant`. The default is `quadrant_by_quadrant`. For the valid values, see the next list.
+  `missing_teeth`: A comma-separated list of the teeth that are missing, by tooth number from 1 to 32, for example `missing_teeth: 1,16,17,32`. These teeth appear in the periodontal chart with `missing` set to `true`, and the service skips them when it charts dictated values. By default, no teeth are missing.
The `route` key accepts the following values, in which you can separate words with underscores, hyphens, or spaces:
+  `quadrant_by_quadrant`: One quadrant at a time, in the order teeth 1 to 8, 9 to 16, 17 to 24, and 25 to 32. In each quadrant, the buccal surfaces in ascending tooth order, then the lingual surfaces in descending order.
+  `arch_buccal_then_lingual`: The upper arch (teeth 1 to 16), then the lower arch (teeth 17 to 32). In each arch, the buccal surfaces in ascending tooth order, then the lingual surfaces in descending order.
+  `reverse_start_upper_left`: The upper arch, then the lower arch. In each arch, the buccal surfaces in descending tooth order, then the lingual surfaces in ascending order.
+  `all_buccal_then_all_lingual`: The buccal surfaces of all teeth from 1 to 32, then the lingual surfaces from 32 to 1.
+  `sextant_serpentine`: One sextant at a time, in the order teeth 1 to 5, 6 to 11, 12 to 16, 17 to 21, 22 to 27, and 28 to 32. In each sextant, the buccal surfaces, then the lingual surfaces, with the direction reversed from one sextant to the next.
The block, including the marker lines, can contain up to 1,024 characters. The service ignores a longer block. If this field contains more than one block, the service uses only the first. If the service can't read the block, for example because it contains a value that isn't valid, it charts the session as if the block were absent and adds a review item with the reason `SESSION_ISSUE` to the first periodontal chart event.
Type: String
Pattern: `[\p{L}\p{N}\s\*_\-#\[\]\(\)\.,:;!?'"`<>~/|+=&%@\\{}^]+`
Required: No

## See Also
<a name="API_EncounterContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/EncounterContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/EncounterContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/EncounterContext)

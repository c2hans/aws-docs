---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Challenge.html
---

# Challenge
<a name="API_Challenge"></a>

Describes the type and version of the challenge being used for the Face Liveness session.

## Contents
<a name="API_Challenge_Contents"></a>

 ** Type **   <a name="rekognition-Type-Challenge-Type"></a>
The type of the challenge being used for the Face Liveness session.
Type: String
Valid Values: `FaceMovementAndLightChallenge | FaceMovementChallenge`
Required: Yes

 ** Version **   <a name="rekognition-Type-Challenge-Version"></a>
The version of the challenge being used for the Face Liveness session.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 11.
Pattern: `^(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})$`
Required: Yes

## See Also
<a name="API_Challenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/Challenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/Challenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/Challenge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

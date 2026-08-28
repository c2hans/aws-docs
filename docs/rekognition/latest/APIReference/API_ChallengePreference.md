---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ChallengePreference.html
---

# ChallengePreference
<a name="API_ChallengePreference"></a>

An ordered list of preferred challenge type and versions.

## Contents
<a name="API_ChallengePreference_Contents"></a>

 ** Type **   <a name="rekognition-Type-ChallengePreference-Type"></a>
The types of challenges that have been selected for the Face Liveness session.
Type: String
Valid Values: `FaceMovementAndLightChallenge | FaceMovementChallenge`
Required: Yes

 ** Versions **   <a name="rekognition-Type-ChallengePreference-Versions"></a>
The version of the challenges that have been selected for the Face Liveness session.
Type: [Versions](API_Versions.md) object
Required: No

## See Also
<a name="API_ChallengePreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ChallengePreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ChallengePreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ChallengePreference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

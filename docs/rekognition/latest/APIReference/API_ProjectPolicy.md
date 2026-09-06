---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ProjectPolicy.html
---

# ProjectPolicy
<a name="API_ProjectPolicy"></a>

Describes a project policy in the response from [ListProjectPolicies](API_ListProjectPolicies.md).

## Contents
<a name="API_ProjectPolicy_Contents"></a>

 ** CreationTimestamp **   <a name="rekognition-Type-ProjectPolicy-CreationTimestamp"></a>
The Unix datetime for the creation of the project policy.
Type: Timestamp
Required: No

 ** LastUpdatedTimestamp **   <a name="rekognition-Type-ProjectPolicy-LastUpdatedTimestamp"></a>
The Unix datetime for when the project policy was last updated.
Type: Timestamp
Required: No

 ** PolicyDocument **   <a name="rekognition-Type-ProjectPolicy-PolicyDocument"></a>
The JSON document for the project policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** PolicyName **   <a name="rekognition-Type-ProjectPolicy-PolicyName"></a>
The name of the project policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: No

 ** PolicyRevisionId **   <a name="rekognition-Type-ProjectPolicy-PolicyRevisionId"></a>
The revision ID of the project policy.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[0-9A-Fa-f]+`
Required: No

 ** ProjectArn **   <a name="rekognition-Type-ProjectPolicy-ProjectArn"></a>
The Amazon Resource Name (ARN) of the project to which the project policy is attached.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: No

## See Also
<a name="API_ProjectPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProjectPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProjectPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProjectPolicy)

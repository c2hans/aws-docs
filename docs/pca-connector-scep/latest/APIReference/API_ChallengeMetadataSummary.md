---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ChallengeMetadataSummary.html
---

# ChallengeMetadataSummary
<a name="API_ChallengeMetadataSummary"></a>

Details about the specified challenge, returned by the [GetChallengeMetadata](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_GetChallengeMetadata.html) action.

## Contents
<a name="API_ChallengeMetadataSummary_Contents"></a>

 ** Arn **   <a name="pcaconnectorscep-Type-ChallengeMetadataSummary-Arn"></a>
The Amazon Resource Name (ARN) of the challenge.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/challenge\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** ConnectorArn **   <a name="pcaconnectorscep-Type-ChallengeMetadataSummary-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CreatedAt **   <a name="pcaconnectorscep-Type-ChallengeMetadataSummary-CreatedAt"></a>
The date and time that the challenge was created.
Type: Timestamp
Required: No

 ** UpdatedAt **   <a name="pcaconnectorscep-Type-ChallengeMetadataSummary-UpdatedAt"></a>
The date and time that the challenge was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ChallengeMetadataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/ChallengeMetadataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/ChallengeMetadataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/ChallengeMetadataSummary)

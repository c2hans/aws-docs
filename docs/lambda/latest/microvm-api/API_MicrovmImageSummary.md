---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_MicrovmImageSummary.html
---

# MicrovmImageSummary
<a name="API_MicrovmImageSummary"></a>

Contains summary information about a MicroVM image.

## Contents
<a name="API_MicrovmImageSummary_Contents"></a>

 ** createdAt **   <a name="lambdamicrovm-Type-MicrovmImageSummary-createdAt"></a>
The timestamp when the MicroVM image was created.
Type: Timestamp
Required: Yes

 ** imageArn **   <a name="lambdamicrovm-Type-MicrovmImageSummary-imageArn"></a>
The ARN of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** name **   <a name="lambdamicrovm-Type-MicrovmImageSummary-name"></a>
The name of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** state **   <a name="lambdamicrovm-Type-MicrovmImageSummary-state"></a>
The current state of the MicroVM image.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | UPDATING | UPDATED | UPDATE_FAILED | DELETING | DELETE_FAILED | DELETED`
Required: Yes

 ** latestActiveImageVersion **   <a name="lambdamicrovm-Type-MicrovmImageSummary-latestActiveImageVersion"></a>
The latest active version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: No

 ** latestFailedImageVersion **   <a name="lambdamicrovm-Type-MicrovmImageSummary-latestFailedImageVersion"></a>
The latest failed version of the MicroVM image, if any.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: No

## See Also
<a name="API_MicrovmImageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/MicrovmImageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/MicrovmImageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/MicrovmImageSummary)

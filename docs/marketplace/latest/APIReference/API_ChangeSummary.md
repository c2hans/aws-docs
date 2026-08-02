---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ChangeSummary.html
---

# ChangeSummary
<a name="API_ChangeSummary"></a>

This object is a container for common summary information about the change. The summary doesn't contain the whole change structure.

## Contents
<a name="API_ChangeSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ChangeName **   <a name="AWSMarketplaceService-Type-ChangeSummary-ChangeName"></a>
Optional name for the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 72.
Pattern: `^[a-zA-Z]$`
Required: No

 ** ChangeType **   <a name="AWSMarketplaceService-Type-ChangeSummary-ChangeType"></a>
The type of the change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[A-Z][\w]*$`
Required: No

 ** Details **   <a name="AWSMarketplaceService-Type-ChangeSummary-Details"></a>
This object contains details specific to the change type of the requested change.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 16384.
Pattern: `^[\s]*\{[\s\S]*\}[\s]*$`
Required: No

 ** DetailsDocument **   <a name="AWSMarketplaceService-Type-ChangeSummary-DetailsDocument"></a>
The JSON value of the details specific to the change type of the requested change.
To download the "DetailsDocument" shapes, see the [Python](https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-python) and [Java](https://github.com/awslabs/aws-marketplace-catalog-api-shapes-for-java/tree/main) shapes on GitHub.
Type: JSON value
Required: No

 ** Entity **   <a name="AWSMarketplaceService-Type-ChangeSummary-Entity"></a>
The entity to be changed.
Type: [Entity](API_Entity.md) object
Required: No

 ** ErrorDetailList **   <a name="AWSMarketplaceService-Type-ChangeSummary-ErrorDetailList"></a>
An array of `ErrorDetail` objects associated with the change.
Type: Array of [ErrorDetail](API_ErrorDetail.md) objects
Required: No

## See Also
<a name="API_ChangeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ChangeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ChangeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ChangeSummary)

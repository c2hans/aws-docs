---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDataviewConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxDataviewConfiguration
<a name="API_KxDataviewConfiguration"></a>

 The structure that stores the configuration details of a dataview.

## Contents
<a name="API_KxDataviewConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** changesetId **   <a name="finspace-Type-KxDataviewConfiguration-changesetId"></a>
A unique identifier for the changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** dataviewName **   <a name="finspace-Type-KxDataviewConfiguration-dataviewName"></a>
 The unique identifier of the dataview.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** dataviewVersionId **   <a name="finspace-Type-KxDataviewConfiguration-dataviewVersionId"></a>
 The version of the dataview corresponding to a given changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: No

 ** segmentConfigurations **   <a name="finspace-Type-KxDataviewConfiguration-segmentConfigurations"></a>
 The db path and volume configuration for the segmented database.
Type: Array of [KxDataviewSegmentConfiguration](API_KxDataviewSegmentConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_KxDataviewConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxDataviewConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxDataviewConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxDataviewConfiguration)

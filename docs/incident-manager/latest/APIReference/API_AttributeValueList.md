---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_AttributeValueList.html
---

# AttributeValueList
<a name="API_AttributeValueList"></a>

Use the AttributeValueList to filter by string or integer values.

## Contents
<a name="API_AttributeValueList_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** integerValues **   <a name="IncidentManager-Type-AttributeValueList-integerValues"></a>
The list of integer values that the filter matches.
Type: Array of integers
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** stringValues **   <a name="IncidentManager-Type-AttributeValueList-stringValues"></a>
The list of string values that the filter matches.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_AttributeValueList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/AttributeValueList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/AttributeValueList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/AttributeValueList)

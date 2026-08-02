---
source_url: https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/API_AttributeValue.html
---

# AttributeValue
<a name="API_AttributeValue"></a>

 The data type for an attribute. Each attribute value is described as a name-value pair. The name is the AD schema name, and the value is the data itself. For a list of supported attributes, see [Directory Service Data Attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html).

## Contents
<a name="API_AttributeValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BOOL **   <a name="directoryservicedata-Type-AttributeValue-BOOL"></a>
 Indicates that the attribute type value is a boolean. For example:
 `"BOOL": true`
Type: Boolean
Required: No

 ** N **   <a name="directoryservicedata-Type-AttributeValue-N"></a>
 Indicates that the attribute type value is a number. For example:
 `"N": "16"`
Type: Long
Required: No

 ** S **   <a name="directoryservicedata-Type-AttributeValue-S"></a>
 Indicates that the attribute type value is a string. For example:
 `"S": "S Group"`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** SS **   <a name="directoryservicedata-Type-AttributeValue-SS"></a>
 Indicates that the attribute type value is a string set. For example:
 `"SS": ["sample_service_class/host.sample.com:1234/sample_service_name_1", "sample_service_class/host.sample.com:1234/sample_service_name_2"]`
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_AttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directory-service-data-2023-05-31/AttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directory-service-data-2023-05-31/AttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directory-service-data-2023-05-31/AttributeValue)

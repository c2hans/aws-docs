---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ResourceDriftIgnoredAttribute.html
---

# ResourceDriftIgnoredAttribute
<a name="API_ResourceDriftIgnoredAttribute"></a>

The `ResourceDriftIgnoredAttribute` data type.

## Contents
<a name="API_ResourceDriftIgnoredAttribute_Contents"></a>

 ** Path **
Path of the resource attribute for which drift was ignored.
Type: String
Required: No

 ** Reason **
Reason why drift was ignored for the attribute, can have 2 possible values:
+  `WRITE_ONLY_PROPERTY` - Property is not included in read response for the resource’s live state.
+  `MANAGED_BY_AWS` - Property is managed by an AWS service and is expected to be dynamically modified.
Type: String
Valid Values: `MANAGED_BY_AWS | WRITE_ONLY_PROPERTY`
Required: No

## See Also
<a name="API_ResourceDriftIgnoredAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ResourceDriftIgnoredAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ResourceDriftIgnoredAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ResourceDriftIgnoredAttribute)

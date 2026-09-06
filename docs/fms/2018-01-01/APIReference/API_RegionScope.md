---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_RegionScope.html
---

# RegionScope
<a name="API_RegionScope"></a>

Defines the AWS Regions that the specified Firewall Manager administrator can manage.

## Contents
<a name="API_RegionScope_Contents"></a>

 ** AllRegionsEnabled **   <a name="fms-Type-RegionScope-AllRegionsEnabled"></a>
Allows the specified Firewall Manager administrator to manage all AWS Regions.
Type: Boolean
Required: No

 ** Regions **   <a name="fms-Type-RegionScope-Regions"></a>
The AWS Regions that the specified Firewall Manager administrator can perform actions in.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 64 items.
Length Constraints: Minimum length of 6. Maximum length of 32.
Pattern: `^(af|ap|ca|eu|il|me|mx|sa|us|cn|us-gov)-\w+-\d+$`
Required: No

## See Also
<a name="API_RegionScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/RegionScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/RegionScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/RegionScope)

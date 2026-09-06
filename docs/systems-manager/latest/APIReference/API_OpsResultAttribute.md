---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsResultAttribute.html
---

# OpsResultAttribute
<a name="API_OpsResultAttribute"></a>

The OpsItem data type to return.

## Contents
<a name="API_OpsResultAttribute_Contents"></a>

 ** TypeName **   <a name="systemsmanager-Type-OpsResultAttribute-TypeName"></a>
Name of the data type. Valid value: `AWS:OpsItem`, `AWS:EC2InstanceInformation`, `AWS:OpsItemTrendline`, or `AWS:ComplianceSummary`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(AWS|Custom):.*$`
Required: Yes

## See Also
<a name="API_OpsResultAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsResultAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsResultAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsResultAttribute)

---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsItemDataValue.html
---

# OpsItemDataValue
<a name="API_OpsItemDataValue"></a>

An object that defines the value of the key and its type in the OperationalData map.

## Contents
<a name="API_OpsItemDataValue_Contents"></a>

 ** Type **   <a name="systemsmanager-Type-OpsItemDataValue-Type"></a>
The type of key-value pair. Valid types include `SearchableString` and `String`.
Type: String
Valid Values: `SearchableString | String`
Required: No

 ** Value **   <a name="systemsmanager-Type-OpsItemDataValue-Value"></a>
The value of the OperationalData key.
Type: String
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

## See Also
<a name="API_OpsItemDataValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsItemDataValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsItemDataValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsItemDataValue)

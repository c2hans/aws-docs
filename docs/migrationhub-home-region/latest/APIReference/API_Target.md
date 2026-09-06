---
source_url: https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/API_Target.html
---

# Target
<a name="API_Target"></a>

The target parameter specifies the identifier to which the home region is applied, which is always an `ACCOUNT`. It applies the home region to the current `ACCOUNT`.

## Contents
<a name="API_Target_Contents"></a>

 ** Type **   <a name="migrationhubhomeregion-Type-Target-Type"></a>
The target type is always an `ACCOUNT`.
Type: String
Valid Values: `ACCOUNT`
Required: Yes

 ** Id **   <a name="migrationhubhomeregion-Type-Target-Id"></a>
The `TargetID` is a 12-character identifier of the `ACCOUNT` for which the control was created. (This must be the current account.)
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

## See Also
<a name="API_Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhub-config-2019-06-30/Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhub-config-2019-06-30/Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhub-config-2019-06-30/Target)

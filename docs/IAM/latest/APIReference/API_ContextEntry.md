---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ContextEntry.html
---

# ContextEntry
<a name="API_ContextEntry"></a>

Contains information about a condition context key. It includes the name of the key and specifies the value (or values, if the context key supports multiple values) to use in the simulation. This information is used when evaluating the `Condition` elements of the input policies.

This data type is used as an input parameter to [SimulateCustomPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulateCustomPolicy.html) and [SimulatePrincipalPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulatePrincipalPolicy.html).

## Contents
<a name="API_ContextEntry_Contents"></a>

 ** ContextKeyName **
The full name of a condition context key, including the service prefix. For example, `aws:SourceIp` or `s3:VersionId`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 256.
Required: No

 ** ContextKeyType **
The data type of the value (or values) specified in the `ContextKeyValues` parameter.
Type: String
Valid Values: `string | stringList | numeric | numericList | boolean | booleanList | ip | ipList | binary | binaryList | date | dateList`
Required: No

 ** ContextKeyValues.member.N **
The value (or values, if the condition context key supports multiple values) to provide to the simulation when the key is referenced by a `Condition` element in an input policy.
Type: Array of strings
Required: No

## See Also
<a name="API_ContextEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ContextEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ContextEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ContextEntry)

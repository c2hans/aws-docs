---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_LocationIdentifier.html
---

# LocationIdentifier
<a name="API_LocationIdentifier"></a>

Identifies an instrumentation configuration by code location or location hash. Used in the Get, Delete, and GetStatus operations to allow flexible identification.

## Contents
<a name="API_LocationIdentifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CodeLocation **   <a name="applicationsignals-Type-LocationIdentifier-CodeLocation"></a>
Identifies a code location to instrument, including the programming language, code unit, class, method, file path, and optional line number.
Type: [CodeLocation](API_CodeLocation.md) object
Required: No

 ** LocationHash **   <a name="applicationsignals-Type-LocationIdentifier-LocationHash"></a>
The pre-computed location hash (a 16-character hexadecimal string).
Type: String
Length Constraints: Fixed length of 16.
Required: No

## See Also
<a name="API_LocationIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/LocationIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/LocationIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/LocationIdentifier)

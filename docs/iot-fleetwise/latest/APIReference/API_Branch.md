---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_Branch.html
---

# Branch
<a name="API_Branch"></a>

A group of signals that are defined in a hierarchical structure.

## Contents
<a name="API_Branch_Contents"></a>

 ** fullyQualifiedName **   <a name="iotfleetwise-Type-Branch-fullyQualifiedName"></a>
The fully qualified name of the branch. For example, the fully qualified name of a branch might be `Vehicle.Body.Engine`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** comment **   <a name="iotfleetwise-Type-Branch-comment"></a>
A comment in addition to the description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** deprecationMessage **   <a name="iotfleetwise-Type-Branch-deprecationMessage"></a>
The deprecation message for the node or the branch that was moved or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** description **   <a name="iotfleetwise-Type-Branch-description"></a>
A brief description of the branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_Branch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/Branch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/Branch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/Branch)

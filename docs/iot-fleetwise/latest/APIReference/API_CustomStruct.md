---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CustomStruct.html
---

# CustomStruct
<a name="API_CustomStruct"></a>

The custom structure represents a complex or higher-order data structure.

## Contents
<a name="API_CustomStruct_Contents"></a>

 ** fullyQualifiedName **   <a name="iotfleetwise-Type-CustomStruct-fullyQualifiedName"></a>
The fully qualified name of the custom structure. For example, the fully qualified name of a custom structure might be `ComplexDataTypes.VehicleDataTypes.SVMCamera`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_.]+`
Required: Yes

 ** comment **   <a name="iotfleetwise-Type-CustomStruct-comment"></a>
A comment in addition to the description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** deprecationMessage **   <a name="iotfleetwise-Type-CustomStruct-deprecationMessage"></a>
The deprecation message for the node or the branch that was moved or deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** description **   <a name="iotfleetwise-Type-CustomStruct-description"></a>
A brief description of the custom structure.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

## See Also
<a name="API_CustomStruct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/CustomStruct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/CustomStruct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/CustomStruct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

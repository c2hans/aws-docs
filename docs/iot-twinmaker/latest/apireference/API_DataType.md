---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_DataType.html
---

# DataType
<a name="API_DataType"></a>

An object that specifies the data type of a property.

## Contents
<a name="API_DataType_Contents"></a>

 ** type **   <a name="tm-Type-DataType-type"></a>
The underlying type of the data type.
Type: String
Valid Values: `RELATIONSHIP | STRING | LONG | BOOLEAN | INTEGER | DOUBLE | LIST | MAP`
Required: Yes

 ** allowedValues **   <a name="tm-Type-DataType-allowedValues"></a>
The allowed values for this data type.
Type: Array of [DataValue](API_DataValue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** nestedType **   <a name="tm-Type-DataType-nestedType"></a>
The nested type in the data type.
Type: [DataType](#API_DataType) object
Required: No

 ** relationship **   <a name="tm-Type-DataType-relationship"></a>
A relationship that associates a component with another component.
Type: [Relationship](API_Relationship.md) object
Required: No

 ** unitOfMeasure **   <a name="tm-Type-DataType-unitOfMeasure"></a>
The unit of measure used in this data type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

## See Also
<a name="API_DataType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/DataType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/DataType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/DataType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

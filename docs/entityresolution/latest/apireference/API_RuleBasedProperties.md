---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_RuleBasedProperties.html
---

# RuleBasedProperties
<a name="API_RuleBasedProperties"></a>

An object which defines the list of matching rules to run in a matching workflow.

## Contents
<a name="API_RuleBasedProperties_Contents"></a>

 ** attributeMatchingModel **   <a name="API-Type-RuleBasedProperties-attributeMatchingModel"></a>
The comparison type. You can choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `attributeMatchingModel`.
If you choose `ONE_TO_ONE`, the system can only match attributes if the sub-types are an exact match. For example, for the `Email` attribute type, the system will only consider it a match if the value of the `Email` field of Profile A matches the value of the `Email` field of Profile B.
If you choose `MANY_TO_MANY`, the system can match attributes across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A and the value of `BusinessEmail` field of Profile B matches, the two profiles are matched on the `Email` attribute type.
Type: String
Valid Values: `ONE_TO_ONE | MANY_TO_MANY`
Required: Yes

 ** rules **   <a name="API-Type-RuleBasedProperties-rules"></a>
A list of `Rule` objects, each of which have fields `RuleName` and `MatchingKeys`.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

 ** matchPurpose **   <a name="API-Type-RuleBasedProperties-matchPurpose"></a>
 An indicator of whether to generate IDs and index the data or not.
If you choose `IDENTIFIER_GENERATION`, the process generates IDs and indexes the data.
If you choose `INDEXING`, the process indexes the data without generating IDs.
Type: String
Valid Values: `IDENTIFIER_GENERATION | INDEXING`
Required: No

## See Also
<a name="API_RuleBasedProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/RuleBasedProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/RuleBasedProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/RuleBasedProperties)

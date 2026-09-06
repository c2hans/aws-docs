---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Predicate.html
---

# Predicate
<a name="API_Predicate"></a>

Defines the predicate of the trigger, which determines when it fires.

## Contents
<a name="API_Predicate_Contents"></a>

 ** Conditions **   <a name="Glue-Type-Predicate-Conditions"></a>
A list of the conditions that determine when the trigger will fire.
Type: Array of [Condition](API_Condition.md) objects
Array Members: Maximum number of 500 items.
Required: No

 ** Logical **   <a name="Glue-Type-Predicate-Logical"></a>
An optional field if only one condition is listed. If multiple conditions are listed, then this field is required.
Type: String
Valid Values: `AND | ANY`
Required: No

## See Also
<a name="API_Predicate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Predicate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Predicate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Predicate)

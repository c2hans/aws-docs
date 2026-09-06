---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DateTimeDefaultValues.html
---

# DateTimeDefaultValues
<a name="API_DateTimeDefaultValues"></a>

The default values of the `DateTimeParameterDeclaration`.

## Contents
<a name="API_DateTimeDefaultValues_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DynamicValue **   <a name="QS-Type-DateTimeDefaultValues-DynamicValue"></a>
The dynamic value of the `DataTimeDefaultValues`. Different defaults are displayed according to users, groups, and values mapping.
Type: [DynamicDefaultValue](API_DynamicDefaultValue.md) object
Required: No

 ** RollingDate **   <a name="QS-Type-DateTimeDefaultValues-RollingDate"></a>
The rolling date of the `DataTimeDefaultValues`. The date is determined from the dataset based on input expression.
Type: [RollingDateConfiguration](API_RollingDateConfiguration.md) object
Required: No

 ** StaticValues **   <a name="QS-Type-DateTimeDefaultValues-StaticValues"></a>
The static values of the `DataTimeDefaultValues`.
Type: Array of timestamps
Array Members: Maximum number of 50000 items.
Required: No

## See Also
<a name="API_DateTimeDefaultValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DateTimeDefaultValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DateTimeDefaultValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DateTimeDefaultValues)

---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Filter the selection by using a condition.

## Contents
<a name="API_Filter_Contents"></a>

 ** condition **   <a name="IncidentManager-Type-Filter-condition"></a>
The condition accepts before or after a specified time, equal to a string, or equal to an integer.
Type: [Condition](API_Condition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** key **   <a name="IncidentManager-Type-Filter-key"></a>
The key that you're filtering on.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/Filter)

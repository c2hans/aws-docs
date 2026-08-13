---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ApplicableTo.html
---

# ApplicableTo
<a name="API_ApplicableTo"></a>

The scoping configuration that determines which principals an approval policy applies to.

## Contents
<a name="API_ApplicableTo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Type **   <a name="QS-Type-ApplicableTo-Type"></a>
The type of scoping that determines which principals the approval policy applies to. Valid values are defined as follows:
+  `GROUP`: The policy applies only to principals in the groups specified by `GroupArns`. When you use `GROUP`, you must also provide a value for `GroupArns`.
Type: String
Valid Values: `GROUP`
Required: Yes

 ** GroupArns **   <a name="QS-Type-ApplicableTo-GroupArns"></a>
The list of group ARNs that the policy applies to. Required when type is GROUP.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_ApplicableTo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ApplicableTo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ApplicableTo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ApplicableTo)

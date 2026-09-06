---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListTargetsFilter.html
---

# ListTargetsFilter
<a name="API_ListTargetsFilter"></a>

Information about a filter to apply to the list of returned targets. You can filter by target type, address, or status. For example, to filter results to notification rules that have active Amazon Q Developer in chat applications topics as targets, you could specify a ListTargetsFilter Name as `TargetType` and a Value of `SNS`, and a Name of `TARGET_STATUS` and a Value of `ACTIVE`.

## Contents
<a name="API_ListTargetsFilter_Contents"></a>

 ** Name **   <a name="codestarnotifications-Type-ListTargetsFilter-Name"></a>
The name of the attribute you want to use to filter the returned targets.
Type: String
Valid Values: `TARGET_TYPE | TARGET_ADDRESS | TARGET_STATUS`
Required: Yes

 ** Value **   <a name="codestarnotifications-Type-ListTargetsFilter-Value"></a>
The value of the attribute you want to use to filter the returned targets. For example, if you specify `SNS` for the Target type, you could specify an Amazon Resource Name (ARN) for a topic as the value.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

## See Also
<a name="API_ListTargetsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/ListTargetsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/ListTargetsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/ListTargetsFilter)

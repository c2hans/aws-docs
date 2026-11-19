---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CaseEventIncludedData.html
---

# CaseEventIncludedData

Details of what case data is published through the case event stream. Use `fields` to include a specific list of fields, and use `autoIncludeFields` to automatically include a category of fields. When both are set, the effective field set is the union of the two.

## Contents
<a name="API_connect-cases_CaseEventIncludedData_Contents"></a>

 ** fields **   <a name="connect-Type-connect-cases_CaseEventIncludedData-fields"></a>
List of field identifiers to include in case event data.
Type: Array of [FieldIdentifier](API_connect-cases_FieldIdentifier.md) objects
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Required: Yes

 ** autoIncludeFields **   <a name="connect-Type-connect-cases_CaseEventIncludedData-autoIncludeFields"></a>
Automatically include a category of fields in case event data, combined as a union with any fields specified in `fields`. Valid values are `All` (include all fields on the case), `System` (include all system fields), and `Custom` (include all custom fields). When this attribute is set, new fields added to the domain are picked up automatically without another call to PutCaseEventConfiguration. For the full behavior matrix and IAM requirements, see [Case event streams in Connect Customer Cases](https://docs.aws.amazon.com/connect/latest/adminguide/case-event-streams.html) in the *Connect Customer Administrator Guide*.
Type: String
Valid Values: `All | System | Custom`
Required: No

## See Also
<a name="API_connect-cases_CaseEventIncludedData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CaseEventIncludedData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CaseEventIncludedData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CaseEventIncludedData)

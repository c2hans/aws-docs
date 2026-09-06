---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_TableLFTagPolicyAndPermissions.html
---

# TableLFTagPolicyAndPermissions
<a name="API_TableLFTagPolicyAndPermissions"></a>

The LF-tag policy and permissions that apply to table resources.

## Contents
<a name="API_TableLFTagPolicyAndPermissions_Contents"></a>

 ** Expression **   <a name="dataexchange-Type-TableLFTagPolicyAndPermissions-Expression"></a>
A list of LF-tag conditions that apply to table resources.
Type: Array of [LFTag](API_LFTag.md) objects
Required: Yes

 ** Permissions **   <a name="dataexchange-Type-TableLFTagPolicyAndPermissions-Permissions"></a>
The permissions granted to subscribers on table resources.
Type: Array of strings
Valid Values: `DESCRIBE | SELECT`
Required: Yes

## See Also
<a name="API_TableLFTagPolicyAndPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/TableLFTagPolicyAndPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/TableLFTagPolicyAndPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/TableLFTagPolicyAndPermissions)

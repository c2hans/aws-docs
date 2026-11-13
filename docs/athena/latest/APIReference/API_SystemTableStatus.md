---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_SystemTableStatus.html
---

# SystemTableStatus
<a name="API_SystemTableStatus"></a>

The enablement status of a single system table. Because system tables are enabled at the account level, every status reflects the same account-wide state.

## Contents
<a name="API_SystemTableStatus_Contents"></a>

 ** Enabled **   <a name="athena-Type-SystemTableStatus-Enabled"></a>
Indicates whether the system table is enabled for the account.
Type: Boolean
Required: Yes

 ** TableName **   <a name="athena-Type-SystemTableStatus-TableName"></a>
The name of the system table, such as `QUERY_EXECUTIONS`.
Type: String
Valid Values: `QUERY_EXECUTIONS`
Required: Yes

## See Also
<a name="API_SystemTableStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/SystemTableStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/SystemTableStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/SystemTableStatus)

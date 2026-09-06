---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_QuickConnectContactData.html
---

# QuickConnectContactData
<a name="API_QuickConnectContactData"></a>

 Contact data associated with quick connect operations.

## Contents
<a name="API_QuickConnectContactData_Contents"></a>

 ** ContactId **   <a name="connect-Type-QuickConnectContactData-ContactId"></a>
 The contact ID for quick connect contact data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** InitiationTimestamp **   <a name="connect-Type-QuickConnectContactData-InitiationTimestamp"></a>
 Timestamp when the quick connect contact was initiated.
Type: Timestamp
Required: No

 ** QuickConnectId **   <a name="connect-Type-QuickConnectContactData-QuickConnectId"></a>
 The quick connect ID.
Type: String
Required: No

 ** QuickConnectName **   <a name="connect-Type-QuickConnectContactData-QuickConnectName"></a>
 The name of the quick connect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** QuickConnectType **   <a name="connect-Type-QuickConnectContactData-QuickConnectType"></a>
 The type of the quick connect.
Type: String
Valid Values: `USER | QUEUE | PHONE_NUMBER | FLOW`
Required: No

## See Also
<a name="API_QuickConnectContactData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/QuickConnectContactData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/QuickConnectContactData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/QuickConnectContactData)

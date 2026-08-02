---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ProtocolsListDataSummary.html
---

# ProtocolsListDataSummary
<a name="API_ProtocolsListDataSummary"></a>

Details of the AWS Firewall Manager protocols list.

## Contents
<a name="API_ProtocolsListDataSummary_Contents"></a>

 ** ListArn **   <a name="fms-Type-ProtocolsListDataSummary-ListArn"></a>
The Amazon Resource Name (ARN) of the specified protocols list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ListId **   <a name="fms-Type-ProtocolsListDataSummary-ListId"></a>
The ID of the specified protocols list.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: No

 ** ListName **   <a name="fms-Type-ProtocolsListDataSummary-ListName"></a>
The name of the specified protocols list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ProtocolsList **   <a name="fms-Type-ProtocolsListDataSummary-ProtocolsList"></a>
An array of protocols in the AWS Firewall Manager protocols list.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_ProtocolsListDataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ProtocolsListDataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ProtocolsListDataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ProtocolsListDataSummary)

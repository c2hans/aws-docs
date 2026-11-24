---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_SourceLogsConfiguration.html
---

# SourceLogsConfiguration

Configuration for selecting and handling source log groups for centralization.

## Contents
<a name="API_SourceLogsConfiguration_Contents"></a>

 ** EncryptedLogGroupStrategy **   <a name="cwoa-Type-SourceLogsConfiguration-EncryptedLogGroupStrategy"></a>
A strategy determining whether to centralize source log groups that are encrypted with customer managed KMS keys (CMK). ALLOW will consider CMK encrypted source log groups for centralization while SKIP will skip CMK encrypted source log groups from centralization.
Type: String
Valid Values: `ALLOW | SKIP`
Required: Yes

 ** CentralizeWithDataProtection **   <a name="cwoa-Type-SourceLogsConfiguration-CentralizeWithDataProtection"></a>
Specifies whether this centralization rule centralizes log events with data protection applied. If you don't specify this setting, or you set it to `DISABLED`, the rule centralizes the original log events, including any sensitive data that a data protection policy on the source log group masks.
When you set this to `ENABLED`, the rule centralizes the same masked data that anyone in the source account without the `logs:Unmask` permission sees. The rule doesn't copy the original values to the destination, so you can't unmask them in the destination account. The rule centralizes log events from source log groups that don't have a data protection policy without changes.
The setting applies only to log events that the rule centralizes after you enable it. It doesn't change log events that the rule already centralized.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** DataSourceSelectionCriteria **   <a name="cwoa-Type-SourceLogsConfiguration-DataSourceSelectionCriteria"></a>
The selection criteria that specifies which data sources to centralize. The selection criteria uses the same filter expression format as `LogGroupSelectionCriteria`, but operates on `DataSourceName` and `DataSourceType` operands. When both `LogGroupSelectionCriteria` and `DataSourceSelectionCriteria` are specified, a log event must match both criteria to be centralized.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

 ** LogGroupSelectionCriteria **   <a name="cwoa-Type-SourceLogsConfiguration-LogGroupSelectionCriteria"></a>
The selection criteria that specifies which source log groups to centralize. The selection criteria uses the same format as OAM link filters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## See Also
<a name="API_SourceLogsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/SourceLogsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/SourceLogsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/SourceLogsConfiguration)

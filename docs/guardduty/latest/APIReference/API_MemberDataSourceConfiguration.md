---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_MemberDataSourceConfiguration.html
---

# MemberDataSourceConfiguration
<a name="API_MemberDataSourceConfiguration"></a>

Contains information on which data sources are enabled for a member account.

## Contents
<a name="API_MemberDataSourceConfiguration_Contents"></a>

 ** accountId **   <a name="guardduty-Type-MemberDataSourceConfiguration-accountId"></a>
The account ID for the member account.
Type: String
Length Constraints: Fixed length of 12.
Required: Yes

 ** dataSources **   <a name="guardduty-Type-MemberDataSourceConfiguration-dataSources"></a>
 *This member has been deprecated.*
Contains information on the status of data sources for the account.
Type: [DataSourceConfigurationsResult](API_DataSourceConfigurationsResult.md) object
Required: Yes

 ** features **   <a name="guardduty-Type-MemberDataSourceConfiguration-features"></a>
Contains information about the status of the features for the member account.
Type: Array of [MemberFeaturesConfigurationResult](API_MemberFeaturesConfigurationResult.md) objects
Required: No

## See Also
<a name="API_MemberDataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/MemberDataSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/MemberDataSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/MemberDataSourceConfiguration)

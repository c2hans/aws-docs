---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DifferentialPrivacyConfiguration.html
---

# DifferentialPrivacyConfiguration
<a name="API_DifferentialPrivacyConfiguration"></a>

Specifies the unique identifier for your users.

## Contents
<a name="API_DifferentialPrivacyConfiguration_Contents"></a>

 ** columns **   <a name="API-Type-DifferentialPrivacyConfiguration-columns"></a>
The name of the column (such as user\_id) that contains the unique identifier of your users whose privacy you want to protect. If you want to turn on diﬀerential privacy for two or more tables in a collaboration, you must conﬁgure the same column as the user identiﬁer column in both analysis rules.
Type: Array of [DifferentialPrivacyColumn](API_DifferentialPrivacyColumn.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## See Also
<a name="API_DifferentialPrivacyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DifferentialPrivacyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DifferentialPrivacyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DifferentialPrivacyConfiguration)

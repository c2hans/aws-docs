---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_QuotaSettings.html
---

# QuotaSettings
<a name="API_QuotaSettings"></a>

Quotas configured for a usage plan.

## Contents
<a name="API_QuotaSettings_Contents"></a>

 ** limit **   <a name="apigw-Type-QuotaSettings-limit"></a>
The target maximum number of requests that can be made in a given time period.
Type: Integer
Required: No

 ** offset **   <a name="apigw-Type-QuotaSettings-offset"></a>
The number of requests subtracted from the given limit in the initial time period.
Type: Integer
Required: No

 ** period **   <a name="apigw-Type-QuotaSettings-period"></a>
The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
Type: String
Valid Values: `DAY | WEEK | MONTH`
Required: No

## See Also
<a name="API_QuotaSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/QuotaSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/QuotaSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/QuotaSettings)

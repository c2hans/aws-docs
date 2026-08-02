---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentTier.html
---

# EnvironmentTier
<a name="API_EnvironmentTier"></a>

Describes the properties of an environment tier

## Contents
<a name="API_EnvironmentTier_Contents"></a>

 ** Name **
The name of this environment tier.
Valid values:
+ For *Web server tier* – `WebServer`
+ For *Worker tier* – `Worker`
Type: String
Required: No

 ** Type **
The type of this environment tier.
Valid values:
+ For *Web server tier* – `Standard`
+ For *Worker tier* – `SQS/HTTP`
Type: String
Required: No

 ** Version **
The version of this environment tier. When you don't set a value to it, Elastic Beanstalk uses the latest compatible worker tier version.
This member is deprecated. Any specific version that you set may become out of date. We recommend leaving it unspecified.
Type: String
Required: No

## See Also
<a name="API_EnvironmentTier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/EnvironmentTier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/EnvironmentTier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/EnvironmentTier)

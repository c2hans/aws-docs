---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationVersionLifecycleConfig.html
---

# ApplicationVersionLifecycleConfig
<a name="API_ApplicationVersionLifecycleConfig"></a>

The application version lifecycle settings for an application. Defines the rules that Elastic Beanstalk applies to an application's versions in order to avoid hitting the per-region limit for application versions.

When Elastic Beanstalk deletes an application version from its database, you can no longer deploy that version to an environment. The source bundle remains in S3 unless you configure the rule to delete it.

## Contents
<a name="API_ApplicationVersionLifecycleConfig_Contents"></a>

 ** MaxAgeRule **
Specify a max age rule to restrict the length of time that application versions are retained for an application.
Type: [MaxAgeRule](API_MaxAgeRule.md) object
Required: No

 ** MaxCountRule **
Specify a max count rule to restrict the number of application versions that are retained for an application.
Type: [MaxCountRule](API_MaxCountRule.md) object
Required: No

## See Also
<a name="API_ApplicationVersionLifecycleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ApplicationVersionLifecycleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ApplicationVersionLifecycleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ApplicationVersionLifecycleConfig)

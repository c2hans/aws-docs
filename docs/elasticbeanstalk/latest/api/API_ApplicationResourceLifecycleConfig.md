---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationResourceLifecycleConfig.html
---

# ApplicationResourceLifecycleConfig
<a name="API_ApplicationResourceLifecycleConfig"></a>

The resource lifecycle configuration for an application. Defines lifecycle settings for resources that belong to the application, and the service role that AWS Elastic Beanstalk assumes in order to apply lifecycle settings. The version lifecycle configuration defines lifecycle settings for application versions.

## Contents
<a name="API_ApplicationResourceLifecycleConfig_Contents"></a>

 ** ServiceRole **
The ARN of an IAM service role that Elastic Beanstalk has permission to assume.
The `ServiceRole` property is required the first time that you provide a `VersionLifecycleConfig` for the application in one of the supporting calls (`CreateApplication` or `UpdateApplicationResourceLifecycle`). After you provide it once, in either one of the calls, Elastic Beanstalk persists the Service Role with the application, and you don't need to specify it again in subsequent `UpdateApplicationResourceLifecycle` calls. You can, however, specify it in subsequent calls to change the Service Role to another value.
Type: String
Required: No

 ** VersionLifecycleConfig **
Defines lifecycle settings for application versions.
Type: [ApplicationVersionLifecycleConfig](API_ApplicationVersionLifecycleConfig.md) object
Required: No

## See Also
<a name="API_ApplicationResourceLifecycleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ApplicationResourceLifecycleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ApplicationResourceLifecycleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ApplicationResourceLifecycleConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

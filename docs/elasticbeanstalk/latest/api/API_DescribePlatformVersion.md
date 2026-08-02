---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribePlatformVersion.html
---

# DescribePlatformVersion
<a name="API_DescribePlatformVersion"></a>

Describes a platform version. Provides full details. Compare to [ListPlatformVersions](API_ListPlatformVersions.md), which provides summary information about a list of platform versions.

For definitions of platform version and other platform-related terms, see [AWS Elastic Beanstalk Platforms Glossary](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html).

This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Request Parameters
<a name="API_DescribePlatformVersion_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** PlatformArn **
The ARN of the platform version.
Type: String
Required: No

## Response Elements
<a name="API_DescribePlatformVersion_ResponseElements"></a>

The following element is returned by the service.

 ** PlatformDescription **
Detailed information about the platform version.
Type: [PlatformDescription](API_PlatformDescription.md) object

## Errors
<a name="API_DescribePlatformVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ElasticBeanstalkService **
A generic service exception has occurred.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

## See Also
<a name="API_DescribePlatformVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribePlatformVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribePlatformVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribePlatformVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribePlatformVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribePlatformVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribePlatformVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribePlatformVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribePlatformVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribePlatformVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribePlatformVersion)

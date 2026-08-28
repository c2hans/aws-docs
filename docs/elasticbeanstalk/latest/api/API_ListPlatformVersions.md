---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListPlatformVersions.html
---

# ListPlatformVersions
<a name="API_ListPlatformVersions"></a>

Lists the platform versions available for your account in an AWS Region. Provides summary information about each platform version. Compare to [DescribePlatformVersion](API_DescribePlatformVersion.md), which provides full details about a single platform version.

This action only returns information about platform versions that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of ten platform versions. When the user calls the *ListPlatformVersions* action, the response will only include the one platform version that the user has permission to access instead of all ten platform versions. If the user doesn’t have access to any of the platform versions an empty result is returned.

**Note**
The *AWSElasticBeanstalkReadOnly* managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

For definitions of platform version and other platform-related terms, see [AWS Elastic Beanstalk Platforms Glossary](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html).

## Request Parameters
<a name="API_ListPlatformVersions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.member.N**
Criteria for restricting the resulting list of platform versions. The filter is interpreted as a logical conjunction (AND) of the separate `PlatformFilter` terms.
Type: Array of [PlatformFilter](API_PlatformFilter.md) objects
Required: No

 ** MaxRecords **
The maximum number of platform version values returned in one call.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** NextToken **
For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.
If no `NextToken` is specified, the first page is retrieved.
Type: String
Required: No

## Response Elements
<a name="API_ListPlatformVersions_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
In a paginated request, if this value isn't `null`, it's the token that you can pass in a subsequent request to get the next response page.
Type: String

 **PlatformSummaryList.member.N**
Summary information about the platform versions.
Type: Array of [PlatformSummary](API_PlatformSummary.md) objects

## Errors
<a name="API_ListPlatformVersions_Errors"></a>

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
<a name="API_ListPlatformVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/ListPlatformVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/ListPlatformVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ListPlatformVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/ListPlatformVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ListPlatformVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/ListPlatformVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/ListPlatformVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/ListPlatformVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/ListPlatformVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ListPlatformVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

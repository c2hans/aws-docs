---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElasticBeanstalkEnvironmentDetails.html
---

# AwsElasticBeanstalkEnvironmentDetails
<a name="API_AwsElasticBeanstalkEnvironmentDetails"></a>

Contains details about an Elastic Beanstalk environment.

## Contents
<a name="API_AwsElasticBeanstalkEnvironmentDetails_Contents"></a>

 ** ApplicationName **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-ApplicationName"></a>
The name of the application that is associated with the environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Cname **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-Cname"></a>
The URL to the CNAME for this environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DateCreated **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-DateCreated"></a>
The creation date for this environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DateUpdated **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-DateUpdated"></a>
The date when this environment was last modified.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-Description"></a>
A description of the environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EndpointUrl **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-EndpointUrl"></a>
For load-balanced, autoscaling environments, the URL to the load balancer. For single-instance environments, the IP address of the instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnvironmentArn **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-EnvironmentArn"></a>
The ARN of the environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnvironmentId **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-EnvironmentId"></a>
The identifier of the environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnvironmentLinks **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-EnvironmentLinks"></a>
Links to other environments in the same group.
Type: Array of [AwsElasticBeanstalkEnvironmentEnvironmentLink](API_AwsElasticBeanstalkEnvironmentEnvironmentLink.md) objects
Required: No

 ** EnvironmentName **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-EnvironmentName"></a>
The name of the environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OptionSettings **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-OptionSettings"></a>
The configuration setting for the environment.
Type: Array of [AwsElasticBeanstalkEnvironmentOptionSetting](API_AwsElasticBeanstalkEnvironmentOptionSetting.md) objects
Required: No

 ** PlatformArn **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-PlatformArn"></a>
The ARN of the platform version for the environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SolutionStackName **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-SolutionStackName"></a>
The name of the solution stack that is deployed with the environment.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Status **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-Status"></a>
The current operational status of the environment. Valid values are as follows:
+  `Aborting`
+  `Launching`
+  `LinkingFrom`
+  `LinkingTo`
+  `Ready`
+  `Terminated`
+  `Terminating`
+  `Updating`
Type: String
Pattern: `.*\S.*`
Required: No

 ** Tier **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-Tier"></a>
The tier of the environment.
Type: [AwsElasticBeanstalkEnvironmentTier](API_AwsElasticBeanstalkEnvironmentTier.md) object
Required: No

 ** VersionLabel **   <a name="securityhub-Type-AwsElasticBeanstalkEnvironmentDetails-VersionLabel"></a>
The application version of the environment.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElasticBeanstalkEnvironmentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElasticBeanstalkEnvironmentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElasticBeanstalkEnvironmentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElasticBeanstalkEnvironmentDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

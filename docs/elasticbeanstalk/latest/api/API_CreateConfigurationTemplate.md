---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateConfigurationTemplate.html
---

# CreateConfigurationTemplate
<a name="API_CreateConfigurationTemplate"></a>

Creates an AWS Elastic Beanstalk configuration template, associated with a specific Elastic Beanstalk application. You define application configuration settings in a configuration template. You can then use the configuration template to deploy different versions of the application with the same configuration settings.

Templates aren't associated with any environment. The `EnvironmentName` response element is always `null`.

Related Topics
+  [DescribeConfigurationOptions](API_DescribeConfigurationOptions.md)
+  [DescribeConfigurationSettings](API_DescribeConfigurationSettings.md)
+  [ListAvailableSolutionStacks](API_ListAvailableSolutionStacks.md)

## Request Parameters
<a name="API_CreateConfigurationTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the Elastic Beanstalk application to associate with this configuration template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Description **
An optional description for this configuration.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** EnvironmentId **
The ID of an environment whose settings you want to use to create the configuration template. You must specify `EnvironmentId` if you don't specify `PlatformArn`, `SolutionStackName`, or `SourceConfiguration`.
Type: String
Required: No

 **OptionSettings.member.N**
Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the * AWS Elastic Beanstalk Developer Guide*.
Type: Array of [ConfigurationOptionSetting](API_ConfigurationOptionSetting.md) objects
Required: No

 ** PlatformArn **
The Amazon Resource Name (ARN) of the custom platform. For more information, see [ Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the * AWS Elastic Beanstalk Developer Guide*.
If you specify `PlatformArn`, then don't specify `SolutionStackName`.
Type: String
Required: No

 ** SolutionStackName **
The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, `64bit Amazon Linux 2013.09 running Tomcat 7 Java 7`. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the * AWS Elastic Beanstalk Developer Guide*.
You must specify `SolutionStackName` if you don't specify `PlatformArn`, `EnvironmentId`, or `SourceConfiguration`.
Use the [`ListAvailableSolutionStacks`](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html) API to obtain a list of available solution stacks.
Type: String
Required: No

 ** SourceConfiguration **
An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
Values specified in `OptionSettings` override any values obtained from the `SourceConfiguration`.
You must specify `SourceConfiguration` if you don't specify `PlatformArn`, `EnvironmentId`, or `SolutionStackName`.
Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.
Type: [SourceConfiguration](API_SourceConfiguration.md) object
Required: No

 **Tags.member.N**
Specifies the tags applied to the configuration template.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TemplateName **
The name of the configuration template.
Constraint: This name must be unique per application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Elements
<a name="API_CreateConfigurationTemplate_ResponseElements"></a>

The following elements are returned by the service.

 ** ApplicationName **
The name of the application associated with this configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** DateCreated **
The date (in UTC time) when this configuration set was created.
Type: Timestamp

 ** DateUpdated **
The date (in UTC time) when this configuration set was last modified.
Type: Timestamp

 ** DeploymentStatus **
 If this configuration set is associated with an environment, the `DeploymentStatus` parameter indicates the deployment status of this configuration set:
+  `null`: This configuration is not associated with a running environment.
+  `pending`: This is a draft configuration that is not deployed to the associated environment but is in the process of deploying.
+  `deployed`: This is the configuration that is currently deployed to the associated running environment.
+  `failed`: This is a draft configuration that failed to successfully deploy.
Type: String
Valid Values: `deployed | pending | failed`

 ** Description **
Describes this configuration set.
Type: String
Length Constraints: Maximum length of 200.

 ** EnvironmentName **
 If not `null`, the name of the environment for this configuration set.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.

 **OptionSettings.member.N**
A list of the configuration options and their values in this configuration set.
Type: Array of [ConfigurationOptionSetting](API_ConfigurationOptionSetting.md) objects

 ** PlatformArn **
The ARN of the platform version.
Type: String

 ** SolutionStackName **
The name of the solution stack this configuration set uses.
Type: String

 ** TemplateName **
 If not `null`, the name of the configuration template for this configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_CreateConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** TooManyBuckets **
The specified account has reached its limit of Amazon S3 buckets.
HTTP Status Code: 400

 ** TooManyConfigurationTemplates **
The specified account has reached its limit of configuration templates.
HTTP Status Code: 400

## Examples
<a name="API_CreateConfigurationTemplate_Examples"></a>

### Example
<a name="API_CreateConfigurationTemplate_Example_1"></a>

This example illustrates one usage of CreateConfigurationTemplate.

#### Sample Request
<a name="API_CreateConfigurationTemplate_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&TemplateName=AppTemplate
&SolutionStackName=32bit%20Amazon%20Linux%20running%20Tomcat%207
&Description=ConfigTemplateDescription
&Operation=CreateConfigurationTemplate
&AuthParams
```

#### Sample Response
<a name="API_CreateConfigurationTemplate_Example_1_Response"></a>

```
<CreateConfigurationTemplateResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <CreateConfigurationTemplateResult>
    <SolutionStackName>32bit Amazon Linux running Tomcat 7</SolutionStackName>
    <OptionSettings>
      <member>
        <OptionName>ImageId</OptionName>
        <Value>ami-f2f0069b</Value>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <OptionName>Notification Endpoint</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <OptionName>PARAM4</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>JDBC_CONNECTION_STRING</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>SecurityGroups</OptionName>
        <Value>elasticbeanstalk-default</Value>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <OptionName>UnhealthyThreshold</OptionName>
        <Value>5</Value>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <OptionName>InstanceType</OptionName>
        <Value>t1.micro</Value>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <OptionName>Statistic</OptionName>
        <Value>Average</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>LoadBalancerHTTPSPort</OptionName>
        <Value>OFF</Value>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
      <member>
        <OptionName>Stickiness Cookie Expiration</OptionName>
        <Value>0</Value>
        <Namespace>aws:elb:policies</Namespace>
      </member>
      <member>
        <OptionName>PARAM5</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>MeasureName</OptionName>
        <Value>NetworkOut</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>Interval</OptionName>
        <Value>30</Value>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <OptionName>Application Healthcheck URL</OptionName>
        <Value>/</Value>
        <Namespace>aws:elasticbeanstalk:application</Namespace>
      </member>
      <member>
        <OptionName>Notification Topic ARN</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <OptionName>LowerBreachScaleIncrement</OptionName>
        <Value>-1</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>XX:MaxPermSize</OptionName>
        <Value>64m</Value>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <OptionName>UpperBreachScaleIncrement</OptionName>
        <Value>1</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>MinSize</OptionName>
        <Value>1</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>Custom Availability Zones</OptionName>
        <Value>us-east-1a</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>Availability Zones</OptionName>
        <Value>Any 1</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>LogPublicationControl</OptionName>
        <Value>false</Value>
        <Namespace>aws:elasticbeanstalk:hostmanager</Namespace>
      </member>
      <member>
        <OptionName>JVM Options</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <OptionName>Notification Topic Name</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <OptionName>PARAM2</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>LoadBalancerHTTPPort</OptionName>
        <Value>80</Value>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
      <member>
        <OptionName>Timeout</OptionName>
        <Value>5</Value>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <OptionName>BreachDuration</OptionName>
        <Value>2</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>MonitoringInterval</OptionName>
        <Value>5 minute</Value>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <OptionName>PARAM1</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>MaxSize</OptionName>
        <Value>4</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>LowerThreshold</OptionName>
        <Value>2000000</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>AWS_SECRET_KEY</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>AWS_ACCESS_KEY_ID</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>UpperThreshold</OptionName>
        <Value>6000000</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>Notification Protocol</OptionName>
        <Value>email</Value>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <OptionName>Unit</OptionName>
        <Value>Bytes</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>Xmx</OptionName>
        <Value>256m</Value>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <OptionName>Cooldown</OptionName>
        <Value>360</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>Period</OptionName>
        <Value>1</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>Xms</OptionName>
        <Value>256m</Value>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <OptionName>EC2KeyName</OptionName>
        <Value/>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <OptionName>Stickiness Policy</OptionName>
        <Value>false</Value>
        <Namespace>aws:elb:policies</Namespace>
      </member>
      <member>
        <OptionName>PARAM3</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>HealthyThreshold</OptionName>
        <Value>3</Value>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <OptionName>SSLCertificateId</OptionName>
        <Value/>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
    </OptionSettings>
    <Description>ConfigTemplateDescription</Description>
    <ApplicationName>SampleApp</ApplicationName>
    <DateCreated>2010-11-17T03:48:19.640Z</DateCreated>
    <TemplateName>AppTemplate</TemplateName>
    <DateUpdated>2010-11-17T03:48:19.640Z</DateUpdated>
  </CreateConfigurationTemplateResult>
  <ResponseMetadata>
    <RequestId>846cd905-f1fd-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</CreateConfigurationTemplateResponse>
```

## See Also
<a name="API_CreateConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/CreateConfigurationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

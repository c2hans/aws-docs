---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationSettings.html
---

# DescribeConfigurationSettings
<a name="API_DescribeConfigurationSettings"></a>

Returns a description of the settings for the specified configuration set, that is, either a configuration template or the configuration set associated with a running environment.

When describing the settings for the configuration set associated with a running environment, it is possible to receive two sets of setting descriptions. One is the deployed configuration set, and the other is a draft configuration of an environment that is either in the process of deployment or that failed to deploy.

This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

Related Topics
+  [DeleteEnvironmentConfiguration](API_DeleteEnvironmentConfiguration.md)

## Request Parameters
<a name="API_DescribeConfigurationSettings_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The application for the environment or configuration template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** EnvironmentName **
The name of the environment to describe.
 Condition: You must specify either this or a TemplateName, but not both. If you specify both, AWS Elastic Beanstalk returns an `InvalidParameterCombination` error. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** TemplateName **
The name of the configuration template to describe.
 Conditional: You must specify either this parameter or an EnvironmentName, but not both. If you specify both, AWS Elastic Beanstalk returns an `InvalidParameterCombination` error. If you do not specify either, AWS Elastic Beanstalk returns a `MissingRequiredParameter` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_DescribeConfigurationSettings_ResponseElements"></a>

The following element is returned by the service.

 **ConfigurationSettings.member.N**
 A list of [ConfigurationSettingsDescription](API_ConfigurationSettingsDescription.md).
Type: Array of [ConfigurationSettingsDescription](API_ConfigurationSettingsDescription.md) objects

## Errors
<a name="API_DescribeConfigurationSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** TooManyBuckets **
The specified account has reached its limit of Amazon S3 buckets.
HTTP Status Code: 400

## Examples
<a name="API_DescribeConfigurationSettings_Examples"></a>

### Example
<a name="API_DescribeConfigurationSettings_Example_1"></a>

This example illustrates one usage of DescribeConfigurationSettings.

#### Sample Request
<a name="API_DescribeConfigurationSettings_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&TemplateName=default
&Operation=DescribeConfigurationSettings
&AuthParams
```

#### Sample Response
<a name="API_DescribeConfigurationSettings_Example_1_Response"></a>

```
<DescribeConfigurationSettingsResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <DescribeConfigurationSettingsResult>
    <ConfigurationSettings>
      <member>
        <SolutionStackName>32bit Amazon Linux running Tomcat 7</SolutionStackName>
        <OptionSettings>
      <member>
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
        <Description>Default Configuration Template</Description>
        <ApplicationName>SampleApp</ApplicationName>
        <DateCreated>2010-11-17T03:20:17.832Z</DateCreated>
        <TemplateName>Default</TemplateName>
        <DateUpdated>2010-11-17T03:20:17.832Z</DateUpdated>
      </member>
    </ConfigurationSettings>
  </DescribeConfigurationSettingsResult>
  <ResponseMetadata>
    <RequestId>4bde8884-f273-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DescribeConfigurationSettingsResponse>
```

## See Also
<a name="API_DescribeConfigurationSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeConfigurationSettings)

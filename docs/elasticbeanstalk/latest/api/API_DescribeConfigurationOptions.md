---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeConfigurationOptions.html
---

# DescribeConfigurationOptions
<a name="API_DescribeConfigurationOptions"></a>

Describes the configuration options that are used in a particular configuration template or environment, or that a specified solution stack defines. The description includes the values the options, their default values, and an indication of the required action on a running environment if an option value is changed.

This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Request Parameters
<a name="API_DescribeConfigurationOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application associated with the configuration template or environment. Only needed if you want to describe the configuration options associated with either the configuration template or environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** EnvironmentName **
The name of the environment whose configuration options you want to describe.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 **Options.member.N**
If specified, restricts the descriptions to only the specified options.
Type: Array of [OptionSpecification](API_OptionSpecification.md) objects
Required: No

 ** PlatformArn **
The ARN of the custom platform.
Type: String
Required: No

 ** SolutionStackName **
The name of the solution stack whose configuration options you want to describe.
Type: String
Required: No

 ** TemplateName **
The name of the configuration template whose configuration options you want to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_DescribeConfigurationOptions_ResponseElements"></a>

The following elements are returned by the service.

 **Options.member.N**
 A list of [ConfigurationOptionDescription](API_ConfigurationOptionDescription.md).
Type: Array of [ConfigurationOptionDescription](API_ConfigurationOptionDescription.md) objects

 ** PlatformArn **
The ARN of the platform version.
Type: String

 ** SolutionStackName **
The name of the solution stack these configuration options belong to.
Type: String

## Errors
<a name="API_DescribeConfigurationOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** TooManyBuckets **
The specified account has reached its limit of Amazon S3 buckets.
HTTP Status Code: 400

## Examples
<a name="API_DescribeConfigurationOptions_Examples"></a>

### Example
<a name="API_DescribeConfigurationOptions_Example_1"></a>

This example illustrates one usage of DescribeConfigurationOptions.

#### Sample Request
<a name="API_DescribeConfigurationOptions_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&TemplateName=default
&Operation=DescribeConfigurationOptions
&AuthParams
```

#### Sample Response
<a name="API_DescribeConfigurationOptions_Example_1_Response"></a>

```
<DescribeConfigurationOptionsResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <DescribeConfigurationOptionsResult>
    <SolutionStackName>32bit Amazon Linux running Tomcat 7</SolutionStackName>
    <Options>
            <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>ImageId</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>ami-6036c009</DefaultValue>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>Notification Endpoint</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>PARAM4</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>JDBC_CONNECTION_STRING</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>SecurityGroups</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>elasticbeanstalk-default</DefaultValue>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>2</MinValue>
        <Name>UnhealthyThreshold</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>5</DefaultValue>
        <MaxValue>10</MaxValue>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <Name>InstanceType</Name>
        <ValueOptions>
          <member>t1.micro</member>
          <member>m1.small</member>
        </ValueOptions>
        <ValueType>Scalar</ValueType>
        <DefaultValue>t1.micro</DefaultValue>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <Name>Statistic</Name>
        <ValueOptions>
          <member>Minimum</member>
          <member>Maximum</member>
          <member>Sum</member>
          <member>Average</member>
        </ValueOptions>
        <ValueType>Scalar</ValueType>
        <DefaultValue>Average</DefaultValue>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <Name>LoadBalancerHTTPSPort</Name>
        <ValueOptions>
          <member>OFF</member>
          <member>443</member>
          <member>8443</member>
          <member>5443</member>
        </ValueOptions>
        <ValueType>Scalar</ValueType>
        <DefaultValue>OFF</DefaultValue>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>0</MinValue>
        <Name>Stickiness Cookie Expiration</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>0</DefaultValue>
        <MaxValue>1000000</MaxValue>
        <Namespace>aws:elb:policies</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>PARAM5</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <Name>MeasureName</Name>
        <ValueOptions>
          <member>CPUUtilization</member>
          <member>NetworkIn</member>
          <member>NetworkOut</member>
          <member>DiskWriteOps</member>
          <member>DiskReadBytes</member>
          <member>DiskReadOps</member>
          <member>DiskWriteBytes</member>
          <member>Latency</member>
          <member>RequestCount</member>
          <member>HealthyHostCount</member>
          <member>UnhealthyHostCount</member>
        </ValueOptions>
        <ValueType>Scalar</ValueType>
        <DefaultValue>NetworkOut</DefaultValue>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>5</MinValue>
        <Name>Interval</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>30</DefaultValue>
        <MaxValue>300</MaxValue>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>Application Healthcheck URL</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>/</DefaultValue>
        <Namespace>aws:elasticbeanstalk:application</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>Notification Topic ARN</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>LowerBreachScaleIncrement</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>-1</DefaultValue>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Regex>
          <Pattern>^\S*$</Pattern>
          <Label>nospaces</Label>
        </Regex>
        <Name>XX:MaxPermSize</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>64m</DefaultValue>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>UpperBreachScaleIncrement</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>1</DefaultValue>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>1</MinValue>
        <Name>MinSize</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>1</DefaultValue>
        <MaxValue>10000</MaxValue>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <Name>Custom Availability Zones</Name>
        <ValueOptions>
          <member>us-east-1a</member>
          <member>us-east-1b</member>
          <member>us-east-1c</member>
          <member>us-east-1d</member>
        </ValueOptions>
        <ValueType>List</ValueType>
        <DefaultValue>us-east-1a</DefaultValue>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <Name>Availability Zones</Name>
        <ValueOptions>
          <member>Any 1</member>
          <member>Any 2</member>
        </ValueOptions>
        <ValueType>Scalar</ValueType>
        <DefaultValue>Any 1</DefaultValue>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <Name>LogPublicationControl</Name>
        <ValueType>Boolean</ValueType>
        <DefaultValue>false</DefaultValue>
        <Namespace>aws:elasticbeanstalk:hostmanager</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>JVM Options</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>Notification Topic Name</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>PARAM2</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <Name>LoadBalancerHTTPPort</Name>
        <ValueOptions>
          <member>OFF</member>
          <member>80</member>
          <member>8080</member>
        </ValueOptions>
        <ValueType>Scalar</ValueType>
        <DefaultValue>80</DefaultValue>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>2</MinValue>
        <Name>Timeout</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>5</DefaultValue>
        <MaxValue>60</MaxValue>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>1</MinValue>
        <Name>BreachDuration</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>2</DefaultValue>
        <MaxValue>600</MaxValue>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <Name>MonitoringInterval</Name>
        <ValueOptions>
          <member>1 minute</member>
          <member>5 minute</member>
        </ValueOptions>
        <ValueType>Scalar</ValueType>
        <DefaultValue>5 minute</DefaultValue>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>PARAM1</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>1</MinValue>
        <Name>MaxSize</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>4</DefaultValue>
        <MaxValue>10000</MaxValue>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>0</MinValue>
        <Name>LowerThreshold</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>2000000</DefaultValue>
        <MaxValue>20000000</MaxValue>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>AWS_SECRET_KEY</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>AWS_ACCESS_KEY_ID</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>0</MinValue>
        <Name>UpperThreshold</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>6000000</DefaultValue>
        <MaxValue>20000000</MaxValue>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <Name>Notification Protocol</Name>
        <ValueOptions>
          <member>http</member>
          <member>https</member>
          <member>email</member>
          <member>email-json</member>
          <member>sqs</member>
        </ValueOptions>
        <ValueType>Scalar</ValueType>
        <DefaultValue>email</DefaultValue>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <Name>Unit</Name>
        <ValueOptions>
          <member>Seconds</member>
          <member>Percent</member>
          <member>Bytes</member>
          <member>Bits</member>
          <member>Count</member>
          <member>Bytes/Second</member>
          <member>Bits/Second</member>
          <member>Count/Second</member>
          <member>None</member>
        </ValueOptions>
        <ValueType>Scalar</ValueType>
        <DefaultValue>Bytes</DefaultValue>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Regex>
          <Pattern>^\S*$</Pattern>
          <Label>nospaces</Label>
        </Regex>
        <Name>Xmx</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>256m</DefaultValue>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>0</MinValue>
        <Name>Cooldown</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>360</DefaultValue>
        <MaxValue>10000</MaxValue>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>1</MinValue>
        <Name>Period</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>1</DefaultValue>
        <MaxValue>600</MaxValue>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Regex>
          <Pattern>^\S*$</Pattern>
          <Label>nospaces</Label>
        </Regex>
        <Name>Xms</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>256m</DefaultValue>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>EC2KeyName</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <Name>Stickiness Policy</Name>
        <ValueType>Boolean</ValueType>
        <DefaultValue>false</DefaultValue>
        <Namespace>aws:elb:policies</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartApplicationServer</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>PARAM3</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>NoInterruption</ChangeSeverity>
        <MinValue>2</MinValue>
        <Name>HealthyThreshold</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue>3</DefaultValue>
        <MaxValue>10</MaxValue>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <UserDefined>false</UserDefined>
        <ChangeSeverity>RestartEnvironment</ChangeSeverity>
        <MaxLength>2000</MaxLength>
        <Name>SSLCertificateId</Name>
        <ValueType>Scalar</ValueType>
        <DefaultValue/>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
    </Options>
  </DescribeConfigurationOptionsResult>
  <ResponseMetadata>
    <RequestId>e8768900-f272-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DescribeConfigurationOptionsResponse>
```

## See Also
<a name="API_DescribeConfigurationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeConfigurationOptions)

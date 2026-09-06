---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateConfigurationTemplate.html
---

# UpdateConfigurationTemplate
<a name="API_UpdateConfigurationTemplate"></a>

Updates the specified configuration template to have the specified properties or configuration option values.

**Note**
If a property (for example, `ApplicationName`) is not provided, its value remains unchanged. To clear such properties, specify an empty string.

Related Topics
+  [DescribeConfigurationOptions](API_DescribeConfigurationOptions.md)

## Request Parameters
<a name="API_UpdateConfigurationTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application associated with the configuration template to update.
 If no application is found with this name, `UpdateConfigurationTemplate` returns an `InvalidParameterValue` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Description **
A new description for the configuration.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 **OptionSettings.member.N**
A list of configuration option settings to update with the new specified option value.
Type: Array of [ConfigurationOptionSetting](API_ConfigurationOptionSetting.md) objects
Required: No

 **OptionsToRemove.member.N**
A list of configuration options to remove from the configuration set.
 Constraint: You can remove only `UserDefined` configuration options.
Type: Array of [OptionSpecification](API_OptionSpecification.md) objects
Required: No

 ** TemplateName **
The name of the configuration template to update.
 If no configuration template is found with this name, `UpdateConfigurationTemplate` returns an `InvalidParameterValue` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Elements
<a name="API_UpdateConfigurationTemplate_ResponseElements"></a>

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
<a name="API_UpdateConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** TooManyBuckets **
The specified account has reached its limit of Amazon S3 buckets.
HTTP Status Code: 400

## Examples
<a name="API_UpdateConfigurationTemplate_Examples"></a>

### Example
<a name="API_UpdateConfigurationTemplate_Example_1"></a>

This example illustrates one usage of UpdateConfigurationTemplate.

#### Sample Request
<a name="API_UpdateConfigurationTemplate_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&TemplateName=default
&Description=changed%20description
&OptionSettings.member.1.Namespace=aws%3Aautoscaling%3Atrigger
&OptionSettings.member.1.OptionName=LowerThreshold
&OptionSettings.member.1.Value=1000000
&Operation=UpdateConfigurationTemplate
&AuthParams
```

#### Sample Response
<a name="API_UpdateConfigurationTemplate_Example_1_Response"></a>

```
<UpdateConfigurationTemplateResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <UpdateConfigurationTemplateResult>
    <SolutionStackName>32bit Amazon Linux running Tomcat 7</SolutionStackName>
    <OptionSettings>
      <member>
        <OptionName>Availability Zones</OptionName>
        <Value>Any 1</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>PARAM5</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>LowerThreshold</OptionName>
        <Value>1000000</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>UpperThreshold</OptionName>
        <Value>9000000</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>LowerBreachScaleIncrement</OptionName>
        <Value>-1</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>MeasureName</OptionName>
        <Value>NetworkOut</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>Period</OptionName>
        <Value>60</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>Xmx</OptionName>
        <Value>256m</Value>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <OptionName>PARAM3</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>EC2KeyName</OptionName>
        <Value/>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <OptionName>MinSize</OptionName>
        <Value>1</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>JVM Options</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <OptionName>XX:MaxPermSize</OptionName>
        <Value>64m</Value>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
      <member>
        <OptionName>AWS_SECRET_KEY</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>UpperBreachScaleIncrement</OptionName>
        <Value>1</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>Notification Topic ARN</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <OptionName>InstanceType</OptionName>
        <Value>t1.micro</Value>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <OptionName>Custom Availability Zones</OptionName>
        <Value>us-east-1a</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>Statistic</OptionName>
        <Value>Average</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>Notification Protocol</OptionName>
        <Value>email</Value>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <OptionName>JDBC_CONNECTION_STRING</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>PARAM2</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>Stickiness Cookie Expiration</OptionName>
        <Value>0</Value>
        <Namespace>aws:elb:policies</Namespace>
      </member>
      <member>
        <OptionName>SSLCertificateId</OptionName>
        <Value/>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
      <member>
        <OptionName>MaxSize</OptionName>
        <Value>4</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>Stickiness Policy</OptionName>
        <Value>false</Value>
        <Namespace>aws:elb:policies</Namespace>
      </member>
      <member>
        <OptionName>Notification Topic Name</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <OptionName>SecurityGroups</OptionName>
        <Value>elasticbeanstalk-default</Value>
        <Namespace>aws:autoscaling:launchconfiguration</Namespace>
      </member>
      <member>
        <OptionName>LoadBalancerHTTPPort</OptionName>
        <Value>80</Value>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
      <member>
        <OptionName>Unit</OptionName>
        <Value>None</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>AWS_ACCESS_KEY_ID</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>PARAM4</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>Application Healthcheck URL</OptionName>
        <Value>/</Value>
        <Namespace>aws:elasticbeanstalk:application</Namespace>
      </member>
      <member>
        <OptionName>LoadBalancerHTTPSPort</OptionName>
        <Value>OFF</Value>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
      <member>
        <OptionName>HealthyThreshold</OptionName>
        <Value>3</Value>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <OptionName>Timeout</OptionName>
        <Value>5</Value>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <OptionName>Cooldown</OptionName>
        <Value>0</Value>
        <Namespace>aws:autoscaling:asg</Namespace>
      </member>
      <member>
        <OptionName>UnhealthyThreshold</OptionName>
        <Value>5</Value>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <OptionName>Interval</OptionName>
        <Value>30</Value>
        <Namespace>aws:elb:healthcheck</Namespace>
      </member>
      <member>
        <OptionName>LogPublicationControl</OptionName>
        <Value>false</Value>
        <Namespace>aws:elasticbeanstalk:hostmanager</Namespace>
      </member>
      <member>
        <OptionName>BreachDuration</OptionName>
        <Value>120</Value>
        <Namespace>aws:autoscaling:trigger</Namespace>
      </member>
      <member>
        <OptionName>PARAM1</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:application:environment</Namespace>
      </member>
      <member>
        <OptionName>Notification Endpoint</OptionName>
        <Value/>
        <Namespace>aws:elasticbeanstalk:sns:topics</Namespace>
      </member>
      <member>
        <OptionName>Protocol</OptionName>
        <Value>HTTP</Value>
        <Namespace>aws:elb:loadbalancer</Namespace>
      </member>
      <member>
        <OptionName>Xms</OptionName>
        <Value>256m</Value>
        <Namespace>aws:elasticbeanstalk:container:tomcat:jvmoptions</Namespace>
      </member>
    </OptionSettings>
    <Description>changed description</Description>
    <ApplicationName>SampleApp</ApplicationName>
    <DateCreated>2010-11-17T19:26:20.420Z</DateCreated>
    <TemplateName>Default</TemplateName>
    <DateUpdated>2010-11-17T20:58:27.508Z</DateUpdated>
  </UpdateConfigurationTemplateResult>
  <ResponseMetadata>
    <RequestId>6cbcb09a-f28d-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</UpdateConfigurationTemplateResponse>
```

## See Also
<a name="API_UpdateConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/UpdateConfigurationTemplate)

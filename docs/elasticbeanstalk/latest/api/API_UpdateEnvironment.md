---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateEnvironment.html
---

# UpdateEnvironment
<a name="API_UpdateEnvironment"></a>

Updates the environment description, deploys a new application version, updates the configuration settings to an entirely new configuration template, or updates select configuration option values in the running environment.

 Attempting to update both the release and configuration is not allowed and AWS Elastic Beanstalk returns an `InvalidParameterCombination` error.

 When updating the configuration settings to a new template or individual settings, a draft configuration is created and [DescribeConfigurationSettings](API_DescribeConfigurationSettings.md) for this environment returns two setting descriptions with different `DeploymentStatus` values.

## Request Parameters
<a name="API_UpdateEnvironment_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application with which the environment is associated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Description **
If this parameter is specified, AWS Elastic Beanstalk updates the description of this environment.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** EnvironmentId **
The ID of the environment to update.
If no environment with this ID exists, AWS Elastic Beanstalk returns an `InvalidParameterValue` error.
Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Required: No

 ** EnvironmentName **
The name of the environment to update. If no environment with this name exists, AWS Elastic Beanstalk returns an `InvalidParameterValue` error.
Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** GroupName **
The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name or environment ID parameters. See [Environment Manifest (env.yaml)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html) for details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Required: No

 **OptionSettings.member.N**
If specified, AWS Elastic Beanstalk updates the configuration set associated with the running environment and sets the specified configuration options to the requested value.
Type: Array of [ConfigurationOptionSetting](API_ConfigurationOptionSetting.md) objects
Required: No

 **OptionsToRemove.member.N**
A list of custom user-defined configuration options to remove from the configuration set for this environment.
Type: Array of [OptionSpecification](API_OptionSpecification.md) objects
Required: No

 ** PlatformArn **
The ARN of the platform, if used.
Type: String
Required: No

 ** SolutionStackName **
This specifies the platform version that the environment will run after the environment is updated.
Type: String
Required: No

 ** TemplateName **
If this parameter is specified, AWS Elastic Beanstalk deploys this configuration template to the environment. If no such configuration template is found, AWS Elastic Beanstalk returns an `InvalidParameterValue` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Tier **
This specifies the tier to use to update the environment.
Condition: At this time, if you change the tier version, name, or type, AWS Elastic Beanstalk returns `InvalidParameterValue` error.
Type: [EnvironmentTier](API_EnvironmentTier.md) object
Required: No

 ** VersionLabel **
If this parameter is specified, AWS Elastic Beanstalk deploys the named application version to the environment. If no such application version is found, returns an `InvalidParameterValue` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_UpdateEnvironment_ResponseElements"></a>

The following elements are returned by the service.

 ** AbortableOperationInProgress **
Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.
 `true:` There is an update in progress.
 `false:` There are no updates currently in progress.
Type: Boolean

 ** ApplicationName **
The name of the application associated with this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** CNAME **
The URL to the CNAME for this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** DateCreated **
The creation date for this environment.
Type: Timestamp

 ** DateUpdated **
The last modified date for this environment.
Type: Timestamp

 ** Description **
Describes this environment.
Type: String
Length Constraints: Maximum length of 200.

 ** EndpointURL **
For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.
Type: String

 ** EnvironmentArn **
The environment's Amazon Resource Name (ARN), which can be used in other API requests that require an ARN.
Type: String

 ** EnvironmentId **
The ID of this environment.
Type: String

 **EnvironmentLinks.member.N**
A list of links to other environments in the same group.
Type: Array of [EnvironmentLink](API_EnvironmentLink.md) objects

 ** EnvironmentName **
The name of this environment.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.

 ** Health **
Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure levels for a running environment:
+  `Red`: Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment.
+  `Yellow`: Indicates that something is wrong. Occurs when two consecutive failures occur for an environment.
+  `Green`: Indicates the environment is healthy and fully functional.
+  `Grey`: Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an `UpdateEnvironment` or `RestartEnvironment` request.
 Default: `Grey`
Type: String
Valid Values: `Green | Yellow | Red | Grey`

 ** HealthStatus **
Returns the health status of the application running in your environment. For more information, see [Health Colors and Statuses](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html).
Type: String
Valid Values: `NoData | Unknown | Pending | Ok | Info | Warning | Degraded | Severe | Suspended`

 ** OperationsRole **
The operations role feature of AWS Elastic Beanstalk is in beta release and is subject to change.
The Amazon Resource Name (ARN) of the environment's operations role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** PlatformArn **
The ARN of the platform version.
Type: String

 ** Resources **
The description of the AWS resources used by this environment.
Type: [EnvironmentResourcesDescription](API_EnvironmentResourcesDescription.md) object

 ** SolutionStackName **
 The name of the `SolutionStack` deployed with this environment.
Type: String

 ** Status **
The current operational status of the environment:
+  `Aborting`: Environment is in the process of aborting a deployment.
+  `Launching`: Environment is in the process of initial deployment.
+  `LinkingFrom`: Environment is in the process of being linked to by another environment. See [Environment links](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-links.html) for details.
+  `LinkingTo`: Environment is in the process of linking to another environment. See [Environment links](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-links.html) for details.
+  `Updating`: Environment is in the process of updating its configuration settings or application version.
+  `Ready`: Environment is available to have an action performed on it, such as update or terminate.
+  `Terminating`: Environment is in the shut-down process.
+  `Terminated`: Environment is not running.
Type: String
Valid Values: `Aborting | Launching | Updating | LinkingFrom | LinkingTo | Ready | Terminating | Terminated`

 ** TemplateName **
The name of the configuration template used to originally launch this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** Tier **
Describes the current tier of this environment.
Type: [EnvironmentTier](API_EnvironmentTier.md) object

 ** VersionLabel **
The application version deployed in this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

## Errors
<a name="API_UpdateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** TooManyBuckets **
The specified account has reached its limit of Amazon S3 buckets.
HTTP Status Code: 400

## Examples
<a name="API_UpdateEnvironment_Examples"></a>

### Example
<a name="API_UpdateEnvironment_Example_1"></a>

This example illustrates one usage of UpdateEnvironment.

#### Sample Request
<a name="API_UpdateEnvironment_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?EnvironmentId=e-hc8mvnayrx
&EnvironmentName=SampleAppVersion
&TemplateName=default
&OptionsToRemove.member.1.Namespace=aws%3Aautoscaling%3Atrigger
&OptionsToRemove.member.1.OptionName=MeasureName
&Operation=UpdateEnvironment
&AuthParams
```

#### Sample Response
<a name="API_UpdateEnvironment_Example_1_Response"></a>

```
<UpdateEnvironmentResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <UpdateEnvironmentResult>
    <VersionLabel>New Version</VersionLabel>
    <Status>Deploying</Status>
    <ApplicationName>SampleApp</ApplicationName>
    <EndpointURL>elasticbeanstalk-SampleAppVersion-246126201.us-east-1.elb.amazonaws.com</EndpointURL>
    <CNAME>SampleApp.elasticbeanstalk.amazonaws.com</CNAME>
    <Health>Grey</Health>
    <EnvironmentId>e-hc8mvnayrx</EnvironmentId>
    <DateUpdated>2010-11-17T21:05:55.251Z</DateUpdated>
    <SolutionStackName>32bit Amazon Linux running Tomcat 7</SolutionStackName>
    <Description>SampleAppDescription</Description>
    <EnvironmentName>SampleAppVersion</EnvironmentName>
    <DateCreated>2010-11-17T20:17:42.339Z</DateCreated>
  </UpdateEnvironmentResult>
  <ResponseMetadata>
    <RequestId>7705f0bc-f28e-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</UpdateEnvironmentResponse>
```

## See Also
<a name="API_UpdateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/UpdateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/UpdateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/UpdateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/UpdateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/UpdateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/UpdateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/UpdateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/UpdateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/UpdateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/UpdateEnvironment)

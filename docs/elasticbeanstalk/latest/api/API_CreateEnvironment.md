---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateEnvironment.html
---

# CreateEnvironment
<a name="API_CreateEnvironment"></a>

Launches an AWS Elastic Beanstalk environment for the specified application using the specified configuration.

## Request Parameters
<a name="API_CreateEnvironment_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application that is associated with this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** CNAMEPrefix **
If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 63.
Required: No

 ** Description **
Your description for this environment.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** EnvironmentName **
A unique name for the environment.
Constraint: Must be from 4 to 40 characters in length. The name can contain only letters, numbers, and hyphens. It can't start or end with a hyphen. This name must be unique within a region in your account. If the specified name already exists in the region, Elastic Beanstalk returns an `InvalidParameterValue` error.
If you don't specify the `CNAMEPrefix` parameter, the environment name becomes part of the CNAME, and therefore part of the visible URL for your application.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** GroupName **
The name of the group to which the target environment belongs. Specify a group name only if the environment's name is specified in an environment manifest and not with the environment name parameter. See [Environment Manifest (env.yaml)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html) for details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Required: No

 ** OperationsRole **
The operations role feature of AWS Elastic Beanstalk is in beta release and is subject to change.
The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role. If specified, Elastic Beanstalk uses the operations role for permissions to downstream services during this call and during subsequent calls acting on this environment. To specify an operations role, you must have the `iam:PassRole` permission for the role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 **OptionSettings.member.N**
If specified, AWS Elastic Beanstalk sets the specified configuration options to the requested value in the configuration set for the new environment. These override the values obtained from the solution stack or the configuration template.
Type: Array of [ConfigurationOptionSetting](API_ConfigurationOptionSetting.md) objects
Required: No

 **OptionsToRemove.member.N**
A list of custom user-defined configuration options to remove from the configuration set for this new environment.
Type: Array of [OptionSpecification](API_OptionSpecification.md) objects
Required: No

 ** PlatformArn **
The Amazon Resource Name (ARN) of the custom platform to use with the environment. For more information, see [Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the * AWS Elastic Beanstalk Developer Guide*.
If you specify `PlatformArn`, don't specify `SolutionStackName`.
Type: String
Required: No

 ** SolutionStackName **
The name of an Elastic Beanstalk solution stack (platform version) to use with the environment. If specified, Elastic Beanstalk sets the configuration values to the default values associated with the specified solution stack. For a list of current solution stacks, see [Elastic Beanstalk Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html) in the * AWS Elastic Beanstalk Platforms* guide.
If you specify `SolutionStackName`, don't specify `PlatformArn` or `TemplateName`.
Type: String
Required: No

 **Tags.member.N**
Specifies the tags applied to resources in the environment.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TemplateName **
The name of the Elastic Beanstalk configuration template to use with the environment.
If you specify `TemplateName`, then don't specify `SolutionStackName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Tier **
Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.
Type: [EnvironmentTier](API_EnvironmentTier.md) object
Required: No

 ** VersionLabel **
The name of the application version to deploy.
Default: If not specified, Elastic Beanstalk attempts to deploy the sample application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_CreateEnvironment_ResponseElements"></a>

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
<a name="API_CreateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** TooManyEnvironments **
The specified account has reached its limit of environments.
HTTP Status Code: 400

## Examples
<a name="API_CreateEnvironment_Examples"></a>

### Example
<a name="API_CreateEnvironment_Example_1"></a>

This example illustrates one usage of CreateEnvironment.

#### Sample Request
<a name="API_CreateEnvironment_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&EnvironmentName=SampleApp
&SolutionStackName=32bit%20Amazon%20Linux%20running%20Tomcat%207
&Description=EnvDescrip
&Operation=CreateEnvironment
&AuthParams
```

#### Sample Response
<a name="API_CreateEnvironment_Example_1_Response"></a>

```
<CreateEnvironmentResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <CreateEnvironmentResult>
    <VersionLabel>Version1</VersionLabel>
    <Status>Deploying</Status>
    <ApplicationName>SampleApp</ApplicationName>
    <Health>Grey</Health>
    <EnvironmentId>e-icsgecu3wf</EnvironmentId>
    <DateUpdated>2010-11-17T03:59:33.520Z</DateUpdated>
    <SolutionStackName>32bit Amazon Linux running Tomcat 7</SolutionStackName>
    <Description>EnvDescrip</Description>
    <EnvironmentName>SampleApp</EnvironmentName>
    <DateCreated>2010-11-17T03:59:33.520Z</DateCreated>
  </CreateEnvironmentResult>
  <ResponseMetadata>
    <RequestId>15db925e-f1ff-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</CreateEnvironmentResponse>
```

## See Also
<a name="API_CreateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/CreateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/CreateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/CreateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/CreateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/CreateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/CreateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/CreateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/CreateEnvironment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/CreateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/CreateEnvironment)

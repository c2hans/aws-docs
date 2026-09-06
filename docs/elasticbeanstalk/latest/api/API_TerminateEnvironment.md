---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_TerminateEnvironment.html
---

# TerminateEnvironment
<a name="API_TerminateEnvironment"></a>

Terminates the specified environment.

## Request Parameters
<a name="API_TerminateEnvironment_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnvironmentId **
The ID of the environment to terminate.
 Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Required: No

 ** EnvironmentName **
The name of the environment to terminate.
 Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** ForceTerminate **
Terminates the target environment even if another environment in the same group is dependent on it.
Type: Boolean
Required: No

 ** TerminateResources **
Indicates whether the associated AWS resources should shut down when the environment is terminated:
+  `true`: The specified environment as well as the associated AWS resources, such as Auto Scaling group and LoadBalancer, are terminated.
+  `false`: AWS Elastic Beanstalk resource management is removed from the environment, but the AWS resources continue to operate.
 For more information, see the [AWS Elastic Beanstalk User Guide. ](https://docs.aws.amazon.com/elasticbeanstalk/latest/ug/)
 Default: `true`
 Valid Values: `true` \| `false`
Type: Boolean
Required: No

## Response Elements
<a name="API_TerminateEnvironment_ResponseElements"></a>

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
<a name="API_TerminateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

## Examples
<a name="API_TerminateEnvironment_Examples"></a>

### Example
<a name="API_TerminateEnvironment_Example_1"></a>

This example illustrates one usage of TerminateEnvironment.

#### Sample Request
<a name="API_TerminateEnvironment_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?EnvironmentId=e-icsgecu3wf
&EnvironmentName=SampleApp
&TerminateResources=true
&Operation=TerminateEnvironment
&AuthParams
```

#### Sample Response
<a name="API_TerminateEnvironment_Example_1_Response"></a>

```
<TerminateEnvironmentResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <TerminateEnvironmentResult>
    <VersionLabel>Version1</VersionLabel>
    <Status>Terminating</Status>
    <ApplicationName>SampleApp</ApplicationName>
    <EndpointURL>elasticbeanstalk-SampleApp-1394386994.us-east-1.elb.amazonaws.com</EndpointURL>
    <CNAME>SampleApp-jxb293wg7n.elasticbeanstalk.amazonaws.com</CNAME>
    <Health>Grey</Health>
    <EnvironmentId>e-icsgecu3wf</EnvironmentId>
    <DateUpdated>2010-11-17T17:10:41.976Z</DateUpdated>
    <SolutionStackName>32bit Amazon Linux running Tomcat 7</SolutionStackName>
    <Description>EnvDescrip</Description>
    <EnvironmentName>SampleApp</EnvironmentName>
    <DateCreated>2010-11-17T03:59:33.520Z</DateCreated>
  </TerminateEnvironmentResult>
  <ResponseMetadata>
    <RequestId>9b71af21-f26d-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</TerminateEnvironmentResponse>
```

## See Also
<a name="API_TerminateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/TerminateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/TerminateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/TerminateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/TerminateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/TerminateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/TerminateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/TerminateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/TerminateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/TerminateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/TerminateEnvironment)

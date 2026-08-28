---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentDescription.html
---

# EnvironmentDescription
<a name="API_EnvironmentDescription"></a>

Describes the properties of an environment.

## Contents
<a name="API_EnvironmentDescription_Contents"></a>

 ** AbortableOperationInProgress **
Indicates if there is an in-progress environment configuration update or application version deployment that you can cancel.
 `true:` There is an update in progress.
 `false:` There are no updates currently in progress.
Type: Boolean
Required: No

 ** ApplicationName **
The name of the application associated with this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** CNAME **
The URL to the CNAME for this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** DateCreated **
The creation date for this environment.
Type: Timestamp
Required: No

 ** DateUpdated **
The last modified date for this environment.
Type: Timestamp
Required: No

 ** Description **
Describes this environment.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** EndpointURL **
For load-balanced, autoscaling environments, the URL to the LoadBalancer. For single-instance environments, the IP address of the instance.
Type: String
Required: No

 ** EnvironmentArn **
The environment's Amazon Resource Name (ARN), which can be used in other API requests that require an ARN.
Type: String
Required: No

 ** EnvironmentId **
The ID of this environment.
Type: String
Required: No

 ** EnvironmentLinks.member.N **
A list of links to other environments in the same group.
Type: Array of [EnvironmentLink](API_EnvironmentLink.md) objects
Required: No

 ** EnvironmentName **
The name of this environment.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** Health **
Describes the health status of the environment. AWS Elastic Beanstalk indicates the failure levels for a running environment:
+  `Red`: Indicates the environment is not responsive. Occurs when three or more consecutive failures occur for an environment.
+  `Yellow`: Indicates that something is wrong. Occurs when two consecutive failures occur for an environment.
+  `Green`: Indicates the environment is healthy and fully functional.
+  `Grey`: Default health for a new environment. The environment is not fully launched and health checks have not started or health checks are suspended during an `UpdateEnvironment` or `RestartEnvironment` request.
 Default: `Grey`
Type: String
Valid Values: `Green | Yellow | Red | Grey`
Required: No

 ** HealthStatus **
Returns the health status of the application running in your environment. For more information, see [Health Colors and Statuses](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html).
Type: String
Valid Values: `NoData | Unknown | Pending | Ok | Info | Warning | Degraded | Severe | Suspended`
Required: No

 ** OperationsRole **
The operations role feature of AWS Elastic Beanstalk is in beta release and is subject to change.
The Amazon Resource Name (ARN) of the environment's operations role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** PlatformArn **
The ARN of the platform version.
Type: String
Required: No

 ** Resources **
The description of the AWS resources used by this environment.
Type: [EnvironmentResourcesDescription](API_EnvironmentResourcesDescription.md) object
Required: No

 ** SolutionStackName **
 The name of the `SolutionStack` deployed with this environment.
Type: String
Required: No

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
Required: No

 ** TemplateName **
The name of the configuration template used to originally launch this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Tier **
Describes the current tier of this environment.
Type: [EnvironmentTier](API_EnvironmentTier.md) object
Required: No

 ** VersionLabel **
The application version deployed in this environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_EnvironmentDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/EnvironmentDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/EnvironmentDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/EnvironmentDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

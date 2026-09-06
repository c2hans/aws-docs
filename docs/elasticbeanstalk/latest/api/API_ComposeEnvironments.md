---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ComposeEnvironments.html
---

# ComposeEnvironments
<a name="API_ComposeEnvironments"></a>

Create or update a group of environments that each run a separate component of a single application. Takes a list of version labels that specify application source bundles for each of the environments to create or update. The name of each environment and other required information must be included in the source bundles in an environment manifest named `env.yaml`. See [Compose Environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-mgmt-compose.html) for details.

## Request Parameters
<a name="API_ComposeEnvironments_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application to which the specified source bundles belong.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** GroupName **
The name of the group to which the target environments belong. Specify a group name only if the environment name defined in each target environment's manifest ends with a \+ (plus) character. See [Environment Manifest (env.yaml)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html) for details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 19.
Required: No

 **VersionLabels.member.N**
A list of version labels, specifying one or more application source bundles that belong to the target application. Each source bundle must include an environment manifest that specifies the name of the environment and the name of the solution stack to use, and optionally can specify environment links to create.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_ComposeEnvironments_ResponseElements"></a>

The following elements are returned by the service.

 **Environments.member.N**
 Returns an [EnvironmentDescription](API_EnvironmentDescription.md) list.
Type: Array of [EnvironmentDescription](API_EnvironmentDescription.md) objects

 ** NextToken **
In a paginated request, the token that you can pass in a subsequent request to get the next response page.
Type: String

## Errors
<a name="API_ComposeEnvironments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** TooManyEnvironments **
The specified account has reached its limit of environments.
HTTP Status Code: 400

## See Also
<a name="API_ComposeEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/ComposeEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/ComposeEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ComposeEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/ComposeEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ComposeEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/ComposeEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/ComposeEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/ComposeEnvironments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/ComposeEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ComposeEnvironments)

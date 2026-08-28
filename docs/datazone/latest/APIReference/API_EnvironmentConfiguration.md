---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EnvironmentConfiguration.html
---

# EnvironmentConfiguration
<a name="API_EnvironmentConfiguration"></a>

The configuration of an environment.

## Contents
<a name="API_EnvironmentConfiguration_Contents"></a>

 ** environmentBlueprintId **   <a name="datazone-Type-EnvironmentConfiguration-environmentBlueprintId"></a>
The environment blueprint ID.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-EnvironmentConfiguration-name"></a>
The environment name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: Yes

 ** accountPools **   <a name="datazone-Type-EnvironmentConfiguration-accountPools"></a>
The account pools used by a custom project profile.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** awsAccount **   <a name="datazone-Type-EnvironmentConfiguration-awsAccount"></a>
The AWS account of the environment.
Type: [AwsAccount](API_AwsAccount.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** awsRegion **   <a name="datazone-Type-EnvironmentConfiguration-awsRegion"></a>
The AWS Region of the environment.
Type: [Region](API_Region.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** configurationParameters **   <a name="datazone-Type-EnvironmentConfiguration-configurationParameters"></a>
The configuration parameters of the environment.
Type: [EnvironmentConfigurationParametersDetails](API_EnvironmentConfigurationParametersDetails.md) object
Required: No

 ** deploymentMode **   <a name="datazone-Type-EnvironmentConfiguration-deploymentMode"></a>
The deployment mode of the environment.
Type: String
Valid Values: `ON_CREATE | ON_DEMAND`
Required: No

 ** deploymentOrder **   <a name="datazone-Type-EnvironmentConfiguration-deploymentOrder"></a>
The deployment order of the environment.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 16.
Required: No

 ** description **   <a name="datazone-Type-EnvironmentConfiguration-description"></a>
The environment description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** id **   <a name="datazone-Type-EnvironmentConfiguration-id"></a>
The environment ID.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_EnvironmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EnvironmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EnvironmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EnvironmentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

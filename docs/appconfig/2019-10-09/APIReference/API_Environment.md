---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Environment.html
---

# Environment
<a name="API_Environment"></a>

## Contents
<a name="API_Environment_Contents"></a>

 ** ApplicationId **   <a name="appconfig-Type-Environment-ApplicationId"></a>
The application ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** Description **   <a name="appconfig-Type-Environment-Description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Id **   <a name="appconfig-Type-Environment-Id"></a>
The environment ID.
Type: String
Pattern: `[a-z0-9]{4,7}`
Required: No

 ** Monitors **   <a name="appconfig-Type-Environment-Monitors"></a>
Amazon CloudWatch alarms monitored during the deployment.
Type: Array of [Monitor](API_Monitor.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** Name **   <a name="appconfig-Type-Environment-Name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** State **   <a name="appconfig-Type-Environment-State"></a>
The state of the environment. An environment can be in one of the following states: `READY_FOR_DEPLOYMENT`, `DEPLOYING`, `ROLLING_BACK`, or `ROLLED_BACK`
Type: String
Valid Values: `READY_FOR_DEPLOYMENT | DEPLOYING | ROLLING_BACK | ROLLED_BACK | REVERTED`
Required: No

## See Also
<a name="API_Environment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/Environment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/Environment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/Environment)

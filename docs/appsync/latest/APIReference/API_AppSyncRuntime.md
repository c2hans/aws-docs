---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_AppSyncRuntime.html
---

# AppSyncRuntime
<a name="API_AppSyncRuntime"></a>

Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.

## Contents
<a name="API_AppSyncRuntime_Contents"></a>

 ** name **   <a name="appsync-Type-AppSyncRuntime-name"></a>
The `name` of the runtime to use. Currently, the only allowed value is `APPSYNC_JS`.
Type: String
Valid Values: `APPSYNC_JS`
Required: Yes

 ** runtimeVersion **   <a name="appsync-Type-AppSyncRuntime-runtimeVersion"></a>
The `version` of the runtime to use. Currently, the only allowed version is `1.0.0`.
Type: String
Required: Yes

## See Also
<a name="API_AppSyncRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/AppSyncRuntime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/AppSyncRuntime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/AppSyncRuntime)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

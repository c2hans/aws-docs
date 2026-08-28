---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Scope.html
---

# Scope
<a name="API_Scope"></a>

 The wrapper that contains the AWS accounts that are in scope for the assessment.

**Note**
You no longer need to specify which AWS services are in scope when you create or update an assessment. Audit Manager infers the services in scope by examining your assessment controls and their data sources, and then mapping this information to the relevant AWS services.
If an underlying data source changes for your assessment, we automatically update the services scope as needed to reflect the correct AWS services. This ensures that your assessment collects accurate and comprehensive evidence about all of the relevant services in your AWS environment.

## Contents
<a name="API_Scope_Contents"></a>

 ** awsAccounts **   <a name="auditmanager-Type-Scope-awsAccounts"></a>
 The AWS accounts that are included in the scope of the assessment.
Type: Array of [AWSAccount](API_AWSAccount.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** awsServices **   <a name="auditmanager-Type-Scope-awsServices"></a>
 *This member has been deprecated.*
 The AWS services that are included in the scope of the assessment.
This API parameter is no longer supported. If you use this parameter to specify one or more AWS services, Audit Manager ignores this input. Instead, the value for `awsServices` will show as empty.
Type: Array of [AWSService](API_AWSService.md) objects
Required: No

## See Also
<a name="API_Scope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/Scope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/Scope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/Scope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

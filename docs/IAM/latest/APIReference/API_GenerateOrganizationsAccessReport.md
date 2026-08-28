---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GenerateOrganizationsAccessReport.html
---

# GenerateOrganizationsAccessReport
<a name="API_GenerateOrganizationsAccessReport"></a>

Generates a report for service last accessed data for AWS Organizations. You can generate a report for any entities (organization root, organizational unit, or account) or policies in your organization.

To call this operation, you must be signed in using your Organizations management account credentials. You can use your long-term IAM user or root user credentials, or temporary credentials from assuming an IAM role. SCPs must be enabled for your organization root. You must have the required IAM and Organizations permissions. For more information, see [Refining permissions using service last accessed data](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html) in the *IAM User Guide*.

You can generate a service last accessed data report for entities by specifying only the entity's path. This data includes a list of services that are allowed by any service control policies (SCPs) that apply to the entity.

You can generate a service last accessed data report for a policy by specifying an entity's path and an optional Organizations policy ID. This data includes a list of services that are allowed by the specified SCP.

For each service in both report types, the data includes the most recent account activity that the policy allows to account principals in the entity or the entity's children. For important information about the data, reporting period, permissions required, troubleshooting, and supported Regions see [Reducing permissions using service last accessed data](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html) in the *IAM User Guide*.

**Important**
The data includes all attempts to access AWS, not just the successful ones. This includes all attempts that were made using the AWS Management Console, the AWS API through any of the SDKs, or any of the command line tools. An unexpected entry in the service last accessed data does not mean that an account has been compromised, because the request might have been denied. Refer to your CloudTrail logs as the authoritative source for information about all API calls and whether they were successful or denied access. For more information, see [Logging IAM events with CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html) in the *IAM User Guide*.

This operation returns a `JobId`. Use this parameter in the ` [GetOrganizationsAccessReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOrganizationsAccessReport.html) ` operation to check the status of the report generation. To check the status of this request, use the `JobId` parameter in the ` [GetOrganizationsAccessReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOrganizationsAccessReport.html) ` operation and test the `JobStatus` response parameter. When the job is complete, you can retrieve the report.

To generate a service last accessed data report for entities, specify an entity path without specifying the optional Organizations policy ID. The type of entity that you specify determines the data returned in the report.
+  **Root** – When you specify the organizations root as the entity, the resulting report lists all of the services allowed by SCPs that are attached to your root. For each service, the report includes data for all accounts in your organization except the management account, because the management account is not limited by SCPs.
+  **OU** – When you specify an organizational unit (OU) as the entity, the resulting report lists all of the services allowed by SCPs that are attached to the OU and its parents. For each service, the report includes data for all accounts in the OU or its children. This data excludes the management account, because the management account is not limited by SCPs.
+  **management account** – When you specify the management account, the resulting report lists all AWS services, because the management account is not limited by SCPs. For each service, the report includes data for only the management account.
+  **Account** – When you specify another account as the entity, the resulting report lists all of the services allowed by SCPs that are attached to the account and its parents. For each service, the report includes data for only the specified account.

To generate a service last accessed data report for policies, specify an entity path and the optional Organizations policy ID. The type of entity that you specify determines the data returned for each service.
+  **Root** – When you specify the root entity and a policy ID, the resulting report lists all of the services that are allowed by the specified SCP. For each service, the report includes data for all accounts in your organization to which the SCP applies. This data excludes the management account, because the management account is not limited by SCPs. If the SCP is not attached to any entities in the organization, then the report will return a list of services with no data.
+  **OU** – When you specify an OU entity and a policy ID, the resulting report lists all of the services that are allowed by the specified SCP. For each service, the report includes data for all accounts in the OU or its children to which the SCP applies. This means that other accounts outside the OU that are affected by the SCP might not be included in the data. This data excludes the management account, because the management account is not limited by SCPs. If the SCP is not attached to the OU or one of its children, the report will return a list of services with no data.
+  **management account** – When you specify the management account, the resulting report lists all AWS services, because the management account is not limited by SCPs. If you specify a policy ID in the CLI or API, the policy is ignored. For each service, the report includes data for only the management account.
+  **Account** – When you specify another account entity and a policy ID, the resulting report lists all of the services that are allowed by the specified SCP. For each service, the report includes data for only the specified account. This means that other accounts in the organization that are affected by the SCP might not be included in the data. If the SCP is not attached to the account, the report will return a list of services with no data.

**Note**
Service last accessed data does not use other policy types when determining whether a principal could access a service. These other policy types include identity-based policies, resource-based policies, access control lists, IAM permissions boundaries, and AWS STS assume role policies. It only applies SCP logic. For more about the evaluation of policy types, see [Evaluating policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-basics) in the *IAM User Guide*.

For more information about service last accessed data, see [Reducing policy scope by viewing user activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_GenerateOrganizationsAccessReport_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EntityPath **
The path of the AWS Organizations entity (root, OU, or account). You can build an entity path using the known structure of your organization. For example, assume that your account ID is `123456789012` and its parent OU ID is `ou-rge0-awsabcde`. The organization root ID is `r-f6g7h8i9j0example` and your organization ID is `o-a1b2c3d4e5`. Your entity path is `o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-rge0-awsabcde/123456789012`.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 427.
Pattern: `^o-[0-9a-z]{10,32}\/r-[0-9a-z]{4,32}[0-9a-z-\/]*`
Required: Yes

 ** OrganizationsPolicyId **
The identifier of the AWS Organizations service control policy (SCP). This parameter is optional.
This ID is used to generate information about when an account principal that is limited by the SCP attempted to access an AWS service.
Type: String
Pattern: `^p-[0-9a-zA-Z_]{8,128}$`
Required: No

## Response Elements
<a name="API_GenerateOrganizationsAccessReport_ResponseElements"></a>

The following element is returned by the service.

 ** JobId **
The job identifier that you can use in the [GetOrganizationsAccessReport](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOrganizationsAccessReport.html) operation.
Type: String
Length Constraints: Fixed length of 36.

## Errors
<a name="API_GenerateOrganizationsAccessReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ReportGenerationLimitExceeded **
The request failed because the maximum number of concurrent requests for this account are already running.
HTTP Status Code: 409

## Examples
<a name="API_GenerateOrganizationsAccessReport_Examples"></a>

### Example
<a name="API_GenerateOrganizationsAccessReport_Example_1"></a>

This example illustrates one usage of GenerateOrganizationsAccessReport.

#### Sample Request
<a name="API_GenerateOrganizationsAccessReport_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GenerateOrganizationsAccessReport
&EntityPath=o-a1b2c3d4e5/r-f6g7h8i9j0example/ou-1a2b3c-k9l8m7n6o5example
&OrganizationsPolicyId=p-9l89z4nw
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GenerateOrganizationsAccessReport_Example_1_Response"></a>

```
<JobId>examplea-1234-b567-cde8-90fg123abcd4</JobId>
```

## See Also
<a name="API_GenerateOrganizationsAccessReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GenerateOrganizationsAccessReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GenerateOrganizationsAccessReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GenerateOrganizationsAccessReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GenerateOrganizationsAccessReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GenerateOrganizationsAccessReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GenerateOrganizationsAccessReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GenerateOrganizationsAccessReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GenerateOrganizationsAccessReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GenerateOrganizationsAccessReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GenerateOrganizationsAccessReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

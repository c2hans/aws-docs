---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverDetail.html
---

# SwitchoverDetail
<a name="API_SwitchoverDetail"></a>

Contains the details about a blue/green deployment.

For more information, see [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html) in the *Amazon RDS User Guide* and [Using Amazon RDS Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html) in the *Amazon Aurora User Guide*.

## Contents
<a name="API_SwitchoverDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SourceMember **
The Amazon Resource Name (ARN) of a resource in the blue environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[A-Za-z][0-9A-Za-z-:._]*`
Required: No

 ** Status **
The switchover status of a resource in a blue/green deployment.
Values:
+  `PROVISIONING` - The resource is being prepared to switch over.
+  `AVAILABLE` - The resource is ready to switch over.
+  `SWITCHOVER_IN_PROGRESS` - The resource is being switched over.
+  `SWITCHOVER_COMPLETED` - The resource has been switched over.
+  `SWITCHOVER_FAILED` - The resource attempted to switch over but failed.
+  `MISSING_SOURCE` - The source resource has been deleted.
+  `MISSING_TARGET` - The target resource has been deleted.
Type: String
Required: No

 ** TargetMember **
The Amazon Resource Name (ARN) of a resource in the green environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[A-Za-z][0-9A-Za-z-:._]*`
Required: No

## See Also
<a name="API_SwitchoverDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/SwitchoverDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/SwitchoverDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/SwitchoverDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

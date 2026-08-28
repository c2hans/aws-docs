---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_Framework.html
---

# Framework
<a name="API_Framework"></a>

Contains detailed information about a framework. Frameworks contain controls, which evaluate and report on your backup events and resources. Frameworks generate daily compliance results.

## Contents
<a name="API_Framework_Contents"></a>

 ** CreationTime **   <a name="Backup-Type-Framework-CreationTime"></a>
The date and time that a framework is created, in ISO 8601 representation. The value of `CreationTime` is accurate to milliseconds. For example, 2020-07-10T15:00:00.000-08:00 represents the 10th of July 2020 at 3:00 PM 8 hours behind UTC.
Type: Timestamp
Required: No

 ** DeploymentStatus **   <a name="Backup-Type-Framework-DeploymentStatus"></a>
The deployment status of a framework. The statuses are:
 `CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | COMPLETED | FAILED`
Type: String
Required: No

 ** FrameworkArn **   <a name="Backup-Type-Framework-FrameworkArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
Type: String
Required: No

 ** FrameworkDescription **   <a name="Backup-Type-Framework-FrameworkDescription"></a>
An optional description of the framework with a maximum 1,024 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** FrameworkName **   <a name="Backup-Type-Framework-FrameworkName"></a>
The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (\_).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][_a-zA-Z0-9]*`
Required: No

 ** NumberOfControls **   <a name="Backup-Type-Framework-NumberOfControls"></a>
The number of controls contained by the framework.
Type: Integer
Required: No

## See Also
<a name="API_Framework_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/Framework)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/Framework)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/Framework)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

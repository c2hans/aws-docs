---
source_url: https://docs.aws.amazon.com/serverlessrepo/latest/devguide/operations.html
---

# Operations
<a name="operations"></a>

The AWS Serverless Application Repository REST API includes the following operations.
+ [CreateApplication](applications.md#CreateApplication)

  Creates an application, optionally including an AWS SAM file to create the first application version in the same call.
+ [CreateApplicationVersion](applications-applicationid-versions-semanticversion.md#CreateApplicationVersion)

  Creates an application version.
+ [CreateCloudFormationChangeSet](applications-applicationid-changesets.md#CreateCloudFormationChangeSet)

  Creates an AWS CloudFormation change set for the given application.
+ [CreateCloudFormationTemplate](applications-applicationid-templates.md#CreateCloudFormationTemplate)

  Creates an AWS CloudFormation template.
+ [DeleteApplication](applications-applicationid.md#DeleteApplication)

  Deletes the specified application.
+ [GetApplication](applications-applicationid.md#GetApplication)

  Gets the specified application.
+ [GetApplicationPolicy](applications-applicationid-policy.md#GetApplicationPolicy)

  Retrieves the policy for the application.
+ [GetCloudFormationTemplate](applications-applicationid-templates-templateid.md#GetCloudFormationTemplate)

  Gets the specified AWS CloudFormation template.
+ [ListApplicationDependencies](applications-applicationid-dependencies.md#ListApplicationDependencies)

  Retrieves the list of applications nested in the containing application.
+ [ListApplications](applications.md#ListApplications)

  Lists applications owned by the requester.
+ [ListApplicationVersions](applications-applicationid-versions.md#ListApplicationVersions)

  Lists versions for the specified application.
+ [PutApplicationPolicy](applications-applicationid-policy.md#PutApplicationPolicy)

  Sets the permission policy for an application. For the list of actions supported for this operation, see [Application Permissions](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/access-control-resource-based.html#application-permissions) .
+ [UnshareApplication](applications-applicationid-unshare.md#UnshareApplication)

  Unshares an application from an AWS Organization.

  This operation can be called only from the organization's management account.
+ [UpdateApplication](applications-applicationid.md#UpdateApplication)

  Updates the specified application.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Repository. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverlessrepo` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

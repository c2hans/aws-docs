---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_IdentityResolutionJob.html
---

# IdentityResolutionJob
<a name="API_connect-customer-profiles_IdentityResolutionJob"></a>

Information about the Identity Resolution Job.

## Contents
<a name="API_connect-customer-profiles_IdentityResolutionJob_Contents"></a>

 ** DomainName **   <a name="connect-Type-connect-customer-profiles_IdentityResolutionJob-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** ExportingLocation **   <a name="connect-Type-connect-customer-profiles_IdentityResolutionJob-ExportingLocation"></a>
The S3 location where the Identity Resolution Job writes result files.
Type: [ExportingLocation](API_connect-customer-profiles_ExportingLocation.md) object
Required: No

 ** JobEndTime **   <a name="connect-Type-connect-customer-profiles_IdentityResolutionJob-JobEndTime"></a>
The timestamp of when the job was completed.
Type: Timestamp
Required: No

 ** JobId **   <a name="connect-Type-connect-customer-profiles_IdentityResolutionJob-JobId"></a>
The unique identifier of the Identity Resolution Job.
Type: String
Pattern: `[a-f0-9]{32}`
Required: No

 ** JobStartTime **   <a name="connect-Type-connect-customer-profiles_IdentityResolutionJob-JobStartTime"></a>
The timestamp of when the job was started or will be started.
Type: Timestamp
Required: No

 ** JobStats **   <a name="connect-Type-connect-customer-profiles_IdentityResolutionJob-JobStats"></a>
Statistics about an Identity Resolution Job.
Type: [JobStats](API_connect-customer-profiles_JobStats.md) object
Required: No

 ** Message **   <a name="connect-Type-connect-customer-profiles_IdentityResolutionJob-Message"></a>
The error messages that are generated when the Identity Resolution Job runs.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `.*`
Required: No

 ** Status **   <a name="connect-Type-connect-customer-profiles_IdentityResolutionJob-Status"></a>
The status of the Identity Resolution Job.
+  `PENDING`: The Identity Resolution Job is scheduled but has not started yet. If you turn off the Identity Resolution feature in your domain, jobs in the `PENDING` state are deleted.
+  `PREPROCESSING`: The Identity Resolution Job is loading your data.
+  `FIND_MATCHING`: The Identity Resolution Job is using the machine learning model to identify profiles that belong to the same matching group.
+  `MERGING`: The Identity Resolution Job is merging duplicate profiles.
+  `COMPLETED`: The Identity Resolution Job completed successfully.
+  `PARTIAL_SUCCESS`: There's a system error and not all of the data is merged. The Identity Resolution Job writes a message indicating the source of the problem.
+  `FAILED`: The Identity Resolution Job did not merge any data. It writes a message indicating the source of the problem.
Type: String
Valid Values: `PENDING | PREPROCESSING | FIND_MATCHING | MERGING | COMPLETED | PARTIAL_SUCCESS | FAILED`
Required: No

## See Also
<a name="API_connect-customer-profiles_IdentityResolutionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/IdentityResolutionJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/IdentityResolutionJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/IdentityResolutionJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

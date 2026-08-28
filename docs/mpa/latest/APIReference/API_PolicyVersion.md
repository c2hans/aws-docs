---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_PolicyVersion.html
---

# PolicyVersion
<a name="API_PolicyVersion"></a>

Contains details for the version of a policy. Policies define what operations a team that define the permissions for team resources.

## Contents
<a name="API_PolicyVersion_Contents"></a>

 ** Arn **   <a name="mpa-Type-PolicyVersion-Arn"></a>
Amazon Resource Name (ARN) for the team.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1224.
Pattern: `arn:.{1,63}:mpa:::aws:policy/[a-zA-Z0-9_\.-]{1,1023}/[a-zA-Z0-9_\.-]{1,1023}/(?:[\d]+|\$DEFAULT)`
Required: Yes

 ** CreationTime **   <a name="mpa-Type-PolicyVersion-CreationTime"></a>
Timestamp when the policy was created.
Type: Timestamp
Required: Yes

 ** Document **   <a name="mpa-Type-PolicyVersion-Document"></a>
Document that contains the policy contents.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 400000.
Required: Yes

 ** IsDefault **   <a name="mpa-Type-PolicyVersion-IsDefault"></a>
Determines if the specified policy is the default for the team.
Type: Boolean
Required: Yes

 ** LastUpdatedTime **   <a name="mpa-Type-PolicyVersion-LastUpdatedTime"></a>
Timestamp when the policy was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="mpa-Type-PolicyVersion-Name"></a>
Name of the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: Yes

 ** PolicyArn **   <a name="mpa-Type-PolicyVersion-PolicyArn"></a>
Amazon Resource Name (ARN) for the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1224.
Pattern: `arn:.{1,63}:mpa:::aws:policy/[a-zA-Z0-9_\.-]{1,1023}/[a-zA-Z0-9_\.-]{1,1023}`
Required: Yes

 ** PolicyType **   <a name="mpa-Type-PolicyVersion-PolicyType"></a>
The type of policy.
Type: String
Valid Values: `AWS_MANAGED | AWS_RAM`
Required: Yes

 ** Status **   <a name="mpa-Type-PolicyVersion-Status"></a>
Status for the policy. For example, if the policy is [attachable](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_attach-policy.html) or [deprecated](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-deprecated.html).
Type: String
Valid Values: `ATTACHABLE | DEPRECATED`
Required: Yes

 ** VersionId **   <a name="mpa-Type-PolicyVersion-VersionId"></a>
Verison ID
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

## See Also
<a name="API_PolicyVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/PolicyVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/PolicyVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/PolicyVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_EnvironmentVpc.html
---

# EnvironmentVpc
<a name="API_EnvironmentVpc"></a>

Provides summary information for the `EnvironmentVpc` resource as a response to `ListEnvironmentVpc`.

## Contents
<a name="API_EnvironmentVpc_Contents"></a>

 ** AccountId **   <a name="migrationhubrefactorspaces-Type-EnvironmentVpc-AccountId"></a>
The AWS account ID of the virtual private cloud (VPC) owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** CidrBlocks **   <a name="migrationhubrefactorspaces-Type-EnvironmentVpc-CidrBlocks"></a>
The list of Amazon Virtual Private Cloud (Amazon VPC) CIDR blocks.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** CreatedTime **   <a name="migrationhubrefactorspaces-Type-EnvironmentVpc-CreatedTime"></a>
A timestamp that indicates when the VPC is first added to the environment.
Type: Timestamp
Required: No

 ** EnvironmentId **   <a name="migrationhubrefactorspaces-Type-EnvironmentVpc-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: No

 ** LastUpdatedTime **   <a name="migrationhubrefactorspaces-Type-EnvironmentVpc-LastUpdatedTime"></a>
A timestamp that indicates when the VPC was last updated by the environment.
Type: Timestamp
Required: No

 ** VpcId **   <a name="migrationhubrefactorspaces-Type-EnvironmentVpc-VpcId"></a>
The ID of the VPC.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[-a-f0-9]{8}([-a-f0-9]{9})?`
Required: No

 ** VpcName **   <a name="migrationhubrefactorspaces-Type-EnvironmentVpc-VpcName"></a>
The name of the VPC at the time it is added to the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

## See Also
<a name="API_EnvironmentVpc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/EnvironmentVpc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/EnvironmentVpc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/EnvironmentVpc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

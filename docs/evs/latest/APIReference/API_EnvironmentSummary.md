---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_EnvironmentSummary.html
---

# EnvironmentSummary
<a name="API_EnvironmentSummary"></a>

A list of environments with summarized environment details.

## Contents
<a name="API_EnvironmentSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** createdAt **   <a name="evs-Type-EnvironmentSummary-createdAt"></a>
 The date and time that the environment was created.
Type: Timestamp
Required: No

 ** environmentArn **   <a name="evs-Type-EnvironmentSummary-environmentArn"></a>
The Amazon Resource Name (ARN) that is associated with the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:evs:[a-z]{2}-[a-z]+-[0-9]:[0-9]{12}:environment/[a-zA-Z0-9_-]+`
Required: No

 ** environmentId **   <a name="evs-Type-EnvironmentSummary-environmentId"></a>
A unique ID for the environment.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: No

 ** environmentName **   <a name="evs-Type-EnvironmentSummary-environmentName"></a>
 The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** environmentState **   <a name="evs-Type-EnvironmentSummary-environmentState"></a>
The state of an environment.
Type: String
Valid Values: `CREATING | CREATED | DELETING | DELETED | CREATE_FAILED`
Required: No

 ** environmentStatus **   <a name="evs-Type-EnvironmentSummary-environmentStatus"></a>
Reports impaired functionality that stems from issues internal to the environment, such as impaired reachability.
Type: String
Valid Values: `PASSED | FAILED | UNKNOWN`
Required: No

 ** modifiedAt **   <a name="evs-Type-EnvironmentSummary-modifiedAt"></a>
 The date and time that the environment was modified.
Type: Timestamp
Required: No

 ** vcfVersion **   <a name="evs-Type-EnvironmentSummary-vcfVersion"></a>
The VCF version of the environment.
Type: String
Valid Values: `VCF-5.2.1 | VCF-5.2.2 | SELF_DEPLOYED`
Required: No

## See Also
<a name="API_EnvironmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/EnvironmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/EnvironmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/EnvironmentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

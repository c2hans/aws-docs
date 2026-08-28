---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsClusterConfigurationExecuteCommandConfigurationDetails.html
---

# AwsEcsClusterConfigurationExecuteCommandConfigurationDetails
<a name="API_AwsEcsClusterConfigurationExecuteCommandConfigurationDetails"></a>

Contains the run command configuration for the cluster.

## Contents
<a name="API_AwsEcsClusterConfigurationExecuteCommandConfigurationDetails_Contents"></a>

 ** KmsKeyId **   <a name="securityhub-Type-AwsEcsClusterConfigurationExecuteCommandConfigurationDetails-KmsKeyId"></a>
The identifier of the KMS key that is used to encrypt the data between the local client and the container.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LogConfiguration **   <a name="securityhub-Type-AwsEcsClusterConfigurationExecuteCommandConfigurationDetails-LogConfiguration"></a>
The log configuration for the results of the run command actions. Required if `Logging` is `NONE`.
Type: [AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails](API_AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails.md) object
Required: No

 ** Logging **   <a name="securityhub-Type-AwsEcsClusterConfigurationExecuteCommandConfigurationDetails-Logging"></a>
The log setting to use for redirecting logs for run command results.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsClusterConfigurationExecuteCommandConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsClusterConfigurationExecuteCommandConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsClusterConfigurationExecuteCommandConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsClusterConfigurationExecuteCommandConfigurationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

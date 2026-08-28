---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RedshiftParameters.html
---

# RedshiftParameters
<a name="API_RedshiftParameters"></a>

The parameters for Amazon Redshift. The `ClusterId` field can be blank if `Host` and `Port` are both set. The `Host` and `Port` fields can be blank if the `ClusterId` field is set.

## Contents
<a name="API_RedshiftParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Database **   <a name="QS-Type-RedshiftParameters-Database"></a>
Database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** ClusterId **   <a name="QS-Type-RedshiftParameters-ClusterId"></a>
Cluster ID. This field can be blank if the `Host` and `Port` are provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Host **   <a name="QS-Type-RedshiftParameters-Host"></a>
Host. This field can be blank if `ClusterId` is provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** IAMParameters **   <a name="QS-Type-RedshiftParameters-IAMParameters"></a>
An optional parameter that uses IAM authentication to grant Quick Sight access to your cluster. This parameter can be used instead of [DataSourceCredentials](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSourceCredentials.html).
Type: [RedshiftIAMParameters](API_RedshiftIAMParameters.md) object
Required: No

 ** IdentityCenterConfiguration **   <a name="QS-Type-RedshiftParameters-IdentityCenterConfiguration"></a>
An optional parameter that configures IAM Identity Center authentication to grant Quick Sight access to your cluster.
This parameter can only be specified if your Quick Sight account is configured with IAM Identity Center.
Type: [IdentityCenterConfiguration](API_IdentityCenterConfiguration.md) object
Required: No

 ** Port **   <a name="QS-Type-RedshiftParameters-Port"></a>
Port. This field can be blank if the `ClusterId` is provided.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

## See Also
<a name="API_RedshiftParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RedshiftParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RedshiftParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RedshiftParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

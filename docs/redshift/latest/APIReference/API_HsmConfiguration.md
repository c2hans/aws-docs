---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_HsmConfiguration.html
---

# HsmConfiguration
<a name="API_HsmConfiguration"></a>

Returns information about an HSM configuration, which is an object that describes to Amazon Redshift clusters the information they require to connect to an HSM where they can store database encryption keys.

## Contents
<a name="API_HsmConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Description **
A text description of the HSM configuration.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** HsmConfigurationIdentifier **
The name of the Amazon Redshift HSM configuration.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** HsmIpAddress **
The IP address that the Amazon Redshift cluster must use to access the HSM.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** HsmPartitionName **
The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Tags.Tag.N **
The list of tags for the HSM configuration.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_HsmConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/HsmConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/HsmConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/HsmConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

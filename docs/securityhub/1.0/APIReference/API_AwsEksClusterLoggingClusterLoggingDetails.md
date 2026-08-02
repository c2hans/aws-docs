---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEksClusterLoggingClusterLoggingDetails.html
---

# AwsEksClusterLoggingClusterLoggingDetails
<a name="API_AwsEksClusterLoggingClusterLoggingDetails"></a>

Details for a cluster logging configuration.

## Contents
<a name="API_AwsEksClusterLoggingClusterLoggingDetails_Contents"></a>

 ** Enabled **   <a name="securityhub-Type-AwsEksClusterLoggingClusterLoggingDetails-Enabled"></a>
Whether the logging types that are listed in `Types` are enabled.
Type: Boolean
Required: No

 ** Types **   <a name="securityhub-Type-AwsEksClusterLoggingClusterLoggingDetails-Types"></a>
A list of logging types. Valid values are as follows:
+  `api`
+  `audit`
+  `authenticator`
+  `controllerManager`
+  `scheduler`
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEksClusterLoggingClusterLoggingDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEksClusterLoggingClusterLoggingDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEksClusterLoggingClusterLoggingDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEksClusterLoggingClusterLoggingDetails)

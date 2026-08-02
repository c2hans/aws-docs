---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterClusterParameterStatus.html
---

# AwsRedshiftClusterClusterParameterStatus
<a name="API_AwsRedshiftClusterClusterParameterStatus"></a>

The status of a parameter in a cluster parameter group for an Amazon Redshift cluster.

## Contents
<a name="API_AwsRedshiftClusterClusterParameterStatus_Contents"></a>

 ** ParameterApplyErrorDescription **   <a name="securityhub-Type-AwsRedshiftClusterClusterParameterStatus-ParameterApplyErrorDescription"></a>
The error that prevented the parameter from being applied to the database.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ParameterApplyStatus **   <a name="securityhub-Type-AwsRedshiftClusterClusterParameterStatus-ParameterApplyStatus"></a>
The status of the parameter. Indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when it was applied.
Valid values: `in-sync` \| `pending-reboot` \| `applying` \| `invalid-parameter` \| `apply-deferred` \| `apply-error` \| `unknown-error`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ParameterName **   <a name="securityhub-Type-AwsRedshiftClusterClusterParameterStatus-ParameterName"></a>
The name of the parameter.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRedshiftClusterClusterParameterStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterClusterParameterStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterClusterParameterStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterClusterParameterStatus)

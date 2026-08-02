---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEksClusterDetails.html
---

# AwsEksClusterDetails
<a name="API_AwsEksClusterDetails"></a>

Provides details about an Amazon EKS cluster.

## Contents
<a name="API_AwsEksClusterDetails_Contents"></a>

 ** Arn **   <a name="securityhub-Type-AwsEksClusterDetails-Arn"></a>
The ARN of the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CertificateAuthorityData **   <a name="securityhub-Type-AwsEksClusterDetails-CertificateAuthorityData"></a>
The certificate authority data for the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterStatus **   <a name="securityhub-Type-AwsEksClusterDetails-ClusterStatus"></a>
The status of the cluster. Valid values are as follows:
+  `ACTIVE`
+  `CREATING`
+  `DELETING`
+  `FAILED`
+  `PENDING`
+  `UPDATING`
Type: String
Pattern: `.*\S.*`
Required: No

 ** Endpoint **   <a name="securityhub-Type-AwsEksClusterDetails-Endpoint"></a>
The endpoint for the Amazon EKS API server.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Logging **   <a name="securityhub-Type-AwsEksClusterDetails-Logging"></a>
The logging configuration for the cluster.
Type: [AwsEksClusterLoggingDetails](API_AwsEksClusterLoggingDetails.md) object
Required: No

 ** Name **   <a name="securityhub-Type-AwsEksClusterDetails-Name"></a>
The name of the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ResourcesVpcConfig **   <a name="securityhub-Type-AwsEksClusterDetails-ResourcesVpcConfig"></a>
The VPC configuration used by the cluster control plane.
Type: [AwsEksClusterResourcesVpcConfigDetails](API_AwsEksClusterResourcesVpcConfigDetails.md) object
Required: No

 ** RoleArn **   <a name="securityhub-Type-AwsEksClusterDetails-RoleArn"></a>
The ARN of the IAM role that provides permissions for the Amazon EKS control plane to make calls to AWS API operations on your behalf.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Version **   <a name="securityhub-Type-AwsEksClusterDetails-Version"></a>
The Amazon EKS server version for the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEksClusterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEksClusterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEksClusterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEksClusterDetails)

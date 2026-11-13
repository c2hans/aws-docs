---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AffectedResource.html
---

# AffectedResource
<a name="API_AffectedResource"></a>

Contains information about a resource that an action applies to.

## Contents
<a name="API_AffectedResource_Contents"></a>

 ** arn **   <a name="guardduty-Type-AffectedResource-arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** identifier **   <a name="guardduty-Type-AffectedResource-identifier"></a>
The identifier of the resource.
Type: String
Required: No

 ** type **   <a name="guardduty-Type-AffectedResource-type"></a>
The type of the resource. Possible values are `EC2_INSTANCE`, `EBS_VOLUME`, `S3_BUCKET`, `IAM_ROLE`, `IAM_USER`, `IAM_ACCESS_KEY`, `LAMBDA_FUNCTION`, `EKS_CLUSTER`, `ECS_CLUSTER`, `KUBERNETES_WORKLOAD`, `RDS_INSTANCE`, `RDS_DB_USER`, and `EC2_SECURITY_GROUP`.
Type: String
Valid Values: `EC2_INSTANCE | EBS_VOLUME | S3_BUCKET | IAM_ROLE | IAM_USER | IAM_ACCESS_KEY | LAMBDA_FUNCTION | EKS_CLUSTER | ECS_CLUSTER | KUBERNETES_WORKLOAD | RDS_INSTANCE | RDS_DB_USER | EC2_SECURITY_GROUP`
Required: No

## See Also
<a name="API_AffectedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AffectedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AffectedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AffectedResource)

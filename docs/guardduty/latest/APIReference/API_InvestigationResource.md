---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationResource.html
---

# InvestigationResource
<a name="API_InvestigationResource"></a>

Contains information about an AWS resource that is relevant to an investigation.

## Contents
<a name="API_InvestigationResource_Contents"></a>

 ** resourceType **   <a name="guardduty-Type-InvestigationResource-resourceType"></a>
The type of the resource. Possible values are `EC2_INSTANCE`, `EBS_VOLUME`, `S3_BUCKET`, `IAM_ROLE`, `IAM_USER`, `IAM_ACCESS_KEY`, `LAMBDA_FUNCTION`, `EKS_CLUSTER`, `ECS_CLUSTER`, `KUBERNETES_WORKLOAD`, `RDS_INSTANCE`, `RDS_DB_USER`, and `EC2_SECURITY_GROUP`.
Type: String
Valid Values: `EC2_INSTANCE | EBS_VOLUME | S3_BUCKET | IAM_ROLE | IAM_USER | IAM_ACCESS_KEY | LAMBDA_FUNCTION | EKS_CLUSTER | ECS_CLUSTER | KUBERNETES_WORKLOAD | RDS_INSTANCE | RDS_DB_USER | EC2_SECURITY_GROUP`
Required: Yes

 ** uid **   <a name="guardduty-Type-InvestigationResource-uid"></a>
The unique identifier of the resource. This is the Amazon Resource Name (ARN) of the resource when it's available. Otherwise, it's the name or ID of the resource.
Type: String
Required: Yes

 ** data **   <a name="guardduty-Type-InvestigationResource-data"></a>
Details that are specific to the type of the resource.
Type: [InvestigationResourceData](API_InvestigationResourceData.md) object
Required: No

 ** name **   <a name="guardduty-Type-InvestigationResource-name"></a>
The name of the resource.
Type: String
Required: No

## See Also
<a name="API_InvestigationResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationResource)

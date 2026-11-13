---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InvestigationResourceData.html
---

# InvestigationResourceData
<a name="API_InvestigationResourceData"></a>

Contains details that are specific to the type of a resource. The member that is set matches the `ResourceType` of the resource, except that `RdsDbInstance` and `RdsDbUser` can be set together.

## Contents
<a name="API_InvestigationResourceData_Contents"></a>

 ** ec2Instance **   <a name="guardduty-Type-InvestigationResourceData-ec2Instance"></a>
Details about an Amazon EC2 instance.
Type: [InvestigationEc2Instance](API_InvestigationEc2Instance.md) object
Required: No

 ** ecsCluster **   <a name="guardduty-Type-InvestigationResourceData-ecsCluster"></a>
Details about an Amazon ECS cluster.
Type: [InvestigationEcsCluster](API_InvestigationEcsCluster.md) object
Required: No

 ** eksCluster **   <a name="guardduty-Type-InvestigationResourceData-eksCluster"></a>
Details about an Amazon EKS cluster.
Type: [InvestigationEksCluster](API_InvestigationEksCluster.md) object
Required: No

 ** lambdaFunction **   <a name="guardduty-Type-InvestigationResourceData-lambdaFunction"></a>
Details about an AWS Lambda function.
Type: [LambdaFunction](API_LambdaFunction.md) object
Required: No

 ** rdsDbInstance **   <a name="guardduty-Type-InvestigationResourceData-rdsDbInstance"></a>
Details about an Amazon RDS database instance.
Type: [RdsDbInstance](API_RdsDbInstance.md) object
Required: No

 ** rdsDbUser **   <a name="guardduty-Type-InvestigationResourceData-rdsDbUser"></a>
Details about the user that logged in to an Amazon RDS database instance.
Type: [RdsDbUser](API_RdsDbUser.md) object
Required: No

## See Also
<a name="API_InvestigationResourceData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/InvestigationResourceData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/InvestigationResourceData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/InvestigationResourceData)

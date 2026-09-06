---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_VpcPropertiesOutput.html
---

# VpcPropertiesOutput
<a name="API_VpcPropertiesOutput"></a>

The VPC connection properties returned in responses.

## Contents
<a name="API_VpcPropertiesOutput_Contents"></a>

 ** status **   <a name="datazone-Type-VpcPropertiesOutput-status"></a>
The status of the VPC connection.
Type: String
Valid Values: `CREATING | CREATE_FAILED | DELETING | DELETE_FAILED | READY | UPDATING | UPDATE_FAILED | DELETED`
Required: Yes

 ** subnetIds **   <a name="datazone-Type-VpcPropertiesOutput-subnetIds"></a>
The subnet IDs of the VPC connection.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `subnet-[a-z0-9]+`
Required: Yes

 ** vpcId **   <a name="datazone-Type-VpcPropertiesOutput-vpcId"></a>
The identifier of the VPC.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `vpc-[a-z0-9]+`
Required: Yes

 ** glueConnectionNames **   <a name="datazone-Type-VpcPropertiesOutput-glueConnectionNames"></a>
The AWS Glue connection names associated with the VPC connection.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** securityGroupId **   <a name="datazone-Type-VpcPropertiesOutput-securityGroupId"></a>
The security group ID of the VPC connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `sg-[a-z0-9]+`
Required: No

## See Also
<a name="API_VpcPropertiesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/VpcPropertiesOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/VpcPropertiesOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/VpcPropertiesOutput)

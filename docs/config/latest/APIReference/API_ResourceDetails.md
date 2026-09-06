---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ResourceDetails.html
---

# ResourceDetails
<a name="API_ResourceDetails"></a>

Returns information about the resource being evaluated.

## Contents
<a name="API_ResourceDetails_Contents"></a>

 ** ResourceConfiguration **   <a name="config-Type-ResourceDetails-ResourceConfiguration"></a>
The resource definition to be evaluated as per the resource configuration schema type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: Yes

 ** ResourceId **   <a name="config-Type-ResourceDetails-ResourceId"></a>
A unique resource ID for an evaluation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: Yes

 ** ResourceType **   <a name="config-Type-ResourceDetails-ResourceType"></a>
The type of resource being evaluated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ResourceConfigurationSchemaType **   <a name="config-Type-ResourceDetails-ResourceConfigurationSchemaType"></a>
The schema type of the resource configuration.
You can find the [Resource type schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html), or `CFN_RESOURCE_SCHEMA`, in "* AWS public extensions*" within the AWS CloudFormation registry or with the following CLI commmand: `aws cloudformation describe-type --type-name "AWS::S3::Bucket" --type RESOURCE`.
For more information, see [Managing extensions through the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html#registry-view) and [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the AWS CloudFormation User Guide.
Type: String
Valid Values: `CFN_RESOURCE_SCHEMA`
Required: No

## See Also
<a name="API_ResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ResourceDetails)

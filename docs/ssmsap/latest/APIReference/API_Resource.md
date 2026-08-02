---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

The resource contains a `ResourceArn` and the `ResourceType`.

## Contents
<a name="API_Resource_Contents"></a>

 ** ResourceArn **   <a name="ssmsap-Type-Resource-ResourceArn"></a>
The Amazon Resource Name (ARN) of the source resource.
Example of `ResourceArn`: "`arn:aws:ec2:us-east-1:111111111111:instance/i-abcdefgh987654321`"
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** ResourceType **   <a name="ssmsap-Type-Resource-ResourceType"></a>
The resource type.
Example of `ResourceType`: "`AWS::SystemsManagerSAP::Component`" or "`AWS::EC2::Instance`".
Type: String
Pattern: `[\w]+::[\w]+::[\w]+`
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/Resource)

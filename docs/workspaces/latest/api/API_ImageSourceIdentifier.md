---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ImageSourceIdentifier.html
---

# ImageSourceIdentifier
<a name="API_ImageSourceIdentifier"></a>

Describes the image import source.

## Contents
<a name="API_ImageSourceIdentifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Ec2ImageId **   <a name="WorkSpaces-Type-ImageSourceIdentifier-Ec2ImageId"></a>
The identifier of the EC2 image.
Type: String
Pattern: `^ami\-([a-f0-9]{8}|[a-f0-9]{17})$`
Required: No

 ** Ec2ImportTaskId **   <a name="WorkSpaces-Type-ImageSourceIdentifier-Ec2ImportTaskId"></a>
The EC2 import task ID to import the image from the Amazon EC2 VM import process.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 28.
Pattern: `^import-ami\-([a-zA-Z0-9]{8}|[a-zA-Z0-9]{17})$`
Required: No

 ** ImageBuildVersionArn **   <a name="WorkSpaces-Type-ImageSourceIdentifier-ImageBuildVersionArn"></a>
The ARN of the EC2 Image Builder image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
Required: No

## See Also
<a name="API_ImageSourceIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ImageSourceIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ImageSourceIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ImageSourceIdentifier)

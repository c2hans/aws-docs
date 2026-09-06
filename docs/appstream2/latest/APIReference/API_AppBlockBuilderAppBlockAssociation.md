---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AppBlockBuilderAppBlockAssociation.html
---

# AppBlockBuilderAppBlockAssociation
<a name="API_AppBlockBuilderAppBlockAssociation"></a>

Describes an association between an app block builder and app block.

## Contents
<a name="API_AppBlockBuilderAppBlockAssociation_Contents"></a>

 ** AppBlockArn **   <a name="WorkSpacesApplications-Type-AppBlockBuilderAppBlockAssociation-AppBlockArn"></a>
The ARN of the app block.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** AppBlockBuilderName **   <a name="WorkSpacesApplications-Type-AppBlockBuilderAppBlockAssociation-AppBlockBuilderName"></a>
The name of the app block builder.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## See Also
<a name="API_AppBlockBuilderAppBlockAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AppBlockBuilderAppBlockAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AppBlockBuilderAppBlockAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AppBlockBuilderAppBlockAssociation)

---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AppBlock.html
---

# AppBlock
<a name="API_AppBlock"></a>

Describes an app block.

App blocks are a WorkSpaces Applications resource that stores the details about the virtual hard disk in an S3 bucket. It also stores the setup script with details about how to mount the virtual hard disk. The virtual hard disk includes the application binaries and other files necessary to launch your applications. Multiple applications can be assigned to a single app block.

This is only supported for Elastic fleets.

## Contents
<a name="API_AppBlock_Contents"></a>

 ** Arn **   <a name="WorkSpacesApplications-Type-AppBlock-Arn"></a>
The ARN of the app block.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** Name **   <a name="WorkSpacesApplications-Type-AppBlock-Name"></a>
The name of the app block.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** AppBlockErrors **   <a name="WorkSpacesApplications-Type-AppBlock-AppBlockErrors"></a>
The errors of the app block.
Type: Array of [ErrorDetails](API_ErrorDetails.md) objects
Required: No

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-AppBlock-CreatedTime"></a>
The created time of the app block.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpacesApplications-Type-AppBlock-Description"></a>
The description of the app block.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DisplayName **   <a name="WorkSpacesApplications-Type-AppBlock-DisplayName"></a>
The display name of the app block.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** PackagingType **   <a name="WorkSpacesApplications-Type-AppBlock-PackagingType"></a>
The packaging type of the app block.
Type: String
Valid Values: `CUSTOM | APPSTREAM2`
Required: No

 ** PostSetupScriptDetails **   <a name="WorkSpacesApplications-Type-AppBlock-PostSetupScriptDetails"></a>
The post setup script details of the app block.
This only applies to app blocks with PackagingType `APPSTREAM2`.
Type: [ScriptDetails](API_ScriptDetails.md) object
Required: No

 ** SetupScriptDetails **   <a name="WorkSpacesApplications-Type-AppBlock-SetupScriptDetails"></a>
The setup script details of the app block.
This only applies to app blocks with PackagingType `CUSTOM`.
Type: [ScriptDetails](API_ScriptDetails.md) object
Required: No

 ** SourceS3Location **   <a name="WorkSpacesApplications-Type-AppBlock-SourceS3Location"></a>
The source S3 location of the app block.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** State **   <a name="WorkSpacesApplications-Type-AppBlock-State"></a>
The state of the app block.
An app block with WorkSpaces Applications packaging will be in the `INACTIVE` state if no application package (VHD) is assigned to it. After an application package (VHD) is created by an app block builder for an app block, it becomes `ACTIVE`.
Custom app blocks are always in the `ACTIVE` state and no action is required to use them.
Type: String
Valid Values: `INACTIVE | ACTIVE`
Required: No

## See Also
<a name="API_AppBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AppBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AppBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AppBlock)

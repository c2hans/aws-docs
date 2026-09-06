---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AppBlockBuilder.html
---

# AppBlockBuilder
<a name="API_AppBlockBuilder"></a>

Describes an app block builder.

## Contents
<a name="API_AppBlockBuilder_Contents"></a>

 ** Arn **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-Arn"></a>
The ARN of the app block builder.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** InstanceType **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-InstanceType"></a>
The instance type of the app block builder.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Name **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-Name"></a>
The name of the app block builder.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Platform **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-Platform"></a>
The platform of the app block builder.
 `WINDOWS_SERVER_2019` is the only valid value.
Type: String
Valid Values: `WINDOWS_SERVER_2019`
Required: Yes

 ** State **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-State"></a>
The state of the app block builder.
Type: String
Valid Values: `STARTING | RUNNING | STOPPING | STOPPED`
Required: Yes

 ** VpcConfig **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-VpcConfig"></a>
The VPC configuration for the app block builder.
Type: [VpcConfig](API_VpcConfig.md) object
Required: Yes

 ** AccessEndpoints **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-AccessEndpoints"></a>
The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints.
Type: Array of [AccessEndpoint](API_AccessEndpoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

 ** AppBlockBuilderErrors **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-AppBlockBuilderErrors"></a>
The app block builder errors.
Type: Array of [ResourceError](API_ResourceError.md) objects
Required: No

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-CreatedTime"></a>
The creation time of the app block builder.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-Description"></a>
The description of the app block builder.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** DisableIMDSV1 **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-DisableIMDSV1"></a>
Indicates whether Instance Metadata Service Version 1 (IMDSv1) is disabled for the app block builder.
Type: Boolean
Required: No

 ** DisplayName **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-DisplayName"></a>
The display name of the app block builder.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** EnableDefaultInternetAccess **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-EnableDefaultInternetAccess"></a>
Indicates whether default internet access is enabled for the app block builder.
Type: Boolean
Required: No

 ** IamRoleArn **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-IamRoleArn"></a>
The ARN of the IAM role that is applied to the app block builder.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** StateChangeReason **   <a name="WorkSpacesApplications-Type-AppBlockBuilder-StateChangeReason"></a>
The state change reason.
Type: [AppBlockBuilderStateChangeReason](API_AppBlockBuilderStateChangeReason.md) object
Required: No

## See Also
<a name="API_AppBlockBuilder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AppBlockBuilder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AppBlockBuilder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AppBlockBuilder)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html
---

# CreateLaunchTemplateVersion
<a name="API_CreateLaunchTemplateVersion"></a>

Creates a new version of a launch template. You must specify an existing launch template, either by name or ID. You can determine whether the new version inherits parameters from a source version, and add or overwrite parameters as needed.

Launch template versions are numbered in the order in which they are created. You can't specify, change, or replace the numbering of launch template versions.

Launch templates are immutable; after you create a launch template, you can't modify it. Instead, you can create a new version of the launch template that includes the changes that you require.

For more information, see [Modify a launch template (manage launch template versions)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-launch-template-versions.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateLaunchTemplateVersion_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If a client token isn't specified, a randomly generated token is used in the request to ensure idempotency.
For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Constraint: Maximum 128 ASCII characters.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **LaunchTemplateData**
The information for the launch template.
Type: [RequestLaunchTemplateData](API_RequestLaunchTemplateData.md) object
Required: Yes

 **LaunchTemplateId**
The ID of the launch template.
You must specify either the launch template ID or the launch template name, but not both.
Type: String
Required: No

 **LaunchTemplateName**
The name of the launch template.
You must specify either the launch template ID or the launch template name, but not both.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9\(\)\.\-/_]+`
Required: No

 **ResolveAlias**
If `true`, and if a Systems Manager parameter is specified for `ImageId`, the AMI ID is displayed in the response for `imageID`. For more information, see [Use a Systems Manager parameter instead of an AMI ID](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id) in the *Amazon EC2 User Guide*.
Default: `false`
Type: Boolean
Required: No

 **SourceVersion**
The version of the launch template on which to base the new version. Snapshots applied to the block device mapping are ignored when creating a new version unless they are explicitly included.
If you specify this parameter, the new version inherits the launch parameters from the source version. If you specify additional launch parameters for the new version, they overwrite any corresponding launch parameters inherited from the source version.
If you omit this parameter, the new version contains only the launch parameters that you specify for the new version.
Type: String
Required: No

 **VersionDescription**
A description for the version of the launch template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## Response Elements
<a name="API_CreateLaunchTemplateVersion_ResponseElements"></a>

The following elements are returned by the service.

 **launchTemplateVersion**
Information about the launch template version.
Type: [LaunchTemplateVersion](API_LaunchTemplateVersion.md) object

 **requestId**
The ID of the request.
Type: String

 **warning**
If the new version of the launch template contains parameters or parameter combinations that are not valid, an error code and an error message are returned for each issue that's found.
Type: [ValidationWarning](API_ValidationWarning.md) object

## Errors
<a name="API_CreateLaunchTemplateVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateLaunchTemplateVersion_Examples"></a>

### Example
<a name="API_CreateLaunchTemplateVersion_Example_1"></a>

The following example creates a new launch template version for launch template `MyLaunchTemplate` and uses version 2 of the launch template as the base for the new version. The new launch template uses `ami-aabbccdd`. All other launch template data is inherited from the source version.

#### Sample Request
<a name="API_CreateLaunchTemplateVersion_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateLaunchTemplate
&SourceVersion=2
&LaunchTemplateName=MyLaunchTemplate
&VersionDescription=VersionWithNewAMI
&LaunchTemplateData.ImageId=ami-aabbccdd
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateLaunchTemplateVersion_Example_1_Response"></a>

```
<CreateLaunchTemplateVersionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>6657423a-2616-461a-9ce5-3c65example</requestId>
    <launchTemplateVersion>
        <createTime>2017-10-31T11:56:00.000Z</createTime>
        <createdBy>arn:aws:iam::123456789012:root</createdBy>
        <defaultVersion>false</defaultVersion>
        <launchTemplateData>
            <imageId>ami-aabbccdd</imageId>
            <instanceType>t2.micro</instanceType>
        </launchTemplateData>
        <launchTemplateId>lt-0a20c965061f6454a</launchTemplateId>
        <launchTemplateName>MyLaunchTemplate</launchTemplateName>
        <versionDescription>VersionWithNewAMI</versionDescription>
        <versionNumber>4</versionNumber>
    </launchTemplateVersion>
</CreateLaunchTemplateVersionResponse>
```

## See Also
<a name="API_CreateLaunchTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateLaunchTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateLaunchTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateLaunchTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateLaunchTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateLaunchTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateLaunchTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateLaunchTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateLaunchTemplateVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateLaunchTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateLaunchTemplateVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

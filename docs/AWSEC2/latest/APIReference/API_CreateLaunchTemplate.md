---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html
---

# CreateLaunchTemplate
<a name="API_CreateLaunchTemplate"></a>

Creates a launch template.

A launch template contains the parameters to launch an instance. When you launch an instance using [RunInstances](API_RunInstances.md), you can specify a launch template instead of providing the launch parameters in the request. For more information, see [Store instance launch parameters in Amazon EC2 launch templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.

To clone an existing launch template as the basis for a new launch template, use the Amazon EC2 console. The API, SDKs, and CLI do not support cloning a template. For more information, see [Create a launch template from an existing launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#create-launch-template-from-existing-launch-template) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateLaunchTemplate_RequestParameters"></a>

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

 **LaunchTemplateName**
A name for the launch template.
Type: String
Required: Yes

 **Operator**
Reserved for internal use.
Type: [OperatorRequest](API_OperatorRequest.md) object
Required: No

 **TagSpecification.N**
The tags to apply to the launch template on creation. To tag the launch template, the resource type must be `launch-template`.
To specify the tags for the resources that are created when an instance is launched, you must use the `TagSpecifications` parameter in the [launch template data](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestLaunchTemplateData.html) structure.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VersionDescription**
A description for the first version of the launch template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## Response Elements
<a name="API_CreateLaunchTemplate_ResponseElements"></a>

The following elements are returned by the service.

 **launchTemplate**
Information about the launch template.
Type: [LaunchTemplate](API_LaunchTemplate.md) object

 **requestId**
The ID of the request.
Type: String

 **warning**
If the launch template contains parameters or parameter combinations that are not valid, an error code and an error message are returned for each issue that's found.
Type: [ValidationWarning](API_ValidationWarning.md) object

## Errors
<a name="API_CreateLaunchTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateLaunchTemplate_Examples"></a>

### Example 1
<a name="API_CreateLaunchTemplate_Example_1"></a>

The following example creates a launch template that specifies AMI `ami-1a2b3c4d` and an instance type of `t2.micro`.

#### Sample Request
<a name="API_CreateLaunchTemplate_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateLaunchTemplate
&LaunchTemplateName=MyLaunchTemplate
&VersionDescription=FirstVersion
&LaunchTemplateData.ImageId=ami-1a2b3c4d
&LaunchTemplateData.InstanceType=t2.micro
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateLaunchTemplate_Example_1_Response"></a>

```
<CreateLaunchTemplateResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>39f602bc-7580-4239-a6d8-af56example</requestId>
    <launchTemplate>
        <createTime>2017-10-31T11:38:52.000Z</createTime>
        <createdBy>arn:aws:iam::123456789012:root</createdBy>
        <defaultVersionNumber>1</defaultVersionNumber>
        <latestVersionNumber>1</latestVersionNumber>
        <launchTemplateId>lt-0a20c965061f64abc</launchTemplateId>
        <launchTemplateName>MyLaunchTemplate</launchTemplateName>
    </launchTemplate>
</CreateLaunchTemplateResponse>
```

### Example 2
<a name="API_CreateLaunchTemplate_Example_2"></a>

The following example creates a launch template that specifies the subnet in which to launch the instance (`subnet-7b16de0c`), assigns a public IP address and an IPv6 address to the instance, and creates a tag for the instance (`Name=webserver`).

#### Sample Request
<a name="API_CreateLaunchTemplate_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateLaunchTemplate
&LaunchTemplateName=TemplateForWebServer
&VersionDescription=WebVersion1
&LaunchTemplateData.ImageId=ami-8c1be5f6
&LaunchTemplateData.InstanceType=t2.micro
&LaunchTemplateData.NetworkInterface.1.AssociatePublicIpAddress=true
&LaunchTemplateData.NetworkInterface.1.DeviceIndex=0
&LaunchTemplateData.NetworkInterface.1.SubnetId=subnet-7b16de0c
&LaunchTemplateData.NetworkInterface.1.Ipv6AddressCount=1
&LaunchTemplateData.TagSpecification.1.ResourceType=instance
&LaunchTemplateData.TagSpecification.1.Tag.1.Key=Name
&LaunchTemplateData.TagSpecification.1.Tag.1.Value=webserver
&AUTHPARAMS
```

## See Also
<a name="API_CreateLaunchTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateLaunchTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateLaunchTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateLaunchTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateLaunchTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateLaunchTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateLaunchTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateLaunchTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateLaunchTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateLaunchTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateLaunchTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

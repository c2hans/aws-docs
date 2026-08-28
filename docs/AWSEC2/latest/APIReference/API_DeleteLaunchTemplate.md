---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteLaunchTemplate.html
---

# DeleteLaunchTemplate
<a name="API_DeleteLaunchTemplate"></a>

Deletes a launch template. Deleting a launch template deletes all of its versions.

## Request Parameters
<a name="API_DeleteLaunchTemplate_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

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

## Response Elements
<a name="API_DeleteLaunchTemplate_ResponseElements"></a>

The following elements are returned by the service.

 **launchTemplate**
Information about the launch template.
Type: [LaunchTemplate](API_LaunchTemplate.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DeleteLaunchTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteLaunchTemplate_Examples"></a>

### Example
<a name="API_DeleteLaunchTemplate_Example_1"></a>

This example deletes launch template `lt-0a20c965061f64abc`.

#### Sample Request
<a name="API_DeleteLaunchTemplate_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteLaunchTemplate
&LaunchTemplateId=lt-0a20c965061f64abc
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteLaunchTemplate_Example_1_Response"></a>

```
<DeleteLaunchTemplateResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>c12605de-c470-4eaa-a4d0-ab4dexample</requestId>
    <launchTemplate>
        <createTime>2017-10-31T11:38:52.000Z</createTime>
        <createdBy>arn:aws:iam::123456789012:root</createdBy>
        <defaultVersionNumber>2</defaultVersionNumber>
        <latestVersionNumber>2</latestVersionNumber>
        <launchTemplateId>lt-0a20c965061f64abc</launchTemplateId>
        <launchTemplateName>MyLaunchTemplate</launchTemplateName>
    </launchTemplate>
</DeleteLaunchTemplateResponse>
```

## See Also
<a name="API_DeleteLaunchTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteLaunchTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteLaunchTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteLaunchTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteLaunchTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteLaunchTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteLaunchTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteLaunchTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteLaunchTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteLaunchTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteLaunchTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

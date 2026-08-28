---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html
---

# DescribeLaunchTemplates
<a name="API_DescribeLaunchTemplates"></a>

Describes one or more launch templates.

## Request Parameters
<a name="API_DescribeLaunchTemplates_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `create-time` - The time the launch template was created.
+  `launch-template-name` - The name of the launch template.
+  `tag`:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
+  `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IncludeManagedResources**
Indicates whether to include managed resources in the output. If this parameter is set to `true`, the output includes resources that are managed by AWS services, even if managed resource visibility is set to hidden.
Type: Boolean
Required: No

 **LaunchTemplateId.N**
One or more launch template IDs.
Type: Array of strings
Required: No

 **LaunchTemplateName.N**
One or more launch template names.
Type: Array of strings
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9\(\)\.\-/_]+`
Required: No

 **MaxResults**
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `NextToken` value. This value can be between 1 and 200.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 **NextToken**
The token to request the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_DescribeLaunchTemplates_ResponseElements"></a>

The following elements are returned by the service.

 **launchTemplates**
Information about the launch templates.
Type: Array of [LaunchTemplate](API_LaunchTemplate.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeLaunchTemplates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeLaunchTemplates_Examples"></a>

### Example
<a name="API_DescribeLaunchTemplates_Example_1"></a>

This example describes all of your launch templates.

#### Sample Request
<a name="API_DescribeLaunchTemplates_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeLaunchTemplates
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeLaunchTemplates_Example_1_Response"></a>

```
<DescribeLaunchTemplatesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1afa6e44-eb38-4229-8db6-d5eaexample</requestId>
    <launchTemplates>
        <item>
            <createTime>2017-10-31T11:38:52.000Z</createTime>
            <createdBy>arn:aws:iam::123456789012:root</createdBy>
            <defaultVersionNumber>1</defaultVersionNumber>
            <latestVersionNumber>1</latestVersionNumber>
            <launchTemplateId>lt-0a20c965061f64abc</launchTemplateId>
            <launchTemplateName>MyLaunchTemplate</launchTemplateName>
        </item>
    </launchTemplates>
</DescribeLaunchTemplatesResponse>
```

## See Also
<a name="API_DescribeLaunchTemplates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeLaunchTemplates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeLaunchTemplates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeLaunchTemplates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeLaunchTemplates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeLaunchTemplates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeLaunchTemplates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeLaunchTemplates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeLaunchTemplates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeLaunchTemplates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeLaunchTemplates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

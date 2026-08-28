---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html
---

# CreateTags
<a name="API_CreateTags"></a>

Adds or overwrites only the specified tags for the specified Amazon EC2 resource or resources. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique per resource.

For more information about tags, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the *Amazon Elastic Compute Cloud User Guide*. For more information about creating IAM policies that control users' access to resources based on tags, see [Supported resource-level permissions for Amazon EC2 API actions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-supported-iam-actions-resources.html) in the *Amazon Elastic Compute Cloud User Guide*.

## Request Parameters
<a name="API_CreateTags_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ResourceId.N**
The IDs of the resources, separated by spaces.
Constraints: Up to 1000 resource IDs. We recommend breaking up this request into smaller batches.
Type: Array of strings
Required: Yes

 **Tag.N**
The tags. The `value` parameter is required, but if you don't want the tag to have a value, specify the parameter with no value, and we set the value to an empty string.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Response Elements
<a name="API_CreateTags_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_CreateTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateTags_Examples"></a>

### Example
<a name="API_CreateTags_Example_1"></a>

This example request adds (or overwrites) two tags for an AMI and an instance. One of the tags is a key (`webserver`), with no value (we set the value to an empty string). The other tag consists of a key (`stack`) and value (`Production`).

#### Sample Request
<a name="API_CreateTags_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateTags
&ResourceId.1=ami-1a2b3c4d
&ResourceId.2=i-1234567890abcdef0
&Tag.1.Key=webserver
&Tag.1.Value=
&Tag.2.Key=stack
&Tag.2.Value=Production
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateTags_Example_1_Response"></a>

```
<CreateTagsResponse
xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <return>true</return>
</CreateTagsResponse>
```

## See Also
<a name="API_CreateTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

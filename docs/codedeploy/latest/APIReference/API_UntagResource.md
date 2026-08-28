---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

 Disassociates a resource from a list of tags. The resource is identified by the `ResourceArn` input parameter. The tags are identified by the list of keys in the `TagKeys` input parameter.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="CodeDeploy-UntagResource-request-ResourceArn"></a>
 The Amazon Resource Name (ARN) that specifies from which resource to disassociate the tags with the keys in the `TagKeys` input parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="CodeDeploy-UntagResource-request-TagKeys"></a>
 A list of keys of `Tag` objects. The `Tag` objects identified by the keys are disassociated from the resource specified by the `ResourceArn` input parameter.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationDoesNotExistException **
The application does not exist with the user or AWS account.
HTTP Status Code: 400

 ** ArnNotSupportedException **
 The specified ARN is not supported. For example, it might be an ARN for a resource that is not expected.
HTTP Status Code: 400

 ** DeploymentConfigDoesNotExistException **
The deployment configuration does not exist with the user or AWS account.
HTTP Status Code: 400

 ** DeploymentGroupDoesNotExistException **
The named deployment group with the user or AWS account does not exist.
HTTP Status Code: 400

 ** InvalidArnException **
 The specified ARN is not in a valid format.
HTTP Status Code: 400

 ** InvalidTagsToAddException **
 The specified tags are not valid.
HTTP Status Code: 400

 ** ResourceArnRequiredException **
 The ARN of a resource is required, but was not found.
HTTP Status Code: 400

 ** TagRequiredException **
A tag was not specified.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/UntagResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

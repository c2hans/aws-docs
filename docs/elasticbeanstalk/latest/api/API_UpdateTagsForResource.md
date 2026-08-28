---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateTagsForResource.html
---

# UpdateTagsForResource
<a name="API_UpdateTagsForResource"></a>

Update the list of tags applied to an AWS Elastic Beanstalk resource. Two lists can be passed: `TagsToAdd` for tags to add or update, and `TagsToRemove`.

Elastic Beanstalk supports tagging of all of its resources. For details about resource tagging, see [Tagging Application Resources](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-tagging-resources.html).

If you create a custom policy to control permission to this operation, specify one of the following two virtual actions (or both) instead of the API operation name:

elasticbeanstalk:AddTags
Controls permission to call `UpdateTagsForResource` and pass a list of tags to add in the `TagsToAdd` parameter.

elasticbeanstalk:RemoveTags
Controls permission to call `UpdateTagsForResource` and pass a list of tag keys to remove in the `TagsToRemove` parameter.

For details about creating a custom user policy, see [Creating a Custom User Policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#AWSHowTo.iam.policies).

## Request Parameters
<a name="API_UpdateTagsForResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceArn **
The Amazon Resource Name (ARN) of the resouce to be updated.
Must be the ARN of an Elastic Beanstalk resource.
Type: String
Required: Yes

 **TagsToAdd.member.N**
A list of tags to add or update. If a key of an existing tag is added, the tag's value is updated.
Specify at least one of these parameters: `TagsToAdd`, `TagsToRemove`.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 **TagsToRemove.member.N**
A list of tag keys to remove. If a tag key doesn't exist, it is silently ignored.
Specify at least one of these parameters: `TagsToAdd`, `TagsToRemove`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## Errors
<a name="API_UpdateTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** OperationInProgressFailure **
Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.
HTTP Status Code: 400

 ** ResourceNotFound **
A resource doesn't exist for the specified Amazon Resource Name (ARN).
HTTP Status Code: 400

 ** ResourceTypeNotSupported **
The type of the specified Amazon Resource Name (ARN) isn't supported for this operation.
HTTP Status Code: 400

 ** TooManyTags **
The number of tags in the resource would exceed the number of tags that each resource can have.
To calculate this, the operation considers both the number of tags the resource already has and the tags this operation would add if it succeeded.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/UpdateTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/UpdateTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/UpdateTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/UpdateTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/UpdateTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/UpdateTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/UpdateTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/UpdateTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/UpdateTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/UpdateTagsForResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

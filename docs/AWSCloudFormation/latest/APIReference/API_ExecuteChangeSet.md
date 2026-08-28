---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html
---

# ExecuteChangeSet
<a name="API_ExecuteChangeSet"></a>

Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the [DescribeStacks](API_DescribeStacks.md) action to view the status of the update.

When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack.

If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy.

To create a change set for the entire stack hierarchy, `IncludeNestedStacks` must have been set to `True`.

## Request Parameters
<a name="API_ExecuteChangeSet_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ChangeSetName **
The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*|arn:[-a-zA-Z0-9:/]*`
Required: Yes

 ** ClientRequestToken **
A unique identifier for this `ExecuteChangeSet` request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to execute a change set to update a stack with the same name. You might retry `ExecuteChangeSet` requests to ensure that CloudFormation successfully received them.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`
Required: No

 ** DisableRollback **
Preserves the state of previously provisioned resources when an operation fails. This parameter can't be specified when the `OnStackFailure` parameter to the [CreateChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html) API operation was specified.
+  `True` - if the stack creation fails, do nothing. This is equivalent to specifying `DO_NOTHING` for the `OnStackFailure` parameter to the [CreateChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html) API operation.
+  `False` - if the stack creation fails, roll back the stack. This is equivalent to specifying `ROLLBACK` for the `OnStackFailure` parameter to the [CreateChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html) API operation.
Default: `True`
Type: Boolean
Required: No

 ** RetainExceptOnCreate **
When set to `true`, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of `Retain`.
Default: `false`
Type: Boolean
Required: No

 ** StackName **
If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that's associated with the change set you want to execute.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`
Required: No

## Errors
<a name="API_ExecuteChangeSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ChangeSetNotFound **
The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the `ListChangeSets` operation.
HTTP Status Code: 404

 ** InsufficientCapabilities **
The template contains resources with capabilities that weren't specified in the Capabilities parameter.
HTTP Status Code: 400

 ** InvalidChangeSetStatus **
The specified change set can't be used to update the stack. For example, the change set status might be `CREATE_IN_PROGRESS`, or the stack status might be `UPDATE_IN_PROGRESS`.
HTTP Status Code: 400

 ** TokenAlreadyExists **
A client request token already exists.
HTTP Status Code: 400

## Examples
<a name="API_ExecuteChangeSet_Examples"></a>

### ExecuteChangeSet
<a name="API_ExecuteChangeSet_Example_1"></a>

This example illustrates one usage of ExecuteChangeSet.

#### Sample Request
<a name="API_ExecuteChangeSet_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ExecuteChangeSet
 &ChangeSetName=arn:aws:cloudformation:us-east-1:123456789012:changeSet/SampleChangeSet/12a3b456-0e10-4ce0-9052-5d484a8c4e5b
 &Version=2010-05-15
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20160316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_ExecuteChangeSet_Example_1_Response"></a>

```
<ExecuteChangeSetResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ExecuteChangeSetResult/>
  <ResponseMetadata>
    <RequestId>5ccc7dcd-744c-11e5-be70-example</RequestId>
  </ResponseMetadata>
</ExecuteChangeSetResponse>
```

## See Also
<a name="API_ExecuteChangeSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ExecuteChangeSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/ExecuteChangeSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ExecuteChangeSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ExecuteChangeSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ExecuteChangeSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ExecuteChangeSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ExecuteChangeSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ExecuteChangeSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ExecuteChangeSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ExecuteChangeSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CancelUpdateStack.html
---

# CancelUpdateStack
<a name="API_CancelUpdateStack"></a>

Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.

**Note**
You can cancel only stacks that are in the `UPDATE_IN_PROGRESS` state.

## Request Parameters
<a name="API_CancelUpdateStack_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClientRequestToken **
A unique identifier for this `CancelUpdateStack` request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to cancel an update on a stack with the same name. You might retry `CancelUpdateStack` requests to ensure that CloudFormation successfully received them.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`
Required: No

 ** StackName **
If you don't pass a parameter to `StackName`, the API returns a response that describes all resources in the account.
The IAM policy below can be added to IAM policies when you want to limit resource-level permissions and avoid returning a response when no parameter is sent in the request:
 `{ "Version": "2012-10-17", "Statement": [{ "Effect": "Deny", "Action": "cloudformation:DescribeStacks", "NotResource": "arn:aws:cloudformation:*:*:stack/*/*" }] }`
The name or the unique stack ID that's associated with the stack.
Type: String
Required: Yes

## Errors
<a name="API_CancelUpdateStack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** TokenAlreadyExists **
A client request token already exists.
HTTP Status Code: 400

## Examples
<a name="API_CancelUpdateStack_Examples"></a>

### CancelUpdateStack
<a name="API_CancelUpdateStack_Example_1"></a>

This example illustrates one usage of CancelUpdateStack.

#### Sample Request
<a name="API_CancelUpdateStack_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=CancelUpdateStack
 &StackName=MyStack
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response
<a name="API_CancelUpdateStack_Example_1_Response"></a>

```
<CancelUpdateStackResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ResponseMetadata>
    <RequestId>5ccc7dcd-744c-11e5-be70-1b08c228efb3</RequestId>
  </ResponseMetadata>
</CancelUpdateStackResponse>
```

## See Also
<a name="API_CancelUpdateStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CancelUpdateStack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/CancelUpdateStack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CancelUpdateStack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CancelUpdateStack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CancelUpdateStack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CancelUpdateStack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CancelUpdateStack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CancelUpdateStack)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CancelUpdateStack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CancelUpdateStack)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

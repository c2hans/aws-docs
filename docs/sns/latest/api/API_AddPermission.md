---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_AddPermission.html
---

# AddPermission
<a name="API_AddPermission"></a>

Adds a statement to a topic's access control policy, granting access for the specified AWS accounts to the specified actions.

**Note**
To remove the ability to change topic permissions, you must deny permissions to the `AddPermission`, `RemovePermission`, and `SetTopicAttributes` actions in your IAM policy.

## Request Parameters
<a name="API_AddPermission_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ActionName.member.N**
The action you want to allow for the specified principal(s).
Valid values: Any Amazon SNS action name, for example `Publish`.
Type: Array of strings
Required: Yes

 **AWSAccountId.member.N**
The AWS account IDs of the users (principals) who will be given access to the specified actions. The users must have AWS account, but do not need to be signed up for this service.
Type: Array of strings
Required: Yes

 ** Label **
A unique identifier for the new policy statement.
Type: String
Required: Yes

 ** TopicArn **
The ARN of the topic whose access control policy you wish to modify.
Type: String
Required: Yes

## Errors
<a name="API_AddPermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

## Examples
<a name="API_AddPermission_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_AddPermission_Example_1"></a>

This example illustrates one usage of AddPermission.

#### Sample Request
<a name="API_AddPermission_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=AddPermission
&TopicArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Test
&Label=NewPermission
&ActionName.member.1=Publish
&ActionName.member.2=GetTopicAttributes
&AWSAccountId.member.1=987654321000
&AWSAccountId.member.2=876543210000
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_AddPermission_Example_1_Response"></a>

```
<AddPermissionResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>6a213e4e-33a8-11df-9540-99d0768312d3</RequestId>
    </ResponseMetadata>
</AddPermissionResponse>
```

## See Also
<a name="API_AddPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/AddPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/AddPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/AddPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/AddPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/AddPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/AddPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/AddPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/AddPermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/AddPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/AddPermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

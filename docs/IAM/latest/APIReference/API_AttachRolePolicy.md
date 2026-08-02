---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AttachRolePolicy.html
---

# AttachRolePolicy
<a name="API_AttachRolePolicy"></a>

Attaches the specified managed policy to the specified IAM role. When you attach a managed policy to a role, the managed policy becomes part of the role's permission (access) policy.

**Note**
You cannot use a managed policy as the role's trust policy. The role's trust policy is created at the same time as the role, using [https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html). You can update a role's trust policy using [https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAssumeRolePolicy.html](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateAssumeRolePolicy.html).

Use this operation to attach a *managed* policy to a role. To embed an inline policy in a role, use [https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePolicy.html](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePolicy.html). For more information about policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.

As a best practice, you can validate your IAM policies. To learn more, see [Validating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_AttachRolePolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** PolicyArn **
The Amazon Resource Name (ARN) of the IAM policy you want to attach.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** RoleName **
The name (friendly name, not ARN) of the role to attach the policy to.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Errors
<a name="API_AttachRolePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** PolicyNotAttachable **
The request failed because AWS service role policies can only be attached to the service-linked role for that service.
HTTP Status Code: 400

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** UnmodifiableEntity **
The request was rejected because service-linked roles are protected AWS resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf. The error message includes the name of the service that depends on this service-linked role. You must request the change through that service.
HTTP Status Code: 400

## Examples
<a name="API_AttachRolePolicy_Examples"></a>

### Example
<a name="API_AttachRolePolicy_Example_1"></a>

This example illustrates one usage of AttachRolePolicy.

#### Sample Request
<a name="API_AttachRolePolicy_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=AttachRolePolicy
&PolicyArn=arn:aws:iam::aws:policy/ReadOnlyAccess
&RoleName=ReadOnlyRole
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_AttachRolePolicy_Example_1_Response"></a>

```
<AttachRolePolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>37a87673-3d07-11e4-bfad-8d1c6EXAMPLE</RequestId>
  </ResponseMetadata>
</AttachRolePolicyResponse>
```

## See Also
<a name="API_AttachRolePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/AttachRolePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/AttachRolePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/AttachRolePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/AttachRolePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/AttachRolePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/AttachRolePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/AttachRolePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/AttachRolePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/AttachRolePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/AttachRolePolicy)

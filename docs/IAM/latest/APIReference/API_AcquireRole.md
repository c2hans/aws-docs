---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html
---

# AcquireRole
<a name="API_AcquireRole"></a>

Creates an IAM role from the specified role template. The new role takes its configuration—including its name, path, trust policy, inline and managed policies, permissions boundary, tags, and maximum session duration—from the role template version that you specify. For more information about roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *IAM User Guide*.

If the template version defines parameters, use the `ReplacementValues` parameter to supply the values that the service substitutes into the role during creation.

## Request Parameters
<a name="API_AcquireRole_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ReplacementValues** ReplacementValues.entry.N.key (key)ReplacementValues.entry.N.value (value)
A map of values to substitute for the parameters that are defined in the role template version. Each key is a parameter name from the template, and each value is a structure that contains the replacement values for that parameter.
Type: String to [ReplacementValueEntry](API_ReplacementValueEntry.md) object map
Map Entries: Maximum number of 30 items.
Required: No

 ** TemplateArn **
The Amazon Resource Name (ARN) of the role template to create the role from.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** TemplateMinorVersion **
The minor version of the role template to use. If you do not specify a minor version, the service uses the template's default minor version.
Type: Integer
Required: No

## Response Elements
<a name="API_AcquireRole_ResponseElements"></a>

The following element is returned by the service.

 ** Role **
A structure that contains details about the IAM role that was created.
Type: [Role](API_Role.md) object

## Errors
<a name="API_AcquireRole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

 ** EntityAlreadyExists **
The request was rejected because it attempted to create a resource that already exists.
HTTP Status Code: 409

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** LimitExceeded **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 409

 ** MalformedPolicyDocument **
The request was rejected because the policy document was malformed. The error message describes the specific error.
HTTP Status Code: 400

 ** NameConflict **
The request was rejected because the resulting role name conflicts with an existing role in the account.
HTTP Status Code: 409

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** RoleModified **
The request was rejected because someone modified the role template while the service was creating the role. Wait a few minutes and try the request again.
HTTP Status Code: 409

 ** RoleTemplateDisabled **
The request was rejected because the specified role template is disabled. A disabled role template cannot be used to create new roles. Contact your administrator to enable the role template, or use a different role template.
HTTP Status Code: 400

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_AcquireRole_Examples"></a>

### Example
<a name="API_AcquireRole_Example_1"></a>

This example illustrates one usage of AcquireRole.

#### Sample Request
<a name="API_AcquireRole_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=AcquireRole
&TemplateArn=arn:aws:iam::aws:role-template/awsserviceprincipal/Example:1
&TemplateMinorVersion=1
&ReplacementValues.entry.1.key=Department
&ReplacementValues.entry.1.value.Values.member.1=Engineering
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_AcquireRole_Example_1_Response"></a>

```
<AcquireRoleResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <AcquireRoleResult>
    <Role>
      <Path>/awsserviceprincipal/</Path>
      <Arn>arn:aws:iam::aws:role/awsserviceprincipal/Example-Engineering</Arn>
      <RoleName>Example-Engineering</RoleName>
      <AssumeRolePolicyDocument>
        {"Version":"2012-10-17",		 	 	 "Statement":[{"Effect":"Allow",
        "Principal":{"Service":["ec2.amazonaws.com"]},"Action":["sts:AssumeRole"]}]}
      </AssumeRolePolicyDocument>
      <CreateDate>2026-06-26T20:43:32Z</CreateDate>
      <RoleId>AROADBQP57FF2AEXAMPLE</RoleId>
    </Role>
  </AcquireRoleResult>
  <ResponseMetadata>
    <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</AcquireRoleResponse>
```

## See Also
<a name="API_AcquireRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/AcquireRole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/AcquireRole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/AcquireRole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/AcquireRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/AcquireRole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/AcquireRole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/AcquireRole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/AcquireRole)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/AcquireRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/AcquireRole)

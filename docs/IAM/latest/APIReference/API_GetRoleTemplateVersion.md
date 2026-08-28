---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRoleTemplateVersion.html
---

# GetRoleTemplateVersion
<a name="API_GetRoleTemplateVersion"></a>

Retrieves information about a version of the specified role template. Role templates define a reusable configuration—including role name and path patterns, trust policy, inline and managed policies, permissions boundary, tags, and maximum session duration—that you use to create IAM roles with [AcquireRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcquireRole.html).

If you do not specify a minor version, the service returns the template's default minor version.

## Request Parameters
<a name="API_GetRoleTemplateVersion_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** MinorVersion **
The minor version of the role template to retrieve. If you do not specify a minor version, the service returns the template's default minor version.
Type: Integer
Required: No

 ** TemplateArn **
The Amazon Resource Name (ARN) of the role template whose version you want to retrieve.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

## Response Elements
<a name="API_GetRoleTemplateVersion_ResponseElements"></a>

The following element is returned by the service.

 ** RoleTemplateVersion **
A structure that contains details about the requested role template version.
Type: [RoleTemplateVersion](API_RoleTemplateVersion.md) object

## Errors
<a name="API_GetRoleTemplateVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetRoleTemplateVersion_Examples"></a>

### Example
<a name="API_GetRoleTemplateVersion_Example_1"></a>

This example illustrates one usage of GetRoleTemplateVersion.

#### Sample Request
<a name="API_GetRoleTemplateVersion_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetRoleTemplateVersion
&TemplateArn=arn:aws:iam::aws:role-template/awsserviceprincipal/Example:1
&MinorVersion=1
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetRoleTemplateVersion_Example_1_Response"></a>

```
<GetRoleTemplateVersionResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetRoleTemplateVersionResult>
    <RoleTemplateVersion>
      <TemplateArn>arn:aws:iam::aws:role-template/awsserviceprincipal/Example:1</TemplateArn>
      <TemplateName>Example</TemplateName>
      <MajorVersion>1</MajorVersion>
      <MinorVersion>1</MinorVersion>
      <DefaultMinorVersion>1</DefaultMinorVersion>
      <Enabled>true</Enabled>
      <RoleNamePattern>Example-@{Department}</RoleNamePattern>
      <AssumeRolePolicyDocumentTemplate>
        {"Version":"2012-10-17",		 	 	 "Statement":[{"Effect":"Allow",
        "Principal":{"Service":["ec2.amazonaws.com"]},"Action":["sts:AssumeRole"]}]}
      </AssumeRolePolicyDocumentTemplate>
      <CreateTimestamp>2026-06-26T20:43:32Z</CreateTimestamp>
    </RoleTemplateVersion>
  </GetRoleTemplateVersionResult>
  <ResponseMetadata>
    <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</GetRoleTemplateVersionResponse>
```

## See Also
<a name="API_GetRoleTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetRoleTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetRoleTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetRoleTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetRoleTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetRoleTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetRoleTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetRoleTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetRoleTemplateVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetRoleTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetRoleTemplateVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

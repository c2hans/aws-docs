---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ValidateTemplate.html
---

# ValidateTemplate
<a name="API_ValidateTemplate"></a>

Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.

## Request Parameters
<a name="API_ValidateTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** TemplateBody **
Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
Conditional: You must pass `TemplateURL` or `TemplateBody`. If both are passed, only `TemplateBody` is used.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** TemplateURL **
The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that is located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with `https://`.
Conditional: You must pass `TemplateURL` or `TemplateBody`. If both are passed, only `TemplateBody` is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5120.
Required: No

## Response Elements
<a name="API_ValidateTemplate_ResponseElements"></a>

The following elements are returned by the service.

 **Capabilities.member.N**
The capabilities found within the template. If your template contains IAM resources, you must specify the CAPABILITY\_IAM or CAPABILITY\_NAMED\_IAM value for this parameter when you use the [CreateStack](API_CreateStack.md) or [UpdateStack](API_UpdateStack.md) actions with your template; otherwise, those actions return an InsufficientCapabilities error.
For more information, see [Acknowledging IAM resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities).
Type: Array of strings
Valid Values: `CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_AUTO_EXPAND`

 ** CapabilitiesReason **
The list of resources that generated the values in the `Capabilities` response element.
Type: String

 **DeclaredTransforms.member.N**
A list of the transforms that are declared in the template.
Type: Array of strings

 ** Description **
The description found within the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 **Parameters.member.N**
A list of `TemplateParameter` structures.
Type: Array of [TemplateParameter](API_TemplateParameter.md) objects

## Errors
<a name="API_ValidateTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ValidateTemplate_Examples"></a>

### ValidateTemplate
<a name="API_ValidateTemplate_Example_1"></a>

This example illustrates one usage of ValidateTemplate.

#### Sample Request
<a name="API_ValidateTemplate_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ValidateTemplate
 &TemplateBody=http://myTemplateRepository/TemplateOne.template
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response
<a name="API_ValidateTemplate_Example_1_Response"></a>

```
<ValidateTemplateResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ValidateTemplateResult>
    <Description></Description>
    <Parameters>
      <member>
        <NoEcho>false</NoEcho>
        <ParameterKey>InstanceType</ParameterKey>
        <Description>Type of instance to launch</Description>
        <DefaultValue>m1.small</DefaultValue>
      </member>
      <member>
        <NoEcho>false</NoEcho>
        <ParameterKey>WebServerPort</ParameterKey>
        <Description>The TCP port for the Web Server</Description>
        <DefaultValue>8888</DefaultValue>
      </member>
      <member>
        <NoEcho>false</NoEcho>
        <ParameterKey>KeyName</ParameterKey>
        <Description>Name of an existing EC2 KeyPair to enable SSH access into the server</Description>
      </member>
    </Parameters>
  </ValidateTemplateResult>
  <ResponseMetadata>
    <RequestId>0be7b6e8-e4a0-11e0-a5bd-example</RequestId>
  </ResponseMetadata>
</ValidateTemplateResponse>
```

## See Also
<a name="API_ValidateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ValidateTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/ValidateTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ValidateTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ValidateTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ValidateTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ValidateTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ValidateTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ValidateTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ValidateTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ValidateTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_GetTemplateSummary.html
---

# GetTemplateSummary
<a name="API_GetTemplateSummary"></a>

Returns information about a new or existing template. The `GetTemplateSummary` action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or StackSet.

You can use the `GetTemplateSummary` action when you submit a template, or you can get template information for a StackSet, or a running or deleted stack.

For deleted stacks, `GetTemplateSummary` returns the template information for up to 90 days after the stack has been deleted. If the template doesn't exist, a `ValidationError` is returned.

## Request Parameters
<a name="API_GetTemplateSummary_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CallAs **
[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.
By default, `SELF` is specified. Use `SELF` for StackSets with self-managed permissions.
+ If you are signed in to the management account, specify `SELF`.
+ If you are signed in to a delegated administrator account, specify `DELEGATED_ADMIN`.

  Your AWS account must be registered as a delegated administrator in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the * AWS CloudFormation User Guide*.
Type: String
Valid Values: `SELF | DELEGATED_ADMIN`
Required: No

 ** StackName **
The name or the stack ID that's associated with the stack, which aren't always interchangeable. For running stacks, you can specify either the stack's name or its unique stack ID. For deleted stack, you must specify the unique stack ID.
Conditional: You must specify only one of the following parameters: `StackName`, `StackSetName`, `TemplateBody`, or `TemplateURL`.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`
Required: No

 ** StackSetName **
The name or unique ID of the StackSet from which the stack was created.
Conditional: You must specify only one of the following parameters: `StackName`, `StackSetName`, `TemplateBody`, or `TemplateURL`.
Type: String
Pattern: `[a-zA-Z][-a-zA-Z0-9]*(?::[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12})?`
Required: No

 ** TemplateBody **
Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
Conditional: You must specify only one of the following parameters: `StackName`, `StackSetName`, `TemplateBody`, or `TemplateURL`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** TemplateSummaryConfig **
Specifies options for the `GetTemplateSummary` API action.
Type: [TemplateSummaryConfig](API_TemplateSummaryConfig.md) object
Required: No

 ** TemplateURL **
The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with `https://`.
Conditional: You must specify only one of the following parameters: `StackName`, `StackSetName`, `TemplateBody`, or `TemplateURL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5120.
Required: No

## Response Elements
<a name="API_GetTemplateSummary_ResponseElements"></a>

The following elements are returned by the service.

 **Capabilities.member.N**
The capabilities found within the template. If your template contains IAM resources, you must specify the `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` value for this parameter when you use the [CreateStack](API_CreateStack.md) or [UpdateStack](API_UpdateStack.md) actions with your template; otherwise, those actions return an `InsufficientCapabilities` error.
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
The value that's defined in the `Description` property of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** Metadata **
The value that's defined for the `Metadata` property of the template.
Type: String

 **Parameters.member.N**
A list of parameter declarations that describe various properties for each parameter.
Type: Array of [ParameterDeclaration](API_ParameterDeclaration.md) objects

 **ResourceIdentifierSummaries.member.N**
A list of resource identifier summaries that describe the target resources of an import operation and the properties you can provide during the import to identify the target resources. For example, `BucketName` is a possible identifier property for an `AWS::S3::Bucket` resource.
Type: Array of [ResourceIdentifierSummary](API_ResourceIdentifierSummary.md) objects

 **ResourceTypes.member.N**
A list of all the template resource types that are defined in the template, such as `AWS::EC2::Instance`, `AWS::Dynamo::Table`, and `Custom::MyCustomInstance`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** Version **
The AWS template format version, which identifies the capabilities of the template.
Type: String

 ** Warnings **
An object that contains any warnings returned.
Type: [Warnings](API_Warnings.md) object

## Errors
<a name="API_GetTemplateSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** StackSetNotFound **
The specified StackSet doesn't exist.
HTTP Status Code: 404

## Examples
<a name="API_GetTemplateSummary_Examples"></a>

### GetTemplateSummary
<a name="API_GetTemplateSummary_Example_1"></a>

This example illustrates one usage of GetTemplateSummary.

#### Sample Request
<a name="API_GetTemplateSummary_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=GetTemplateSummary
 &TemplateURL=https%3A%2F%2Fs3-us-east-1.amazonaws.com%2Fsamplebucketname%2Fsampletemplate.template
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response
<a name="API_GetTemplateSummary_Example_1_Response"></a>

```
<GetTemplateSummaryResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <GetTemplateSummaryResult>
    <Description>A sample template description.</Description>
    <Parameters>
      <member>
        <NoEcho>false</NoEcho>
        <ParameterKey>KeyName</ParameterKey>
        <Description>Name of an existing EC2 KeyPair to enable SSH access to the instance</Description>
        <ParameterType>AWS::EC2::KeyPair::KeyName</ParameterType>
      </member>
    </Parameters>
    <Metadata>{"Instances":{"SampleDescription":"Information about the instances"}}</Metadata>
    <Version>2010-09-09</Version>
  </GetTemplateSummaryResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</GetTemplateSummaryResponse>
```

## See Also
<a name="API_GetTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/GetTemplateSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/GetTemplateSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/GetTemplateSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/GetTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/GetTemplateSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/GetTemplateSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/GetTemplateSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/GetTemplateSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/GetTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/GetTemplateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

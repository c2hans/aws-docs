---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_GetTemplate.html
---

# GetTemplate
<a name="API_GetTemplate"></a>

Returns the template body for a specified stack. You can get the template for running or deleted stacks.

For deleted stacks, `GetTemplate` returns the template for up to 90 days after the stack has been deleted.

**Note**
If the template doesn't exist, a `ValidationError` is returned.

## Request Parameters
<a name="API_GetTemplate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ChangeSetName **
The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you specify a name, you must also specify the `StackName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*|arn:[-a-zA-Z0-9:/]*`
Required: No

 ** StackName **
The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:
+ Running stacks: You can specify either the stack's name or its unique stack ID.
+ Deleted stacks: You must specify the unique stack ID.
Type: String
Required: No

 ** TemplateStage **
For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify `Original`. To get the template after CloudFormation has processed all transforms, specify `Processed`.
If the template doesn't include transforms, `Original` and `Processed` return the same template. By default, CloudFormation specifies `Processed`.
Type: String
Valid Values: `Original | Processed`
Required: No

## Response Elements
<a name="API_GetTemplate_ResponseElements"></a>

The following elements are returned by the service.

 **StagesAvailable.member.N**
The stage of the template that you can retrieve. For stacks, the `Original` and `Processed` templates are always available. For change sets, the `Original` template is always available. After CloudFormation finishes creating the change set, the `Processed` template becomes available.
Type: Array of strings
Valid Values: `Original | Processed`

 ** TemplateBody **
Structure that contains the template body.
CloudFormation returns the same template that was used when the stack was created.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_GetTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ChangeSetNotFound **
The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the `ListChangeSets` operation.
HTTP Status Code: 404

## Examples
<a name="API_GetTemplate_Examples"></a>

### GetTemplate
<a name="API_GetTemplate_Example_1"></a>

This example illustrates one usage of GetTemplate.

#### Sample Request
<a name="API_GetTemplate_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=GetTemplate
 &StackName=MyStack
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response
<a name="API_GetTemplate_Example_1_Response"></a>

```
<GetTemplateResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <GetTemplateResult>
    <TemplateBody>"{
    "AWSTemplateFormatVersion" : "2010-09-09",
    "Description" : "Simple example",
    "Resources" : {
      "MySQS" : {
        "Type" : "AWS::SQS::Queue",
        "Properties" : {
        }
      }
    }
  }</TemplateBody>
  </GetTemplateResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</GetTemplateResponse>
```

## See Also
<a name="API_GetTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/GetTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/GetTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/GetTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/GetTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/GetTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/GetTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/GetTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/GetTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/GetTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/GetTemplate)

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListImports.html
---

# ListImports
<a name="API_ListImports"></a>

Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see [ListExports](API_ListExports.md).

For more information about importing an exported output value, see the [Fn::ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html) function.

## Request Parameters
<a name="API_ListImports_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ExportName **
The name of the exported output value. CloudFormation returns the stack names that are importing this value.
Type: String
Required: Yes

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Elements
<a name="API_ListImports_ResponseElements"></a>

The following elements are returned by the service.

 **Imports.member.N**
A list of stack names that are importing the specified exported output value.
Type: Array of strings

 ** NextToken **
A string that identifies the next page of exports. If there is no additional page, this value is null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListImports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ListImports_Examples"></a>

### ListExports
<a name="API_ListImports_Example_1"></a>

This example illustrates one usage of ListImports.

#### Sample Request
<a name="API_ListImports_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListImports
 &ExportName=SampleStack-MyExportedValue
 &Version=2010-05-15
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20160316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_ListImports_Example_1_Response"></a>

```
<ListImportsResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ListImportsResult>
    <Imports>
      <member>Import-SampleStack</member>
    </Imports>
  </ListImportsResult>
  <ResponseMetadata>
    <RequestId>a13656a8-a7b9-11e6-964c-41b56747ddb0</RequestId>
  </ResponseMetadata>
</ListImportsResponse>
```

## See Also
<a name="API_ListImports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListImports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/ListImports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListImports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListImports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListImports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListImports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListImports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListImports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListImports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListImports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

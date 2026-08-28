---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListExports.html
---

# ListExports
<a name="API_ListExports"></a>

Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the [ Fn::ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html) function.

For more information, see [Get exported outputs from a deployed CloudFormation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html).

## Request Parameters
<a name="API_ListExports_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NextToken **
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Elements
<a name="API_ListExports_ResponseElements"></a>

The following elements are returned by the service.

 **Exports.member.N**
The output for the [ListExports](#API_ListExports) action.
Type: Array of [Export](API_Export.md) objects

 ** NextToken **
If the output exceeds 100 exported output values, a string that identifies the next page of exports. If there is no additional page, this value is null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListExports_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ListExports_Examples"></a>

### ListExports
<a name="API_ListExports_Example_1"></a>

This example illustrates one usage of ListExports.

#### Sample Request
<a name="API_ListExports_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=ListExports
 &Version=2010-05-15
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20160316T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_ListExports_Example_1_Response"></a>

```
<ListExportsResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <ListExportsResult>
    <Exports>
      <member>
        <Name>mySampleStack1-SecurityGroupID</Name>
        <ExportingStackId>arn:aws:cloudformation:us-east-1:123456789012:stack/mySampleStack1/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ExportingStackId>
        <Value>sg-0a123b45</Value>
      </member>
      <member>
        <Name>mySampleStack1-SubnetID</Name>
        <ExportingStackId>arn:aws:cloudformation:us-east-1:123456789012:stack/mySampleStack1/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ExportingStackId>
        <Value>subnet-0a123b45</Value>
      </member>
      <member>
        <Name>mySampleStack1-VPCID</Name>
        <ExportingStackId>arn:aws:cloudformation:us-east-1:123456789012:stack/mySampleStack1/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ExportingStackId>
        <Value>vpc-0a123b45</Value>
      </member>
      <member>
        <Name>WebSiteURL</Name>
        <ExportingStackId>arn:aws:cloudformation:us-east-1:123456789012:stack/myS3StaticSite/12a3b456-0e10-4ce0-9052-5d484a8c4e5b</ExportingStackId>
        <Value>http://testsite.com.s3-website-us-east-1.amazonaws.com</Value>
      </member>
    </Exports>
  </ListExportsResult>
  <ResponseMetadata>
    <RequestId>5ccc7dcd-744c-11e5-be70-1b08c228efb3</RequestId>
  </ResponseMetadata>
</ListExportsResponse>
```

## See Also
<a name="API_ListExports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/ListExports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/ListExports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/ListExports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/ListExports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/ListExports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/ListExports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/ListExports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/ListExports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/ListExports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/ListExports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

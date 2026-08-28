---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RestoreManagedPrefixListVersion.html
---

# RestoreManagedPrefixListVersion
<a name="API_RestoreManagedPrefixListVersion"></a>

Restores the entries from a previous version of a managed prefix list to a new version of the prefix list.

## Request Parameters
<a name="API_RestoreManagedPrefixListVersion_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CurrentVersion**
The current version number for the prefix list.
Type: Long
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PrefixListId**
The ID of the prefix list.
Type: String
Required: Yes

 **PreviousVersion**
The version to restore.
Type: Long
Required: Yes

## Response Elements
<a name="API_RestoreManagedPrefixListVersion_ResponseElements"></a>

The following elements are returned by the service.

 **prefixList**
Information about the prefix list.
Type: [ManagedPrefixList](API_ManagedPrefixList.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_RestoreManagedPrefixListVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RestoreManagedPrefixListVersion_Examples"></a>

### Example
<a name="API_RestoreManagedPrefixListVersion_Example_1"></a>

This example restores the entries from version 1 of the specified prefix list.

#### Sample Request
<a name="API_RestoreManagedPrefixListVersion_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=RestoreManagedPrefixListVersion
&PrefixListId=pl-0123123123123aabb
&CurrentVersion=3
&PreviousVersion=1
&AUTHPARAMS
```

#### Sample Response
<a name="API_RestoreManagedPrefixListVersion_Example_1_Response"></a>

```
<RestoreManagedPrefixListVersionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>aeb3faff-8938-41a0-9747-example</requestId>
    <prefixList>
        <addressFamily>IPv4</addressFamily>
        <maxEntries>10</maxEntries>
        <ownerId>123456789012</ownerId>
        <prefixListArn>arn:aws:ec2:us-east-1:123456789012:prefix-list/pl-0123123123123aabb</prefixListArn>
        <prefixListId>pl-0123123123123aabb</prefixListId>
        <prefixListName>tgw-attachments</prefixListName>
        <state>restore-in-progress</state>
        <version>3</version>
    </prefixList>
</RestoreManagedPrefixListVersionResponse>
```

## See Also
<a name="API_RestoreManagedPrefixListVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/RestoreManagedPrefixListVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/RestoreManagedPrefixListVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/RestoreManagedPrefixListVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/RestoreManagedPrefixListVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/RestoreManagedPrefixListVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/RestoreManagedPrefixListVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/RestoreManagedPrefixListVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/RestoreManagedPrefixListVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/RestoreManagedPrefixListVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/RestoreManagedPrefixListVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateManagedPrefixList.html
---

# CreateManagedPrefixList
<a name="API_CreateManagedPrefixList"></a>

Creates a managed prefix list. You can specify entries for the prefix list. Each entry consists of a CIDR block and an optional description.

## Request Parameters
<a name="API_CreateManagedPrefixList_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddressFamily**
The IP address type.
Valid Values: `IPv4` \| `IPv6`
Type: String
Required: Yes

 **ClientToken**
Unique, case-sensitive identifier you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Constraints: Up to 255 UTF-8 characters in length.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Entry.N**
One or more entries for the prefix list.
Type: Array of [AddPrefixListEntry](API_AddPrefixListEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 **MaxEntries**
The maximum number of entries for the prefix list.
Type: Integer
Required: Yes

 **PrefixListName**
A name for the prefix list.
Constraints: Up to 255 characters in length. The name cannot start with `com.amazonaws`.
Type: String
Required: Yes

 **TagSpecification.N**
The tags to apply to the prefix list during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateManagedPrefixList_ResponseElements"></a>

The following elements are returned by the service.

 **prefixList**
Information about the prefix list.
Type: [ManagedPrefixList](API_ManagedPrefixList.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateManagedPrefixList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateManagedPrefixList_Examples"></a>

### Example
<a name="API_CreateManagedPrefixList_Example_1"></a>

This example creates a managed prefix list with a maximum of 10 entries, and adds 2 entries. The prefix list support IPv4 CIDR blocks.

#### Sample Request
<a name="API_CreateManagedPrefixList_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateManagedPrefixList
&PrefixListName=tgw-attachments
&Entry.1.Cidr=10.0.0.0/16
&Entry.1.Description=vpc-a
&Entry.2.Cidr=10.2.0.0/16
&Entry.2.Description=vpc-b
&MaxEntries=10
&AddressFamily=IPv4
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateManagedPrefixList_Example_1_Response"></a>

```
<CreateManagedPrefixListResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>2989de6e-5305-49c7-809a-example</requestId>
    <prefixList>
            <addressFamily>IPv4</addressFamily>
            <maxEntries>10</maxEntries>
            <ownerId>123456789012</ownerId>
            <prefixListArn>arn:aws:ec2:us-east-1:123456789012:prefix-list/pl-0123123123123abcd</prefixListArn>
            <prefixListId>pl-0123123123123abcd</prefixListId>
            <prefixListName>tgw-attachments</prefixListName>
            <state>create-in-progress</state>
            <tagSet/>
            <version>1</version>
    </prefixList>
</CreateManagedPrefixListResponse>
```

## See Also
<a name="API_CreateManagedPrefixList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateManagedPrefixList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateManagedPrefixList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateManagedPrefixList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateManagedPrefixList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateManagedPrefixList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateManagedPrefixList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateManagedPrefixList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateManagedPrefixList)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateManagedPrefixList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateManagedPrefixList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

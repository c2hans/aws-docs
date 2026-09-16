---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteManagedPrefixList.html
---

# DeleteManagedPrefixList
<a name="API_DeleteManagedPrefixList"></a>

Deletes the specified managed prefix list. You must first remove all references to the prefix list in your resources.

## Request Parameters
<a name="API_DeleteManagedPrefixList_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PrefixListId**
The ID of the prefix list.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteManagedPrefixList_ResponseElements"></a>

The following elements are returned by the service.

 **prefixList**
Information about the prefix list.
Type: [ManagedPrefixList](API_ManagedPrefixList.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DeleteManagedPrefixList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteManagedPrefixList_Examples"></a>

### Example
<a name="API_DeleteManagedPrefixList_Example_1"></a>

This example deletes the specified prefix list.

#### Sample Request
<a name="API_DeleteManagedPrefixList_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteManagedPrefixList
&PrefixListId=pl-0123123123123aabb
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteManagedPrefixList_Example_1_Response"></a>

```
<DeleteManagedPrefixListResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>06152571-575a-49aa-af95-example</requestId>
    <prefixList>
        <addressFamily>IPv6</addressFamily>
        <maxEntries>25</maxEntries>
        <ownerId>123456789012</ownerId>
        <prefixListArn>arn:aws:ec2:us-east-1:123456789012:prefix-list/pl-0123123123123aabb</prefixListArn>
        <prefixListId>pl-0123123123123aabb</prefixListId>
        <prefixListName>test-pl</prefixListName>
        <state>delete-in-progress</state>
        <version>1</version>
    </prefixList>
</DeleteManagedPrefixListResponse>'
```

## See Also
<a name="API_DeleteManagedPrefixList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteManagedPrefixList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteManagedPrefixList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteManagedPrefixList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteManagedPrefixList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteManagedPrefixList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteManagedPrefixList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteManagedPrefixList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteManagedPrefixList)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteManagedPrefixList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteManagedPrefixList)

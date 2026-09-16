---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeManagedPrefixLists.html
---

# DescribeManagedPrefixLists
<a name="API_DescribeManagedPrefixLists"></a>

Describes your managed prefix lists and any AWS-managed prefix lists.

To view the entries for your prefix list, use [GetManagedPrefixListEntries](API_GetManagedPrefixListEntries.md).

## Request Parameters
<a name="API_DescribeManagedPrefixLists_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters.
+  `owner-id` - The ID of the prefix list owner.
+  `prefix-list-id` - The ID of the prefix list.
+  `prefix-list-name` - The name of the prefix list.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **PrefixListId.N**
One or more prefix list IDs.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeManagedPrefixLists_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **prefixListSet**
Information about the prefix lists.
Type: Array of [ManagedPrefixList](API_ManagedPrefixList.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeManagedPrefixLists_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeManagedPrefixLists_Examples"></a>

### Example
<a name="API_DescribeManagedPrefixLists_Example_1"></a>

This example describes managed prefix lists and filters by the prefix lists owned by account `123456789012`.

#### Sample Request
<a name="API_DescribeManagedPrefixLists_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeManagedPrefixList
&Filter.1.Name=owner-id
&Filter.1.Value.1=123456789012
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeManagedPrefixLists_Example_1_Response"></a>

```
<DescribeManagedPrefixListsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>ace27020-4268-4c9c-a8d3-example</requestId>
    <prefixListSet>
            <item>
                <addressFamily>IPv4</addressFamily>
                <maxEntries>10</maxEntries>
                <ownerId>123456789012</ownerId>
                <prefixListArn>arn:aws:ec2:us-east-1:123456789012:prefix-list/pl-0123123123123aabb</prefixListArn>
                <prefixListId>pl-0123123123123aabb</prefixListId>
                <prefixListName>tgw-attachments</prefixListName>
                <state>create-complete</state>
                <tagSet>
                    <item>
                      <key>Purpose</key>
                      <value>For TGW-1a attachments</value>
                    </item>
                </tagSet>
                <version>1</version>
            </item>
    </prefixListSet>
</DescribeManagedPrefixListsResponse>
```

## See Also
<a name="API_DescribeManagedPrefixLists_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeManagedPrefixLists)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeManagedPrefixLists)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeManagedPrefixLists)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeManagedPrefixLists)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeManagedPrefixLists)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeManagedPrefixLists)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeManagedPrefixLists)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeManagedPrefixLists)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeManagedPrefixLists)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeManagedPrefixLists)

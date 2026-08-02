---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetManagedPrefixListAssociations.html
---

# GetManagedPrefixListAssociations
<a name="API_GetManagedPrefixListAssociations"></a>

Gets information about the resources that are associated with the specified managed prefix list.

## Request Parameters
<a name="API_GetManagedPrefixListAssociations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 255.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **PrefixListId**
The ID of the prefix list.
Type: String
Required: Yes

## Response Elements
<a name="API_GetManagedPrefixListAssociations_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **prefixListAssociationSet**
Information about the associations.
Type: Array of [PrefixListAssociation](API_PrefixListAssociation.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetManagedPrefixListAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetManagedPrefixListAssociations_Examples"></a>

### Example
<a name="API_GetManagedPrefixListAssociations_Example_1"></a>

This example gets the associations for the specified managed prefix list.

#### Sample Request
<a name="API_GetManagedPrefixListAssociations_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetManagedPrefixListAssociations
&PrefixListId=pl-0123123123123aabb
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetManagedPrefixListAssociations_Example_1_Response"></a>

```
<GetManagedPrefixListAssociationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>3ae1bcdf-4042-47f8-9b8a-example</requestId>
    <prefixListAssociationSet>
        <item>
            <resourceId>sg-01234567811abcaba</resourceId>
            <resourceOwner>123456789012</resourceOwner>
        </item>
    </prefixListAssociationSet>
</GetManagedPrefixListAssociationsResponse>
```

## See Also
<a name="API_GetManagedPrefixListAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetManagedPrefixListAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetManagedPrefixListAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetManagedPrefixListAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetManagedPrefixListAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetManagedPrefixListAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetManagedPrefixListAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetManagedPrefixListAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetManagedPrefixListAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetManagedPrefixListAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetManagedPrefixListAssociations)

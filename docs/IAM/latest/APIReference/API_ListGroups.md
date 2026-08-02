---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListGroups.html
---

# ListGroups
<a name="API_ListGroups"></a>

Lists the IAM groups that have the specified path prefix.

 You can paginate the results using the `MaxItems` and `Marker` parameters.

## Request Parameters
<a name="API_ListGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **
Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the `Marker` element in the response that you received to indicate where the next call should start.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** MaxItems **
Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the `IsTruncated` response element is `true`.
If you do not include this parameter, the number of items defaults to 100. Note that IAM might return fewer results, even when there are more results available. In that case, the `IsTruncated` response element returns `true`, and `Marker` contains a value to include in the subsequent call that tells the service where to continue from.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** PathPrefix **
 The path prefix for filtering the results. For example, the prefix `/division_abc/subdivision_xyz/` gets all groups whose path starts with `/division_abc/subdivision_xyz/`.
This parameter is optional. If it is not included, it defaults to a slash (/), listing all groups. This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the \! (`\u0021`) through the DEL character (`\u007F`), including most punctuation characters, digits, and upper and lowercased letters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `\u002F[\u0021-\u007F]*`
Required: No

## Response Elements
<a name="API_ListGroups_ResponseElements"></a>

The following elements are returned by the service.

 **Groups.member.N**
A list of groups.
Type: Array of [Group](API_Group.md) objects

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

## Errors
<a name="API_ListGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ListGroups_Examples"></a>

### Example
<a name="API_ListGroups_Example_1"></a>

This example illustrates one usage of ListGroups.

#### Sample Request
<a name="API_ListGroups_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListGroups
&PathPrefix=/division_abc/subdivision_xyz/
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListGroups_Example_1_Response"></a>

```
<ListGroupsResponse>
  <ListGroupsResult>
    <Groups>
       <member>
          <Path>/division_abc/subdivision_xyz/</Path>
          <GroupName>Admins</GroupName>
          <GroupId>AGPACKCEVSQ6C2EXAMPLE</GroupId>
          <Arn>arn:aws:iam::123456789012:group/Admins</Arn>
       </member>
       <member>
          <Path>/division_abc/subdivision_xyz/product_1234/engineering/
          </Path>
          <GroupName>Test</GroupName>
          <GroupId>AGP2MAB8DPLSRHEXAMPLE</GroupId>
          <Arn>arn:aws:iam::123456789012:group
          /division_abc/subdivision_xyz/product_1234/engineering/Test</Arn>
       </member>
       <member>
          <Path>/division_abc/subdivision_xyz/product_1234/</Path>
          <GroupName>Managers</GroupName>
          <GroupId>AGPIODR4TAW7CSEXAMPLE</GroupId>
          <Arn>arn:aws:iam::123456789012
          :group/division_abc/subdivision_xyz/product_1234/Managers</Arn>
       </member>
    </Groups>
    <IsTruncated>false</IsTruncated>
  </ListGroupsResult>
  <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
  </ResponseMetadata>
</ListGroupsResponse>
```

## See Also
<a name="API_ListGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListGroups)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListGroups)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListGroups)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListGroups)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListGroups)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListGroups)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListGroups)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListGroups)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListGroups)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListGroups)

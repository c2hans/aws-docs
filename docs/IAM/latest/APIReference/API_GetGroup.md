---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetGroup.html
---

# GetGroup
<a name="API_GetGroup"></a>

 Returns a list of IAM users that are in the specified IAM group. You can paginate the results using the `MaxItems` and `Marker` parameters.

## Request Parameters
<a name="API_GetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** GroupName **
The name of the group.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]+`
Required: Yes

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

## Response Elements
<a name="API_GetGroup_ResponseElements"></a>

The following elements are returned by the service.

 ** Group **
A structure that contains details about the group.
Type: [Group](API_Group.md) object

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

 **Users.member.N**
A list of users in the group.
Type: Array of [User](API_User.md) objects

## Errors
<a name="API_GetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetGroup_Examples"></a>

### Example
<a name="API_GetGroup_Example_1"></a>

This example illustrates one usage of GetGroup.

#### Sample Request
<a name="API_GetGroup_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetGroup
&GroupName=Admins
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetGroup_Example_1_Response"></a>

```
<GetGroupResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
 <GetGroupResult>
    <Group>
       <Path>/</Path>
       <GroupName>Admins</GroupName>
       <GroupId>AGPACKCEVSQ6C2EXAMPLE</GroupId>
       <Arn>arn:aws:iam::123456789012:group/Admins</Arn>
    </Group>
    <Users>
       <member>
          <Path>/division_abc/subdivision_xyz/</Path>
          <UserName>Bob</UserName>
          <UserId>AIDACKCEVSQ6C2EXAMPLE</UserId>
          <Arn>
          arn:aws:iam::123456789012:user/division_abc/subdivision_xyz/Bob
          </Arn>
       </member>
       <member>
          <Path>/division_abc/subdivision_xyz/</Path>
          <UserName>Susan</UserName>
          <UserId>AIDACKCEVSQ6C2EXAMPLE</UserId>
          <Arn>
          arn:aws:iam::123456789012:user/division_abc/subdivision_xyz/Susan
          </Arn>
       </member>
    </Users>
    <IsTruncated>false</IsTruncated>
 </GetGroupResult>
 <ResponseMetadata>
    <RequestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</RequestId>
 </ResponseMetadata>
</GetGroupResponse>
```

## See Also
<a name="API_GetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

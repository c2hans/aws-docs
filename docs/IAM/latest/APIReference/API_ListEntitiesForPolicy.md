---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListEntitiesForPolicy.html
---

# ListEntitiesForPolicy
<a name="API_ListEntitiesForPolicy"></a>

Lists all IAM users, groups, and roles that the specified managed policy is attached to.

You can use the optional `EntityFilter` parameter to limit the results to a particular type of entity (users, groups, or roles). For example, to list only the roles that are attached to the specified policy, set `EntityFilter` to `Role`.

You can paginate the results using the `MaxItems` and `Marker` parameters.

## Request Parameters
<a name="API_ListEntitiesForPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EntityFilter **
The entity type to use for filtering the results.
For example, when `EntityFilter` is `Role`, only the roles that are attached to the specified policy are returned. This parameter is optional. If it is not included, all attached entities (users, groups, and roles) are returned. The argument for this parameter must be one of the valid values listed below.
Type: String
Valid Values: `User | Role | Group | LocalManagedPolicy | AWSManagedPolicy`
Required: No

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
The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all entities.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the \! (`\u0021`) through the DEL character (`\u007F`), including most punctuation characters, digits, and upper and lowercased letters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
Required: No

 ** PolicyArn **
The Amazon Resource Name (ARN) of the IAM policy for which you want the versions.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** PolicyUsageFilter **
The policy usage method to use for filtering the results.
To list only permissions policies, set `PolicyUsageFilter` to `PermissionsPolicy`. To list only the policies used to set permissions boundaries, set the value to `PermissionsBoundary`.
This parameter is optional. If it is not included, all policies are returned.
Type: String
Valid Values: `PermissionsPolicy | PermissionsBoundary`
Required: No

## Response Elements
<a name="API_ListEntitiesForPolicy_ResponseElements"></a>

The following elements are returned by the service.

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

 **PolicyGroups.member.N**
A list of IAM groups that the policy is attached to.
Type: Array of [PolicyGroup](API_PolicyGroup.md) objects

 **PolicyRoles.member.N**
A list of IAM roles that the policy is attached to.
Type: Array of [PolicyRole](API_PolicyRole.md) objects

 **PolicyUsers.member.N**
A list of IAM users that the policy is attached to.
Type: Array of [PolicyUser](API_PolicyUser.md) objects

## Errors
<a name="API_ListEntitiesForPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ListEntitiesForPolicy_Examples"></a>

### Example
<a name="API_ListEntitiesForPolicy_Example_1"></a>

This example illustrates one usage of ListEntitiesForPolicy.

#### Sample Request
<a name="API_ListEntitiesForPolicy_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListEntitiesForPolicy
&PolicyArn=arn:aws:iam::123456789012:policy/EC2-Devs
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListEntitiesForPolicy_Example_1_Response"></a>

```
<ListEntitiesForPolicyResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListEntitiesForPolicyResult>
    <PolicyRoles>
      <member>
        <RoleName>DevRole</RoleName>
        <RoleId>AROADBQP57FF2AEXAMPLE</RoleId>
      </member>
    </PolicyRoles>
    <PolicyGroups>
      <member>
        <GroupName>Dev</GroupName>
        <GroupId>AGPACKCEVSQ6C2EXAMPLE</GroupId>
      </member>
    </PolicyGroups>
    <IsTruncated>false</IsTruncated>
    <PolicyUsers>
      <member>
        <UserName>Alice</UserName>
        <UserId>AIDACKCEVSQ6C2EXAMPLE</UserId>
      </member>
      <member>
        <UserName>Bob</UserName>
        <UserId>BIDACKCEVSQ6C2EXAMPLE</UserId>
      </member>
    </PolicyUsers>
  </ListEntitiesForPolicyResult>
  <ResponseMetadata>
    <RequestId>eb358e22-9d1f-11e4-93eb-190ecEXAMPLE</RequestId>
  </ResponseMetadata>
</ListEntitiesForPolicyResponse>
```

## See Also
<a name="API_ListEntitiesForPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListEntitiesForPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListEntitiesForPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListEntitiesForPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListEntitiesForPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListEntitiesForPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListEntitiesForPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListEntitiesForPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListEntitiesForPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListEntitiesForPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListEntitiesForPolicy)

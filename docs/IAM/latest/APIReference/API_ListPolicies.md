---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPolicies.html
---

# ListPolicies
<a name="API_ListPolicies"></a>

Lists all the managed policies that are available in your AWS account, including your own customer-defined managed policies and all AWS managed policies.

You can filter the list of policies that is returned using the optional `OnlyAttached`, `Scope`, and `PathPrefix` parameters. For example, to list only the customer managed policies in your AWS account, set `Scope` to `Local`. To list only AWS managed policies, set `Scope` to `AWS`.

You can paginate the results using the `MaxItems` and `Marker` parameters.

For more information about managed policies, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html) in the *IAM User Guide*.

**Note**
IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for a customer manged policy, see [GetPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetPolicy.html).

## Request Parameters
<a name="API_ListPolicies_RequestParameters"></a>

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

 ** OnlyAttached **
A flag to filter the results to only the attached policies.
When `OnlyAttached` is `true`, the returned list contains only the policies that are attached to an IAM user, group, or role. When `OnlyAttached` is `false`, or when the parameter is not included, all policies are returned.
Type: Boolean
Required: No

 ** PathPrefix **
The path prefix for filtering the results. This parameter is optional. If it is not included, it defaults to a slash (/), listing all policies. This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the \! (`\u0021`) through the DEL character (`\u007F`), including most punctuation characters, digits, and upper and lowercased letters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `((/[A-Za-z0-9\.,\+@=_-]+)*)/`
Required: No

 ** PolicyUsageFilter **
The policy usage method to use for filtering the results.
To list only permissions policies, set `PolicyUsageFilter` to `PermissionsPolicy`. To list only the policies used to set permissions boundaries, set the value to `PermissionsBoundary`.
This parameter is optional. If it is not included, all policies are returned.
Type: String
Valid Values: `PermissionsPolicy | PermissionsBoundary`
Required: No

 ** Scope **
The scope to use for filtering the results.
To list only AWS managed policies, set `Scope` to `AWS`. To list only the customer managed policies in your AWS account, set `Scope` to `Local`.
This parameter is optional. If it is not included, or if it is set to `All`, all policies are returned.
Type: String
Valid Values: `All | AWS | Local`
Required: No

## Response Elements
<a name="API_ListPolicies_ResponseElements"></a>

The following elements are returned by the service.

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

 **Policies.member.N**
A list of policies.
Type: Array of [Policy](API_Policy.md) objects

## Errors
<a name="API_ListPolicies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ListPolicies_Examples"></a>

### Example
<a name="API_ListPolicies_Example_1"></a>

This example illustrates one usage of ListPolicies.

#### Sample Request
<a name="API_ListPolicies_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListPolicies
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListPolicies_Example_1_Response"></a>

```
<ListPoliciesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListPoliciesResult>
    <IsTruncated>true</IsTruncated>
    <Marker>EXAMPLEkakv9BCuUNFDtxWSyfzetYwEx2ADc8dnzfvERF5S6YMvXKx41t6gCl/eeaCX3Jo94/bKqezEAg8TEVS
    99EKFLxm3jtbpl25FDWEXAMPLE
    </Marker>
    <Policies>
      <member>
        <Arn>arn:aws:iam::123456789012:policy/ExamplePolicy</Arn>
        <AttachmentCount>2</AttachmentCount>
        <CreateDate>2014-09-15T17:36:14Z</CreateDate>
        <DefaultVersionId>v1</DefaultVersionId>
        <IsAttachable>true</IsAttachable>
        <Path>/</Path>
        <PermissionsBoundaryUsageCount>0</PermissionsBoundaryUsageCount>
        <PolicyId>AGPACKCEVSQ6C2EXAMPLE</PolicyId>
        <PolicyName>ExamplePolicy</PolicyName>
        <UpdateDate>2014-09-15T20:31:47Z</UpdateDate>
      </member>
      <member>
        <Arn>arn:aws:iam::aws:policy/PowerUserAccess</Arn>
        <AttachmentCount>0</AttachmentCount>
        <CreateDate>2014-08-21T20:25:01Z</CreateDate>
        <DefaultVersionId>v1</DefaultVersionId>
        <IsAttachable>true</IsAttachable>
        <Path>/</Path>
        <PermissionsBoundaryUsageCount>0</PermissionsBoundaryUsageCount>
        <PolicyId>AGPACKCEVSQ6C2EXAMPLE</PolicyId>
        <PolicyName>PowerUserAccess</PolicyName>
        <UpdateDate>2014-08-21T20:25:01Z</UpdateDate>
      </member>
      <member>
        <Arn>arn:aws:iam::aws:policy/AdministratorAccess</Arn>
        <AttachmentCount>1</AttachmentCount>
        <CreateDate>2014-08-21T20:11:25Z</CreateDate>
        <DefaultVersionId>v1</DefaultVersionId>
        <IsAttachable>true</IsAttachable>
        <Path>/</Path>
        <PermissionsBoundaryUsageCount>1</PermissionsBoundaryUsageCount>
        <PolicyId>AGPACKCEVSQ6C2EXAMPLE</PolicyId>
        <PolicyName>AdministratorAccess</PolicyName>
        <UpdateDate>2014-08-21T20:11:25Z</UpdateDate>
      </member>
      <member>
        <Arn>arn:aws:iam::aws:policy/ReadOnlyAccess</Arn>
        <AttachmentCount>6</AttachmentCount>
        <CreateDate>2014-08-21T20:31:44Z</CreateDate>
        <DefaultVersionId>v1</DefaultVersionId>
        <IsAttachable>true</IsAttachable>
        <Path>/</Path>
        <PermissionsBoundaryUsageCount>2</PermissionsBoundaryUsageCount>
        <PolicyId>AGPACKCEVSQ6C2EXAMPLE</PolicyId>
        <PolicyName>ReadOnlyAccess</PolicyName>
        <UpdateDate>2014-08-21T20:31:44Z</UpdateDate>
      </member>
    </Policies>
  </ListPoliciesResult>
  <ResponseMetadata>
    <RequestId>6207e832-3eb7-11e4-9d0d-6f969EXAMPLE</RequestId>
  </ResponseMetadata>
</ListPoliciesResponse>
```

## See Also
<a name="API_ListPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListPolicies)

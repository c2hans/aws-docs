---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListInstanceProfiles.html
---

# ListInstanceProfiles
<a name="API_ListInstanceProfiles"></a>

Lists the instance profiles that have the specified path prefix. If there are none, the operation returns an empty list. For more information about instance profiles, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) in the *IAM User Guide*.

**Note**
IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for an instance profile, see [GetInstanceProfile](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetInstanceProfile.html).

You can paginate the results using the `MaxItems` and `Marker` parameters.

## Request Parameters
<a name="API_ListInstanceProfiles_RequestParameters"></a>

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
 The path prefix for filtering the results. For example, the prefix `/application_abc/component_xyz/` gets all instance profiles whose path starts with `/application_abc/component_xyz/`.
This parameter is optional. If it is not included, it defaults to a slash (/), listing all instance profiles. This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of either a forward slash (/) by itself or a string that must begin and end with forward slashes. In addition, it can contain any ASCII character from the \! (`\u0021`) through the DEL character (`\u007F`), including most punctuation characters, digits, and upper and lowercased letters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `\u002F[\u0021-\u007F]*`
Required: No

## Response Elements
<a name="API_ListInstanceProfiles_ResponseElements"></a>

The following elements are returned by the service.

 **InstanceProfiles.member.N**
A list of instance profiles.
Type: Array of [InstanceProfile](API_InstanceProfile.md) objects

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

## Errors
<a name="API_ListInstanceProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_ListInstanceProfiles_Examples"></a>

### Example
<a name="API_ListInstanceProfiles_Example_1"></a>

This example illustrates one usage of ListInstanceProfiles.

#### Sample Request
<a name="API_ListInstanceProfiles_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListInstanceProfiles
&MaxItems=100
&PathPrefix=/application_abc/
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListInstanceProfiles_Example_1_Response"></a>

```
<ListInstanceProfilesResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
<ListInstanceProfilesResult>
  <IsTruncated>false</IsTruncated>
  <InstanceProfiles>
    <member>
      <Arn>arn:aws:iam::123456789012:instance-profile/application_abc/component_xyz/Database</Arn>
      <CreateDate>2012-05-09T16:27:03Z</CreateDate>
      <InstanceProfileId>AIPA1234567890EXAMPLE</InstanceProfileId>
      <InstanceProfileName>Database</InstanceProfileName>
      <Path>/</Path>,
      <Roles>
        <member>
          <Arn>arn:aws:iam::123456789012:role/ec2instancerole-MyADFSTestServer</Arn>
          <AssumeRolePolicyDocument>{  …  JSON POLICY DOCUMENT HERE … }</AssumeRolePolicyDocument>
          <CreateDate>2016-04-27T21:18:27Z</CreateDate>
          <Path>/</Path>
          <RoleId>AROA1234567890EXAMPLE</RoleId>
          <RoleName>ec2instancerole-MyADFSTestServer</RoleName>
        </member>
      </Roles>
    </member>
    <member>
      <Arn>arn:aws:iam::123456789012:instance-profile/application_abc/component_xyz/Webserver</Arn>
      <CreateDate>2012-05-09T16:27:11Z</CreateDate>
      <InstanceProfileId>AIPA2345678901EXAMPLE</InstanceProfileId>
      <InstanceProfileName>Webserver</InstanceProfileName>
      <Path>/application_abc/component_xyz/</Path>
      <Roles/>
    </member>
  </InstanceProfiles>
</ListInstanceProfilesResult>
<ResponseMetadata>
  <RequestId>fd74fa8d-99f3-11e1-a4c3-27EXAMPLE804</RequestId>
</ResponseMetadata>
</ListInstanceProfilesResponse>
```

## See Also
<a name="API_ListInstanceProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListInstanceProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListInstanceProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListInstanceProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListInstanceProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListInstanceProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListInstanceProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListInstanceProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListInstanceProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListInstanceProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListInstanceProfiles)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

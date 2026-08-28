---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountAuthorizationDetails.html
---

# GetAccountAuthorizationDetails
<a name="API_GetAccountAuthorizationDetails"></a>

Retrieves information about all IAM users, groups, roles, and policies in your AWS account, including their relationships to one another. Use this operation to obtain a snapshot of the configuration of IAM permissions (users, groups, roles, and policies) in your account.

**Note**
Policies returned by this operation are URL-encoded compliant with [RFC 3986](https://tools.ietf.org/html/rfc3986). You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the `decode` method of the `java.net.URLDecoder` utility class in the Java SDK. Other languages and SDKs provide similar functionality, and some SDKs do this decoding automatically.

You can optionally filter the results using the `Filter` parameter. You can paginate the results using the `MaxItems` and `Marker` parameters.

## Request Parameters
<a name="API_GetAccountAuthorizationDetails_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filter.member.N**
A list of entity types used to filter the results. Only the entities that match the types you specify are included in the output. Use the value `LocalManagedPolicy` to include customer managed policies.
The format for this parameter is a comma-separated (if more than one) list of strings. Each string value in the list must be one of the valid values listed below.
Type: Array of strings
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

## Response Elements
<a name="API_GetAccountAuthorizationDetails_ResponseElements"></a>

The following elements are returned by the service.

 **GroupDetailList.member.N**
A list containing information about IAM groups.
Type: Array of [GroupDetail](API_GroupDetail.md) objects

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the `Marker` request parameter to retrieve more items. Note that IAM might return fewer than the `MaxItems` number of results even when there are more results available. We recommend that you check `IsTruncated` after every call to ensure that you receive all your results.
Type: Boolean

 ** Marker **
When `IsTruncated` is `true`, this element is present and contains the value to use for the `Marker` parameter in a subsequent pagination request.
Type: String

 **Policies.member.N**
A list containing information about managed policies.
Type: Array of [ManagedPolicyDetail](API_ManagedPolicyDetail.md) objects

 **RoleDetailList.member.N**
A list containing information about IAM roles.
Type: Array of [RoleDetail](API_RoleDetail.md) objects

 **UserDetailList.member.N**
A list containing information about IAM users.
Type: Array of [UserDetail](API_UserDetail.md) objects

## Errors
<a name="API_GetAccountAuthorizationDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetAccountAuthorizationDetails_Examples"></a>

### Example
<a name="API_GetAccountAuthorizationDetails_Example_1"></a>

This example illustrates one usage of GetAccountAuthorizationDetails.

#### Sample Request
<a name="API_GetAccountAuthorizationDetails_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetAccountAuthorizationDetails
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetAccountAuthorizationDetails_Example_1_Response"></a>

```
<GetAccountAuthorizationDetailsResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetAccountAuthorizationDetailsResult>
    <IsTruncated>true</IsTruncated>
    <UserDetailList>
      <member>
        <GroupList>
          <member>Admins</member>
        </GroupList>
        <AttachedManagedPolicies/>
        <UserId>AIDACKCEVSQ6C2EXAMPLE</UserId>
        <Path>/</Path>
        <UserName>Alice</UserName>
        <Arn>arn:aws:iam::123456789012:user/Alice</Arn>
        <CreateDate>2013-10-14T18:32:24Z</CreateDate>
      </member>
      <member>
        <GroupList>
          <member>Admins</member>
        </GroupList>
        <AttachedManagedPolicies/>
        <UserPolicyList>
          <member>
            <PolicyName>DenyBillingAndIAMPolicy</PolicyName>
            <PolicyDocument>
              {"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Deny","Action":
              ["aws-portal:*","iam:*"],"Resource":"*"}}
            </PolicyDocument>
          </member>
        </UserPolicyList>
        <UserId>AIDACKCEVSQ6C3EXAMPLE</UserId>
        <Path>/</Path>
        <UserName>Bob</UserName>
        <Arn>arn:aws:iam::123456789012:user/Bob</Arn>
        <CreateDate>2013-10-14T18:32:25Z</CreateDate>
      </member>
      <member>
        <GroupList>
          <member>Dev</member>
        <AttachedManagedPolicies/>
        </GroupList>
        <UserId>AIDACKCEVSQ6C4EXAMPLE</UserId>
        <Path>/</Path>
        <UserName>Charlie</UserName>
        <Arn>arn:aws:iam::123456789012:user/Charlie</Arn>
        <CreateDate>2013-10-14T18:33:56Z</CreateDate>
      </member>
      <member>
        <GroupList>
          <member>Dev</member>
        </GroupList>
        <AttachedManagedPolicies/>
        <UserId>AIDACKCEVSQ6C5EXAMPLE</UserId>
        <Path>/</Path>
        <UserName>Danielle</UserName>
        <Arn>arn:aws:iam::123456789012:user/Danielle</Arn>
        <CreateDate>2013-10-14T18:33:56Z</CreateDate>
      </member>
      <member>
        <GroupList>
          <member>Finance</member>
        </GroupList>
        <AttachedManagedPolicies/>
        <UserId>AIDACKCEVSQ6C6EXAMPLE</UserId>
        <Path>/</Path>
        <UserName>Elaine</UserName>
        <Arn>arn:aws:iam::123456789012:user/Elaine</Arn>
        <CreateDate>2013-10-14T18:57:48Z</CreateDate>
      </member>
    </UserDetailList>
    <Marker>
      EXAMPLEkakv9BCuUNFDtxWSyfzetYwEx2ADc8dnzfvERF5S6YMvXKx41t6gCl/eeaCX3Jo94/
      bKqezEAg8TEVS99EKFLxm3jtbpl25FDWEXAMPLE
    </Marker>
    <GroupDetailList>
      <member>
        <GroupId>AIDACKCEVSQ6C7EXAMPLE</GroupId>
        <AttachedManagedPolicies>
          <member>
            <PolicyName>AdministratorAccess</PolicyName>
            <PolicyArn>arn:aws:iam::aws:policy/AdministratorAccess</PolicyArn>
          </member>
        </AttachedManagedPolicies>
        <GroupName>Admins</GroupName>
        <Path>/</Path>
        <Arn>arn:aws:iam::123456789012:group/Admins</Arn>
        <CreateDate>2013-10-14T18:32:24Z</CreateDate>
        <GroupPolicyList/>
      </member>
      <member>
        <GroupId>AIDACKCEVSQ6C8EXAMPLE</GroupId>
        <AttachedManagedPolicies>
          <member>
            <PolicyName>PowerUserAccess</PolicyName>
            <PolicyArn>arn:aws:iam::aws:policy/PowerUserAccess</PolicyArn>
          </member>
        </AttachedManagedPolicies>
        <GroupName>Dev</GroupName>
        <Path>/</Path>
        <Arn>arn:aws:iam::123456789012:group/Dev</Arn>
        <CreateDate>2013-10-14T18:33:55Z</CreateDate>
        <GroupPolicyList/>
      </member>
      <member>
        <GroupId>AIDACKCEVSQ6C9EXAMPLE</GroupId>
        <AttachedManagedPolicies/>
        <GroupName>Finance</GroupName>
        <Path>/</Path>
        <Arn>arn:aws:iam::123456789012:group/Finance</Arn>
        <CreateDate>2013-10-14T18:57:48Z</CreateDate>
        <GroupPolicyList>
          <member>
            <PolicyName>policygen-201310141157</PolicyName>
            <PolicyDocument>
              {"Version":"2012-10-17",		 	 	 "Statement":[{"Action":["aws-portal:*"],
              "Sid":"Stmt1381777017000","Resource":["*"],"Effect":"Allow"}]}
            </PolicyDocument>
          </member>
        </GroupPolicyList>
      </member>
    </GroupDetailList>
    <RoleDetailList>
      <member>
        <RolePolicyList/>
        <AttachedManagedPolicies>
          <member>
            <PolicyName>AmazonS3FullAccess</PolicyName>
            <PolicyArn>arn:aws:iam::aws:policy/AmazonS3FullAccess</PolicyArn>
          </member>
          <member>
            <PolicyName>AmazonDynamoDBFullAccess</PolicyName>
            <PolicyArn>arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess</PolicyArn>
          </member>
        </AttachedManagedPolicies>
        <InstanceProfileList>
          <member>
            <InstanceProfileName>EC2role</InstanceProfileName>
            <Roles>
              <member>
                <Path>/</Path>
                <Arn>arn:aws:iam::123456789012:role/EC2role</Arn>
                <RoleName>EC2role</RoleName>
                <AssumeRolePolicyDocument>
                  {"Version":"2012-10-17",		 	 	 "Statement":[{"Sid":"",
                  "Effect":"Allow","Principal":{"Service":"ec2.amazonaws.com"},
                  "Action":"sts:AssumeRole"}]}
                </AssumeRolePolicyDocument>
                <CreateDate>2014-07-30T17:09:20Z</CreateDate>
                <RoleId>AROAFP4BKI7Y7TEXAMPLE</RoleId>
                <RoleLastUsed>
                  <LastUsedDate>2019-11-20T17:09:20Z</LastUsedDate>
                  <Region>us-east-1</Region>
                </RoleLastUsed>
              </member>
            </Roles>
            <Path>/</Path>
            <Arn>arn:aws:iam::123456789012:instance-profile/EC2role</Arn>
            <InstanceProfileId>AIPAFFYRBHWXW2EXAMPLE</InstanceProfileId>
            <CreateDate>2014-07-30T17:09:20Z</CreateDate>
          </member>
        </InstanceProfileList>
        <Path>/</Path>
        <Arn>arn:aws:iam::123456789012:role/EC2role</Arn>
        <RoleName>EC2role</RoleName>
        <AssumeRolePolicyDocument>
          {"Version":"2012-10-17",		 	 	 "Statement":[{"Sid":"","Effect":"Allow",
          "Principal":{"Service":"ec2.amazonaws.com"},
          "Action":"sts:AssumeRole"}]}
        </AssumeRolePolicyDocument>
        <CreateDate>2014-07-30T17:09:20Z</CreateDate>
        <RoleId>AROAFP4BKI7Y7TEXAMPLE</RoleId>      </member>
    </RoleDetailList>
    <Policies>
      <member>
        <PolicyName>create-update-delete-set-managed-policies</PolicyName>
        <DefaultVersionId>v1</DefaultVersionId>
        <PolicyId>ANPAJ2UCCR6DPCEXAMPLE</PolicyId>
        <Path>/</Path>
        <PolicyVersionList>
          <member>
            <Document>
              {"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow",
              "Action":["iam:CreatePolicy","iam:CreatePolicyVersion",
              "iam:DeletePolicy","iam:DeletePolicyVersion","iam:GetPolicy",
              "iam:GetPolicyVersion","iam:ListPolicies",
              "iam:ListPolicyVersions","iam:SetDefaultPolicyVersion"],
              "Resource":"*"}}
            </Document>
            <IsDefaultVersion>true</IsDefaultVersion>
            <VersionId>v1</VersionId>
            <CreateDate>2015-02-06T19:58:34Z</CreateDate>
          </member>
        </PolicyVersionList>
        <Arn>
          arn:aws:iam::123456789012:policy/create-update-delete-set-managed-policies
        </Arn>
        <AttachmentCount>1</AttachmentCount>
        <CreateDate>2015-02-06T19:58:34Z</CreateDate>
        <IsAttachable>true</IsAttachable>
        <UpdateDate>2015-02-06T19:58:34Z</UpdateDate>
      </member>
      <member>
        <PolicyName>S3-read-only-specific-bucket</PolicyName>
        <DefaultVersionId>v1</DefaultVersionId>
        <PolicyId>ANPAJ4AE5446DAEXAMPLE</PolicyId>
        <Path>/</Path>
        <PolicyVersionList>
          <member>
            <Document>
              {"Version":"2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Action":
              ["s3:Get*","s3:List*"],"Resource":["arn:aws:s3:::example-bucket",
              "arn:aws:s3:::example-bucket/*"]}]}
            </Document>
            <IsDefaultVersion>true</IsDefaultVersion>
            <VersionId>v1</VersionId>
            <CreateDate>2015-01-21T21:39:41Z</CreateDate>
          </member>
        </PolicyVersionList>
        <Arn>arn:aws:iam::123456789012:policy/S3-read-only-specific-bucket</Arn>
        <AttachmentCount>1</AttachmentCount>
        <CreateDate>2015-01-21T21:39:41Z</CreateDate>
        <IsAttachable>true</IsAttachable>
        <UpdateDate>2015-01-21T23:39:41Z</UpdateDate>
      </member>
      <member>
        <PolicyName>AWSOpsWorksRole</PolicyName>
        <DefaultVersionId>v1</DefaultVersionId>
        <PolicyId>ANPAE376NQ77WV6KGJEBE</PolicyId>
        <Path>/service-role/</Path>
        <PolicyVersionList>
          <member>
            <Document>
              {"Version":"2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Action":
              ["cloudwatch:GetMetricStatistics","ec2:DescribeAccountAttributes",
              "ec2:DescribeAvailabilityZones","ec2:DescribeInstances",
              "ec2:DescribeKeyPairs","ec2:DescribeSecurityGroups","ec2:DescribeSubnets",
              "ec2:DescribeVpcs","elasticloadbalancing:DescribeInstanceHealth",
              "elasticloadbalancing:DescribeLoadBalancers","iam:GetRolePolicy",
              "iam:ListInstanceProfiles","iam:ListRoles","iam:ListUsers",
              "iam:PassRole","opsworks:*","rds:*"],"Resource":["*"]}]}
            </Document>
            <IsDefaultVersion>true</IsDefaultVersion>
            <VersionId>v1</VersionId>
            <CreateDate>2014-12-10T22:57:47Z</CreateDate>
          </member>
        </PolicyVersionList>
        <Arn>arn:aws:iam::aws:policy/service-role/AWSOpsWorksRole</Arn>
        <AttachmentCount>1</AttachmentCount>
        <CreateDate>2015-02-06T18:41:27Z</CreateDate>
        <IsAttachable>true</IsAttachable>
        <UpdateDate>2015-02-06T18:41:27Z</UpdateDate>
      </member>
      <member>
        <PolicyName>AmazonEC2FullAccess</PolicyName>
        <DefaultVersionId>v1</DefaultVersionId>
        <PolicyId>ANPAE3QWE5YT46TQ34WLG</PolicyId>
        <Path>/</Path>
        <PolicyVersionList>
          <member>
            <Document>
              {"Version":"2012-10-17",		 	 	 "Statement":[{"Action":"ec2:*",
              "Effect":"Allow","Resource":"*"},{"Effect":"Allow",
              "Action":"elasticloadbalancing:*","Resource":"*"},{"Effect":"Allow",
              "Action":"cloudwatch:*","Resource":"*"},{"Effect":"Allow",
              "Action":"autoscaling:*","Resource":"*"}]}
            </Document>
            <IsDefaultVersion>true</IsDefaultVersion>
            <VersionId>v1</VersionId>
            <CreateDate>2014-10-30T20:59:46Z</CreateDate>
          </member>
        </PolicyVersionList>
        <Arn>arn:aws:iam::aws:policy/AmazonEC2FullAccess</Arn>
        <AttachmentCount>1</AttachmentCount>
        <CreateDate>2015-02-06T18:40:15Z</CreateDate>
        <IsAttachable>true</IsAttachable>
        <UpdateDate>2015-02-06T18:40:15Z</UpdateDate>
      </member>
    </Policies>
  </GetAccountAuthorizationDetailsResult>
  <ResponseMetadata>
    <RequestId>92e79ae7-7399-11e4-8c85-4b53eEXAMPLE</RequestId>
  </ResponseMetadata>
</GetAccountAuthorizationDetailsResponse>
```

## See Also
<a name="API_GetAccountAuthorizationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetAccountAuthorizationDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetAccountAuthorizationDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetAccountAuthorizationDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetAccountAuthorizationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetAccountAuthorizationDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetAccountAuthorizationDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetAccountAuthorizationDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetAccountAuthorizationDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetAccountAuthorizationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetAccountAuthorizationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

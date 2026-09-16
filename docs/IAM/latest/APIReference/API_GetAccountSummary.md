---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetAccountSummary.html
---

# GetAccountSummary
<a name="API_GetAccountSummary"></a>

Retrieves information about IAM entity usage and IAM quotas in the AWS account.

 For information about IAM quotas, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html) in the *IAM User Guide*.

## Response Elements
<a name="API_GetAccountSummary_ResponseElements"></a>

The following element is returned by the service.

 **SummaryMap** SummaryMap.entry.N.key (key)SummaryMap.entry.N.value (value)
A set of key–value pairs containing information about IAM entity usage and IAM quotas.
Type: String to integer map
Valid Keys: `Users | UsersQuota | Groups | GroupsQuota | ServerCertificates | ServerCertificatesQuota | UserPolicySizeQuota | GroupPolicySizeQuota | GroupsPerUserQuota | SigningCertificatesPerUserQuota | AccessKeysPerUserQuota | MFADevices | MFADevicesInUse | AccountMFAEnabled | AccountAccessKeysPresent | AccountPasswordPresent | AccountSigningCertificatesPresent | AttachedPoliciesPerGroupQuota | AttachedPoliciesPerRoleQuota | AttachedPoliciesPerUserQuota | Policies | PoliciesQuota | PolicySizeQuota | PolicyVersionsInUse | PolicyVersionsInUseQuota | VersionsPerPolicyQuota | GlobalEndpointTokenVersion | AssumeRolePolicySizeQuota | InstanceProfiles | InstanceProfilesQuota | Providers | RolePolicySizeQuota | Roles | RolesQuota`

## Errors
<a name="API_GetAccountSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_GetAccountSummary_Examples"></a>

### Example
<a name="API_GetAccountSummary_Example_1"></a>

This example illustrates one usage of GetAccountSummary.

#### Sample Request
<a name="API_GetAccountSummary_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=GetAccountSummary
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetAccountSummary_Example_1_Response"></a>

```
<GetAccountSummaryResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <GetAccountSummaryResult>
    <SummaryMap>
      <entry>
        <key>Users</key>
        <value>32</value>
      </entry>
      <entry>
        <key>GroupPolicySizeQuota</key>
        <value>10240</value>
      </entry>
      <entry>
        <key>PolicyVersionsInUseQuota</key>
        <value>10000</value>
      </entry>
      <entry>
        <key>ServerCertificatesQuota</key>
        <value>20</value>
      </entry>
      <entry>
        <key>AccountSigningCertificatesPresent</key>
        <value>0</value>
      </entry>
      <entry>
        <key>AccountAccessKeysPresent</key>
        <value>0</value>
      </entry>
      <entry>
        <key>Groups</key>
        <value>7</value>
      </entry>
      <entry>
        <key>UsersQuota</key>
        <value>150</value>
      </entry>
      <entry>
        <key>UserPolicySizeQuota</key>
        <value>10240</value>
      </entry>
      <entry>
        <key>GroupsPerUserQuota</key>
        <value>10</value>
      </entry
      <entry>
        <key>AttachedPoliciesPerGroupQuota</key>
        <value>2</value>
      </entry>
      <entry>
        <key>VersionsPerPolicyQuota</key>
        <value>5</value>
      </entry>
      <entry>
        <key>GroupsQuota</key>
        <value>50</value>
      </entry>
      <entry>
        <key>PolicySizeQuota</key>
        <value>5120</value>
      </entry>
      <entry>
        <key>Policies</key>
        <value>22</value>
      </entry>
      <entry>
        <key>ServerCertificates</key>
        <value>1</value>
      </entry>
      <entry>
        <key>AttachedPoliciesPerRoleQuota</key>
        <value>2</value>
      </entry>
      <entry>
        <key>MFADevicesInUse</key>
        <value>4</value>
      </entry>
      <entry>
        <key>PoliciesQuota</key>
        <value>1000</value>
      </entry>
      <entry>
        <key>AccountMFAEnabled</key>
        <value>1</value>
      </entry>
      <entry>
        <key>MFADevices</key>
        <value>4</value>
      </entry>
      <entry>
        <key>AccessKeysPerUserQuota</key>
        <value>2</value>
      </entry>
      <entry>
        <key>AttachedPoliciesPerUserQuota</key>
        <value>2</value>
      </entry>
      <entry>
        <key>SigningCertificatesPerUserQuota</key>
        <value>2</value>
      </entry>
      <entry>
        <key>PolicyVersionsInUse</key>
        <value>27</value>
      </entry>
      <entry>
        <key>GlobalEndpointTokenVersion</key>
        <value>2</value>
      </entry>
      <entry>
        <key>AccountPasswordPresent</key>
        <value>1</value>
      </entry>
    </SummaryMap>
  </GetAccountSummaryResult>
  <ResponseMetadata>
    <RequestId>85cb9b90-ac28-11e4-a88d-97964EXAMPLE</RequestId>
  </ResponseMetadata>
</GetAccountSummaryResponse>
```

## See Also
<a name="API_GetAccountSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/GetAccountSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/GetAccountSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/GetAccountSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/GetAccountSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/GetAccountSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/GetAccountSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/GetAccountSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/GetAccountSummary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/GetAccountSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/GetAccountSummary)

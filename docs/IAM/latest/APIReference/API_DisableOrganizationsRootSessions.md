---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_DisableOrganizationsRootSessions.html
---

# DisableOrganizationsRootSessions
<a name="API_DisableOrganizationsRootSessions"></a>

Disables root user sessions for privileged tasks across member accounts in your organization. When you disable this feature, the management account and the delegated administrator for IAM can no longer perform privileged tasks on member accounts in your organization.

## Response Elements
<a name="API_DisableOrganizationsRootSessions_ResponseElements"></a>

The following elements are returned by the service.

 **EnabledFeatures.member.N**
The features you have enabled for centralized root access of member accounts in your organization.
Type: Array of strings
Valid Values: `RootCredentialsManagement | RootSessions`

 ** OrganizationId **
The unique identifier (ID) of an organization.
Type: String
Length Constraints: Maximum length of 34.
Pattern: `^o-[a-z0-9]{10,32}$`

## Errors
<a name="API_DisableOrganizationsRootSessions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountNotManagementOrDelegatedAdministrator **
The request was rejected because the account making the request is not the management account or delegated administrator account for [centralized root access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management).
HTTP Status Code: 400

 ** OrganizationNotFound **
The request was rejected because no organization is associated with your account.
HTTP Status Code: 400

 ** OrganizationNotInAllFeaturesMode **
The request was rejected because your organization does not have All features enabled. For more information, see [Available feature sets](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set) in the * AWS Organizations User Guide*.
HTTP Status Code: 400

 ** ServiceAccessNotEnabled **
The request was rejected because trusted access is not enabled for IAM in AWS Organizations. For details, see IAM and AWS Organizations in the * AWS Organizations User Guide*.
HTTP Status Code: 400

## Examples
<a name="API_DisableOrganizationsRootSessions_Examples"></a>

### Example
<a name="API_DisableOrganizationsRootSessions_Example_1"></a>

This example illustrates one usage of DisableOrganizationsRootSessions.

#### Sample Request
<a name="API_DisableOrganizationsRootSessions_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=DisableOrganizationsRootSessions
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisableOrganizationsRootSessions_Example_1_Response"></a>

```
<DisableOrganizationsRootSessionsResponse xmlns="https://iam.amazonaws.com/doc/2024-11-03/">
  <ResponseMetadata>
    <EnabledFeatures>
        <member><RootCredentialsManagement></member>
    </EnabledFeatures>
    <OrganizationId>o111122223333</OrganizationId>
  </ResponseMetadata>
</DisableOrganizationsRootSessionsResponse>
```

## See Also
<a name="API_DisableOrganizationsRootSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/DisableOrganizationsRootSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/DisableOrganizationsRootSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/DisableOrganizationsRootSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/DisableOrganizationsRootSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/DisableOrganizationsRootSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/DisableOrganizationsRootSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/DisableOrganizationsRootSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/DisableOrganizationsRootSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/DisableOrganizationsRootSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/DisableOrganizationsRootSessions)

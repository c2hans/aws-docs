---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_EnableOrganizationsRootCredentialsManagement.html
---

# EnableOrganizationsRootCredentialsManagement
<a name="API_EnableOrganizationsRootCredentialsManagement"></a>

Enables the management of privileged root user credentials across member accounts in your organization. When you enable root credentials management for [centralized root access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management), the management account and the delegated administrator for IAM can manage root user credentials for member accounts in your organization.

Before you enable centralized root access, you must have an account configured with the following settings:
+ You must manage your AWS accounts in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).
+ Enable trusted access for AWS Identity and Access Management in AWS Organizations. For details, see [IAM and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-iam.html) in the * AWS Organizations User Guide*.

## Response Elements
<a name="API_EnableOrganizationsRootCredentialsManagement_ResponseElements"></a>

The following elements are returned by the service.

 **EnabledFeatures.member.N**
The features you have enabled for centralized root access.
Type: Array of strings
Valid Values: `RootCredentialsManagement | RootSessions`

 ** OrganizationId **
The unique identifier (ID) of an organization.
Type: String
Length Constraints: Maximum length of 34.
Pattern: `^o-[a-z0-9]{10,32}$`

## Errors
<a name="API_EnableOrganizationsRootCredentialsManagement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccountNotManagementOrDelegatedAdministrator **
The request was rejected because the account making the request is not the management account or delegated administrator account for [centralized root access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management).
HTTP Status Code: 400

 ** CallerIsNotManagementAccount **
The request was rejected because the account making the request is not the management account for the organization.
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
<a name="API_EnableOrganizationsRootCredentialsManagement_Examples"></a>

### Example
<a name="API_EnableOrganizationsRootCredentialsManagement_Example_1"></a>

This example illustrates one usage of EnableOrganizationsRootCredentialsManagement.

#### Sample Request
<a name="API_EnableOrganizationsRootCredentialsManagement_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=EnableOrganizationsRootCredentialsManagement
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_EnableOrganizationsRootCredentialsManagement_Example_1_Response"></a>

```
<EnableOrganizationsRootCredentialsManagementResponse xmlns="https://iam.amazonaws.com/doc/2024-11-03/">
  <ResponseMetadata>
    <EnabledFeatures>
        <member><RootCredentialsManagement></member>
        <member><RootSessions></member>
    </EnabledFeatures>
    <OrganizationId>o111122223333</OrganizationId>
  </ResponseMetadata>
</EnableOrganizationsRootCredentialsManagementResponse>
```

## See Also
<a name="API_EnableOrganizationsRootCredentialsManagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/EnableOrganizationsRootCredentialsManagement)

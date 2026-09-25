---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_InstanceMetadata.html
---

# InstanceMetadata
<a name="API_InstanceMetadata"></a>

Provides information about the IAM Identity Center instance.

## Contents
<a name="API_InstanceMetadata_Contents"></a>

 ** CreatedDate **   <a name="singlesignon-Type-InstanceMetadata-CreatedDate"></a>
The date and time that the Identity Center instance was created.
Type: Timestamp
Required: No

 ** IdentityStoreArn **   <a name="singlesignon-Type-InstanceMetadata-IdentityStoreArn"></a>
The ARN of the identity store that is connected to the Identity Center instance.
Type: String
Length Constraints: Minimum length of 62. Maximum length of 93.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:identitystore::\d{12}:identitystore/(d-[0-9a-f]{10}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: No

 ** IdentityStoreId **   <a name="singlesignon-Type-InstanceMetadata-IdentityStoreId"></a>
The identifier of the identity store that is connected to the Identity Center instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** InstanceArn **   <a name="singlesignon-Type-InstanceMetadata-InstanceArn"></a>
The ARN of the Identity Center instance under which the operation will be executed. For more information about ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: No

 ** Name **   <a name="singlesignon-Type-InstanceMetadata-Name"></a>
The name of the Identity Center instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\w+=,.@-]+`
Required: No

 ** OwnerAccountId **   <a name="singlesignon-Type-InstanceMetadata-OwnerAccountId"></a>
The AWS account ID number of the owner of the Identity Center instance.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** PrimaryRegion **   <a name="singlesignon-Type-InstanceMetadata-PrimaryRegion"></a>
The primary Region where the IAM Identity Center instance was originally enabled. The primary Region cannot be removed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([a-z]+-){2,3}\d`
Required: No

 ** Regions **   <a name="singlesignon-Type-InstanceMetadata-Regions"></a>
The list of Regions enabled in the IAM Identity Center instance, including Regions with ACTIVE, ADDING, or REMOVING status.
Type: Array of [RegionMetadata](API_RegionMetadata.md) objects
Required: No

 ** Status **   <a name="singlesignon-Type-InstanceMetadata-Status"></a>
The current status of this Identity Center instance.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | DELETE_IN_PROGRESS | ACTIVE`
Required: No

 ** StatusReason **   <a name="singlesignon-Type-InstanceMetadata-StatusReason"></a>
Provides additional context about the current status of the IAM Identity Center instance. This field is particularly useful when an instance is in a non-ACTIVE state, such as CREATE\_FAILED. When an instance creation fails, this field contains information about the cause, which may include issues with KMS key configuration or insufficient permissions.
Type: String
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

## See Also
<a name="API_InstanceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/InstanceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/InstanceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/InstanceMetadata)

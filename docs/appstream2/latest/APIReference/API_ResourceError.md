---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ResourceError.html
---

# ResourceError
<a name="API_ResourceError"></a>

Describes a resource error.

## Contents
<a name="API_ResourceError_Contents"></a>

 ** ErrorCode **   <a name="WorkSpacesApplications-Type-ResourceError-ErrorCode"></a>
The error code.
Type: String
Valid Values: `IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION | IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION | IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION | NETWORK_INTERFACE_LIMIT_EXCEEDED | INTERNAL_SERVICE_ERROR | IAM_SERVICE_ROLE_IS_MISSING | MACHINE_ROLE_IS_MISSING | STS_DISABLED_IN_REGION | SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES | IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION | SUBNET_NOT_FOUND | IMAGE_NOT_FOUND | INVALID_SUBNET_CONFIGURATION | SECURITY_GROUPS_NOT_FOUND | IGW_NOT_ATTACHED | IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION | FLEET_STOPPED | FLEET_INSTANCE_PROVISIONING_FAILURE | DOMAIN_JOIN_ERROR_FILE_NOT_FOUND | DOMAIN_JOIN_ERROR_ACCESS_DENIED | DOMAIN_JOIN_ERROR_LOGON_FAILURE | DOMAIN_JOIN_ERROR_INVALID_PARAMETER | DOMAIN_JOIN_ERROR_MORE_DATA | DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN | DOMAIN_JOIN_ERROR_NOT_SUPPORTED | DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME | DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED | DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED | DOMAIN_JOIN_NERR_PASSWORD_EXPIRED | DOMAIN_JOIN_INTERNAL_SERVICE_ERROR | VALIDATION_ERROR`
Required: No

 ** ErrorMessage **   <a name="WorkSpacesApplications-Type-ResourceError-ErrorMessage"></a>
The error message.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** ErrorTimestamp **   <a name="WorkSpacesApplications-Type-ResourceError-ErrorTimestamp"></a>
The time the error occurred.
Type: Timestamp
Required: No

## See Also
<a name="API_ResourceError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ResourceError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ResourceError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ResourceError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

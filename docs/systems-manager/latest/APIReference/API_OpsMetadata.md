---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsMetadata.html
---

# OpsMetadata
<a name="API_OpsMetadata"></a>

Operational metadata for an application in Application Manager.

## Contents
<a name="API_OpsMetadata_Contents"></a>

 ** CreationDate **   <a name="systemsmanager-Type-OpsMetadata-CreationDate"></a>
The date the OpsMetadata objects was created.
Type: Timestamp
Required: No

 ** LastModifiedDate **   <a name="systemsmanager-Type-OpsMetadata-LastModifiedDate"></a>
The date the OpsMetadata object was last updated.
Type: Timestamp
Required: No

 ** LastModifiedUser **   <a name="systemsmanager-Type-OpsMetadata-LastModifiedUser"></a>
The user name who last updated the OpsMetadata object.
Type: String
Required: No

 ** OpsMetadataArn **   <a name="systemsmanager-Type-OpsMetadata-OpsMetadataArn"></a>
The Amazon Resource Name (ARN) of the OpsMetadata Object or blob.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:(aws[a-zA-Z-]*)?:ssm:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:opsmetadata\/([a-zA-Z0-9-_\.\/]*)`
Required: No

 ** ResourceId **   <a name="systemsmanager-Type-OpsMetadata-ResourceId"></a>
The ID of the Application Manager application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`
Required: No

## See Also
<a name="API_OpsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

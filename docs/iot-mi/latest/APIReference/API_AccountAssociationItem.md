---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_AccountAssociationItem.html
---

# AccountAssociationItem
<a name="API_AccountAssociationItem"></a>

Structure containing information about an account association, including its identifier, state, and related metadata.

## Contents
<a name="API_AccountAssociationItem_Contents"></a>

 ** AccountAssociationId **   <a name="managedintegrations-Type-AccountAssociationItem-AccountAssociationId"></a>
The unique identifier of the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`
Required: Yes

 ** AssociationState **   <a name="managedintegrations-Type-AccountAssociationItem-AssociationState"></a>
The current state of the account association, indicating its status in the association lifecycle.
Type: String
Valid Values: `ASSOCIATION_IN_PROGRESS | ASSOCIATION_FAILED | ASSOCIATION_SUCCEEDED | ASSOCIATION_DELETING | REFRESH_TOKEN_EXPIRED`
Required: Yes

 ** Arn **   <a name="managedintegrations-Type-AccountAssociationItem-Arn"></a>
The Amazon Resource Name (ARN) of the account association.
Type: String
Length Constraints: Minimum length of 67. Maximum length of 1011.
Pattern: `arn:aws:iotmanagedintegrations:[0-9a-zA-Z-]+:[0-9]+:account-association/[0-9a-zA-Z]+`
Required: No

 ** ConnectorDestinationId **   <a name="managedintegrations-Type-AccountAssociationItem-ConnectorDestinationId"></a>
The identifier of the connector destination associated with this account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** Description **   <a name="managedintegrations-Type-AccountAssociationItem-Description"></a>
A description of the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** ErrorMessage **   <a name="managedintegrations-Type-AccountAssociationItem-ErrorMessage"></a>
The error message explaining any issues with the account association, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

 ** Name **   <a name="managedintegrations-Type-AccountAssociationItem-Name"></a>
The name of the account association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: No

## See Also
<a name="API_AccountAssociationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/AccountAssociationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/AccountAssociationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/AccountAssociationItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

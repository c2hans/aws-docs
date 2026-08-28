---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_SecurityGroup.html
---

# SecurityGroup
<a name="API_SecurityGroup"></a>

Represents a security group in a Wickr network, containing membership statistics, configuration, and all permission settings that apply to its members.

## Contents
<a name="API_SecurityGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** activeMembers **   <a name="wickr-Type-SecurityGroup-activeMembers"></a>
The number of active user members currently in the security group.
Type: Integer
Required: Yes

 ** botMembers **   <a name="wickr-Type-SecurityGroup-botMembers"></a>
The number of bot members currently in the security group.
Type: Integer
Required: Yes

 ** id **   <a name="wickr-Type-SecurityGroup-id"></a>
The unique identifier of the security group.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** isDefault **   <a name="wickr-Type-SecurityGroup-isDefault"></a>
Indicates whether this is the default security group for the network. Each network has only one default group.
Type: Boolean
Required: Yes

 ** modified **   <a name="wickr-Type-SecurityGroup-modified"></a>
The timestamp when the security group was last modified, specified in epoch seconds.
Type: Integer
Required: Yes

 ** name **   <a name="wickr-Type-SecurityGroup-name"></a>
The human-readable name of the security group.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** securityGroupSettings **   <a name="wickr-Type-SecurityGroup-securityGroupSettings"></a>
The comprehensive configuration settings that define capabilities and restrictions for members of this security group.
Type: [SecurityGroupSettings](API_SecurityGroupSettings.md) object
Required: Yes

 ** activeDirectoryGuid **   <a name="wickr-Type-SecurityGroup-activeDirectoryGuid"></a>
The GUID of the Active Directory group associated with this security group, if synchronized with LDAP.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_SecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/SecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/SecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/SecurityGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsAmazonMqBrokerLdapServerMetadataDetails.html
---

# AwsAmazonMqBrokerLdapServerMetadataDetails
<a name="API_AwsAmazonMqBrokerLdapServerMetadataDetails"></a>

 The metadata of the Lightweight Directory Access Protocol (LDAP) server used to authenticate and authorize connections to the broker. This is an optional failover server.

## Contents
<a name="API_AwsAmazonMqBrokerLdapServerMetadataDetails_Contents"></a>

 ** Hosts **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-Hosts"></a>
 Specifies the location of the LDAP server, such as AWS Directory Service for Microsoft Active Directory.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** RoleBase **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-RoleBase"></a>
 The distinguished name of the node in the directory information tree (DIT) to search for roles or groups.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoleName **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-RoleName"></a>
 The group name attribute in a role entry whose value is the name of that role.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoleSearchMatching **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-RoleSearchMatching"></a>
 The LDAP search filter used to find roles within the `roleBase`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RoleSearchSubtree **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-RoleSearchSubtree"></a>
 The directory search scope for the role. If set to `true`, the scope is to search the entire subtree.
Type: Boolean
Required: No

 ** ServiceAccountUsername **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-ServiceAccountUsername"></a>
 A username for the service account, which is an account in your LDAP server that has access to initiate a connection.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserBase **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-UserBase"></a>
 Selects a particular subtree of the directory information tree (DIT) to search for user entries.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserRoleName **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-UserRoleName"></a>
 The name of the LDAP attribute in the user's directory entry for the user's group membership.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserSearchMatching **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-UserSearchMatching"></a>
 The LDAP search filter used to find users within the `userBase`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UserSearchSubtree **   <a name="securityhub-Type-AwsAmazonMqBrokerLdapServerMetadataDetails-UserSearchSubtree"></a>
 The directory search scope for the user. If set to true, the scope is to search the entire subtree.
Type: Boolean
Required: No

## See Also
<a name="API_AwsAmazonMqBrokerLdapServerMetadataDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsAmazonMqBrokerLdapServerMetadataDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsAmazonMqBrokerLdapServerMetadataDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsAmazonMqBrokerLdapServerMetadataDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

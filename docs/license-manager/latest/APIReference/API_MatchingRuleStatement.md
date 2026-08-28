---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_MatchingRuleStatement.html
---

# MatchingRuleStatement
<a name="API_MatchingRuleStatement"></a>

Matching rule statement.

## Contents
<a name="API_MatchingRuleStatement_Contents"></a>

 ** Constraint **   <a name="licensemanager-Type-MatchingRuleStatement-Constraint"></a>
Constraint.
Type: String
Required: Yes

 ** KeyToMatch **   <a name="licensemanager-Type-MatchingRuleStatement-KeyToMatch"></a>
Key to match.
The following keys and are supported when the RuleStatement type is `Instance`:
+  `Platform` - The name of the platform. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `EC2BillingProduct` - The billing product code. Logical operators are `EQUALS` and `NOT_EQUALS`. Possible values are: `windows-server-enterprise` \| `windows-byol` \| `rhel` \| `rhel-byol` \| `rhel-high-availability` \| `ubuntu-pro` \| `suse-linux` \| `sql-server-standard` \| `sql-server-enterprise`.
+  `MarketPlaceProductCode` - The Marketplace product code. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `AMIId` - The ID of the AMI. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `InstanceType` - The instance type. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `InstanceId` - The ID of the instance. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `HostId` - The ID of the host. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `AccountId` - The ID of the account. Logical operators are `EQUALS` and `NOT_EQUALS`.
The following keys and are supported when the RuleStatement type is `License`:
+  `LicenseArn` - The ARN of a Managed Entitlement License. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `ProductSKU` - The productSKU of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `Issuer` - The issuer of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `Beneficiary` - The beneficiary of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `LicenseStatus` - The status of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `HomeRegion` - The home region of the license. Logical operators are `EQUALS` and `NOT_EQUALS`.
The following keys and are supported when the RuleStatement type is `License Configuration`:
+  `LicenseConfigurationArn` - The ARN of a self-managed license configuration. Logical operators are `EQUALS` and `NOT_EQUALS`.
+  `AccountId` - The account of the license configuration. Logical operators are `EQUALS` and `NOT_EQUALS`.
Type: String
Required: Yes

 ** ValueToMatch **   <a name="licensemanager-Type-MatchingRuleStatement-ValueToMatch"></a>
Value to match.
Type: Array of strings
Required: Yes

## See Also
<a name="API_MatchingRuleStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/MatchingRuleStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/MatchingRuleStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/MatchingRuleStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

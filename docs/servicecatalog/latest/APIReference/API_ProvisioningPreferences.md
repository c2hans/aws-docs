---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_ProvisioningPreferences.html
---

# ProvisioningPreferences
<a name="API_ProvisioningPreferences"></a>

The user-defined preferences that will be applied when updating a provisioned product. Not all preferences are applicable to all provisioned product type

One or more AWS accounts that will have access to the provisioned product.

Applicable only to a `CFN_STACKSET` provisioned product type.

The AWS accounts specified should be within the list of accounts in the `STACKSET` constraint. To get the list of accounts in the `STACKSET` constraint, use the `DescribeProvisioningParameters` operation.

If no values are specified, the default value is all accounts from the `STACKSET` constraint.

## Contents
<a name="API_ProvisioningPreferences_Contents"></a>

 ** StackSetAccounts **   <a name="servicecatalog-Type-ProvisioningPreferences-StackSetAccounts"></a>
One or more AWS accounts where the provisioned product will be available.
Applicable only to a `CFN_STACKSET` provisioned product type.
The specified accounts should be within the list of accounts from the `STACKSET` constraint. To get the list of accounts in the `STACKSET` constraint, use the `DescribeProvisioningParameters` operation.
If no values are specified, the default value is all acounts from the `STACKSET` constraint.
Type: Array of strings
Pattern: `^[0-9]{12}$`
Required: No

 ** StackSetFailureToleranceCount **   <a name="servicecatalog-Type-ProvisioningPreferences-StackSetFailureToleranceCount"></a>
The number of accounts, per Region, for which this operation can fail before AWS Service Catalog stops the operation in that Region. If the operation is stopped in a Region, AWS Service Catalog doesn't attempt the operation in any subsequent Regions.
Applicable only to a `CFN_STACKSET` provisioned product type.
Conditional: You must specify either `StackSetFailureToleranceCount` or `StackSetFailureTolerancePercentage`, but not both.
The default value is `0` if no value is specified.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** StackSetFailureTolerancePercentage **   <a name="servicecatalog-Type-ProvisioningPreferences-StackSetFailureTolerancePercentage"></a>
The percentage of accounts, per Region, for which this stack operation can fail before AWS Service Catalog stops the operation in that Region. If the operation is stopped in a Region, AWS Service Catalog doesn't attempt the operation in any subsequent Regions.
When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number.
Applicable only to a `CFN_STACKSET` provisioned product type.
Conditional: You must specify either `StackSetFailureToleranceCount` or `StackSetFailureTolerancePercentage`, but not both.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** StackSetMaxConcurrencyCount **   <a name="servicecatalog-Type-ProvisioningPreferences-StackSetMaxConcurrencyCount"></a>
The maximum number of accounts in which to perform this operation at one time. This is dependent on the value of `StackSetFailureToleranceCount`. `StackSetMaxConcurrentCount` is at most one more than the `StackSetFailureToleranceCount`.
Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
Applicable only to a `CFN_STACKSET` provisioned product type.
Conditional: You must specify either `StackSetMaxConcurrentCount` or `StackSetMaxConcurrentPercentage`, but not both.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** StackSetMaxConcurrencyPercentage **   <a name="servicecatalog-Type-ProvisioningPreferences-StackSetMaxConcurrencyPercentage"></a>
The maximum percentage of accounts in which to perform this operation at one time.
When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as `1` instead.
Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling.
Applicable only to a `CFN_STACKSET` provisioned product type.
Conditional: You must specify either `StackSetMaxConcurrentCount` or `StackSetMaxConcurrentPercentage`, but not both.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** StackSetRegions **   <a name="servicecatalog-Type-ProvisioningPreferences-StackSetRegions"></a>
One or more AWS Regions where the provisioned product will be available.
Applicable only to a `CFN_STACKSET` provisioned product type.
The specified Regions should be within the list of Regions from the `STACKSET` constraint. To get the list of Regions in the `STACKSET` constraint, use the `DescribeProvisioningParameters` operation.
If no values are specified, the default value is all Regions from the `STACKSET` constraint.
Type: Array of strings
Required: No

## See Also
<a name="API_ProvisioningPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

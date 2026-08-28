---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ProductInformation.html
---

# ProductInformation
<a name="API_ProductInformation"></a>

Describes product information for a license configuration.

## Contents
<a name="API_ProductInformation_Contents"></a>

 ** ProductInformationFilterList **   <a name="licensemanager-Type-ProductInformation-ProductInformationFilterList"></a>
A Product information filter consists of a `ProductInformationFilterComparator` which is a logical operator, a `ProductInformationFilterName` which specifies the type of filter being declared, and a `ProductInformationFilterValue` that specifies the value to filter on.
Accepted values for `ProductInformationFilterName` are listed here along with descriptions and valid options for `ProductInformationFilterComparator`.
The following filters and are supported when the resource type is `SSM_MANAGED`:
+  `Application Name` - The name of the application. Logical operator is `EQUALS`.
+  `Application Publisher` - The publisher of the application. Logical operator is `EQUALS`.
+  `Application Version` - The version of the application. Logical operator is `EQUALS`.
+  `Platform Name` - The name of the platform. Logical operator is `EQUALS`.
+  `Platform Type` - The platform type. Logical operator is `EQUALS`.
+  `Tag:key` - The key of a tag attached to an AWS resource you wish to exclude from automated discovery. Logical operator is `NOT_EQUALS`. The key for your tag must be appended to `Tag:` following the example: `Tag:name-of-your-key`. `ProductInformationFilterValue` is optional if you are not using values for the key.
+  `AccountId` - The 12-digit ID of an AWS account you wish to exclude from automated discovery. Logical operator is `NOT_EQUALS`.
+  `License Included` - The type of license included. Logical operators are `EQUALS` and `NOT_EQUALS`. Possible values are: `sql-server-enterprise` \| `sql-server-standard` \| `sql-server-web` \| `windows-server-datacenter`.
The following filters and logical operators are supported when the resource type is `RDS`:
+  `Engine Edition` - The edition of the database engine. Logical operator is `EQUALS`. Possible values are: `oracle-ee` \| `oracle-se` \| `oracle-se1` \| `oracle-se2` \| `db2-se` \| `db2-ae`.
+  `License Pack` - The license pack. Logical operator is `EQUALS`. Possible values are: `data guard` \| `diagnostic pack sqlt` \| `tuning pack sqlt` \| `ols` \| `olap`.
Type: Array of [ProductInformationFilter](API_ProductInformationFilter.md) objects
Required: Yes

 ** ResourceType **   <a name="licensemanager-Type-ProductInformation-ResourceType"></a>
Resource type. The possible values are `SSM_MANAGED` \| `RDS`.
Type: String
Required: Yes

## See Also
<a name="API_ProductInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ProductInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ProductInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ProductInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

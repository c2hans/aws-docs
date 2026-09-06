---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StrategyOption.html
---

# StrategyOption
<a name="API_StrategyOption"></a>

 Information about all the available strategy options for migrating and modernizing an application component.

## Contents
<a name="API_StrategyOption_Contents"></a>

 ** isPreferred **   <a name="migrationhubstrategy-Type-StrategyOption-isPreferred"></a>
 Indicates if a specific strategy is preferred for the application component.
Type: Boolean
Required: No

 ** strategy **   <a name="migrationhubstrategy-Type-StrategyOption-strategy"></a>
 Type of transformation. For example, Rehost, Replatform, and so on.
Type: String
Valid Values: `Rehost | Retirement | Refactor | Replatform | Retain | Relocate | Repurchase`
Required: No

 ** targetDestination **   <a name="migrationhubstrategy-Type-StrategyOption-targetDestination"></a>
 Destination information about where the application component can migrate to. For example, `EC2`, `ECS`, and so on.
Type: String
Valid Values: `None specified | AWS Elastic BeanStalk | AWS Fargate | Amazon Elastic Cloud Compute (EC2) | Amazon Elastic Container Service (ECS) | Amazon Elastic Kubernetes Service (EKS) | Aurora MySQL | Aurora PostgreSQL | Amazon Relational Database Service on MySQL | Amazon Relational Database Service on PostgreSQL | Amazon DocumentDB | Amazon DynamoDB | Amazon Relational Database Service | Babelfish for Aurora PostgreSQL`
Required: No

 ** toolName **   <a name="migrationhubstrategy-Type-StrategyOption-toolName"></a>
 The name of the tool that can be used to transform an application component using this strategy.
Type: String
Valid Values: `App2Container | Porting Assistant For .NET | End of Support Migration | Windows Web Application Migration Assistant | Application Migration Service | Strategy Recommendation Support | In Place Operating System Upgrade | Schema Conversion Tool | Database Migration Service | Native SQL Server Backup/Restore`
Required: No

## See Also
<a name="API_StrategyOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/StrategyOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/StrategyOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/StrategyOption)

---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html
---

# Endpoint
<a name="API_Endpoint"></a>

This data type represents the information you need to connect to an Amazon RDS DB instance. This data type is used as a response element in the following actions:
+  `CreateDBInstance`
+  `DescribeDBInstances`
+  `DeleteDBInstance`

For the data structure that represents Amazon Aurora DB cluster endpoints, see `DBClusterEndpoint`.

## Contents
<a name="API_Endpoint_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Address **
Specifies the DNS address of the DB instance.
Type: String
Required: No

 ** HostedZoneId **
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
Type: String
Required: No

 ** Port **
Specifies the port that the database engine is listening on.
Type: Integer
Required: No

## See Also
<a name="API_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/Endpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/Endpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/Endpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

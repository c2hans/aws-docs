---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.QueryDataInDynamoDB.html
---

# Step 6: Query the data in the DynamoDB table
<a name="EMRforDynamoDB.Tutorial.QueryDataInDynamoDB"></a>

In this step, you will use HiveQL to query the Features table in DynamoDB. Try the following Hive queries:

1. All of the feature types (`feature_class`) in alphabetical order:

   ```
   SELECT DISTINCT feature_class
   FROM ddb_features
   ORDER BY feature_class;
   ```

1. All of the lakes that begin with the letter "M":

   ```
   SELECT feature_name, state_alpha
   FROM ddb_features
   WHERE feature_class = 'Lake'
   AND feature_name LIKE 'M%'
   ORDER BY feature_name;
   ```

1. States with at least three features higher than a mile (5,280 feet):

   ```
   SELECT state_alpha, feature_class, COUNT(*)
   FROM ddb_features
   WHERE elev_in_ft > 5280
   GROUP by state_alpha, feature_class
   HAVING COUNT(*) >= 3
   ORDER BY state_alpha, feature_class;
   ```

**Next step**
[Step 7: (Optional) clean up](EMRforDynamoDB.Tutorial.CleanUp.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

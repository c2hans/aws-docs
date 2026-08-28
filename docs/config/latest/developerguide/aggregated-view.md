---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/aggregated-view.html
---

# Viewing Aggregators for AWS Config
<a name="aggregated-view"></a>

You can use the AWS Config console or the AWS CLI to view your aggregators.

------
#### [ Viewing Aggregators (Console) ]

To view your conformance packs in the AWS Management Console, see [Aggregator Dashboard](https://docs.aws.amazon.com/config/latest/developerguide/viewing-the-aggregate-dashboard.html).

------
#### [ Viewing Aggregators (AWS CLI) ]

1. Enter the following command:

   ```
   aws configservice describe-configuration-aggregators
   ```

1. Depending on your source account you should see output similar to the following:

   **For individuals accounts**

   ```
   {
       "ConfigurationAggregators": [
           {
               "ConfigurationAggregatorArn": "arn:aws:config:{{Region}}:{{AccountID}}:config-aggregator/config-aggregator-floqpus3",
               "CreationTime": 1517942461.442,
               "ConfigurationAggregatorName": "MyAggregator",
               "AccountAggregationSources": [
                   {
                       "AllAwsRegions": true,
                       "AccountIds": [
                           "AccountID1",
                           "AccountID2",
                           "AccountID3"
                       ]
                   }
               ],
               "LastUpdatedTime": 1517942461.455
           }
       ]
   }
   ```

   OR

   **For an organization**

   ```
   {
       "ConfigurationAggregator": {
           "ConfigurationAggregatorArn": "arn:aws:config:{{Region}}:{{AccountID}}:config-aggregator/config-aggregator-floqpus3",
           "CreationTime": 1517942461.442,
           "ConfigurationAggregatorName": "MyAggregator",
           "OrganizationAggregationSource": {
                   "AllAwsRegions": true,
                   "RoleArn": "arn:aws:iam::{{account-of-role-to-assume}}:role/{{name-of-role}}"
            },
           "LastUpdatedTime": 1517942461.442
       }
   }
   ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

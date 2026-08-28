---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-seed-data-requirements.html
---

# Seed data requirements for Clean Rooms ML
<a name="ml-seed-data-requirements"></a>

The seed data for a lookalike model can either come directly from an Amazon S3 bucket or from the results of an SQL query.

Seed data that's provided directly must meet the following requirements:
+ The seed data must be in JSON lines format with a list of user IDs.
+ The seed size should be between 25 and 500,000 unique user IDs.
+ The minimum number of seed users must match the minimum matching seed size value that was specified when you created the configured audience model.

The following is an example of a valid training data set in CSV format

```
{"user_id": "abc"}
{"user_id": "def"}
{"user_id": "ghijkl"}
{"user_id": "123"}
{"user_id": "456"}
{"user_id": "7890"}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

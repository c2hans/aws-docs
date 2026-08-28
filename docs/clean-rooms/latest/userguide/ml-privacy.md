---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/ml-privacy.html
---

# Privacy protections of AWS Clean Rooms ML
<a name="ml-privacy"></a>

Clean Rooms ML is designed to reduce the risk of *membership inference attacks* where the training data provider can learn who is in the seed data and the seed data provider can learn who is in the training data. Several steps are taken to prevent this attack.

First, seed data providers don't directly observe the Clean Rooms ML output and training data providers can never observe the seed data. Seed data providers can choose to include the seed data in the output segment.

Next, the lookalike model is created from a random sample of the training data. This sample includes a significant number of users that don't match the seed audience. This process makes it harder to determine whether a user was not in the data, which is another avenue for membership inference.

Further, multiple seed customers can be used for every parameter of seed-specific lookalike model training. This limits how much the model can overfit, and thus how much can be inferred about a user. As a result, we recommend that the minimum size of the seed data is 500 users.

Finally, user-level metrics are never provided to training data providers, which eliminates another avenue for a membership inference attack.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations-list.html
---

# List configurations in your account for the current Region
<a name="msk-configuration-operations-list"></a>

This process describes how to list all Amazon MSK configurations in your account for the current AWS Region.
+ Run the following command.

  ```
  aws kafka list-configurations
  ```

  The following is an example of a successful response after you run this command.

  ```
  {
      "Configurations": [
          {
              "Arn": "arn:aws:kafka:us-east-1:123456789012:configuration/SomeTest/abcdabcd-abcd-1234-abcd-abcd123e8e8e-1",
              "CreationTime": "2019-05-21T00:54:23.591Z",
              "Description": "Example configuration description.",
              "KafkaVersions": [
                  "1.1.1"
              ],
              "LatestRevision": {
                  "CreationTime": "2019-05-21T00:54:23.591Z",
                  "Description": "Example configuration description.",
                  "Revision": 1
              },
              "Name": "SomeTest"
          },
          {
              "Arn": "arn:aws:kafka:us-east-1:123456789012:configuration/SomeTest/abcdabcd-1234-abcd-1234-abcd123e8e8e-1",
              "CreationTime": "2019-05-03T23:08:29.446Z",
              "Description": "Example configuration description.",
              "KafkaVersions": [
                  "1.1.1"
              ],
              "LatestRevision": {
                  "CreationTime": "2019-05-03T23:08:29.446Z",
                  "Description": "Example configuration description.",
                  "Revision": 1
              },
              "Name": "ExampleConfigurationName"
          }
      ]
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

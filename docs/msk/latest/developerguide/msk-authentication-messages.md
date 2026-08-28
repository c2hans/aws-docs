---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication-messages.html
---

# Produce and consume messages using authentication
<a name="msk-authentication-messages"></a>

This process describes how to produce and consume messages using authentication.

1. Run the following command to create a topic. The file named `client.properties` is the one you created in the previous procedure.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-topics.sh --create --bootstrap-server {{BootstrapBroker-String}} --replication-factor 3 --partitions 1 --topic ExampleTopic --command-config client.properties
   ```

1. Run the following command to start a console producer. The file named `client.properties` is the one you created in the previous procedure.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-console-producer.sh --bootstrap-server {{BootstrapBroker-String}} --topic ExampleTopic --producer.config client.properties
   ```

1. In a new command window on your client machine, run the following command to start a console consumer.

   ```
   {{<path-to-your-kafka-installation>}}/bin/kafka-console-consumer.sh --bootstrap-server {{BootstrapBroker-String}} --topic ExampleTopic --consumer.config client.properties
   ```

1. Type messages in the producer window and watch them appear in the consumer window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

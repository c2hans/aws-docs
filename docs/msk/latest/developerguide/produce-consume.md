---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/produce-consume.html
---

# Step 5: Produce and consume data
<a name="produce-consume"></a>

In this step of [Get Started Using Amazon MSK](getting-started.md), you produce and consume data.

**To produce and consume messages**Produce and consume messages

1. Run the following command to start a console producer.

   ```
   $KAFKA_ROOT/bin/kafka-console-producer.sh --broker-list $BOOTSTRAP_SERVER --producer.config $KAFKA_ROOT/config/client.properties --topic {{MSKTutorialTopic}}
   ```

1. Enter any message that you want, and press **Enter**. Repeat this step two or three times. Every time you enter a line and press **Enter**, that line is sent to your Apache Kafka cluster as a separate message.

1. Keep the connection to the client machine open, and then open a second, separate connection to that machine in a new window. Because this is a new session, set the `KAFKA_ROOT` and `BOOTSTRAP_SERVER` environment variables again. For information about how to set these environment variables, see [Creating a topic on the client machine](create-topic.md#create-topic-client-machine).

1. Run the following command with your second connection string to the client machine to create a console consumer.

   ```
   $KAFKA_ROOT/bin/kafka-console-consumer.sh --bootstrap-server $BOOTSTRAP_SERVER --consumer.config $KAFKA_ROOT/config/client.properties --topic {{MSKTutorialTopic}} --from-beginning
   ```

   You should start seeing the messages you entered earlier when you used the console producer command.

1. Enter more messages in the producer window, and watch them appear in the consumer window.

**Next Step**

[Step 6: Use Amazon CloudWatch to view Amazon MSK metrics](view-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

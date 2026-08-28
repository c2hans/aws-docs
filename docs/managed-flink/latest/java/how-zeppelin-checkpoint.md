---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/how-zeppelin-checkpoint.html
---

# Enable checkpointing
<a name="how-zeppelin-checkpoint"></a>

You enable checkpointing by using environment settings. For information about checkpointing, see [Fault Tolerance](https://docs.aws.amazon.com/managed-flink/latest/java/how-fault.html) in the [Managed Service for Apache Flink Developer Guide](https://docs.aws.amazon.com/managed-flink/latest/java/).

## Set the checkpointing interval
<a name="how-zeppelin-checkpoint-interval"></a>

The following Scala code example sets your application's checkpoint interval to one minute:

```
// start a checkpoint every 1 minute
stenv.enableCheckpointing(60000)
```

The following Python code example sets your application's checkpoint interval to one minute:

```
st_env.get_config().get_configuration().set_string(
    "execution.checkpointing.interval", "1min"
)
```

## Set the checkpointing type
<a name="how-zeppelin-checkpoint-type"></a>

The following Scala code example sets your application's checkpoint mode to `EXACTLY_ONCE` (the default):

```
// set mode to exactly-once (this is the default)
stenv.getCheckpointConfig.setCheckpointingMode(CheckpointingMode.EXACTLY_ONCE)
```

The following Python code example sets your application's checkpoint mode to `EXACTLY_ONCE` (the default):

```
st_env.get_config().get_configuration().set_string(
    "execution.checkpointing.mode", "EXACTLY_ONCE"
)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_kinesis_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Kinesis examples using SDK for Python (Boto3)
<a name="python_3_kinesis_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with Kinesis.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)
+ [Serverless examples](#serverless_examples)

## Get started
<a name="get_started"></a>

### Hello
<a name="kinesis_Hello_python_3_topic"></a>

The following code example shows how to get started using .

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def hello_kinesis():
    """
    Lists Kinesis data streams with a limit of 10 and displays the results.
    Use this example to verify that your environment is configured correctly.
    """
    kinesis_client = boto3.client("kinesis")
    print("Hello, Amazon Kinesis! Let's list some of your streams:\n")
    try:
        response = kinesis_client.list_streams(Limit=10)
        stream_summaries = response.get("StreamSummaries", list())
        if stream_summaries:
            for summary in stream_summaries:
                print(f"  Stream: {summary['StreamName']}")
            print(f"\nFound {len(stream_summaries)} stream(s).")
        else:
            print("No streams found in your account.")
    except ClientError as err:
        if err.response["Error"]["Code"] == "LimitExceededException":
            logger.error("Request rate too high. Retry after a brief delay.")
        else:
            logger.error(
                "Error listing streams: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
        raise

if __name__ == "__main__":
    hello_kinesis()
```
+  For API details, see [ListStreams](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListStreams) in *AWS SDK for Python (Boto3) API Reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="kinesis_Scenario_GettingStarted_python_3_topic"></a>

The following code example shows how to:
+ Create a stream and wait for it to become ACTIVE.
+ List streams and verify creation.
+ Describe stream summary to get metadata.
+ List shards in the stream.
+ Batch put records using PutRecords.
+ Get a shard iterator and read records.
+ Add tags to the stream.
+ List tags for the stream.
+ Remove tags from the stream.
+ Register an enhanced fan-out consumer.
+ Deregister the consumer.
+ Clean up all resources.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).
Run the Kinesis Data Streams basics scenario.

```
def run_scenario(kinesis_wrapper):
    """
    Runs the Kinesis Data Streams basics scenario.

    :param kinesis_wrapper: A KinesisWrapper instance.
    """
    stream_name = f"sdk-example-stream-{int(time.time())}"
    consumer_name = "sdk-example-consumer"
    consumer_arn = None
    stream_arn = None

    print(DASHES)
    print("Welcome to the Amazon Kinesis Data Streams Scenario.")
    print(
        "This scenario demonstrates advanced stream management, batch data\n"
        "ingestion, shard inspection, tagging, and enhanced fan-out consumers."
    )
    print(DASHES)

    try:
        # --- Setup: Create stream ---
        print("\nSetting up resources...")
        print(f"Creating Kinesis stream: {stream_name}")
        kinesis_wrapper.kinesis_client.create_stream(
            StreamName=stream_name, ShardCount=1
        )
        print("Waiting for stream to become ACTIVE...")
        summary = kinesis_wrapper.wait_for_stream_active(stream_name)
        stream_arn = summary.get("StreamARN", "")
        print("Stream is now ACTIVE.")
        print(DASHES)

        # --- Step 1: List Streams ---
        print("\nStep 1: Listing streams in your account...")
        streams = kinesis_wrapper.list_streams()
        for s in streams:
            mode = s.get("StreamModeDetails", dict()).get("StreamMode", "N/A")
            print(
                f"  Stream: {s.get('StreamName')} "
                f"(Status: {s.get('StreamStatus')}, Mode: {mode})"
            )
        found = any(s.get("StreamName") == stream_name for s in streams)
        print(
            f"Found {len(streams)} stream(s). "
            f"Our scenario stream is {'present' if found else 'NOT found'}."
        )
        print(DASHES)

        # --- Step 2: Describe Stream Summary ---
        print("\nStep 2: Describing stream summary...")
        summary = kinesis_wrapper.describe_stream_summary(stream_name)
        print(f"  Stream Name: {summary.get('StreamName')}")
        print(f"  Stream ARN: {summary.get('StreamARN')}")
        print(f"  Status: {summary.get('StreamStatus')}")
        print(f"  Retention Period: {summary.get('RetentionPeriodHours')} hours")
        print(f"  Open Shard Count: {summary.get('OpenShardCount')}")
        print(f"  Encryption: {summary.get('EncryptionType', 'NONE')}")
        mode = summary.get("StreamModeDetails", dict()).get("StreamMode", "N/A")
        print(f"  Stream Mode: {mode}")
        stream_arn = summary.get("StreamARN", stream_arn)
        print(DASHES)

        # --- Step 3: List Shards ---
        print("\nStep 3: Listing shards in the stream...")
        shards = kinesis_wrapper.list_shards(stream_name)
        first_shard_id = None
        for shard in shards:
            shard_id = shard.get("ShardId", "")
            if first_shard_id is None:
                first_shard_id = shard_id
            hash_range = shard.get("HashKeyRange", dict())
            seq_range = shard.get("SequenceNumberRange", dict())
            print(f"  Shard ID: {shard_id}")
            print(
                f"    Hash Key Range: {hash_range.get('StartingHashKey')} - "
                f"{hash_range.get('EndingHashKey')}"
            )
            print(
                f"    Starting Sequence Number: "
                f"{seq_range.get('StartingSequenceNumber')}"
            )
        print(f"Found {len(shards)} shard(s).")
        print(DASHES)

        # --- Step 4: PutRecords ---
        print("\nStep 4: Putting 5 records into the stream using PutRecords...")
        sensor_data = [
            {
                "sensor_id": "sensor-001",
                "temperature": 72.5,
                "timestamp": "2024-01-15T10:00:00Z",
            },
            {
                "sensor_id": "sensor-002",
                "temperature": 68.3,
                "timestamp": "2024-01-15T10:00:01Z",
            },
            {
                "sensor_id": "sensor-001",
                "temperature": 73.1,
                "timestamp": "2024-01-15T10:00:02Z",
            },
            {
                "sensor_id": "sensor-003",
                "temperature": 75.8,
                "timestamp": "2024-01-15T10:00:03Z",
            },
            {
                "sensor_id": "sensor-002",
                "temperature": 67.9,
                "timestamp": "2024-01-15T10:00:04Z",
            },
        ]
        records = [
            {
                "Data": json.dumps(data).encode("utf-8"),
                "PartitionKey": data["sensor_id"],
            }
            for data in sensor_data
        ]
        put_response = kinesis_wrapper.put_records(stream_name, records)
        for idx, rec in enumerate(put_response.get("Records", list()), 1):
            if rec.get("ErrorCode"):
                print(
                    f"  Record {idx}: FAILED - {rec.get('ErrorCode')}: "
                    f"{rec.get('ErrorMessage')}"
                )
            else:
                print(
                    f"  Record {idx}: ShardId={rec.get('ShardId')}, "
                    f"SequenceNumber={rec.get('SequenceNumber')}"
                )
        failed = put_response.get("FailedRecordCount", 0)
        print(f"Successfully put 5 record(s) with {failed} failures.")
        print(DASHES)

        # --- Step 5: GetShardIterator and read records ---
        print("\nStep 5: Getting shard iterator (TRIM_HORIZON) and reading records...")
        shard_iterator = kinesis_wrapper.get_shard_iterator(
            stream_name, first_shard_id, "TRIM_HORIZON"
        )
        print(f"  Obtained shard iterator for {first_shard_id}.")
        print("  Reading records from the stream...")
        get_response = kinesis_wrapper.kinesis_client.get_records(
            ShardIterator=shard_iterator, Limit=10
        )
        data_records = get_response.get("Records", list())
        for idx, rec in enumerate(data_records, 1):
            payload = rec.get("Data", b"").decode("utf-8")
            print(f"  Record {idx}: {payload}")
        print(f"Read {len(data_records)} record(s) from the stream.")
        print(DASHES)

        # --- Step 6: Add Tags ---
        print("\nStep 6: Adding tags to the stream...")
        tags = {
            "Project": "kinesis-demo",
            "Environment": "development",
            "CostCenter": "12345",
        }
        kinesis_wrapper.add_tags_to_stream(stream_name, tags)
        for key, value in tags.items():
            print(f"  Added tag: {key} = {value}")
        print("Tags added successfully.")
        print(DASHES)

        # --- Step 7: List Tags ---
        print("\nStep 7: Listing tags for the stream...")
        tag_list, has_more_tags = kinesis_wrapper.list_tags_for_stream(stream_name)
        for tag in tag_list:
            print(f"  Tag: {tag.get('Key')} = {tag.get('Value')}")
        print(f"Found {len(tag_list)} tag(s). HasMoreTags: {has_more_tags}")
        print(DASHES)

        # --- Step 8: Remove Tags ---
        print("\nStep 8: Removing the CostCenter tag from the stream...")
        kinesis_wrapper.remove_tags_from_stream(stream_name, ["CostCenter"])
        print("Tag removed successfully.")
        print("Verifying remaining tags...")
        remaining_tags, _ = kinesis_wrapper.list_tags_for_stream(stream_name)
        for tag in remaining_tags:
            print(f"  Tag: {tag.get('Key')} = {tag.get('Value')}")
        print(f"Confirmed: {len(remaining_tags)} tag(s) remaining after removal.")
        print(DASHES)

        # --- Step 9: Register Consumer ---
        print("\nStep 9: Registering an enhanced fan-out consumer...")
        consumer = kinesis_wrapper.register_stream_consumer(stream_arn, consumer_name)
        consumer_arn = consumer.get("ConsumerARN", "")
        print(f"  Consumer Name: {consumer.get('ConsumerName')}")
        print(f"  Consumer ARN: {consumer_arn}")
        print(f"  Status: {consumer.get('ConsumerStatus')}")
        print("Waiting for consumer to become ACTIVE...")
        desc = kinesis_wrapper.wait_for_consumer_active(stream_arn, consumer_name)
        print(f"  Consumer status: {desc.get('ConsumerStatus')}")
        print("Enhanced fan-out consumer registered successfully.")
        print(DASHES)

        # --- Step 10: Deregister Consumer ---
        print("\nStep 10: Deregistering the enhanced fan-out consumer...")
        kinesis_wrapper.deregister_stream_consumer(consumer_arn)
        print(f"Consumer '{consumer_name}' deregistered successfully.")
        print("Enhanced fan-out charges will stop for this consumer.")
        consumer_arn = None
        print(DASHES)

    finally:
        # --- Cleanup ---
        print(DASHES)
        print("Cleaning up resources...")

        # Deregister consumer if still registered
        if consumer_arn:
            print("Ensuring consumer is deregistered...")
            try:
                kinesis_wrapper.deregister_stream_consumer(consumer_arn)
                print("  Consumer deregistered during cleanup.")
            except ClientError as err:
                if err.response["Error"]["Code"] == "ResourceNotFoundException":
                    print("  Consumer already deregistered.")
                else:
                    logger.error("Error deregistering consumer: %s", err)

        # Delete the stream
        print(f"Deleting stream: {stream_name}")
        try:
            kinesis_wrapper.kinesis_client.delete_stream(
                StreamName=stream_name, EnforceConsumerDeletion=True
            )
            print("Waiting for stream deletion to complete...")
            # Use the built-in waiter so the expected "not found" result
            # isn't logged as an error while polling.
            waiter = kinesis_wrapper.kinesis_client.get_waiter("stream_not_exists")
            waiter.wait(
                StreamName=stream_name,
                WaiterConfig={"Delay": 2, "MaxAttempts": 60},
            )
            print("Stream deleted successfully.")
        except WaiterError as err:
            logger.error("Timed out waiting for stream deletion: %s", err)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                print("Stream already deleted.")
            else:
                logger.error("Error deleting stream: %s", err)

        print(DASHES)
        print("Amazon Kinesis Data Streams scenario complete!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    wrapper = KinesisWrapper.from_client()
    run_scenario(wrapper)
```
Define a wrapper class that is called by the scenario to manage Kinesis actions.

```
class KinesisWrapper:
    """Encapsulates Amazon Kinesis Data Streams operations."""

    def __init__(self, kinesis_client):
        """
        Initializes the KinesisWrapper with a Kinesis client.

        :param kinesis_client: A Boto3 Kinesis client.
        """
        self.kinesis_client = kinesis_client

    @classmethod
    def from_client(cls):
        """
        Creates a KinesisWrapper instance with a default Kinesis client.

        :return: A KinesisWrapper instance.
        """
        kinesis_client = boto3.client("kinesis")
        return cls(kinesis_client)

    def list_streams(self, limit=100):
        """
        Lists Kinesis data streams in the account.

        :param limit: The maximum number of streams to list.
        :return: A list of stream summary dictionaries.
        """
        try:
            streams = list()
            response = self.kinesis_client.list_streams(Limit=limit)
            streams.extend(response.get("StreamSummaries", list()))
            while response.get("HasMoreStreams", False):
                summaries = response.get("StreamSummaries", list())
                if not summaries:
                    break
                next_name = summaries[-1]["StreamName"]
                response = self.kinesis_client.list_streams(
                    Limit=limit, ExclusiveStartStreamName=next_name
                )
                streams.extend(response.get("StreamSummaries", list()))
            logger.info("Listed %s stream(s).", len(streams))
            return streams
        except ClientError as err:
            if err.response["Error"]["Code"] == "LimitExceededException":
                logger.error(
                    "Request rate too high for ListStreams. Retry after a brief delay."
                )
            raise

    def describe_stream_summary(self, stream_name):
        """
        Provides a summarized description of a Kinesis data stream.

        :param stream_name: The name of the stream to describe.
        :return: A dictionary containing the stream description summary.
        """
        try:
            response = self.kinesis_client.describe_stream_summary(
                StreamName=stream_name
            )
            summary = response.get("StreamDescriptionSummary", dict())
            logger.info(
                "Described stream summary for '%s'. Status: %s.",
                stream_name,
                summary.get("StreamStatus", "UNKNOWN"),
            )
            return summary
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Stream '%s' not found. Verify the stream name.", stream_name
                )
            raise

    def list_shards(self, stream_name, max_wait=30, poll_interval=2):
        """
        Lists the shards in a Kinesis data stream.

        A freshly created stream can report ACTIVE via DescribeStreamSummary
        before its shards are listable. Because ListShards is eventually
        consistent, it may briefly raise ResourceInUseException ("in state
        CREATING") or ResourceNotFoundException. This method retries on those
        errors until the shards become available or ``max_wait`` elapses.

        :param stream_name: The name of the stream whose shards to list.
        :param max_wait: Maximum seconds to retry while the stream is still
                         settling after creation.
        :param poll_interval: Seconds between retries.
        :return: A list of shard dictionaries.
        """
        elapsed = 0
        while True:
            try:
                shards = list()
                response = self.kinesis_client.list_shards(StreamName=stream_name)
                shards.extend(response.get("Shards", list()))
                while "NextToken" in response:
                    response = self.kinesis_client.list_shards(
                        NextToken=response["NextToken"]
                    )
                    shards.extend(response.get("Shards", list()))
                logger.info(
                    "Listed %s shard(s) for stream '%s'.", len(shards), stream_name
                )
                return shards
            except ClientError as err:
                code = err.response["Error"]["Code"]
                retryable = ("ResourceInUseException", "ResourceNotFoundException")
                if code in retryable and elapsed < max_wait:
                    logger.info(
                        "Stream '%s' not ready for ListShards yet. Retrying...",
                        stream_name,
                    )
                    time.sleep(poll_interval)
                    elapsed += poll_interval
                    continue
                if code == "ResourceNotFoundException":
                    logger.error(
                        "Stream '%s' not found. Verify the stream is ACTIVE.",
                        stream_name,
                    )
                raise

    def put_records(self, stream_name, records):
        """
        Writes multiple data records into a Kinesis data stream in a single call.

        :param stream_name: The name of the stream to write records to.
        :param records: A list of dicts, each with 'Data' (bytes) and 'PartitionKey' (str).
        :return: The response from the PutRecords call.
        """
        try:
            response = self.kinesis_client.put_records(
                StreamName=stream_name, Records=records
            )
            failed_count = response.get("FailedRecordCount", 0)
            logger.info(
                "Put %s record(s) to stream '%s' with %s failure(s).",
                len(records),
                stream_name,
                failed_count,
            )
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidArgumentException":
                logger.error(
                    "Invalid argument for PutRecords. Check record sizes and parameters."
                )
            raise

    def get_shard_iterator(self, stream_name, shard_id, iterator_type="TRIM_HORIZON"):
        """
        Gets a shard iterator for reading data records from a shard.

        :param stream_name: The name of the stream.
        :param shard_id: The ID of the shard.
        :param iterator_type: The shard iterator type (e.g., TRIM_HORIZON, LATEST).
        :return: A shard iterator string.
        """
        try:
            response = self.kinesis_client.get_shard_iterator(
                StreamName=stream_name,
                ShardId=shard_id,
                ShardIteratorType=iterator_type,
            )
            shard_iterator = response.get("ShardIterator", None)
            logger.info(
                "Got shard iterator for shard '%s' of type '%s'.",
                shard_id,
                iterator_type,
            )
            return shard_iterator
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Stream '%s' or shard '%s' not found. Verify shard ID is correct.",
                    stream_name,
                    shard_id,
                )
            raise

    def add_tags_to_stream(self, stream_name, tags):
        """
        Adds or updates tags for a Kinesis data stream.

        :param stream_name: The name of the stream to tag.
        :param tags: A dictionary of tag key-value pairs.
        """
        try:
            self.kinesis_client.add_tags_to_stream(StreamName=stream_name, Tags=tags)
            logger.info("Added %s tag(s) to stream '%s'.", len(tags), stream_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found. Cannot add tags.", stream_name)
            raise

    def list_tags_for_stream(self, stream_name):
        """
        Lists the tags for a Kinesis data stream.

        :param stream_name: The name of the stream whose tags to list.
        :return: A tuple of (list of tag dictionaries with 'Key' and 'Value',
                 bool indicating whether more tags are available).
        """
        try:
            response = self.kinesis_client.list_tags_for_stream(StreamName=stream_name)
            tags = response.get("Tags", list())
            has_more = response.get("HasMoreTags", False)
            logger.info(
                "Listed %s tag(s) for stream '%s'. HasMoreTags: %s.",
                len(tags),
                stream_name,
                has_more,
            )
            return tags, has_more
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found when listing tags.", stream_name)
            raise

    def remove_tags_from_stream(self, stream_name, tag_keys):
        """
        Removes tags from a Kinesis data stream.

        :param stream_name: The name of the stream to remove tags from.
        :param tag_keys: A list of tag keys to remove.
        """
        try:
            self.kinesis_client.remove_tags_from_stream(
                StreamName=stream_name, TagKeys=tag_keys
            )
            logger.info("Removed tag(s) %s from stream '%s'.", tag_keys, stream_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found for tag removal.", stream_name)
            raise

    def register_stream_consumer(self, stream_arn, consumer_name):
        """
        Registers an enhanced fan-out consumer with a Kinesis data stream.

        :param stream_arn: The ARN of the stream.
        :param consumer_name: The name for the consumer.
        :return: A dictionary containing consumer details.
        """
        try:
            response = self.kinesis_client.register_stream_consumer(
                StreamARN=stream_arn, ConsumerName=consumer_name
            )
            consumer = response.get("Consumer", dict())
            logger.info(
                "Registered consumer '%s' with status '%s'.",
                consumer_name,
                consumer.get("ConsumerStatus", "UNKNOWN"),
            )
            return consumer
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceInUseException":
                logger.error(
                    "Consumer '%s' already exists or stream is not available.",
                    consumer_name,
                )
            raise

    def deregister_stream_consumer(self, consumer_arn):
        """
        Deregisters an enhanced fan-out consumer.

        :param consumer_arn: The ARN of the consumer to deregister.
        """
        try:
            self.kinesis_client.deregister_stream_consumer(ConsumerARN=consumer_arn)
            logger.info("Deregistered consumer with ARN '%s'.", consumer_arn)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Consumer not found. It may have already been deregistered."
                )
            raise
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [AddTagsToStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/AddTagsToStream)
  + [CreateStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/CreateStream)
  + [DeleteStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DeleteStream)
  + [DeregisterStreamConsumer](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DeregisterStreamConsumer)
  + [DescribeStreamSummary](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeStreamSummary)
  + [GetRecords](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/GetRecords)
  + [GetShardIterator](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/GetShardIterator)
  + [ListShards](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListShards)
  + [ListStreams](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListStreams)
  + [ListTagsForStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListTagsForStream)
  + [PutRecord](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/PutRecord)
  + [PutRecords](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/PutRecords)
  + [RegisterStreamConsumer](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/RegisterStreamConsumer)
  + [RemoveTagsFromStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/RemoveTagsFromStream)

## Actions
<a name="actions"></a>

### `AddTagsToStream`
<a name="kinesis_AddTagsToStream_python_3_topic"></a>

The following code example shows how to use `AddTagsToStream`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def add_tags_to_stream(self, stream_name, tags):
        """
        Adds or updates tags for a Kinesis data stream.

        :param stream_name: The name of the stream to tag.
        :param tags: A dictionary of tag key-value pairs.
        """
        try:
            self.kinesis_client.add_tags_to_stream(StreamName=stream_name, Tags=tags)
            logger.info("Added %s tag(s) to stream '%s'.", len(tags), stream_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found. Cannot add tags.", stream_name)
            raise
```
+  For API details, see [AddTagsToStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/AddTagsToStream) in *AWS SDK for Python (Boto3) API Reference*.

### `CreateStream`
<a name="kinesis_CreateStream_python_3_topic"></a>

The following code example shows how to use `CreateStream`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
class KinesisStream:
    """Encapsulates a Kinesis stream."""

    def __init__(self, kinesis_client):
        """
        :param kinesis_client: A Boto3 Kinesis client.
        """
        self.kinesis_client = kinesis_client
        self.name = None
        self.details = None
        self.stream_exists_waiter = kinesis_client.get_waiter("stream_exists")

    def create(self, name, wait_until_exists=True):
        """
        Creates a stream.

        :param name: The name of the stream.
        :param wait_until_exists: When True, waits until the service reports that
                                  the stream exists, then queries for its metadata.
        """
        try:
            self.kinesis_client.create_stream(StreamName=name, ShardCount=1)
            self.name = name
            logger.info("Created stream %s.", name)
            if wait_until_exists:
                logger.info("Waiting until exists.")
                self.stream_exists_waiter.wait(StreamName=name)
                self.describe(name)
        except ClientError:
            logger.exception("Couldn't create stream %s.", name)
            raise
```
+  For API details, see [CreateStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/CreateStream) in *AWS SDK for Python (Boto3) API Reference*.

### `DeleteStream`
<a name="kinesis_DeleteStream_python_3_topic"></a>

The following code example shows how to use `DeleteStream`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
class KinesisStream:
    """Encapsulates a Kinesis stream."""

    def __init__(self, kinesis_client):
        """
        :param kinesis_client: A Boto3 Kinesis client.
        """
        self.kinesis_client = kinesis_client
        self.name = None
        self.details = None
        self.stream_exists_waiter = kinesis_client.get_waiter("stream_exists")

    def delete(self):
        """
        Deletes a stream.
        """
        try:
            self.kinesis_client.delete_stream(StreamName=self.name)
            self._clear()
            logger.info("Deleted stream %s.", self.name)
        except ClientError:
            logger.exception("Couldn't delete stream %s.", self.name)
            raise
```
+  For API details, see [DeleteStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DeleteStream) in *AWS SDK for Python (Boto3) API Reference*.

### `DeregisterStreamConsumer`
<a name="kinesis_DeregisterStreamConsumer_python_3_topic"></a>

The following code example shows how to use `DeregisterStreamConsumer`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def deregister_stream_consumer(self, consumer_arn):
        """
        Deregisters an enhanced fan-out consumer.

        :param consumer_arn: The ARN of the consumer to deregister.
        """
        try:
            self.kinesis_client.deregister_stream_consumer(ConsumerARN=consumer_arn)
            logger.info("Deregistered consumer with ARN '%s'.", consumer_arn)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Consumer not found. It may have already been deregistered."
                )
            raise
```
+  For API details, see [DeregisterStreamConsumer](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DeregisterStreamConsumer) in *AWS SDK for Python (Boto3) API Reference*.

### `DescribeStream`
<a name="kinesis_DescribeStream_python_3_topic"></a>

The following code example shows how to use `DescribeStream`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
class KinesisStream:
    """Encapsulates a Kinesis stream."""

    def __init__(self, kinesis_client):
        """
        :param kinesis_client: A Boto3 Kinesis client.
        """
        self.kinesis_client = kinesis_client
        self.name = None
        self.details = None
        self.stream_exists_waiter = kinesis_client.get_waiter("stream_exists")

    def describe(self, name):
        """
        Gets metadata about a stream.

        :param name: The name of the stream.
        :return: Metadata about the stream.
        """
        try:
            response = self.kinesis_client.describe_stream(StreamName=name)
            self.name = name
            self.details = response["StreamDescription"]
            logger.info("Got stream %s.", name)
        except ClientError:
            logger.exception("Couldn't get %s.", name)
            raise
        else:
            return self.details
```
+  For API details, see [DescribeStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeStream) in *AWS SDK for Python (Boto3) API Reference*.

### `DescribeStreamSummary`
<a name="kinesis_DescribeStreamSummary_python_3_topic"></a>

The following code example shows how to use `DescribeStreamSummary`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def describe_stream_summary(self, stream_name):
        """
        Provides a summarized description of a Kinesis data stream.

        :param stream_name: The name of the stream to describe.
        :return: A dictionary containing the stream description summary.
        """
        try:
            response = self.kinesis_client.describe_stream_summary(
                StreamName=stream_name
            )
            summary = response.get("StreamDescriptionSummary", dict())
            logger.info(
                "Described stream summary for '%s'. Status: %s.",
                stream_name,
                summary.get("StreamStatus", "UNKNOWN"),
            )
            return summary
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Stream '%s' not found. Verify the stream name.", stream_name
                )
            raise
```
+  For API details, see [DescribeStreamSummary](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeStreamSummary) in *AWS SDK for Python (Boto3) API Reference*.

### `GetRecords`
<a name="kinesis_GetRecords_python_3_topic"></a>

The following code example shows how to use `GetRecords`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
class KinesisStream:
    """Encapsulates a Kinesis stream."""

    def __init__(self, kinesis_client):
        """
        :param kinesis_client: A Boto3 Kinesis client.
        """
        self.kinesis_client = kinesis_client
        self.name = None
        self.details = None
        self.stream_exists_waiter = kinesis_client.get_waiter("stream_exists")

    def get_records(self, max_records):
        """
        Gets records from the stream. This function is a generator that first gets
        a shard iterator for the stream, then uses the shard iterator to get records
        in batches from the stream. The shard iterator can be accessed through the
        'details' property, which is populated using the 'describe' function of this class.
        Each batch of records is yielded back to the caller until the specified
        maximum number of records has been retrieved.

        :param max_records: The maximum number of records to retrieve.
        :return: Yields the current batch of retrieved records.
        """
        try:
            response = self.kinesis_client.get_shard_iterator(
                StreamName=self.name,
                ShardId=self.details["Shards"][0]["ShardId"],
                ShardIteratorType="LATEST",
            )
            shard_iter = response["ShardIterator"]
            record_count = 0
            while record_count < max_records:
                response = self.kinesis_client.get_records(
                    ShardIterator=shard_iter, Limit=10
                )
                shard_iter = response["NextShardIterator"]
                records = response["Records"]
                logger.info("Got %s records.", len(records))
                record_count += len(records)
                yield records
        except ClientError:
            logger.exception("Couldn't get records from stream %s.", self.name)
            raise

    def describe(self, name):
        """
        Gets metadata about a stream.

        :param name: The name of the stream.
        :return: Metadata about the stream.
        """
        try:
            response = self.kinesis_client.describe_stream(StreamName=name)
            self.name = name
            self.details = response["StreamDescription"]
            logger.info("Got stream %s.", name)
        except ClientError:
            logger.exception("Couldn't get %s.", name)
            raise
        else:
            return self.details
```
+  For API details, see [GetRecords](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/GetRecords) in *AWS SDK for Python (Boto3) API Reference*.

### `GetShardIterator`
<a name="kinesis_GetShardIterator_python_3_topic"></a>

The following code example shows how to use `GetShardIterator`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def get_shard_iterator(self, stream_name, shard_id, iterator_type="TRIM_HORIZON"):
        """
        Gets a shard iterator for reading data records from a shard.

        :param stream_name: The name of the stream.
        :param shard_id: The ID of the shard.
        :param iterator_type: The shard iterator type (e.g., TRIM_HORIZON, LATEST).
        :return: A shard iterator string.
        """
        try:
            response = self.kinesis_client.get_shard_iterator(
                StreamName=stream_name,
                ShardId=shard_id,
                ShardIteratorType=iterator_type,
            )
            shard_iterator = response.get("ShardIterator", None)
            logger.info(
                "Got shard iterator for shard '%s' of type '%s'.",
                shard_id,
                iterator_type,
            )
            return shard_iterator
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Stream '%s' or shard '%s' not found. Verify shard ID is correct.",
                    stream_name,
                    shard_id,
                )
            raise
```
+  For API details, see [GetShardIterator](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/GetShardIterator) in *AWS SDK for Python (Boto3) API Reference*.

### `ListShards`
<a name="kinesis_ListShards_python_3_topic"></a>

The following code example shows how to use `ListShards`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def list_shards(self, stream_name, max_wait=30, poll_interval=2):
        """
        Lists the shards in a Kinesis data stream.

        A freshly created stream can report ACTIVE via DescribeStreamSummary
        before its shards are listable. Because ListShards is eventually
        consistent, it may briefly raise ResourceInUseException ("in state
        CREATING") or ResourceNotFoundException. This method retries on those
        errors until the shards become available or ``max_wait`` elapses.

        :param stream_name: The name of the stream whose shards to list.
        :param max_wait: Maximum seconds to retry while the stream is still
                         settling after creation.
        :param poll_interval: Seconds between retries.
        :return: A list of shard dictionaries.
        """
        elapsed = 0
        while True:
            try:
                shards = list()
                response = self.kinesis_client.list_shards(StreamName=stream_name)
                shards.extend(response.get("Shards", list()))
                while "NextToken" in response:
                    response = self.kinesis_client.list_shards(
                        NextToken=response["NextToken"]
                    )
                    shards.extend(response.get("Shards", list()))
                logger.info(
                    "Listed %s shard(s) for stream '%s'.", len(shards), stream_name
                )
                return shards
            except ClientError as err:
                code = err.response["Error"]["Code"]
                retryable = ("ResourceInUseException", "ResourceNotFoundException")
                if code in retryable and elapsed < max_wait:
                    logger.info(
                        "Stream '%s' not ready for ListShards yet. Retrying...",
                        stream_name,
                    )
                    time.sleep(poll_interval)
                    elapsed += poll_interval
                    continue
                if code == "ResourceNotFoundException":
                    logger.error(
                        "Stream '%s' not found. Verify the stream is ACTIVE.",
                        stream_name,
                    )
                raise
```
+  For API details, see [ListShards](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListShards) in *AWS SDK for Python (Boto3) API Reference*.

### `ListStreams`
<a name="kinesis_ListStreams_python_3_topic"></a>

The following code example shows how to use `ListStreams`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def list_streams(self, limit=100):
        """
        Lists Kinesis data streams in the account.

        :param limit: The maximum number of streams to list.
        :return: A list of stream summary dictionaries.
        """
        try:
            streams = list()
            response = self.kinesis_client.list_streams(Limit=limit)
            streams.extend(response.get("StreamSummaries", list()))
            while response.get("HasMoreStreams", False):
                summaries = response.get("StreamSummaries", list())
                if not summaries:
                    break
                next_name = summaries[-1]["StreamName"]
                response = self.kinesis_client.list_streams(
                    Limit=limit, ExclusiveStartStreamName=next_name
                )
                streams.extend(response.get("StreamSummaries", list()))
            logger.info("Listed %s stream(s).", len(streams))
            return streams
        except ClientError as err:
            if err.response["Error"]["Code"] == "LimitExceededException":
                logger.error(
                    "Request rate too high for ListStreams. Retry after a brief delay."
                )
            raise
```
+  For API details, see [ListStreams](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListStreams) in *AWS SDK for Python (Boto3) API Reference*.

### `ListTagsForStream`
<a name="kinesis_ListTagsForStream_python_3_topic"></a>

The following code example shows how to use `ListTagsForStream`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def list_tags_for_stream(self, stream_name):
        """
        Lists the tags for a Kinesis data stream.

        :param stream_name: The name of the stream whose tags to list.
        :return: A tuple of (list of tag dictionaries with 'Key' and 'Value',
                 bool indicating whether more tags are available).
        """
        try:
            response = self.kinesis_client.list_tags_for_stream(StreamName=stream_name)
            tags = response.get("Tags", list())
            has_more = response.get("HasMoreTags", False)
            logger.info(
                "Listed %s tag(s) for stream '%s'. HasMoreTags: %s.",
                len(tags),
                stream_name,
                has_more,
            )
            return tags, has_more
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found when listing tags.", stream_name)
            raise
```
+  For API details, see [ListTagsForStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListTagsForStream) in *AWS SDK for Python (Boto3) API Reference*.

### `PutRecord`
<a name="kinesis_PutRecord_python_3_topic"></a>

The following code example shows how to use `PutRecord`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
class KinesisStream:
    """Encapsulates a Kinesis stream."""

    def __init__(self, kinesis_client):
        """
        :param kinesis_client: A Boto3 Kinesis client.
        """
        self.kinesis_client = kinesis_client
        self.name = None
        self.details = None
        self.stream_exists_waiter = kinesis_client.get_waiter("stream_exists")

    def put_record(self, data, partition_key):
        """
        Puts data into the stream. The data is formatted as JSON before it is passed
        to the stream.

        :param data: The data to put in the stream.
        :param partition_key: The partition key to use for the data.
        :return: Metadata about the record, including its shard ID and sequence number.
        """
        try:
            response = self.kinesis_client.put_record(
                StreamName=self.name, Data=json.dumps(data), PartitionKey=partition_key
            )
            logger.info("Put record in stream %s.", self.name)
        except ClientError:
            logger.exception("Couldn't put record in stream %s.", self.name)
            raise
        else:
            return response
```
+  For API details, see [PutRecord](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/PutRecord) in *AWS SDK for Python (Boto3) API Reference*.

### `PutRecords`
<a name="kinesis_PutRecords_python_3_topic"></a>

The following code example shows how to use `PutRecords`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def put_records(self, stream_name, records):
        """
        Writes multiple data records into a Kinesis data stream in a single call.

        :param stream_name: The name of the stream to write records to.
        :param records: A list of dicts, each with 'Data' (bytes) and 'PartitionKey' (str).
        :return: The response from the PutRecords call.
        """
        try:
            response = self.kinesis_client.put_records(
                StreamName=stream_name, Records=records
            )
            failed_count = response.get("FailedRecordCount", 0)
            logger.info(
                "Put %s record(s) to stream '%s' with %s failure(s).",
                len(records),
                stream_name,
                failed_count,
            )
            return response
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidArgumentException":
                logger.error(
                    "Invalid argument for PutRecords. Check record sizes and parameters."
                )
            raise
```
+  For API details, see [PutRecords](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/PutRecords) in *AWS SDK for Python (Boto3) API Reference*.

### `RegisterStreamConsumer`
<a name="kinesis_RegisterStreamConsumer_python_3_topic"></a>

The following code example shows how to use `RegisterStreamConsumer`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def register_stream_consumer(self, stream_arn, consumer_name):
        """
        Registers an enhanced fan-out consumer with a Kinesis data stream.

        :param stream_arn: The ARN of the stream.
        :param consumer_name: The name for the consumer.
        :return: A dictionary containing consumer details.
        """
        try:
            response = self.kinesis_client.register_stream_consumer(
                StreamARN=stream_arn, ConsumerName=consumer_name
            )
            consumer = response.get("Consumer", dict())
            logger.info(
                "Registered consumer '%s' with status '%s'.",
                consumer_name,
                consumer.get("ConsumerStatus", "UNKNOWN"),
            )
            return consumer
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceInUseException":
                logger.error(
                    "Consumer '%s' already exists or stream is not available.",
                    consumer_name,
                )
            raise
```
+  For API details, see [RegisterStreamConsumer](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/RegisterStreamConsumer) in *AWS SDK for Python (Boto3) API Reference*.

### `RemoveTagsFromStream`
<a name="kinesis_RemoveTagsFromStream_python_3_topic"></a>

The following code example shows how to use `RemoveTagsFromStream`.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples).

```
    def remove_tags_from_stream(self, stream_name, tag_keys):
        """
        Removes tags from a Kinesis data stream.

        :param stream_name: The name of the stream to remove tags from.
        :param tag_keys: A list of tag keys to remove.
        """
        try:
            self.kinesis_client.remove_tags_from_stream(
                StreamName=stream_name, TagKeys=tag_keys
            )
            logger.info("Removed tag(s) %s from stream '%s'.", tag_keys, stream_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found for tag removal.", stream_name)
            raise
```
+  For API details, see [RemoveTagsFromStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/RemoveTagsFromStream) in *AWS SDK for Python (Boto3) API Reference*.

## Serverless examples
<a name="serverless_examples"></a>

### Invoke a Lambda function from a Kinesis trigger
<a name="serverless_Kinesis_Lambda_python_3_topic"></a>

The following code example shows how to implement a Lambda function that receives an event triggered by receiving records from a Kinesis stream. The function retrieves the Kinesis payload, decodes from Base64, and logs the record contents.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-kinesis-to-lambda) repository.
Consuming a Kinesis event with Lambda using Python.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import base64
def lambda_handler(event, context):

    for record in event['Records']:
        try:
            print(f"Processed Kinesis Event - EventID: {record['eventID']}")
            record_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
            print(f"Record Data: {record_data}")
            # TODO: Do interesting work based on the new data
        except Exception as e:
            print(f"An error occurred {e}")
            raise e
    print(f"Successfully processed {len(event['Records'])} records.")
```

### Reporting batch item failures for Lambda functions with a Kinesis trigger
<a name="serverless_Kinesis_Lambda_batch_item_failures_python_3_topic"></a>

The following code example shows how to implement partial batch response for Lambda functions that receive events from a Kinesis stream. The function reports the batch item failures in the response, signaling to Lambda to retry those messages later.

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-kinesis-to-lambda-with-batch-item-handling) repository.
Reporting Kinesis batch item failures with Lambda using Python.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
def handler(event, context):
    records = event.get("Records")
    curRecordSequenceNumber = ""

    for record in records:
        try:
            # Process your record
            curRecordSequenceNumber = record["kinesis"]["sequenceNumber"]
        except Exception as e:
            # Return failed record's sequence number
            return {"batchItemFailures":[{"itemIdentifier": curRecordSequenceNumber}]}

    return {"batchItemFailures":[]}
```

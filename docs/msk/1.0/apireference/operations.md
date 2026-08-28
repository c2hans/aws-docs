---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/operations.html
---

# Operations
<a name="operations"></a>

The Amazon Managed Streaming for Apache Kafka REST API includes the following operations.
+ [BatchAssociateScramSecret](clusters-clusterarn-scram-secrets.md#BatchAssociateScramSecret)

  Associates a list of SCRAM secrets with a cluster. SCRAM secrets are stored in the Amazon Secrets Manager service, and are used to authenticate clients using sign-in credentials. You can associate up to 10 secrets with a cluster at a time.
+ [BatchDisassociateScramSecret](clusters-clusterarn-scram-secrets.md#BatchDisassociateScramSecret)

  Disassociates a list of SCRAM secrets from a cluster. SCRAM secrets are stored in the Amazon Secrets Manager service, and are used to authenticate clients using sign-in credentials. You can disassociate up to 10 secrets from a cluster at a time.
+ [CreateChannel](clusters-clusterarn-channels.md#CreateChannel)

  Creates a channel using the specified properties in the request on the cluster specified by the Amazon Resource Name (ARN) in the request.
+ [CreateCluster](clusters.md#CreateCluster)

  Creates a new MSK cluster. The following Python 3.6 examples shows how you can create a cluster that's distributed over two Availability Zones. Before you run this Python script, replace the example subnet and security-group IDs with the IDs of your subnets and security group. When you create an MSK cluster, its brokers get evenly distributed over a number of Availability Zones that's equal to the number of subnets that you specify in the `BrokerNodeGroupInfo` parameter. In this example, you can add a third subnet to get a cluster that's distributed over three Availability Zones.

  ```
  import boto3

  client = boto3.client('kafka')

  response = client.create_cluster(
      BrokerNodeGroupInfo={
          'BrokerAZDistribution': 'DEFAULT',
          'ClientSubnets': [
              'subnet-012345678901fedcba',
              'subnet-9876543210abcdef01'
          ],
          'InstanceType': 'kafka.m5.large',
          'SecurityGroups': [
              'sg-012345abcdef789789'
          ]
      },
      ClusterName='SalesCluster',
      EncryptionInfo={
          'EncryptionInTransit': {
              'ClientBroker': 'TLS_PLAINTEXT',
              'InCluster': True
          }
      },
      EnhancedMonitoring='PER_TOPIC_PER_BROKER',
      KafkaVersion='2.2.1',
      NumberOfBrokerNodes=2
  )

  print(response)
  ```
+ [CreateConfiguration](configurations.md#CreateConfiguration)

  Creates a new MSK configuration. To see an example of how to use this operation, first save the following text to a file and name the file `config-file.txt`.

  ```
  auto.create.topics.enable = true

  zookeeper.connection.timeout.ms = 1000

  log.roll.ms = 604800000
  ```

  Now run the following Python 3.6 script in the folder where you saved `config-file.txt`. This script uses the properties specified in `config-file.txt` to create a configuration named `SalesClusterConfiguration`. This configuration can work with Apache Kafka versions 1.1.1 and 2.1.0.

  ```
  import boto3

  client = boto3.client('kafka')

  config_file = open('config-file.txt', 'r')

  server_properties = config_file.read()

  response = client.create_configuration(
      Name='SalesClusterConfiguration',
      Description='The configuration to use on all sales clusters.',
      KafkaVersions=['1.1.1', '2.1.0'],
      ServerProperties=server_properties
  )

  print(response)
  ```
+ [CreateTopic](clusters-clusterarn-topics.md#CreateTopic)

  Creates a topic using the specified properties in the request on the cluster specified by the Amazon Resource Name (ARN) in the request.
+ [CreateVpcConnection](vpc-connection.md#CreateVpcConnection)

  Create remote VPC connection.
+ [DeleteChannel](clusters-clusterarn-channels-channelarn.md#DeleteChannel)

  Deletes the channel specified by the channelArn in the request from the cluster specified by the Amazon Resource Name (ARN) in the request.
+ [DeleteCluster](clusters-clusterarn.md#DeleteCluster)

  Deletes the MSK cluster specified by the Amazon Resource Name (ARN) in the request, and all its revisions.
+ [DeleteClusterPolicy](clusters-clusterarn-policy.md#DeleteClusterPolicy)

  Delete cluster policy.
+ [DeleteConfiguration](configurations-arn.md#DeleteConfiguration)

  Deletes a cluster configuration and all its revisions.
+ [DeleteTopic](clusters-clusterarn-topics-topicname.md#DeleteTopic)

  Deletes the topic specified by the topicName in the request from the cluster specified by the Amazon Resource Name (ARN) in the request.
+ [DeleteVpcConnection](vpc-connection-arn.md#DeleteVpcConnection)

  Delete remote VPC connection.
+ [DescribeChannel](clusters-clusterarn-channels-channelarn.md#DescribeChannel)

  Returns details for a channel resource.
+ [DescribeCluster](clusters-clusterarn.md#DescribeCluster)

  Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request. The following is a Python 3.6 example of how to use this operation. Before you run this Python script, replace the example cluster Amazon Resource Name (ARN) with the ARN of the cluster you want to describe. If you don't know the ARN of the cluster, you can use the `ListClusters` operation to list all the clusters and see their ARNs and full descriptions.

  ```
  import boto3

  client = boto3.client('kafka')

  response = client.describe_cluster(
      ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4'
  )

  print(response)
  ```

  Note that the response to this operation only includes the `ZookeeperConnectStringTls` node in clusters created with Apache Kafka version 2.5.1 and later.
+ [DescribeClusterOperation](operations-clusteroperationarn.md#DescribeClusterOperation)

  Returns a description of the cluster operation specified by the Amazon Resource Name (ARN).
+ [DescribeConfiguration](configurations-arn.md#DescribeConfiguration)

  Returns a description of this MSK configuration.
+ [DescribeConfigurationRevision](configurations-arn-revisions-revision.md#DescribeConfigurationRevision)

  Returns a description of this revision of the configuration.
+ [DescribeTopic](clusters-clusterarn-topics-topicname.md#DescribeTopic)

  Returns details for a topic on a cluster.

  This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.
+ [DescribeTopicPartitions](clusters-clusterarn-topics-topicname-partitions.md#DescribeTopicPartitions)

  Returns all partition information for a topic on a cluster.

  This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.
+ [DescribeVpcConnection](vpc-connection-arn.md#DescribeVpcConnection)

  Describes Remote VPC Connection.
+ [GetBootstrapBrokers](clusters-clusterarn-bootstrap-brokers.md#GetBootstrapBrokers)

  A list of brokers that a client can use to bootstrap. This list doesn't necessarily include all of the brokers in the cluster. The following Python 3.6 example shows how you can use the Amazon Resource Name (ARN) of a cluster to get its bootstrap brokers. If you don't know the ARN of your cluster, you can use the `ListClusters` operation to get the ARNs of all the clusters in this account and Region.

  ```
  import boto3

  client = boto3.client('kafka')

  response = client.get_bootstrap_brokers(
      ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
  )

  print(response['BootstrapBrokerString'])
  ```
+ [GetClusterPolicy](clusters-clusterarn-policy.md#GetClusterPolicy)

  Get cluster policy.
+ [GetCompatibleKafkaVersions](compatible-kafka-versions.md#GetCompatibleKafkaVersions)

  Returns a list of the Apache Kafka versions to which you can update this cluster.
+ [ListChannels](clusters-clusterarn-channels.md#ListChannels)

  Returns all channels in a cluster.
+ [ListClientVpcConnections](clusters-clusterarn-client-vpc-connections.md#ListClientVpcConnections)

  List client VPC connections.
+ [ListClusterOperations](clusters-clusterarn-operations.md#ListClusterOperations)

  Returns a list of all the operations that have been performed on the specified MSK cluster.
+ [ListClusters](clusters.md#ListClusters)

  Returns a list of all the MSK clusters.
+ [ListConfigurationRevisions](configurations-arn-revisions.md#ListConfigurationRevisions)

  Returns a list of all the revisions of an MSK configuration.
+ [ListConfigurations](configurations.md#ListConfigurations)

  Returns a list of all the MSK configurations.
+ [ListKafkaVersions](kafka-versions.md#ListKafkaVersions)

  Returns the Apache Kafka version objects.
+ [ListNodes](clusters-clusterarn-nodes.md#ListNodes)

  Returns a list of the broker nodes in the cluster. The following Python 3.6 example first lists one node of a cluster. Because the cluster has more nodes, the response contains a token that the script then uses to list the remaining nodes.

  ```
  import boto3

  client = boto3.client('kafka')

  list_nodes_response = client.list_nodes(
      ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
      MaxResults=1
  )

  print('\n')
  print('Here is the first node in the list:')
  print('\n')
  print(list_nodes_response['NodeInfoList'])

  next_token = list_nodes_response['NextToken']

  list_nodes_response = client.list_nodes(
      ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
      NextToken=next_token
  )

  print('\n')
  print('Here are the remaining nodes in the list:')
  print('\n')
  print(list_nodes_response['NodeInfoList'])
  ```
+ [ListScramSecrets](clusters-clusterarn-scram-secrets.md#ListScramSecrets)

  Returns a list of SCRAM secrets associated with the cluster. SCRAM secrets are stored in the Amazon Secrets Manager service, and are used to authenticate clients using sign-in credentials.
+ [ListTagsForResource](tags-resourcearn.md#ListTagsForResource)

  Returns a list of the tags associated with the specified resource.
+ [ListTopics](clusters-clusterarn-topics.md#ListTopics)

  Returns all topics in a cluster.

  This API response reflects data that updates approximately every minute. For the most current topic state after making changes, allow approximately one minute before querying.
+ [ListVpcConnections](vpc-connections.md#ListVpcConnections)

  Lists all VPC connections.
+ [PutClusterPolicy](clusters-clusterarn-policy.md#PutClusterPolicy)

  Create or update cluster policy.
+ [RebootBroker](clusters-clusterarn-reboot-broker.md#RebootBroker)

  Reboots a broker. In a given cluster, you can reboot one broker at a time.

  To reboot a broker, wait for the cluster status to be ACTIVE. This operation returns an error if you invoke it while the cluster status is HEALING. You must wait for the status to change from HEALING to ACTIVE before you reboot the broker.
+ [RejectClientVpcConnection](clusters-clusterarn-client-vpc-connection.md#RejectClientVpcConnection)

  Reject client VPC connection.
+ [TagResource](tags-resourcearn.md#TagResource)

  Adds tags to the specified MSK resource.
+ [UntagResource](tags-resourcearn.md#UntagResource)

  Removes the tags associated with the keys that are provided in the query.
+ [UpdateBrokerCount](clusters-clusterarn-nodes-count.md#UpdateBrokerCount)

  Updates the number of broker nodes in the cluster. You can use this operation to increase or decrease the number of brokers in an existing cluster.

  The following Python 3.6 example shows how you can increase the number of brokers in a cluster to 6 brokers. The update operation returns immediately, with a response that includes the Amazon Resource Name (ARN) that Amazon MSK assigns to this cluster operation. You can use that ARN to check the state of the operation. When the state changes from `PENDING` to `UPDATE_COMPLETE`, the operation is complete.

  ```
  import boto3
  import time

  client = boto3.client('kafka')

  update_broker_count_response = client.update_broker_count(
      ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
      CurrentVersion='K12V3IB1VIZHHY',
      TargetNumberOfBrokerNodes=6
  )

  operation_arn = update_broker_count_response['ClusterOperationArn']

  print(operation_arn)

  describe_cluster_operation_response = client.describe_cluster_operation(ClusterOperationArn=operation_arn)
  operation_state = describe_cluster_operation_response['ClusterOperationInfo']['OperationState']
  print(operation_state)

  expanded = False

  while not expanded:
      print('Sleeping for 15 seconds before checking to see if the cluster update is done...')
      time.sleep(15)
      describe_cluster_operation_response = client.describe_cluster_operation(ClusterOperationArn=operation_arn)
      operation_state = describe_cluster_operation_response['ClusterOperationInfo']['OperationState']
      if 'UPDATE_COMPLETE' == operation_state:
          expanded = True
          print('The cluster has 6 brokers now.')
  ```
+ [UpdateBrokerStorage](clusters-clusterarn-nodes-storage.md#UpdateBrokerStorage)

  Updates the EBS storage associated with Amazon MSK brokers. You can increase the amount of EBS storage per broker. You can't decrease the storage. To increase storage, wait for the cluster to be in the ACTIVE state. Storage volumes remain available during this scaling-up operation.
+ [UpdateBrokerType](clusters-clusterarn-nodes-type.md#UpdateBrokerType)

  For information about this operation, see [Updating the broker type](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-broker-type.html) in the developer guide.
+ [UpdateChannel](clusters-clusterarn-channels-channelarn.md#UpdateChannel)

  Updates the channel specified by the channelArn in the request from the cluster specified by the Amazon Resource Name (ARN) in the request.
+ [UpdateClusterConfiguration](clusters-clusterarn-configuration.md#UpdateClusterConfiguration)

  Updates the cluster with the configuration that is specified in the request body. Before you invoke this operation, ensure that the number of partitions per broker on your MSK cluster is under the limits described in [Number of partitions per broker](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html#bestpractices-right-size-cluster). You can't update the configuration of an MSK cluster that exceeds these limits.
+ [UpdateClusterKafkaVersion](clusters-clusterarn-version.md#UpdateClusterKafkaVersion)

  Updates the cluster to the specified Apache Kafka version. Before you invoke this operation, ensure that the number of partitions per broker on your MSK cluster is under the limits described in [Number of partitions per broker](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html#bestpractices-right-size-cluster). You can't update the Apache Kafka version for an MSK cluster that exceeds these limits.
+ [UpdateConfiguration](configurations-arn.md#UpdateConfiguration)

  Creates a new revision of the cluster configuration. The configuration must be in the `ACTIVE` state.
+ [UpdateConnectivity](clusters-clusterarn-connectivity.md#UpdateConnectivity)

  Updates the connectivity setting for the cluster.
+ [UpdateMonitoring](clusters-clusterarn-monitoring.md#UpdateMonitoring)

  Updates the monitoring settings for the cluster. You can use this operation to specify which Apache Kafka metrics you want Amazon MSK to send to Amazon CloudWatch. You can also specify settings for open monitoring with Prometheus. The following Python 3.6 example enables open monitoring with the Node Exporter. It also sets enhanced monitoring to `PER_BROKER`. For more information about monitoring, see [Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html).

  ```
  import boto3
  import time

  client = boto3.client('kafka')

  update_monitoring_response = client.update_monitoring(
      ClusterArn='arn:aws:kafka:us-east-1:0123456789019:cluster/SalesCluster/abcd1234-abcd-cafe-abab-9876543210ab-4',
      CurrentVersion='K12V3IB1VIZHHY',
      EnhancedMonitoring='PER_BROKER',
      OpenMonitoring={"Prometheus":{"JmxExporter":{"EnabledInBroker":False},"NodeExporter":{"EnabledInBroker":True}}}
  )

  operation_arn = update_monitoring_response['ClusterOperationArn']
  print('The ARN of the update operation is ' + operation_arn)

  describe_cluster_operation_response = client.describe_cluster_operation(ClusterOperationArn=operation_arn)

  operation_state = describe_cluster_operation_response['ClusterOperationInfo']['OperationState']
  print('The status of the update operation is ' + operation_state)

  updated = False

  while not updated:
      print('Sleeping for 15 seconds before checking to see if the monitoring update is done...')
      time.sleep(15)
      describe_cluster_operation_response = client.describe_cluster_operation(ClusterOperationArn=operation_arn)
      operation_state = describe_cluster_operation_response['ClusterOperationInfo']['OperationState']
      if 'UPDATE_COMPLETE' == operation_state:
          updated = True
          print('You have successfully updated the monitoring settings.')
  ```
+ [UpdateRebalancing](clusters-clusterarn-rebalancing.md#UpdateRebalancing)

  Use this resource to update the intelligent rebalancing status of an Amazon MSK Provisioned cluster with Express brokers.
+ [UpdateSecurity](clusters-clusterarn-security.md#UpdateSecurity)
+ [UpdateStorage](clusters-clusterarn-storage.md#UpdateStorage)
+ [UpdateTopic](clusters-clusterarn-topics-topicname.md#UpdateTopic)

  Updates topic partition or topic configs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

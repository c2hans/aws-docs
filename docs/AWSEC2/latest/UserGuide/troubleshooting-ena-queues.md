---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-ena-queues.html
---

# Troubleshoot ENA queue issues for Amazon EC2 network interfaces

On instance types that support configurable ENA queue allocation, each network card has a pool of ENA queues, and every network interface on that card takes its queues from the pool. Network interfaces that don't specify a queue count use the default. To see the limits for an instance type, use the following command.

```bash
aws ec2 describe-instance-types --instance-types c6in.8xlarge \
  --query 'InstanceTypes[].NetworkInfo.NetworkCards[].{Card: NetworkCardIndex, Default: DefaultEnaQueueCountPerInterface, MaxPerInterface: MaximumEnaQueueCountPerInterface, Pool: MaximumEnaQueueCount}' \
  --output table
```

For how to calculate a queue count that fits, see [Network interface limits and ENA queues](ena-queues.md#ena-queues-network-interface-limits).

**Topics**
+ [ENA queue pool exceeded](#troubleshooting-ena-queues-pool)
+ [ENA queue count exceeds the maximum per interface](#troubleshooting-ena-queues-per-interface)
+ [ENA queue count isn't a power of 2](#troubleshooting-ena-queues-power-of-2)
+ [ENA queue counts don't fit a new instance type](#troubleshooting-ena-queues-instance-type)
+ [Instance type doesn't support configurable ENA queues](#troubleshooting-ena-queues-unsupported)

## ENA queue pool exceeded
<a name="troubleshooting-ena-queues-pool"></a>

### Description
<a name="troubleshooting-ena-queues-pool-description"></a>

You get the `InvalidParameterValue` error with the following message when you attach a network interface, launch an instance, or change the queue count of an attached network interface: `The sum of ENA queue counts for all interfaces on network card 0 exceeds the maximum allowed value of 128`.

### Cause
<a name="troubleshooting-ena-queues-pool-cause"></a>

The network interfaces on the network card need more ENA queues than its pool provides. This can happen even if the instance hasn't reached its maximum number of network interfaces, and even if you didn't specify a queue count, because the default count doesn't fit.

### Solution
<a name="troubleshooting-ena-queues-pool-solution"></a>

Do one of the following:
+ Specify a smaller queue count: `--ena-queue-count` when you attach, or `EnaQueueCount` for each network interface when you launch. To choose a count that fits, see [Network interface limits and ENA queues](ena-queues.md#ena-queues-network-interface-limits).
+ Lower the queue count of attached network interfaces. Stop the instance first, then run the following command.

  ```bash
  aws ec2 modify-network-interface-attribute --network-interface-id {{eni-1234567890abcdef0}} --attachment AttachmentId={{eni-attach-1234567890abcdef0}},EnaQueueCount=8
  ```
+ Detach a network interface that you don't need.
+ If the instance type has more than one network card, attach the network interface to another card. Each card has its own pool.
+ Choose an instance type with a larger ENA queue pool.

## ENA queue count exceeds the maximum per interface
<a name="troubleshooting-ena-queues-per-interface"></a>

### Description
<a name="troubleshooting-ena-queues-per-interface-description"></a>

You get the `InvalidParameterValue` error with the following message: `The ENA queue count for an interface on network card 0 exceeds the maximum allowed value of 32`.

### Cause
<a name="troubleshooting-ena-queues-per-interface-cause"></a>

The queue count that you specified is higher than the maximum ENA queues per interface for the instance type.

### Solution
<a name="troubleshooting-ena-queues-per-interface-solution"></a>

Specify a queue count that is no more than the maximum per interface (MaxPerInterface in the output of the describe-instance-types command earlier on this page).

## ENA queue count isn't a power of 2
<a name="troubleshooting-ena-queues-power-of-2"></a>

### Description
<a name="troubleshooting-ena-queues-power-of-2-description"></a>

You get the `InvalidParameterValue` error with the following message: `The ENA queue count specified must be a power of 2`.

### Cause
<a name="troubleshooting-ena-queues-power-of-2-cause"></a>

The queue count isn't a power of 2.

### Solution
<a name="troubleshooting-ena-queues-power-of-2-solution"></a>

Specify a power of 2, such as 1, 2, 4, 8, 16, or 32, that is no more than the maximum per interface. To use the default, omit the queue count. For an attached network interface, specify `DefaultEnaQueueCount=true` instead.

## ENA queue counts don't fit a new instance type
<a name="troubleshooting-ena-queues-instance-type"></a>

### Description
<a name="troubleshooting-ena-queues-instance-type-description"></a>

You get the `InvalidParameterValue` error with one of the following messages when you change the instance type:
+ `The sum of ENA queue counts 160 for all interfaces on network card 0 would exceed the maximum allowed value of 128 for the new instance type`
+ `The ENA queue count for an interface on network card 0 would exceed the maximum allowed value of 32 for the new instance type`

### Cause
<a name="troubleshooting-ena-queues-instance-type-cause"></a>

You changed the instance type, and the queue counts on the network interfaces don't fit the new instance type. Either the total on a network card is more than the new pool, or one network interface has more queues than the new maximum per interface. Network interfaces without a queue count are counted at the new instance type's default.

### Solution
<a name="troubleshooting-ena-queues-instance-type-solution"></a>

With the instance stopped, lower the queue counts or detach network interfaces until they fit the new instance type's limits, then change the instance type. You can also choose an instance type with a larger ENA queue pool.

## Instance type doesn't support configurable ENA queues
<a name="troubleshooting-ena-queues-unsupported"></a>

### Description
<a name="troubleshooting-ena-queues-unsupported-description"></a>

You get the `InvalidParameterValue` error with the following message: `You can't specify ENA queue counts if the instance type does not support flexible ENA queues`.

### Cause
<a name="troubleshooting-ena-queues-unsupported-cause"></a>

The instance type doesn't support configurable ENA queue allocation.

### Solution
<a name="troubleshooting-ena-queues-unsupported-solution"></a>

Remove the queue count from the request, or choose an instance type listed in [ENA queue specifications for EC2 instance types](ena-queues.md#supported-instances).

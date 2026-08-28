---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/hsm-metrics-cw.html
---

# Getting CloudWatch metrics for AWS CloudHSM
<a name="hsm-metrics-cw"></a>

Use CloudWatch to monitor your AWS CloudHSM cluster in real time. The metrics can be grouped by region, cluster ID, or cluster ID and HSM ID.

The `AWS/CloudHSM` namespace includes the following metrics:

| Metric | Description |
| --- | --- |
| HsmUnhealthy  | The HSM instance is not performing properly. AWS CloudHSM automatically replaces unhealthy instances for you. You may choose to proactively expand cluster size to reduce performance impact while we are replacing the HSM. |
| HsmTemperature [1](#metric-1) | The junction temperature of the hardware processor. The system shuts down if temperature reaches 110 degrees Centigrade. |
| HsmKeysSessionOccupied  | The number of session keys being used by the HSM instance. |
| HsmKeysTokenOccupied  | The number of token keys being used by the HSM instance and the cluster.  |
| HsmSslCtxsOccupied [1](#metric-1) | The number of end-to-end encrypted channels currently established for the HSM instance. Up to 2,048 channels are allowed. |
| HsmSessionCount  | The number of open connections to the HSM instance. Up to 2,048 are allowed. By default, the client daemon is configured to open two sessions with each HSM instance under one end-to-end encrypted channel. AWS CloudHSM may also have up to 2 connections open with the HSM to monitor the health of the HSMs.  |
| HsmUsersAvailable  | The number of additional users that can be created. This equals the maximum number of users (listed in HsmUsersMax) minus the users created to date. |
| HsmUsersMax [1](#metric-1) | The maximum number of users that can be created on the HSM instance. |
| InterfaceEth2OctetsInput [1](#metric-1) | The cumulative sum of incoming traffic to the HSM to date. |
| InterfaceEth2OctetsOutput [1](#metric-1) | The cumulative sum of outgoing traffic to the HSM to date. |
+ [1] This metric is not available for hsm2m.medium.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
